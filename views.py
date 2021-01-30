"""
Routes and views for the flask application.
"""
from flask import Flask, request, session, url_for, redirect, flash, send_file
from flask import render_template
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import tweepy
import re
import time
from random import randint
from textblob import TextBlob
from tweepy import OAuthHandler
import csv
import numpy as np
from sklearn.svm import SVR
import pymysql
import pygal
import pickle
from functools import wraps
from flask_mail import Mail, Message
from GoogleNews import GoogleNews


app = Flask(__name__)
app.config.update(DEBUG=True, MAIL_SERVER='smtp.gmail.com', MAIL_PORT=465, MAIL_USE_SSL=True,
                  MAIL_USERNAME='notification.wallstreet@gmail.com', MAIL_PASSWORD='WALLSTREET@123')
mail = Mail(app)

app.secret_key = 'abcdefg'


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""

    return render_template(
        'contact.html',
        title='Contact Us',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/signup')
def signup():
    """Renders the about page."""
    return render_template(
        'signup.html',
        title='Signup',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/signupch', methods=['GET', 'POST'])
def signupch():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cursor = db.cursor();
    cursor.execute("SELECT VERSION()")
    nm = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['confirm-password']
    unames = "select username from user where username=%s"
    if cursor.execute(unames, nm) != 0:
        flash("Username already exist...!")
        return redirect(url_for('signup'))

    if password != cpassword:
        flash("Confirm Password does not matched..!")
        return redirect(url_for('signup'))

    try:
        data = cursor.fetchone()
        with db.cursor() as cursor:
            sql = "insert into user(username,email,password)values(%s,%s,%s)"
            cursor.execute(sql, (nm, email, password))
            db.commit()
            sign = "sign up successfully"
    finally:
        db.close()

    return render_template(
        'signup.html',
        year=datetime.now().year,
        sign=sign,
    )


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('signup'))

    return wrap


@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cursor = db.cursor();
    fnm = request.form['username']
    passw = request.form['password']
    msg = ""

    sql = "select * from user where username= %s AND password= %s"
    if cursor.execute(sql, (fnm, passw)) != 0:
        db.commit()
        msg = "Logged In"
        session['logged_in'] = True
        session['username'] = request.form['username']
        return render_template(
            'index.html',
            title='Signup',
            year=datetime.now().year,
            message='Your application description page.',
            msg=msg
        )
    elif (fnm == 'Admin' and passw == '123'):
        db.commit()
        msg = "Logged In"
        session['logged_in'] = True
        session['Alogged_in'] = True
        session['username'] = request.form['username']
        return render_template(
            'admin.html',
            title='Signup',
            year=datetime.now().year,
            message='Your application description page.',
            msg=msg
        )
    else:
        db.commit()
        msg = "*InValid Details"
        return render_template(
            'signup.html',
            year=datetime.now().year,
            msg=msg
        )


@app.route('/stockPriceForm')
def stockPriceForm():
    """Renders the stockPriceform page."""
    return render_template(
        'stockPriceForm.html',
        title='stockPriceForm',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/displayStock', methods=["post"])
def displayStock():
    """Renders the stockPriceform page."""
    import datetime as dt
    import pandas_datareader.data as web
    dates = []
    Close = []
    High = []
    Low = []
    Open = []
    Volume = []
    # sdate = int(request.form['sdate'])
    date = request.form['sdate']
    date.split("-")
    a, b, c = date.split("-")
    syear = int(a)
    smonth = int(b)
    sdate = int(c)

    eedate = request.form["edate"]
    eedate.split("-")
    a, b, c = eedate.split("-")
    eyear = int(a)
    emonth = int(b)
    edate = int(c)

    name = request.form['companyName']
    with open("s.pickle", "rb") as f:
        tickers = pickle.load(f)
    now = int(datetime.now().year)
    n = name.upper()
    if sdate > 31 or edate > 31 or smonth > 12 or emonth > 12 or syear < 2010 or eyear > now:
        flash("Enter valid Date ")
        return redirect(url_for('stockPriceForm'))
    else:
        start = dt.datetime(syear, smonth, sdate)
        end = dt.datetime(eyear, emonth, edate)
    if end > start:
        if n in tickers:
            try:
                df = web.DataReader(name, 'yahoo', start, end)
            except:
                flash("Network is too slow...!")
                return redirect(url_for('stockPriceForm'))
        else:
            flash("Enter valid S&P500 stock code ")
            return redirect(url_for('stockPriceForm'))
    else:
        flash("End date is must be greater then start date")
        return redirect(url_for('stockPriceForm'))

    requests.adapters.DEFAULT_RETRIES = 5
    count = len(df)
    df.to_csv('data.csv')

    def get_data(filename):
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)  # skipping column names
            for row in csvFileReader:
                dates.append(row[0])
                Close.append(float(row[4]))
                High.append(float(row[1]))
                Low.append(float(row[2]))
                Open.append(float(row[3]))
                Volume.append(row[5])

        return

    graph = pygal.Line()
    graph.title = 'Price of Stock over time'
    get_data('data.csv')
    graph.x_labels = dates
    graph.add(name, Open)
    graph_data = graph.render_data_uri()
    max1 = max(Open)
    min1 = min(Open)
    # print(graph.x_labels,type(graph.x_labels))
    return render_template(
        'displayStock.html',
        title='displayStock',
        year=datetime.now().year,
        message='Your application description page.',
        name=name,
        dates=dates,
        Close=Close,
        High=High,
        Low=Low,
        Open=Open,
        Volume=Volume,
        count=count,
        df=df,
        graph_data=graph_data,
        max1=max1,
        min1=min1
    )


@app.route('/dash/urlToDownload')
def download_csv():
    return send_file('data.csv',
                     mimetype='text/csv',
                     attachment_filename='data.csv',
                     as_attachment=True)

@app.route('/predictPriceForm')
def predictPriceForm():
    """Renders the stockPriceform page."""
    return render_template(
        'predictPriceForm.html',
        title='predictPriceForm',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/predictedData', methods=["post"])
@login_required
def predictedData():
    """Renders the stockPriceform page."""
    import datetime as dt
    import pandas_datareader.data as web

    name = request.form['companyName']
    with open("s.pickle", "rb") as f:
        tickers = pickle.load(f)

    n = name.upper()

    if 'logged_in' in session:
        time1 = datetime.now()
        unm = session["username"]
        db = pymysql.connect(host="localhost", user="root", password="", database="stock")

        try:
            with db.cursor() as cursor:
                sql = "insert into predictionhistory(searchname,time,username)values(%s,%s,%s)"
                cursor.execute(sql, (name, time1, unm))
                db.commit()

        finally:

            db.close()

    year = datetime.now().year
    month = datetime.now().month
    date = datetime.now().day
    days_before = (datetime.now() - timedelta(days=28))
    start = dt.datetime(days_before.year, days_before.month, days_before.day)
    end = dt.datetime(year, month, date)

    if n in tickers:
        try:
            time.sleep(randint(0, 2))
            df = web.DataReader(name, 'yahoo', start, end)
        except:
            flash("Network is too slow...!")
            return redirect(url_for('predictPriceForm'))
    else:
        flash("Enter valid S&P500 stock code ")
        return redirect(url_for('predictPriceForm'))

    requests.adapters.DEFAULT_RETRIES = 5
    df.to_csv('predict.csv')

    dates = []
    prices = []

    def get_data(filename):
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)  # skipping column names
            for row in csvFileReader:
                dates.append(int(row[0].split('-')[2]))
                prices.append(float(row[4]))
        return

    def predict_price(dates, prices, x):
        dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1

        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)  # defining the support vector regression models
        svr_rbf.fit(dates, prices)  # fitting the data points in the models

        return svr_rbf.predict(dates)[0]

    get_data('predict.csv')  # calling get_data method by passing the csv file to it
    predictdate = (datetime.now() + timedelta(days=1))
    predicted_price =0
    predicted_price= predict_price(dates, prices, [predictdate.day])

    graph = pygal.Line()
    graph.title = '%Change  StockValue over last 1 month'
    graph.x_labels = dates
    graph.add(name, prices)
    graph_data = graph.render_data_uri()

    return render_template(
        'predictedData.html',
        title='predictedData',
        year=datetime.now().year,
        message='Your application description page.',
        predicted_price=predicted_price,
        dates=dates,
        graph_data=graph_data,
        prices=prices,
        start=start,
        end=end,
        name=name
    )


@app.route('/passwordRecovery')
def passwordRecovery():
    """Renders the stockPriceform page."""
    return render_template(
        'passwordRecovery.html',
        title='Password Recovery',
        year=datetime.now().year,

    )


@app.route('/send_mail', methods=["post"])
def send_mail():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cursor = db.cursor();
    username = request.form["username"]

    emaill = "select email from user where username= %s "
    password = "select password from user where username= %s "
    email_addr = cursor.execute(emaill, (username))

    email = cursor.fetchone()
    data = email[0]
    cursor.execute(password, (username))
    password = cursor.fetchone()
    passw = password[0]
    time = str(datetime.now().year)
    if (email_addr) != 0:
        try:
            msg = Message("Forgot Password - Wall street", sender="notification.wallstreet@gmail.com",
                          recipients=[data])
            msg.body = 'Hello ' + username + ',\n     You recently requested  for forgot password of your WallStreet account. \n your password is:' + passw + '\n@' + time + '-WallStreet'
            msg.html = render_template('sendMail.html', username=username, passw=passw)
            mail.send(msg)
            mess = "Email Sent"
            return render_template(
                'signup.html',
                title='Signup',
                year=datetime.now().year,
                message='Your application description page.',
                mess=mess
            )
        except Exception as e:
            return str(e)
    else:
        db.commit()
        msg = "No username found"
        return render_template(
            'passwordRecovery.html',
            year=datetime.now().year,
            msg=msg
        )


@app.route('/newsform')
def newsform():
    """Renders the newsform page."""

    return render_template(
        'newsform.html',
        title='Newsform',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/DetailedNews', methods=["post"])
def detailedNews():
    name = request.form["companyName"]
    googlenews = GoogleNews()
    googlenews.clear()
    googlenews.search(name)
    newsresult = googlenews.result(sort=True)
    if 'logged_in' in session:
        time1 = datetime.now()
        unm = session["username"]
        db = pymysql.connect(host="localhost", user="root", password="", database="stock")
        cursor = db.cursor();
        sqlnews = "select * from newshistory where username= %s ";

        if ((cursor.execute(sqlnews, (unm)) != 0)):
            db.commit()
            newshistory = cursor.fetchall()
            count1 = len(newsresult)

        if (count1 > 5):
            count1 = 5
        else:
            count1 = count1

        try:

            with db.cursor() as cursor:
                sql = "insert into newshistory(newsname,username,time)values(%s,%s,%s)"
                cursor.execute(sql, (name, unm, time1))
                db.commit()

        finally:
            db.close()

    return render_template(
        'DetailedNews.html',
        title='Display News',
        l=newsresult,
        year=datetime.now().year,
        name=name,
        newshistory=newshistory,
        count1=count1
    )


@app.route('/displayNews', methods=["post"])
def displayNews():
    """Renders the displayNews page."""
    newsresult = []
    count1 = 0

    def scrape_news_summaries(s):
        time.sleep(randint(0, 2))
        r = requests.get("http://www.google.com/search?q=" + s + "&tbm=nws")
        print(r.status_code)  # Print the status code
        content = r.text
        news_summaries = []
        soup = BeautifulSoup(content, "html.parser")
        st_divs = soup.findAll("div", {"class": "Y3v8qd"})
        for st_div in st_divs:
            news_summaries.append(st_div.text)
        return news_summaries

    def scrap_title(s):
        time.sleep(randint(0, 2))
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        url = "https://www.google.com/search?q=" + s + "&tbm=nws"
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        title = [a.get_text() for a in soup.find_all("a", class_="l lLrAF")]
        return title

    def scrap_link(s):
        time.sleep(randint(0, 2))
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        url = "https://www.google.com/search?q=" + s + "&tbm=nws"
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        # you don't even have to process the div container
        # just go strait to <a> and using indexing get "href"
        # headlines
        ahref = [a["href"] for a in soup.find_all("a", class_="l lLrAF")]
        return ahref

    # def scrape_news_head(s):
    #     time.sleep(randint(0, 2))  # relax and don't let google be angry
    #     html = requests.get("https://news.google.com/news/search/section/q/" + s + "/" + s + "?hl=en&gl=US&ned=us")
    #     content = html.text
    #
    #     news_head = []
    #     soup = BeautifulSoup(content, "html.parser")
    #     st_divs = soup.findAll("div", {"class": "v4IxVd"})
    #
    #     for st_div in st_divs:
    #         news_head.append(st_div.a)
    #
    #     return news_head

    def scrape_news_head(s):
        time.sleep(randint(0, 2))  # relax and don't let google be angry
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        url = "https://www.google.com/search?q=" + s + "&tbm=nws"
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        # you don't even have to process the div container
        # just go strait to <a> and using indexing get "href"
        # headlines
        news_head = [a.text for a in soup.find_all("a", class_="l lLrAF")]

        return news_head

    name = request.form["companyName"]
    if 'logged_in' in session:
        time1 = datetime.now()
        unm = session["username"]
        db = pymysql.connect(host="localhost", user="root", password="", database="stock")
        cursor = db.cursor();
        sqlnews = "select * from newshistory where username= %s ";

        if ((cursor.execute(sqlnews, (unm)) != 0)):
            db.commit()
            newsresult = cursor.fetchall()
            count1 = len(newsresult)

        if (count1 > 5):
            count1 = 5
        else:
            count1 = count1

        try:

            with db.cursor() as cursor:
                sql = "insert into newshistory(newsname,username,time)values(%s,%s,%s)"
                cursor.execute(sql, (name, unm, time1))
                db.commit()

        finally:
            db.close()

    l = scrape_news_summaries(name)
    sc = scrape_news_head(name)

    title1 = scrap_title(name)
    link = scrap_link(name)

    fSentiment_list = []
    sent = []
    fSentiment = 0
    p = 0
    nu = 0
    ne = 0
    count = 1
    for n in l:
        analysis = TextBlob(n)
        # set sentiment
        if analysis.sentiment.polarity > 0:
            fSentiment = fSentiment + analysis.sentiment.polarity
            dsentiment = 'Positive'
            p = p + 1
            count = count + 1
            sent.append(analysis.sentiment.polarity)
            fSentiment_list.append(dsentiment)

        elif analysis.sentiment.polarity == 0:
            fSentiment = fSentiment + analysis.sentiment.polarity
            dsentiment = 'Neutral'
            nu = nu + 1
            count = count + 1
            sent.append(analysis.sentiment.polarity)
            fSentiment_list.append(dsentiment)

        else:
            fSentiment = fSentiment + analysis.sentiment.polarity
            dsentiment = 'Negative'
            count = count + 1
            ne = ne + 1
            sent.append(analysis.sentiment.polarity)
            fSentiment_list.append(dsentiment)

    final = fSentiment / count
    perpnews = ((p * 100) / count)
    pernnews = ((ne * 100) / count)
    pernunews = ((nu * 100) / count)
    sent = p - ne
    foutput = ''
    print(sent)
    if (sent == 0):
        foutput = 'Neutral'
    elif (perpnews >= 50 and perpnews <= 60):
        foutput = 'Weakly positive'
    elif (perpnews > 60 and perpnews <= 80):
        foutput = 'positive'
    elif (perpnews > 80 and perpnews <= 100):
        foutput = 'strongly positive'
    elif (pernnews >= 50 and pernnews <= 60):
        foutput = 'Weakly negative'
    elif (pernnews > 60 and pernnews <= 80):
        foutput = 'Negative'
    elif (pernnews > 80 and pernnews <= 100):
        foutput = 'Strongly negative'

    print(foutput)

    return render_template(
        'displayNews.html',
        title='Display News',
        l=l,
        year=datetime.now().year,
        fSentiment_list=fSentiment_list,
        final=final,
        foutput=foutput,
        name=name,
        sent=sent,
        title1=title1,
        sc=sc,
        link=link,
        newsresult=newsresult,
        count1=count1,
        perpnews=perpnews,
        pernnews=pernnews,
        pernunews=pernunews
    )


@app.route('/tweetForm')
@login_required
def tweetForm():
    """Renders the tweetform page."""

    return render_template(
        'tweetForm.html',
        title='TweetForm',
        year=datetime.now().year,
        message='Your application description page.'
    )


class TwitterClient(object):

    def __init__(self):

        consumer_key = 'MgSZX1yjFRjqs5bhdUWq98uxw'
        consumer_secret = 'x0CCj5ZxAvroNzS2NQdP8fy5Ot4K31QDhmSjHc3RhzQH6NSxH8'
        access_token = '965563331070193667-VTdEAgE97tBUNKkEQcxun2shlcO6vya'
        access_token_secret = 'sPc2ci04ZZddODOeBJ5doKz9rt0WWufiVPYyRZOkwZdSd'

        # attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)

        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count):
        tweets = []
        n = 0
        m = 0
        try:
            # call twitter api to fetch tweets
            print(count)
            fetched_tweets = self.api.search(q=query, count=count, lang='en')

            for tweet in fetched_tweets:

                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        m = m + 1
                        tweets.append(parsed_tweet)
                else:
                    n = n + 1
                    tweets.append(parsed_tweet)

            # return parsed tweets
            print(n)
            print(m)
            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


@app.route('/displayTweet', methods=["post"])
@login_required
def displayTweet():
    # creating object of TwitterClient Class
    api = TwitterClient()
    name = request.form["KeywordName"]
    count1 = request.form["TweetNum"]
    tweets = api.get_tweets(query=name, count=count1)

    if 'logged_in' in session:
        time1 = datetime.now()
        unm = session["username"]
        db = pymysql.connect(host="localhost", user="root", password="", database="stock")
        try:
            with db.cursor() as cursor:
                sql = "insert into tweethistory(searchName,numoftweet,username,time)values(%s,%s,%s,%s)"
                cursor.execute(sql, (name, count1, unm, time1))
                db.commit()
        finally:

            db.close()

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    perptweet = format(100 * len(ptweets) / len(tweets))
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    perntweet = format(100 * len(ntweets) / len(tweets))
    pernutweet = format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))

    return render_template(
        'displayTweet.html',
        title='Display Tweet',
        year=datetime.now().year,
        message='Please try Again',
        ptweets=ptweets,
        tweets=tweets,
        ntweets=ntweets,
        perptweet=perptweet,
        perntweet=perntweet,
        pernutweet=pernutweet,
        name=name
    )


@app.route('/admin')
@login_required
def admin():
    """Renders the about page."""
    return render_template(
        'admin.html',
        title='admin',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/AdminHistoryForm')
@login_required
def AdminHistoryForm():
    return render_template(
        'AdminHistoryForm.html',
        title='HistoryForm',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/userhistory', methods=["post"])
@login_required
def userhistory():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cursor = db.cursor();
    fnm = request.form['username']
    tweetresult = ()
    newsresult = ()
    sqlnews = "select * from newshistory where username= %s ";
    sqltweet = "select * from tweethistory where username= %s";
    if ((cursor.execute(sqlnews, (fnm)) != 0)):
        db.commit()
        newsresult = cursor.fetchall()

    if ((cursor.execute(sqltweet, (fnm)) != 0)):
        db.commit()
        tweetresult = cursor.fetchall()

    count1 = len(newsresult)
    count2 = len(tweetresult)
    print(newsresult)
    print(tweetresult)
    return render_template(
        'userhistory.html',
        title='userhistory',
        year=datetime.now().year,
        newsresult=newsresult,
        tweetresult=tweetresult,
        count1=count1,
        count2=count2,
        fnm=fnm
    )


@app.route('/companyhistory', methods=["post"])
def companyhistory():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cursor = db.cursor();
    fnm = request.form['companyname']
    print(fnm)
    tweetresult = ()
    newsresult = ()
    sqlnews = "select * from newshistory where newsname= %s ";
    print(sqlnews)
    sqltweet = "select * from tweethistory where searchname= %s";
    if ((cursor.execute(sqlnews, (fnm)) != 0)):
        db.commit()
        newsresult = cursor.fetchall()

    if ((cursor.execute(sqltweet, (fnm)) != 0)):
        db.commit()
        tweetresult = cursor.fetchall()

    count1 = len(newsresult)
    count2 = len(tweetresult)

    return render_template(
        'companyhistory.html',
        title='companyhistory',
        year=datetime.now().year,
        message='Your application description page.',
        newsresult=newsresult,
        tweetresult=tweetresult,
        count1=count1,
        count2=count2,
        fnm=fnm
    )


@app.route('/temp', methods=["post"])
def temp():
    """Renders the about page."""
    msg = request.form['date']
    print(type(msg))
    msg.split("-")
    a, b, c = msg.split("-")
    year = int(a)
    print(type(year))
    return render_template(
        'main.html',
        title='admin',
        msg=msg,
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/temp1')
def temp1():
    """Renders the about page."""
    return render_template(
        'temp.html',
        title='aadmin',
        year=datetime.now().year,
        message='Your application description page.'
    )


app.run(debug=True)

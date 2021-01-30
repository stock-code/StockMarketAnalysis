-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2018 at 10:05 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stock`
--

-- --------------------------------------------------------

--
-- Table structure for table `tweethistory`
--

CREATE TABLE `tweethistory` (
  `searchName` varchar(30) NOT NULL,
  `numoftweet` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `time` datetime NOT NULL,
  `tweetid` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tweethistory`
--

INSERT INTO `tweethistory` (`searchName`, `numoftweet`, `username`, `time`, `tweetid`) VALUES
('tsla', 123, 'smg', '2018-04-08 01:54:31', 1),
('ford', 12, 'hello', '2018-04-08 18:33:15', 2),
('F', 1, 'smg', '2018-04-08 19:13:35', 3),
('F', 123, 'smg', '2018-04-08 19:15:15', 4),
('abc', 1, 'smg', '2018-04-11 16:22:58', 16),
('relaince', 100, 'smg', '2018-04-11 13:11:03', 15),
('AMZN', 100, 'twinkle', '2018-04-10 02:29:19', 14),
('F', 50, 'smg', '2018-04-10 02:28:34', 13);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tweethistory`
--
ALTER TABLE `tweethistory`
  ADD PRIMARY KEY (`tweetid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tweethistory`
--
ALTER TABLE `tweethistory`
  MODIFY `tweetid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

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
-- Table structure for table `predictionhistory`
--

CREATE TABLE `predictionhistory` (
  `searchname` varchar(30) NOT NULL,
  `time` datetime NOT NULL,
  `username` varchar(30) NOT NULL,
  `predictionid` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `predictionhistory`
--

INSERT INTO `predictionhistory` (`searchname`, `time`, `username`, `predictionid`) VALUES
('tsla', '2018-04-08 02:34:36', 'smg', 1),
('F', '2018-04-08 19:56:10', 'smg', 2),
('amzn', '2018-04-09 15:35:58', 'hello', 3),
('F', '2018-04-09 15:39:04', 'hello', 4),
('cascs', '2018-04-09 16:16:05', 'hello', 5),
('f', '2018-04-09 16:16:15', 'hello', 6),
('amzn', '2018-04-09 16:16:26', 'hello', 7),
('aaplap', '2018-04-09 16:16:33', 'hello', 8),
('svdv', '2018-04-09 16:18:40', 'hello', 9),
('csc', '2018-04-09 16:18:53', 'hello', 10),
('amzn', '2018-04-09 16:19:00', 'hello', 11),
('amzon', '2018-04-09 16:19:08', 'hello', 12),
('csdcs', '2018-04-09 16:19:12', 'hello', 13),
('vdvds', '2018-04-09 16:19:14', 'hello', 14),
('tsla', '2018-04-10 02:13:23', 'SMG', 15),
('tsla', '2018-04-10 02:13:27', 'SMG', 16),
('F', '2018-04-10 02:15:22', 'SMG', 17),
('F', '2018-04-10 23:09:34', 'smg', 18),
('F', '2018-04-10 23:16:55', 'smg', 19),
('F', '2018-04-10 23:17:25', 'smg', 20),
('F', '2018-04-10 23:24:05', 'smg', 21),
('TSLA', '2018-04-11 11:33:58', 'smg', 22),
('AMZN', '2018-04-11 11:34:04', 'smg', 23),
('AMZN', '2018-04-11 11:35:25', 'smg', 24),
('FB', '2018-04-11 11:48:18', 'smg', 25),
('fb', '2018-04-11 13:14:07', 'smg', 26),
('prime focus', '2018-04-11 16:31:47', 'bb', 27),
('amazon', '2018-04-11 16:31:54', 'bb', 28),
('amzn', '2018-04-11 16:32:07', 'bb', 29);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `predictionhistory`
--
ALTER TABLE `predictionhistory`
  ADD PRIMARY KEY (`predictionid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `predictionhistory`
--
ALTER TABLE `predictionhistory`
  MODIFY `predictionid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

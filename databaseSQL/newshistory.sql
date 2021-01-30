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
-- Table structure for table `newshistory`
--

CREATE TABLE `newshistory` (
  `newsname` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `time` datetime NOT NULL,
  `news_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `newshistory`
--

INSERT INTO `newshistory` (`newsname`, `username`, `time`, `news_id`) VALUES
('Google', 'hello', '2018-04-07 01:28:27', 2),
('Tesla', 'smg', '2018-04-07 01:29:01', 3),
('reliance', 'Gopesh', '2018-04-07 13:44:03', 4),
('googl', 'Gopesh', '2018-04-07 17:58:08', 5),
('Google', 'Admin', '2018-04-07 21:20:56', 6),
('tesla', 'Admin', '2018-04-07 21:21:44', 7),
('tesla', 'Admin', '2018-04-07 21:22:27', 8),
('Tesla', 'Admin', '2018-04-07 21:22:50', 9),
('tesla', 'Admin', '2018-04-07 21:23:13', 10),
('Google', 'Admin', '2018-04-07 21:23:45', 11),
('Google', 'smg', '2018-04-07 21:24:42', 12),
('Google', 'smg', '2018-04-07 21:26:26', 13),
('Google', 'smg', '2018-04-08 13:24:38', 14),
('Google', 'smg', '2018-04-08 13:32:03', 15),
('Google', 'smg', '2018-04-08 13:32:42', 16),
('Google', 'smg', '2018-04-08 13:34:12', 17),
('Google', 'smg', '2018-04-08 13:34:46', 18),
('Google', 'smg', '2018-04-08 13:34:59', 19),
('Google', 'smg', '2018-04-08 13:35:22', 20),
('Google', 'smg', '2018-04-08 13:37:11', 21),
('Google', 'smg', '2018-04-08 13:37:17', 22),
('Google', 'smg', '2018-04-08 13:38:09', 23),
('Google', 'smg', '2018-04-08 13:39:00', 24),
('Google', 'smg', '2018-04-08 13:41:59', 25),
('Google', 'smg', '2018-04-08 13:42:14', 26),
('Google', 'smg', '2018-04-08 13:48:09', 27),
('Google', 'smg', '2018-04-08 13:48:25', 28),
('tesla', 'smg', '2018-04-08 13:48:58', 29),
('tesla', 'smg', '2018-04-08 13:49:43', 30),
('tesla', 'smg', '2018-04-08 14:08:36', 31),
('tesla', 'smg', '2018-04-08 14:09:19', 32),
('tesla', 'smg', '2018-04-08 14:10:42', 33),
('tesla', 'smg', '2018-04-08 17:48:45', 34),
('tesla', 'smg', '2018-04-08 17:49:25', 35),
('tesla', 'smg', '2018-04-08 17:50:42', 36),
('tesla', 'smg', '2018-04-08 17:51:18', 37),
('tesla', 'smg', '2018-04-08 17:52:33', 38),
('tesla', 'smg', '2018-04-08 17:53:53', 39),
('tesla', 'smg', '2018-04-08 17:54:07', 40),
('tesla', 'smg', '2018-04-08 17:54:40', 41),
('tesla', 'smg', '2018-04-08 17:56:33', 42),
('tesla', 'smg', '2018-04-08 17:56:51', 43),
('tesla', 'smg', '2018-04-08 17:57:17', 44),
('tesla', 'smg', '2018-04-08 17:59:19', 45),
('tesla', 'smg', '2018-04-08 17:59:57', 46),
('tesla', 'smg', '2018-04-08 18:01:24', 47),
('tesla', 'smg', '2018-04-08 18:14:19', 48),
('tesla', 'smg', '2018-04-08 18:15:11', 49),
('tesla', 'smg', '2018-04-08 18:15:36', 50),
('tesla', 'smg', '2018-04-08 18:16:33', 51),
('tesla', 'smg', '2018-04-08 18:21:17', 52),
('tesla', 'smg', '2018-04-08 18:21:35', 53),
('tesla', 'smg', '2018-04-08 18:22:12', 54),
('tesla', 'smg', '2018-04-08 18:23:10', 55),
('tesla', 'smg', '2018-04-08 18:25:34', 56),
('tesla', 'smg', '2018-04-08 18:26:23', 57),
('tesla', 'smg', '2018-04-08 18:26:45', 58),
('tesla', 'smg', '2018-04-08 18:27:03', 59),
('tesla', 'smg', '2018-04-08 18:27:26', 60),
('F', 'hello', '2018-04-08 18:27:51', 61),
('F', 'hello', '2018-04-08 18:30:48', 62),
('F', 'hello', '2018-04-08 18:31:37', 63),
('google', 'hello', '2018-04-08 18:36:51', 64),
('google', 'hello', '2018-04-08 18:37:06', 65),
('Apple', 'smg', '2018-04-08 19:56:51', 66),
('Google', 'smg', '2018-04-09 16:54:28', 67),
('google', 'smg', '2018-04-09 16:57:25', 68),
('', '', '2018-04-09 18:29:55', 69),
('Google', 'SMG', '2018-04-10 02:10:16', 70);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `newshistory`
--
ALTER TABLE `newshistory`
  ADD PRIMARY KEY (`news_id`),
  ADD KEY `news_id` (`news_id`),
  ADD KEY `news_id_2` (`news_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `newshistory`
--
ALTER TABLE `newshistory`
  MODIFY `news_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2018 at 10:06 AM
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
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `email`, `password`, `user_id`) VALUES
('twinkle', 'patelt707@gmail.com', 'twinkle', 1),
('Shubham', 'shubham@me.com', '123', 2),
('Gopesh', 'hello@gmail.com', '1234', 3),
('hello', 'hello@gmail.com', '123', 4),
('s', 'hell@gmail.com', '123', 5),
('Shubham12', 's@gmail.com', '123', 6),
('smg', 'anonymous.stock.code@gmail.com', '123', 7),
('sum', 'shubhamgajera1@gmail.com', '123', 8),
('shubham123', 'anonymous.stock.code@gmail.com', '123', 9),
('me', 'myself@gmail.com', '12', 10),
('ce1', 'sdf@fsg', '123', 14),
('abc', 'anonymous.stock.code@gmail.com', '123', 12),
('abc1', 'anonymous.stock.code@gmail.com', '123', 13),
('dikshu', 'dikgajera@gmail.com', '1234', 16),
('bb', 'bb@b.n', 'bbb', 17);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

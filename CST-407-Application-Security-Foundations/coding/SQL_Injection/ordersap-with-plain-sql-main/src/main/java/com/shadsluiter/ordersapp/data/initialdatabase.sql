-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 10, 2024 at 02:22 PM
-- Server version: 5.7.39
-- PHP Version: 8.1.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: orders-app
--
CREATE DATABASE IF NOT EXISTS `orders-app` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `orders-app`;

-- --------------------------------------------------------

--
-- Table structure for table orders
--

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id bigint(20) NOT NULL,
  date datetime(6) NOT NULL,
  customerid bigint(20) NOT NULL,
  notes varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table orders
--

INSERT INTO orders (id, date, customerid, notes) VALUES
(1, '2024-01-01 00:00:00.000000', 1, 'Customer requested a fast delivery.'),
(3, '2024-01-03 00:00:00.000000', 3, 'This is for a birthday. \n Special message included.'),
(4, '2024-01-04 00:00:00.000000', 4, 'Specific delivery time for after 5 pm'),
(5, '2024-01-05 00:00:00.000000', 5, 'Please use eco-friendly packaging.'),
(7, '2024-01-07 00:00:00.000000', 2, 'Customer requested an expedited shipping.'),
(12, '2024-01-12 00:00:00.000000', 2, 'Customer requested a return label.'),
(15, '2024-01-15 00:00:00.000000', 5, 'Customer requested a price match.'),
(16, '2024-01-16 00:00:00.000000', 1, 'Customer wanted to track the shipment.'),
(18, '2024-01-18 00:00:00.000000', 3, 'Customer requested an extended warranty.');

-- --------------------------------------------------------

--
-- Table structure for table users
--

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id bigint(20) NOT NULL,
  login_name varchar(255) NOT NULL,
  password varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table users
--

INSERT INTO users (id, login_name, password) VALUES
(1, 'alice', 'password123'),
(2, 'bob', 'Iwishtoberichandfamous!'),
(3, 'charlie', 'new_password'),
(4, 'david', '!%1abc'),
(5, 'eve', 'eveeveeveeve'),
(10, 'shad', '$2a$10$Bf88dy0PvXrVpH/sKy00vOcxq5XibCK3gAkATdc/ZnT7IsbvWtXtm');

--
-- Indexes for dumped tables
--

--
-- Indexes for table orders
--
ALTER TABLE orders
  ADD PRIMARY KEY (id),
  ADD KEY customerid (customerid);

--
-- Indexes for table users
--
ALTER TABLE users
  ADD PRIMARY KEY (id);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table orders
--
ALTER TABLE orders
  MODIFY id bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table users
--
ALTER TABLE users
  MODIFY id bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1002;

--
-- Constraints for dumped tables
--

--
-- Constraints for table orders
--
ALTER TABLE orders
  ADD CONSTRAINT orders_ibfk_1 FOREIGN KEY (customerid) REFERENCES `users` (id);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

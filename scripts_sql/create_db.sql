DROP DATABASE IF EXISTS `demodb_1`;
CREATE DATABASE `demodb_1`;
CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `zipcode` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `demodb_1`.`videos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `year` INT(4) NULL,
  `genre` VARCHAR(45) NULL,
  `synopsis` TEXT(1000) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `demodb_1`.`rentals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_video` VARCHAR(45) NULL,
  `id_customer` VARCHAR(45) NULL,
  `start` DATETIME NULL,
  `stop` DATETIME NULL,
  PRIMARY KEY (`id`));

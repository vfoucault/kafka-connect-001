DROP DATABASE IF EXISTS `demodb_1`;
CREATE DATABASE `demodb_1`;
CREATE TABLE `demodb_1`.`records` (
  `record_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) DEFAULT NULL,
  `data` VARCHAR(256) DEFAULT NULL,
  PRIMARY KEY (`record_id`));

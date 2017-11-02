USE `demodb_1`;
DROP procedure IF EXISTS `insert_rows`;

DELIMITER $$
USE `demodb_1`$$
CREATE DEFINER=`root`@`%` PROCEDURE `insert_rows`(IN nbs INT)
BEGIN
	DECLARE i INT DEFAULT 0;
	WHILE i <= nbs DO
        INSERT INTO demodb_1.records (name, data) values ( left(uuid(), 8), SUBSTR(CONCAT(MD5(RAND()),MD5(RAND())),1,64) );
		SET i = i +1;
	END WHILE;
END$$

DELIMITER ;



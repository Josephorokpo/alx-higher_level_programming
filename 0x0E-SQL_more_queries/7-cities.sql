
-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create the table cities in the database hbtn_0d_usa on your MySQL server
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    `id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `state_id` INT NOT NULL,
    FOREIGN KEY (`state_id`) REFERENCES `states`(`id`),
    `name` VARCHAR(256) NOT NULL
);

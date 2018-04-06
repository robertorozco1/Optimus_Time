CREATE TABLE `User` (
	`fname` varchar(25) NOT NULL,
	`lname` varchar(25) NOT NULL,
	`employee_id` int NOT NULL UNIQUE,
	`role_id`  NOT NULL,
	`hours_week` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Role` (
	`role_id` int NOT NULL UNIQUE,
	`rolename` varchar(10) NOT NULL,
	PRIMARY KEY (`role_id`)
);

CREATE TABLE `Individual Schedule` (
	`employee_id`  NOT NULL,
	`monday` varchar(255) NOT NULL,
	`tuesday` varchar(255) NOT NULL,
	`wednesday` varchar(255) NOT NULL,
	`thursday` varchar(255) NOT NULL,
	`friday` varchar(255) NOT NULL,
	`saturday` varchar(255) NOT NULL,
	`sunday` varchar(255) NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Work Schedule` (
	`Week` int NOT NULL,
	`monday` BINARY NOT NULL,
	`tuesday` BINARY NOT NULL,
	`wednesday` BINARY NOT NULL,
	`thursday` BINARY NOT NULL,
	`friday` BINARY NOT NULL,
	`saturday` BINARY NOT NULL,
	`sunday` BINARY NOT NULL,
	PRIMARY KEY (`Week`)
);

CREATE TABLE `TimeOff` (
	`employee_id`  NOT NULL,
	`date` DATE NOT NULL,
	`status` BOOLEAN,
	`hours` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

ALTER TABLE `User` ADD CONSTRAINT `User_fk0` FOREIGN KEY (`role_id`) REFERENCES `Role`(`role_id`);

ALTER TABLE `Individual Schedule` ADD CONSTRAINT `Individual Schedule_fk0` FOREIGN KEY (`employee_id`) REFERENCES `User`(`employee_id`);

ALTER TABLE `TimeOff` ADD CONSTRAINT `TimeOff_fk0` FOREIGN KEY (`employee_id`) REFERENCES `User`(`employee_id`);


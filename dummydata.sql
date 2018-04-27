CREATE TABLE `User` (
  `fname` varchar(25) NOT NULL,
  `lname` varchar(25) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `hours_week` int(11) NOT NULL,
  `passwd` varchar(128) DEFAULT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Role` (
	`role_id` INT(11) NOT NULL UNIQUE,
	`rolename` varchar(10) NOT NULL,
	PRIMARY KEY (`role_id`)
);

CREATE TABLE `Availability` (
	`employee_id`  INT NOT NULL,
	`1` varchar(255) NOT NULL,
	`2` varchar(255) NOT NULL,
	`3` varchar(255) NOT NULL,
	`4` varchar(255) NOT NULL,
	`5` varchar(255) NOT NULL,
	`6` varchar(255) NOT NULL,
	`0` varchar(255) NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Work_Schedule` (
	`week_id` INT NOT NULL,
	`schedule` BINARY NOT NULL,
	PRIMARY KEY (`week_id`)
);

CREATE TABLE `TimeOff` (
	`employee_id`  INT NOT NULL,
	`date` DATE NOT NULL,
	`status` BOOLEAN,
	PRIMARY KEY (`employee_id`)
);


INSERT INTO `user` (`fname`, `lname`, `employee_id`, `role_id`, `hours_week`, `passwd`) VALUES
('Chaney', 'Ross', 1, 1, 15, '2dd00bd77e0222ced882665481a9c1d9f907309d16e05ed007a1ea63928477a9'),
('Indigo', 'Cooke', 2, 4, 36, 'e6f2ad814692e3f553d63a5535bfef46c030a680e6c3e79ee850dfcf5ae7798a'),
('Micah', 'Garza', 3, 7, 25, '9f165139a8c2894a47aea23b77d330eca847264224a44d5a17b19db8b9a72c08'),
('Michelle', 'Peters', 4, 10, 4, 'd353fb7a5f5b83cb82ebc17e22bdecd8f431ec38eef6435070586b89f4edf8c9'),
('Kamal', 'Gilmore', 5, 13, 37, '520cdb563bf80b193aab6aad62781a9647c75dbf76748117299c7dac0ae63a87'),
('Ursula', 'Boyle', 6, 16, 28, 'ab27b729d9cc4cb1c00960700446924159e9298d0f952aee3d55408b8e0b1b71'),
('Thane', 'Webster', 7, 19, 20, '2f2fc7f2e9ce13b09b84f63d54d0b4a59f4dbd46aea41da67023817e2d0c5e59'),
('Akeem', 'Kramer', 8, 22, 19, '978aebd56c3857a7ad73ff8ec48f30a5e84124ecdbc5bc4407876cd6eca9dd6d'),
('Jackson', 'Mcconnell', 9, 25, 16, '3158ff7128caa8c4111c93b0456bb320baba297a5628bfcd2399e4d2c73a7312'),
('April', 'Gonzales', 10, 28, 7, '4a69d282e9d8565a45871936d3dc0d5f72d4d64f1bf09e20dfbe67e151e0dfbc'),
('Buffy', 'Middleton', 11, 31, 4, NULL),
('Rana', 'Huber', 12, 34, 25, NULL),
('Colleen', 'Hansen', 13, 37, 28, NULL),
('Boris', 'Anthony', 14, 40, 23, NULL),
('Dai', 'Witt', 15, 43, 4, NULL),
('Iliana', 'Leach', 16, 46, 2, NULL),
('Erasmus', 'Haynes', 17, 49, 30, NULL),
('Madeline', 'Whitehead', 18, 52, 24, NULL),
('Deanna', 'Guerra', 19, 55, 4, NULL),
('Ivana', 'Knox', 20, 58, 40, NULL),
('Martha', 'Goodwin', 21, 61, 8, NULL),
('Aristotle', 'Dickson', 22, 64, 15, NULL),
('Arthur', 'Sykes', 23, 67, 2, NULL),
('Octavius', 'Bauer', 24, 70, 4, NULL),
('Lydia', 'Banks', 25, 73, 13, NULL),
('Mufutau', 'Douglas', 26, 76, 29, NULL),
('Xavier', 'Johnson', 27, 79, 14, NULL),
('Burke', 'Howell', 28, 82, 20, NULL),
('Eric', 'Workman', 29, 85, 14, NULL),
('Brian', 'Fischer', 30, 88, 25, NULL),
('Miranda', 'Valenzuela', 31, 91, 20, NULL),
('Malik', 'Lara', 32, 94, 15, NULL),
('Nissim', 'Farmer', 33, 97, 32, NULL),
('Stewart', 'Palmer', 34, 100, 16, NULL),
('Evelyn', 'Tucker', 35, 103, 23, NULL),
('Jarrod', 'Valenzuela', 36, 106, 0, NULL),
('Derek', 'Hudson', 37, 109, 5, NULL),
('Blaine', 'Lowe', 38, 112, 10, NULL),
('Miriam', 'Christian', 39, 115, 29, NULL),
('Kane', 'Porter', 40, 118, 10, NULL),
('Ainsley', 'Dodson', 41, 121, 1, NULL),
('Elijah', 'Mcclure', 42, 124, 37, NULL),
('Brock', 'Ellis', 43, 127, 17, NULL),
('Carissa', 'Moody', 44, 130, 2, NULL),
('Joel', 'Waters', 45, 133, 29, NULL),
('Kaden', 'Livingston', 46, 136, 17, NULL),
('Slade', 'Lane', 47, 139, 17, NULL),
('Kaden', 'Bell', 48, 142, 22, NULL),
('Leonard', 'Jacobson', 49, 145, 6, NULL),
('Maile', 'Compton', 50, 148, 39, NULL);


INSERT INTO `TimeOff` (`employee_id`,`date`,`status`) VALUES (1,"2018-07-19 21:47:06",2),(2,"2017-09-26 18:15:29",0),(3,"2018-12-10 13:08:39",1),(4,"2017-10-25 02:16:02",0),(5,"2018-08-02 06:47:45",2),(6,"2018-07-07 09:41:30",1),(7,"2018-05-21 14:20:49",0),(8,"2018-06-11 05:46:40",1),(9,"2018-09-14 00:13:05",0),(10,"2019-01-24 23:48:17",0);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`) VALUES (11,"2017-10-01 14:05:14",2),(12,"2017-05-20 01:41:17",0),(13,"2017-05-19 10:20:39",1),(14,"2017-07-08 21:29:20",2),(15,"2018-02-28 06:25:40",0),(16,"2019-02-15 15:41:13",2),(17,"2017-12-18 07:57:45",2),(18,"2018-11-18 00:09:46",2),(19,"2019-02-18 21:58:14",2),(20,"2018-10-14 19:14:40",0);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`) VALUES (21,"2017-12-31 14:36:23",2),(22,"2019-03-31 20:48:58",0),(23,"2019-02-22 06:34:49",1),(24,"2017-07-14 14:52:49",1),(25,"2018-09-25 08:42:57",0),(26,"2018-02-06 18:44:03",2),(27,"2017-09-11 12:29:57",1),(28,"2018-10-04 20:52:35",1),(29,"2017-05-03 05:34:28",1),(30,"2019-02-14 07:31:34",1);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`) VALUES (31,"2018-02-27 23:39:08",2),(32,"2017-05-25 17:22:15",0),(33,"2018-12-16 00:45:28",0),(34,"2018-04-08 07:08:58",1),(35,"2018-11-20 08:38:47",2),(36,"2018-06-29 04:01:59",1),(37,"2018-01-10 22:05:00",0),(38,"2017-12-14 11:47:28",0),(39,"2017-07-21 00:41:02",2),(40,"2017-08-06 10:33:09",1);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`) VALUES (41,"2017-12-16 07:48:27",0),(42,"2018-10-19 11:46:03",1),(43,"2018-11-12 05:41:54",0),(44,"2017-10-23 12:03:29",2),(45,"2019-03-25 17:24:10",0),(46,"2018-05-20 03:06:56",0),(47,"2018-02-12 12:33:13",0),(48,"2018-07-11 05:50:57",2),(49,"2017-11-26 03:42:42",2),(50,"2017-08-26 11:07:23",0);

INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (1, '(0600,0800)', '(1000,1200)', '(2200,2400)', '(2200,2400)', '(0800,1000)', '(0200,0400)', '(0400,0600)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (2, '(1800,2000)', '(1600,1800)', '(2000,2200)', '(0200,0400)', '(0800,1000)', '(0200,0400)', '(2200,2400)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (3, '(1200,1400)', '(2000,2200)', '(0800,1000)', '(0600,0800)', '(1600,1800)', '(0000,0200)', '(1400,1600)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (4, '(2000,2200)', '(1200,1400)', '(2200,2400)', '(2200,2400)', '(0800,1000)', '(2000,2200)', '(2000,2200)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (5, '(2000,2200)', '(0400,0600)', '(0600,0800)', '(1200,1400)', '(0800,1000)', '(1200,1400)', '(0200,0400)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (6, '(0400,0600)', '(1200,1400)', '(0400,0600)', '(1200,1400)', '(1400,1600)', '(1600,1800)', '(1400,1600)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (7, '(0600,0800)', '(0200,0400)', '(1600,1800)', '(0000,0200)', '(1200,1400)', '(0600,0800)', '(1400,1600)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (8, '(2000,2200)', '(0400,0600)', '(1600,1800)', '(2200,2400)', '(0200,0400)', '(0000,0200)', '(1600,1800)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (9, '(0200,0400)', '(1200,1400)', '(1600,1800)', '(0800,1000)', '(1000,1200)', '(2000,2200)', '(0400,0600)');
INSERT INTO Availability (employee_id, `1`, `2`, `3`, `4`, `5`, `6`, `0`) values (10, '(0600,0800)', '(1000,1200)', '(2200,2400)', '(2200,2400)', '(1200,1400)', '(1000,1200)', '(0600,0800)');

CREATE TABLE `User` (
	`fname` varchar(25) NOT NULL,
	`lname` varchar(25) NOT NULL,
	`employee_id` INT NOT NULL UNIQUE,
	`role_id` INT NOT NULL,
	`hours_week` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Role` (
	`role_id` INT NOT NULL UNIQUE,
	`rolename` varchar(10) NOT NULL,
	PRIMARY KEY (`role_id`)
);

CREATE TABLE `Availability` (
	`employee_id`  INT NOT NULL,
	`monday` varchar(255) NOT NULL,
	`tuesday` varchar(255) NOT NULL,
	`wednesday` varchar(255) NOT NULL,
	`thursday` varchar(255) NOT NULL,
	`friday` varchar(255) NOT NULL,
	`saturday` varchar(255) NOT NULL,
	`sunday` varchar(255) NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Work_Schedule` (
	`Week` INT NOT NULL,
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
	`employee_id`  INT NOT NULL,
	`date` DATE NOT NULL,
	`status` BOOLEAN,
	`hours` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);


INSERT INTO `User` (`fname`,`lname`,`employee_id`,`role_id`,`hours_week`) VALUES ("Chaney","Ross",1,1,15),("Indigo","Cooke",2,4,36),("Micah","Garza",3,7,25),("Michelle","Peters",4,10,4),("Kamal","Gilmore",5,13,37),("Ursula","Boyle",6,16,28),("Thane","Webster",7,19,20),("Akeem","Kramer",8,22,19),("Jackson","Mcconnell",9,25,16),("April","Gonzales",10,28,7);
INSERT INTO `User` (`fname`,`lname`,`employee_id`,`role_id`,`hours_week`) VALUES ("Buffy","Middleton",11,31,4),("Rana","Huber",12,34,25),("Colleen","Hansen",13,37,28),("Boris","Anthony",14,40,23),("Dai","Witt",15,43,4),("Iliana","Leach",16,46,2),("Erasmus","Haynes",17,49,30),("Madeline","Whitehead",18,52,24),("Deanna","Guerra",19,55,4),("Ivana","Knox",20,58,40);
INSERT INTO `User` (`fname`,`lname`,`employee_id`,`role_id`,`hours_week`) VALUES ("Martha","Goodwin",21,61,8),("Aristotle","Dickson",22,64,15),("Arthur","Sykes",23,67,2),("Octavius","Bauer",24,70,4),("Lydia","Banks",25,73,13),("Mufutau","Douglas",26,76,29),("Xavier","Johnson",27,79,14),("Burke","Howell",28,82,20),("Eric","Workman",29,85,14),("Brian","Fischer",30,88,25);
INSERT INTO `User` (`fname`,`lname`,`employee_id`,`role_id`,`hours_week`) VALUES ("Miranda","Valenzuela",31,91,20),("Malik","Lara",32,94,15),("Nissim","Farmer",33,97,32),("Stewart","Palmer",34,100,16),("Evelyn","Tucker",35,103,23),("Jarrod","Valenzuela",36,106,0),("Derek","Hudson",37,109,5),("Blaine","Lowe",38,112,10),("Miriam","Christian",39,115,29),("Kane","Porter",40,118,10);
INSERT INTO `User` (`fname`,`lname`,`employee_id`,`role_id`,`hours_week`) VALUES ("Ainsley","Dodson",41,121,1),("Elijah","Mcclure",42,124,37),("Brock","Ellis",43,127,17),("Carissa","Moody",44,130,2),("Joel","Waters",45,133,29),("Kaden","Livingston",46,136,17),("Slade","Lane",47,139,17),("Kaden","Bell",48,142,22),("Leonard","Jacobson",49,145,6),("Maile","Compton",50,148,39);


INSERT INTO `TimeOff` (`employee_id`,`date`,`status`,`hours`) VALUES (1,"2018-07-19 21:47:06",2,6),(2,"2017-09-26 18:15:29",0,2),(3,"2018-12-10 13:08:39",1,8),(4,"2017-10-25 02:16:02",0,4),(5,"2018-08-02 06:47:45",2,5),(6,"2018-07-07 09:41:30",1,0),(7,"2018-05-21 14:20:49",0,3),(8,"2018-06-11 05:46:40",1,5),(9,"2018-09-14 00:13:05",0,7),(10,"2019-01-24 23:48:17",0,5);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`,`hours`) VALUES (11,"2017-10-01 14:05:14",2,3),(12,"2017-05-20 01:41:17",0,1),(13,"2017-05-19 10:20:39",1,2),(14,"2017-07-08 21:29:20",2,6),(15,"2018-02-28 06:25:40",0,8),(16,"2019-02-15 15:41:13",2,0),(17,"2017-12-18 07:57:45",2,5),(18,"2018-11-18 00:09:46",2,0),(19,"2019-02-18 21:58:14",2,7),(20,"2018-10-14 19:14:40",0,7);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`,`hours`) VALUES (21,"2017-12-31 14:36:23",2,1),(22,"2019-03-31 20:48:58",0,3),(23,"2019-02-22 06:34:49",1,8),(24,"2017-07-14 14:52:49",1,5),(25,"2018-09-25 08:42:57",0,3),(26,"2018-02-06 18:44:03",2,8),(27,"2017-09-11 12:29:57",1,1),(28,"2018-10-04 20:52:35",1,7),(29,"2017-05-03 05:34:28",1,2),(30,"2019-02-14 07:31:34",1,8);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`,`hours`) VALUES (31,"2018-02-27 23:39:08",2,5),(32,"2017-05-25 17:22:15",0,5),(33,"2018-12-16 00:45:28",0,2),(34,"2018-04-08 07:08:58",1,1),(35,"2018-11-20 08:38:47",2,7),(36,"2018-06-29 04:01:59",1,5),(37,"2018-01-10 22:05:00",0,5),(38,"2017-12-14 11:47:28",0,8),(39,"2017-07-21 00:41:02",2,4),(40,"2017-08-06 10:33:09",1,5);
INSERT INTO `TimeOff` (`employee_id`,`date`,`status`,`hours`) VALUES (41,"2017-12-16 07:48:27",0,8),(42,"2018-10-19 11:46:03",1,2),(43,"2018-11-12 05:41:54",0,6),(44,"2017-10-23 12:03:29",2,8),(45,"2019-03-25 17:24:10",0,1),(46,"2018-05-20 03:06:56",0,8),(47,"2018-02-12 12:33:13",0,4),(48,"2018-07-11 05:50:57",2,6),(49,"2017-11-26 03:42:42",2,7),(50,"2017-08-26 11:07:23",0,0);

INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (1, '6-8', '10-12', '22-24', '22-24', '8-10', '2-4', '4-6');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (2, '18-20', '16-18', '20-22', '2-4', '8-10', '2-4', '22-24');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (3, '12-14', '20-22', '8-10', '6-8', '16-18', '0-2', '14-16');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (4, '20-22', '12-14', '22-24', '22-24', '8-10', '20-22', '20-22');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (5, '20-22', '4-6', '6-8', '12-14', '8-10', '12-14', '2-4');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (6, '4-6', '12-14', '4-6', '12-14', '14-16', '16-18', '14-16');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (7, '6-8', '2-4', '16-18', '0-2', '12-14', '6-8', '14-16');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (8, '20-22', '4-6', '16-18', '22-24', '2-4', '0-2', '16-18');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (9, '2-4', '12-14', '16-18', '8-10', '10-12', '20-22', '4-6');
INSERT INTO Availability (employee_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) values (10, '6-8', '10-12', '22-24', '22-24', '12-14', '10-12', '6-8');

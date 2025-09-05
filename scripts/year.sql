
drop table `year`;
CREATE TABLE `year` (
  `year_id` bigint NOT NULL AUTO_INCREMENT,
  `is_active` bit(1) DEFAULT 1,
  `is_deleted` bit(1) DEFAULT 0,
  `name` int NOT NULL,
  PRIMARY KEY (`year_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


truncate table `year` ;
select * from year;


insert into `year` (name) values ('1999');
insert into `year` (name) values ('2000');
insert into `year` (name) values ('2001');
insert into `year` (name) values ('2002');
insert into `year` (name) values ('2003');
insert into `year` (name) values ('2004');
insert into `year` (name) values ('2005');

insert into `year` (name) values ('2006');
insert into `year` (name) values ('2007');
insert into `year` (name) values ('2008');
insert into `year` (name) values ('2009');
insert into `year` (name) values ('2010');
insert into `year` (name) values ('2011');
insert into `year` (name) values ('2012');
insert into `year` (name) values ('2013');
insert into `year` (name) values ('2014');
insert into `year` (name) values ('2015');
insert into `year` (name) values ('2016');
insert into `year` (name) values ('2017');
insert into `year` (name) values ('2018');
insert into `year` (name) values ('2019');
insert into `year` (name) values ('2020');
insert into `year` (name) values ('2021');
insert into `year` (name) values ('2022');
insert into `year` (name) values ('2023');
insert into `year` (name) values ('2024');
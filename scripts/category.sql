drop table `category`;

CREATE TABLE `category` (
  `category_id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `is_active` bit(1) DEFAULT 1,
  `is_deleted` bit(1) DEFAULT 0,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

truncate table `category` ;

select * from category c ;



insert into `category` (name, description) values ('Brake Pads', 'Brake Pads Desc');
insert into `category` (name, description) values ('Oil Filter', 'Oil Filter Desc');
insert into `category` (name, description) values ('Air Filter', 'Air Filter Desc');
insert into `category` (name, description) values ('Radiator', 'Radiator Desc');
insert into `category` (name, description) values ('Timing Belt', 'Timing Belt Desc');
insert into `category` (name, description) values ('Alternator', 'Alternator Desc');
insert into `category` (name, description) values ('Spark Plug', 'Spark Plug Desc');
insert into `category` (name, description) values ('Battery', 'Battery Desc');
insert into `category` (name, description) values ('Headlight', 'Headlight Desc');
insert into `category` (name, description) values ('Fuel Pump', 'Fuel Pump Desc');
insert into `category` (name, description) values ('Water Pump', 'Water Pump Desc');
insert into `category` (name, description) values ('Brake Disc', 'Brake Disc Desc');
insert into `category` (name, description) values ('Windshield Wiper', 'Windshield Wiper Desc');
insert into `category` (name, description) values ('Exhaust Pipe', 'Exhaust Pipe Desc');
insert into `category` (name, description) values ('Tire', 'Tire Desc');
ALTER TABLE autoparts.model DROP FOREIGN KEY FKfvdrvechg4dtwo64ut3g01hu4;

-- autoparts.make definition
drop table `make`;

CREATE TABLE `make` (
  `make_id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` bit(1) DEFAULT 0,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`make_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

truncate table `make` ;

select * from make m ;

insert into `make` (name) values ('Toyota');
insert into `make` (name) values ('Honda');
insert into `make` (name) values ('Ford');
insert into `make` (name) values ('Mercedes Benz');
insert into `make` (name) values ('BMW');
insert into `make` (name) values ('Hyundai');
insert into `make` (name) values ('Nissan');
insert into `make` (name) values ('Chevrolet');
insert into `make` (name) values ('Volkswagen');
insert into `make` (name) values ('Audi');
insert into `make` (name) values ('Kia');
insert into `make` (name) values ('Mazda');
insert into `make` (name) values ('Subaru');
insert into `make` (name) values ('Lexus');
insert into `make` (name) values ('Jaguar');
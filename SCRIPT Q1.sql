create table VEHICLE(
VCODE varchar(3),
VEHICLETYPE varchar(20),
PERKM int(3));
insert into VEHICLE values
('V01','VOLVO BUS',150),
('V02','AC DELUXE BUS',125),
('V03','ORDINARY BUS',80),
('V05','SUV',30),
('V04','CAR',18);
CREATE table TRAVEL(
CNO INT(3),
CNAME varchar(20),
TRAVELDATE DATE,
KM INT(3),
VCODE varchar(3),
NOP INT(2));
insert into TRAVEL values
(101,'K. Niwal','2015-12-13',200,'V01',32),
(103,'Fredrick Sym','2016-03-21',120,'V03',45),
(105,'Hitesh Jain','2016-04-23',450,'V02',42),
(102,'Ravi Anish','2016-01-13',080,'V02',40),
(107,'John Malina','2015-02-10',065,'V04',02),
(104,'Sahanubhuti','2016-01-28',090,'V05',04),
(106,'Ramesh Jaya','2016-04-06',100,'V01',25);
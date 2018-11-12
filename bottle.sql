create database `hctf` ;

use hctf;

-- 建表
DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `created_at` bigint(40) DEFAULT NULL,
  `last_modified` bigint(40) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


create table `users`(
    `id` int not null auto_increment,
    `username` char(20) not null,
    `password` char(60) null,
    primary key(id)
)engine=InnoDB;

DROP TABLE IF EXISTS `url`;

create table `url`(
    `id` int not null auto_increment,
    `userId` int not null,
    `url` char(255),
    primary key(id)
)engine=InnoDB;

-- 插入数据
INSERT INTO `users` ( `username`, `password`)
VALUES
    ('Lou00','dc7bc23f4fdd5bd11f25ed50201676e1');
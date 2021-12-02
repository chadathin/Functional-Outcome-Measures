DROP TABLE IF EXISTS assessments;

CREATE TABLE `assessments` (
  `id` int(32) AUTO_INCREMENT NOT NULL,
  `unique_ident`varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `score` int(32) NOT NULL,
  PRIMARY KEY(`id`)
);

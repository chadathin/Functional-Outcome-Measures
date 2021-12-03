DROP TABLE IF EXISTS assessments;

CREATE TABLE `assessments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `unique_ident` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
  `name` VARCHAR(255) NOT NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
  `score` INT(11) NOT NULL DEFAULT '0',
  `date_performed` DATE NOT NULL DEFAULT curdate(),
  `age` INT(11) NULL DEFAULT NULL,
  `sex` CHAR(1) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
  `weight` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
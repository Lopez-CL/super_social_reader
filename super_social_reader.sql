-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema super_social_reader
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `super_social_reader` ;

-- -----------------------------------------------------
-- Schema super_social_reader
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `super_social_reader` DEFAULT CHARACTER SET utf8 ;
USE `super_social_reader` ;

-- -----------------------------------------------------
-- Table `super_social_reader`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `super_social_reader`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `super_social_reader`.`comics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `super_social_reader`.`comics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `title` VARCHAR(255) NULL,
  `author` VARCHAR(255) NULL,
  `artist` VARCHAR(255) NULL,
  `colorist` VARCHAR(255) NULL,
  `letterer` VARCHAR(255) NULL,
  `status` VARCHAR(255) NULL,
  `rating` INT NULL,
  `thought` TEXT NULL,
  `crated_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_comics_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comics_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `super_social_reader`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `super_social_reader`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `super_social_reader`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `comic_id` INT NOT NULL,
  `content` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_comics1_idx` (`comic_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `super_social_reader`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_comics1`
    FOREIGN KEY (`comic_id`)
    REFERENCES `super_social_reader`.`comics` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

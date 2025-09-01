CREATE DATABASE `app` 
CREATE TABLE `list` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TASK` text NOT NULL,
  `STATUS` enum('complete','incomplete') NOT NULL DEFAULT 'incomplete',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

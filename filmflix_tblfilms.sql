-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: filmflix
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblfilms`
--

DROP TABLE IF EXISTS `tblfilms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblfilms` (
  `filmId` int NOT NULL AUTO_INCREMENT,
  `title` varchar(40) DEFAULT NULL,
  `yearReleased` int DEFAULT NULL,
  `rating` varchar(3) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `genre` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`filmId`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblfilms`
--

LOCK TABLES `tblfilms` WRITE;
/*!40000 ALTER TABLE `tblfilms` DISABLE KEYS */;
INSERT INTO `tblfilms` VALUES (1,'Getaway Team',1996,'U',110,'comedy'),(2,'The Family Secret',2022,'U',149,'drama'),(3,'Thackeray',1993,'PG',117,'comedy'),(4,'Arapahoe Squaw',2022,'PG',112,'drama'),(5,'The Ultimate Realisation',2018,'U',110,'comedy'),(6,'Hauk ',2019,'PG',76,'mystery'),(7,'Reinke',1961,'U',114,'documentary'),(8,'Klein Dapin',2014,'15',82,'documentary'),(9,'Onsgard Conspiracy',1964,'15',140,'mystery'),(10,'Mccormick Disappearance',1988,'12A',120,'mystery'),(11,'Corscot Run',2012,'12A',122,'drama'),(12,'Fly by Wire',1990,'PG',110,'drama'),(13,'Sunfield',2003,'12A',69,'action'),(15,'Harper',1977,'12A',88,'comedy'),(16,'Laurel Returns',1990,'U',131,'action'),(17,'Bartelt Goes Fishing',1994,'18',127,'comedy'),(18,'Holmberg ',1964,'PG',117,'science fiction'),(19,'The Reindahl',1987,'18',125,'action'),(20,'Father Hintze',1967,'PG',66,'mystery'),(21,'American Citizen',1974,'PG',134,'drama'),(22,'Sunbrook Supremacy',2018,'PG',117,'action'),(23,'Welch at Home',1993,'U',118,'documentary'),(24,'Decoy Deception',2011,'18',92,'science fiction'),(25,'Fair Oaks',1998,'15',121,'documentary'),(26,'Susan',2018,'18',60,'mystery'),(27,'Brothers Hudson',1982,'PG',143,'comedy'),(28,'Independence Today',1989,'15',88,'action'),(29,'Oriole',1961,'18',63,'science fiction'),(30,'Magdeline Challin',1996,'PG',86,'drama'),(31,'Duke\'s Calling',1977,'PG',120,'drama'),(33,'Darwin in Venice',1977,'15',135,'mystery'),(34,'Daystar',1987,'18',91,'science fiction'),(35,'Moulton in Germany',1985,'18',73,'documentary'),(36,'The Yeti',2004,'18',125,'mystery'),(37,'Runaway Robot',2022,'PG',90,'science fiction'),(38,'Merryweather',1998,'U',94,'comedy'),(39,'The Gold Seeker',2008,'PG',112,'action'),(41,'Journey to Mars',2022,'PG',138,'science fiction'),(43,'Hubble Trouble',2001,'U',68,'documentary'),(49,'The Hulk',1984,'12A',93,''),(51,'Desert Crater',2010,'PG',110,'science fiction'),(55,'Emperor Claudius',1995,'18',114,'drama'),(59,'The Family Secret',2022,'12A',149,'drama'),(60,'Getaway Team',1996,'15',110,'action'),(62,'Thackeray',1993,'15',117,'comedy'),(68,'Return of the Guru',1985,'15',96,'mystery');
/*!40000 ALTER TABLE `tblfilms` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-15 12:57:32

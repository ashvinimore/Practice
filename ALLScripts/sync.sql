-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: 192.168.10.13    Database: DataWarehouse
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `SyncDetails`
--

LOCK TABLES `SyncDetails` WRITE;
/*!40000 ALTER TABLE `SyncDetails` DISABLE KEYS */;
INSERT INTO `SyncDetails` VALUES (1,'Attribute',NULL,'AttID'),(2,'Calendar',NULL,NULL),(3,'CoAttribute',NULL,'SecurityID'),(4,'Company',NULL,'CoID'),(5,'CoSecurity',NULL,NULL),(6,'Country',NULL,NULL),(7,'Currency',NULL,NULL),(8,'DataType',NULL,NULL),(9,'Exchange',NULL,NULL),(10,'GICS',NULL,NULL),(11,'Other',NULL,NULL),(12,'Products',NULL,NULL),(13,'Segment',NULL,NULL),(14,'Regions',NULL,NULL),(15,'Unit',NULL,NULL),(16,'GlobalElement',NULL,NULL),(17,'Period',NULL,NULL);
/*!40000 ALTER TABLE `SyncDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'DataWarehouse'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-01 10:24:58

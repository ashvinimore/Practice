-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: 192.168.10.13    Database: Zeus
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
-- Dumping data for table `DWHMainQuery`
--

LOCK TABLES `DWHMainQuery` WRITE;
/*!40000 ALTER TABLE `DWHMainQuery` DISABLE KEYS */;
INSERT INTO `DWHMainQuery` VALUES (1,'160','None','None','None','None'),(2,'176','None','None','None','None'),(3,'177','None','None','None','None'),(4,'182','None','None','None','None'),(5,'173','None','None','None','None'),(6,'185','None','None','None','None'),(7,'186','None','None','None','None'),(8,'174','None','None','None','None'),(9,'175','None','None','None','None'),(10,'189','None','None','None','None'),(11,'190','None','None','None','None'),(12,'191','None','None','None','None'),(13,'192','None','None','None','None'),(14,'193','None','None','None','None'),(15,'194','None','None','None','None'),(16,'195','None','None','None','None'),(17,'196','None','None','None','None'),(18,'197','None','None','None','None'),(19,'198','None','None','None','None'),(20,'199','None','None','None','None'),(21,'200','None','None','None','None'),(22,'169','None','None','None','None'),(23,'170','None','None','None','None'),(24,'171','None','None','None','None'),(25,'172','None','None','None','None'),(26,'201','None','None','None','None'),(27,'202','None','None','None','None'),(28,'203','None','None','None','None'),(29,'204','None','None','None','None'),(30,'205','None','None','None','None'),(31,'206','None','None','None','None'),(32,'207','None','None','None','None'),(33,'208','None','None','None','None'),(34,'168','None','None','None','None'),(35,'209','None','None','None','None'),(36,'210','None','None','None','None'),(37,'211','None','None','None','None'),(38,'216','None','None','None','None'),(39,'167','None','None','None','None'),(40,'212','None','None','None','None'),(41,'213','None','None','None','None'),(42,'214','None','None','None','None'),(43,'215','None','None','None','None'),(44,'166','None','None','None','None'),(45,'161','None','None','None','None'),(46,'162','None','None','None','None'),(47,'163','None','None','None','None'),(48,'164','None','None','None','None'),(49,'165','None','None','None','None'),(50,'1','None','None','None','None'),(51,'2','None','None','None','None'),(52,'64','None','None','None','None'),(53,'65','None','None','None','None'),(54,'66','None','None','None','None'),(55,'14','None','None','None','None'),(56,'15','None','None','None','None'),(57,'16','None','None','None','None'),(58,'17','None','None','None','None'),(59,'18','None','None','None','None'),(60,'19','None','None','None','None'),(61,'20','None','None','None','None'),(62,'21','None','None','None','None'),(63,'22','None','None','None','None'),(64,'23','None','None','None','None'),(65,'24','None','None','None','None'),(66,'25','None','None','None','None'),(67,'26','None','None','None','None'),(68,'27','None','None','None','None'),(69,'7','None','None','None','None'),(70,'67','None','None','None','None'),(71,'68','None','None','None','None'),(72,'28','None','None','None','None'),(73,'29','None','None','None','None'),(74,'69','None','None','None','None'),(75,'70','None','None','None','None'),(76,'30','None','None','None','None'),(77,'31','None','None','None','None'),(78,'32','None','None','None','None'),(79,'33','None','None','None','None'),(80,'34','None','None','None','None'),(81,'35','None','None','None','None'),(82,'36','None','None','None','None'),(83,'37','None','None','None','None'),(84,'38','None','None','None','None'),(85,'39','None','None','None','None'),(86,'40','None','None','None','None'),(87,'6','None','None','None','None'),(88,'4','None','None','None','None'),(89,'3','None','None','None','None'),(90,'41','None','None','None','None'),(91,'42','None','None','None','None'),(92,'43','None','None','None','None'),(93,'44','None','None','None','None'),(94,'45','None','None','None','None'),(95,'46','None','None','None','None'),(96,'47','None','None','None','None'),(97,'48','None','None','None','None'),(98,'49','None','None','None','None'),(99,'50','None','None','None','None'),(100,'71','None','None','None','None'),(101,'72','None','None','None','None'),(102,'51','None','None','None','None'),(103,'52','None','None','None','None'),(104,'220','None','None','None','None'),(105,'13','None','None','None','None'),(106,'8','None','None','None','None'),(107,'53','None','None','None','None'),(108,'54','None','None','None','None'),(109,'55','None','None','None','None'),(110,'56','None','None','None','None'),(111,'218','None','None','None','None'),(112,'57','None','None','None','None'),(113,'58','None','None','None','None'),(114,'59','None','None','None','None'),(115,'60','None','None','None','None'),(116,'61','None','None','None','None'),(117,'11','None','None','None','None'),(118,'12','None','None','None','None'),(119,'9','None','None','None','None'),(120,'79','None','None','None','None'),(121,'80','None','None','None','None'),(122,'73','None','None','None','None'),(123,'74','None','None','None','None'),(124,'75','None','None','None','None'),(125,'76','None','None','None','None'),(126,'77','None','None','None','None'),(127,'78','None','None','None','None'),(128,'62','None','None','None','None'),(129,'63','None','None','None','None'),(130,'10','None','None','None','None'),(131,'5','None','None','None','None'),(132,'81','None','None','None','None'),(133,'85','None','None','None','None'),(134,'93','None','None','None','None'),(135,'94','None','None','None','None'),(136,'96','None','None','None','None'),(137,'97','None','None','None','None'),(138,'98','None','None','None','None'),(139,'99','None','None','None','None'),(140,'100','None','None','None','None'),(141,'101','None','None','None','None'),(142,'102','None','None','None','None'),(143,'103','None','None','None','None'),(144,'104','None','None','None','None'),(145,'105','None','None','None','None'),(146,'106','None','None','None','None'),(147,'107','None','None','None','None'),(148,'108','None','None','None','None'),(149,'109','None','None','None','None'),(150,'110','None','None','None','None'),(151,'219','None','None','None','None'),(152,'111','None','None','None','None'),(153,'95','None','None','None','None'),(154,'112','None','None','None','None'),(155,'113','None','None','None','None'),(156,'114','None','None','None','None'),(157,'115','None','None','None','None'),(158,'116','None','None','None','None'),(159,'117','None','None','None','None'),(160,'118','None','None','None','None'),(161,'119','None','None','None','None'),(162,'120','None','None','None','None'),(163,'121','None','None','None','None'),(164,'122','None','None','None','None'),(165,'123','None','None','None','None'),(166,'88','None','None','None','None'),(167,'86','None','None','None','None'),(168,'132','None','None','None','None'),(169,'133','None','None','None','None'),(170,'124','None','None','None','None'),(171,'134','None','None','None','None'),(172,'135','None','None','None','None'),(173,'125','None','None','None','None'),(174,'136','None','None','None','None'),(175,'137','None','None','None','None'),(176,'126','None','None','None','None'),(177,'138','None','None','None','None'),(178,'139','None','None','None','None'),(179,'127','None','None','None','None'),(180,'128','None','None','None','None'),(181,'129','None','None','None','None'),(182,'130','None','None','None','None'),(183,'131','None','None','None','None'),(184,'89','None','None','None','None'),(185,'87','None','None','None','None'),(186,'148','None','None','None','None'),(187,'149','None','None','None','None'),(188,'140','None','None','None','None'),(189,'150','None','None','None','None'),(190,'151','None','None','None','None'),(191,'141','None','None','None','None'),(192,'152','None','None','None','None'),(193,'153','None','None','None','None'),(194,'142','None','None','None','None'),(195,'154','None','None','None','None'),(196,'155','None','None','None','None'),(197,'143','None','None','None','None'),(198,'156','None','None','None','None'),(199,'157','None','None','None','None'),(200,'217','None','None','None','None'),(201,'159','None','None','None','None'),(202,'144','None','None','None','None'),(203,'145','None','None','None','None'),(204,'146','None','None','None','None'),(205,'147','None','None','None','None'),(206,'90','None','None','None','None'),(207,'91','None','None','None','None'),(208,'92','None','None','None','None'),(209,'83','None','None','None','None'),(210,'84','None','None','None','None'),(211,'82','None','None','None','None'),(212,'1630','None','None','None','None'),(213,'158','None','None','None','None'),(214,'1089','None','None','None','None'),(215,'1820','None','None','None','None'),(216,'173','1','None','None','9'),(217,'173','1','None','2','9'),(218,'173','1','None','6','9'),(219,'173','1','None','107','9'),(220,'173','2','None','None','9'),(221,'173','2','None','2','9'),(222,'173','2','None','6','9'),(223,'173','2','None','107','9'),(224,'173','None','None','2','0'),(225,'173','None','None','6','0'),(226,'173','None','None','107','0'),(227,'173','None','None','None','Avg of 4 quarter'),(228,'6066','None','None','None','None'),(229,'6066','1','None','None','9'),(230,'6066','2','None','None','9'),(231,'174','1','None','None','9'),(232,'174','2','None','None','9'),(233,'175','1','None','None','9'),(234,'175','2','None','None','9');
/*!40000 ALTER TABLE `DWHMainQuery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `DWHMainQuery1`
--

LOCK TABLES `DWHMainQuery1` WRITE;
/*!40000 ALTER TABLE `DWHMainQuery1` DISABLE KEYS */;
/*!40000 ALTER TABLE `DWHMainQuery1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SchemaEx1`
--

LOCK TABLES `SchemaEx1` WRITE;
/*!40000 ALTER TABLE `SchemaEx1` DISABLE KEYS */;
INSERT INTO `SchemaEx1` VALUES (1,1,'1','2019-10-09',11),(2,1,'2','2019-10-09',34),(3,1,'3','2019-10-09',56),(4,1,'4','2019-10-09',32),(5,1,'5','2019-10-09',90),(6,2,'6','2019-10-09',78);
/*!40000 ALTER TABLE `SchemaEx1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SchemaEx2`
--

LOCK TABLES `SchemaEx2` WRITE;
/*!40000 ALTER TABLE `SchemaEx2` DISABLE KEYS */;
INSERT INTO `SchemaEx2` VALUES (1,1,'11','34','56','90','78','2019-10-09'),(2,2,'45','89','76','55','35','2019-10-09');
/*!40000 ALTER TABLE `SchemaEx2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SchemaEx3`
--

LOCK TABLES `SchemaEx3` WRITE;
/*!40000 ALTER TABLE `SchemaEx3` DISABLE KEYS */;
INSERT INTO `SchemaEx3` VALUES (1,11,45,66,'1','2019-10-09'),(2,45,89,90,'2','2019-10-09');
/*!40000 ALTER TABLE `SchemaEx3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SyncDetails`
--

LOCK TABLES `SyncDetails` WRITE;
/*!40000 ALTER TABLE `SyncDetails` DISABLE KEYS */;
INSERT INTO `SyncDetails` VALUES (1,'Attribute','2019-10-01','AttID'),(2,'Calendar',NULL,NULL),(3,'CoAttribute','2019-10-01','SecurityID'),(4,'Company','2019-10-01','CoID'),(5,'CoSecurity',NULL,NULL),(6,'Country',NULL,NULL),(7,'Currency',NULL,NULL),(8,'DataType',NULL,NULL),(9,'Exchange',NULL,NULL),(10,'GICS',NULL,NULL),(11,'Other',NULL,NULL),(12,'Products',NULL,NULL),(13,'Segment',NULL,NULL),(14,'Regions',NULL,NULL),(15,'Unit',NULL,NULL),(16,'GlobalElement',NULL,NULL),(17,'Period',NULL,NULL);
/*!40000 ALTER TABLE `SyncDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'Zeus'
--
/*!50003 DROP PROCEDURE IF EXISTS `Derived` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `Derived`()
BEGIN
DROP TABLE IF EXISTS DeCompany;
create table DeCompany
 
select Company.CoID,Company.CoName,Company.Description,Company.CountryID,Company.IntGICSID,Company.ExtGICSID,
Company.CoTypeID,CoAttribute.SecurityID as CoAttID,CoAttribute.CompSecInfoID,
CoAttribute.CurID,CoAttribute.UnitID,CoAttribute.ModeID,CoAttribute.SectorID, 
CoSecurity.SecurityID as CoSecID,CoSecurity.Ticker,CoSecurity.ISIN,
CoSecurity.CUSIP,CoSecurity.SEDOL,CoSecurity.MCaps,
CoSecurity.IsPrimary,CoSecurity.ListTypeID,CoSecurity.ExchangeID,
CoSecurity.DepReceipt from Company as Company 
INNER JOIN CoAttribute as CoAttribute ON Company.CoID = CoAttribute.CoID
 INNER JOIN CoSecurity as CoSecurity ON  Company.CoID = CoSecurity.CoID
 and CoSecurity.SecurityID = CoAttribute.SecurityID  ;

ALTER TABLE DeCompany ADD UID int NOT NULL AUTO_INCREMENT primary key;



END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-09 16:00:33

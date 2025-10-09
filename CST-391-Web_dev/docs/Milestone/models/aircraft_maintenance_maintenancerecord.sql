-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: aircraft_maintenance
-- ------------------------------------------------------
-- Server version	5.7.24

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
-- Table structure for table `maintenancerecord`
--

DROP TABLE IF EXISTS `maintenancerecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maintenancerecord` (
  `MaintenanceID` int(11) NOT NULL AUTO_INCREMENT,
  `AircraftID` int(11) NOT NULL,
  `MaintenanceDate` date NOT NULL,
  `Details` text NOT NULL,
  `Technician` varchar(100) DEFAULT NULL,
  `maintenanceType` varchar(20) DEFAULT NULL,
  `nextDueDate` date DEFAULT NULL,
  `maintenanceStatus` varchar(20) DEFAULT NULL,
  `maintenanceCategory` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`MaintenanceID`),
  KEY `AircraftID` (`AircraftID`),
  CONSTRAINT `maintenancerecord_ibfk_1` FOREIGN KEY (`AircraftID`) REFERENCES `aircraft` (`aircraftID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenancerecord`
--

LOCK TABLES `maintenancerecord` WRITE;
/*!40000 ALTER TABLE `maintenancerecord` DISABLE KEYS */;
INSERT INTO `maintenancerecord` VALUES (17,11,'2024-10-02','Replaced landing gear','Alice Johnson','Overhaul','2024-11-01','IN_PROGRESS','AIRFRAME'),(19,17,'2024-11-02','Replaced landing gear','Alice Johnson','Overhaul','2024-11-01','COMPLETED','AIRFRAME'),(20,9,'2024-11-07','Engine R&R Due\n','Owen','REPAIR','2024-12-06','SCHEDULED','ENGINE'),(21,9,'2024-11-19','CIP rack 3 requires card 34 R&R','Sarah Lindsey','INSPECTION','2024-11-14','IN_PROGRESS','AVIONICS'),(22,20,'2024-11-19','CIP rack 3 requires card 34 R&R','Sarah Lindsey','INSPECTION','2024-11-14','IN_PROGRESS','AVIONICS'),(23,19,'2024-11-19','CIP rack 3 requires card 34 R&R','Sarah Lindsey','INSPECTION','2024-11-14','IN_PROGRESS','AVIONICS'),(26,9,'2024-11-19','CIP rack 3 requires card 34 R&R','Sarah Lindsey','INSPECTION','2024-11-14','IN_PROGRESS','AVIONICS'),(27,9,'2024-11-19','CIP rack 3 requires card 34 R&R','Sarah Lindsey','INSPECTION','2024-11-14','IN_PROGRESS','AVIONICS');
/*!40000 ALTER TABLE `maintenancerecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-09 13:52:53

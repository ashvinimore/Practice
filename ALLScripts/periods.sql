-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.10.13    Database: Aletheia
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
-- Dumping data for table `Periods`
--

LOCK TABLES `Periods` WRITE;
/*!40000 ALTER TABLE `Periods` DISABLE KEYS */;
INSERT INTO `Periods` VALUES (200001,1,'H','H1 2000-01','2000-04-01 00:00:00','2000-09-30 00:00:00'),(200001,1,'Q','Q1 2000-01','2000-04-01 00:00:00','2000-06-30 00:00:00'),(200001,1,'Y','FY 2000-01','2000-04-01 00:00:00','2001-03-31 00:00:00'),(200001,2,'H','H2 2000-01','2000-10-01 00:00:00','2001-03-31 00:00:00'),(200001,2,'Q','Q2 2000-01','2000-07-01 00:00:00','2000-09-30 00:00:00'),(200001,3,'Q','Q3 2000-01','2000-10-01 00:00:00','2000-12-31 00:00:00'),(200001,4,'Q','Q4 2000-01','2001-01-01 00:00:00','2001-03-31 00:00:00'),(200102,1,'H','H1 2001-02','2001-04-01 00:00:00','2001-09-30 00:00:00'),(200102,1,'Q','Q1 2001-02','2001-04-01 00:00:00','2001-06-30 00:00:00'),(200102,1,'Y','FY 2001-02','2001-04-01 00:00:00','2002-03-31 00:00:00'),(200102,2,'H','H2 2001-02','2001-10-01 00:00:00','2002-03-31 00:00:00'),(200102,2,'Q','Q2 2001-02','2001-07-01 00:00:00','2001-09-30 00:00:00'),(200102,3,'Q','Q3 2001-02','2001-10-01 00:00:00','2001-12-31 00:00:00'),(200102,4,'Q','Q4 2001-02','2002-01-01 00:00:00','2002-03-31 00:00:00'),(200203,1,'H','H1 2002-03','2002-04-01 00:00:00','2002-09-30 00:00:00'),(200203,1,'Q','Q1 2002-03','2002-04-01 00:00:00','2002-06-30 00:00:00'),(200203,1,'Y','FY 2002-03','2002-04-01 00:00:00','2003-03-31 00:00:00'),(200203,2,'H','H2 2002-03','2002-10-01 00:00:00','2003-03-31 00:00:00'),(200203,2,'Q','Q2 2002-03','2002-07-01 00:00:00','2002-09-30 00:00:00'),(200203,3,'Q','Q3 2002-03','2002-10-01 00:00:00','2002-12-31 00:00:00'),(200203,4,'Q','Q4 2002-03','2003-01-01 00:00:00','2003-03-31 00:00:00'),(200304,1,'H','H1 2003-04','2003-04-01 00:00:00','2003-09-30 00:00:00'),(200304,1,'Q','Q1 2003-04','2003-04-01 00:00:00','2003-06-30 00:00:00'),(200304,1,'Y','FY 2003-04','2003-04-01 00:00:00','2004-03-31 00:00:00'),(200304,2,'H','H2 2003-04','2003-10-01 00:00:00','2004-03-31 00:00:00'),(200304,2,'Q','Q2 2003-04','2003-07-01 00:00:00','2003-09-30 00:00:00'),(200304,3,'Q','Q3 2003-04','2003-10-01 00:00:00','2003-12-31 00:00:00'),(200304,4,'Q','Q4 2003-04','2004-01-01 00:00:00','2004-03-31 00:00:00'),(200405,1,'H','H1 2004-05','2004-04-01 00:00:00','2004-09-30 00:00:00'),(200405,1,'Q','Q1 2004-05','2004-04-01 00:00:00','2004-06-30 00:00:00'),(200405,1,'Y','FY 2004-05','2004-04-01 00:00:00','2005-03-31 00:00:00'),(200405,2,'H','H2 2004-05','2004-10-01 00:00:00','2005-03-31 00:00:00'),(200405,2,'Q','Q2 2004-05','2004-07-01 00:00:00','2004-09-30 00:00:00'),(200405,3,'Q','Q3 2004-05','2004-10-01 00:00:00','2004-12-31 00:00:00'),(200405,4,'Q','Q4 2004-05','2005-01-01 00:00:00','2005-03-31 00:00:00'),(200506,1,'H','H1 2005-06','2005-04-01 00:00:00','2005-09-30 00:00:00'),(200506,1,'Q','Q1 2005-06','2005-04-01 00:00:00','2005-06-30 00:00:00'),(200506,1,'Y','FY 2005-06','2005-04-01 00:00:00','2006-03-31 00:00:00'),(200506,2,'H','H2 2005-06','2005-10-01 00:00:00','2006-03-31 00:00:00'),(200506,2,'Q','Q2 2005-06','2005-07-01 00:00:00','2005-09-30 00:00:00'),(200506,3,'Q','Q3 2005-06','2005-10-01 00:00:00','2005-12-31 00:00:00'),(200506,4,'Q','Q4 2005-06','2006-01-01 00:00:00','2006-03-31 00:00:00'),(200607,1,'H','H1 2006-07','2006-04-01 00:00:00','2006-09-30 00:00:00'),(200607,1,'Q','Q1 2006-07','2006-04-01 00:00:00','2006-06-30 00:00:00'),(200607,1,'Y','FY 2006-07','2006-04-01 00:00:00','2007-03-31 00:00:00'),(200607,2,'H','H2 2006-07','2006-10-01 00:00:00','2007-03-31 00:00:00'),(200607,2,'Q','Q2 2006-07','2006-07-01 00:00:00','2006-09-30 00:00:00'),(200607,3,'Q','Q3 2006-07','2006-10-01 00:00:00','2006-12-31 00:00:00'),(200607,4,'Q','Q4 2006-07','2007-01-01 00:00:00','2007-03-31 00:00:00'),(200708,1,'H','H1 2007-08','2007-04-01 00:00:00','2007-09-30 00:00:00'),(200708,1,'Q','Q1 2007-08','2007-04-01 00:00:00','2007-06-30 00:00:00'),(200708,1,'Y','FY 2007-08','2007-04-01 00:00:00','2008-03-31 00:00:00'),(200708,2,'H','H2 2007-08','2007-10-01 00:00:00','2008-03-31 00:00:00'),(200708,2,'Q','Q2 2007-08','2007-07-01 00:00:00','2007-09-30 00:00:00'),(200708,3,'Q','Q3 2007-08','2007-10-01 00:00:00','2007-12-31 00:00:00'),(200708,4,'Q','Q4 2007-08','2008-01-01 00:00:00','2008-03-31 00:00:00'),(200809,1,'H','H1 2008-09','2008-04-01 00:00:00','2008-09-30 00:00:00'),(200809,1,'Q','Q1 2008-09','2008-04-01 00:00:00','2008-06-30 00:00:00'),(200809,1,'Y','FY 2008-09','2008-04-01 00:00:00','2009-03-31 00:00:00'),(200809,2,'H','H2 2008-09','2008-10-01 00:00:00','2009-03-31 00:00:00'),(200809,2,'Q','Q2 2008-09','2008-07-01 00:00:00','2008-09-30 00:00:00'),(200809,3,'Q','Q3 2008-09','2008-10-01 00:00:00','2008-12-31 00:00:00'),(200809,4,'Q','Q4 2008-09','2009-01-01 00:00:00','2009-03-31 00:00:00'),(200910,1,'H','H1 2009-10','2009-04-01 00:00:00','2009-09-30 00:00:00'),(200910,1,'Q','Q1 2009-10','2009-04-01 00:00:00','2009-06-30 00:00:00'),(200910,1,'Y','FY 2009-10','2009-04-01 00:00:00','2010-03-31 00:00:00'),(200910,2,'H','H2 2009-10','2009-10-01 00:00:00','2010-03-31 00:00:00'),(200910,2,'Q','Q2 2009-10','2009-07-01 00:00:00','2009-09-30 00:00:00'),(200910,3,'Q','Q3 2009-10','2009-10-01 00:00:00','2009-12-31 00:00:00'),(200910,4,'Q','Q4 2009-10','2010-01-01 00:00:00','2010-03-31 00:00:00'),(201011,1,'H','H1 2010-11','2010-04-01 00:00:00','2010-09-30 00:00:00'),(201011,1,'Q','Q1 2010-11','2010-04-01 00:00:00','2010-06-30 00:00:00'),(201011,1,'Y','FY 2010-11','2010-04-01 00:00:00','2011-03-31 00:00:00'),(201011,2,'H','H2 2010-11','2010-10-01 00:00:00','2011-03-31 00:00:00'),(201011,2,'Q','Q2 2010-11','2010-07-01 00:00:00','2010-09-30 00:00:00'),(201011,3,'Q','Q3 2010-11','2010-10-01 00:00:00','2010-12-03 00:00:00'),(201011,4,'Q','Q4 2010-11','2011-01-01 00:00:00','2011-03-31 00:00:00'),(201112,1,'H','H1 2011-12','2011-04-01 00:00:00','2011-09-30 00:00:00'),(201112,1,'Q','Q1 2011-12','2011-04-01 00:00:00','2011-06-30 00:00:00'),(201112,1,'Y','FY 2011-12','2011-04-01 00:00:00','2012-03-31 00:00:00'),(201112,2,'H','H2 2011-12','2011-10-01 00:00:00','2012-03-31 00:00:00'),(201112,2,'Q','Q2 2011-12','2011-07-01 00:00:00','2011-09-30 00:00:00'),(201112,3,'Q','Q3 2011-12','2011-10-01 00:00:00','2011-12-03 00:00:00'),(201112,4,'Q','Q4 2011-12','2012-01-01 00:00:00','2012-03-31 00:00:00'),(201213,1,'H','H1 2012-13','2012-04-01 00:00:00','2012-09-30 00:00:00'),(201213,1,'Q','Q1 2012-13','2012-04-01 00:00:00','2012-06-30 00:00:00'),(201213,1,'Y','FY 2012-13','2012-04-01 00:00:00','2013-03-31 00:00:00'),(201213,2,'H','H2 2012-13','2012-10-01 00:00:00','2013-03-31 00:00:00'),(201213,2,'Q','Q2 2012-13','2012-07-01 00:00:00','2012-09-30 00:00:00'),(201213,3,'Q','Q3 2012-13','2012-10-01 00:00:00','2012-12-03 00:00:00'),(201213,4,'Q','Q4 2012-13','2013-01-01 00:00:00','2013-03-31 00:00:00'),(201314,1,'H','H1 2013-14','2013-04-01 00:00:00','2013-09-30 00:00:00'),(201314,1,'Q','Q1 2013-14','2013-04-01 00:00:00','2013-06-30 00:00:00'),(201314,1,'Y','FY 2013-14','2013-04-01 00:00:00','2014-03-31 00:00:00'),(201314,2,'H','H2 2013-14','2013-10-01 00:00:00','2014-03-31 00:00:00'),(201314,2,'Q','Q2 2013-14','2013-07-01 00:00:00','2013-09-30 00:00:00'),(201314,3,'Q','Q3 2013-14','2013-10-01 00:00:00','2013-12-03 00:00:00'),(201314,4,'Q','Q4 2013-14','2014-01-01 00:00:00','2014-03-31 00:00:00'),(201415,1,'H','H1 2014-15','2014-04-01 00:00:00','2014-09-30 00:00:00'),(201415,1,'Q','Q1 2014-15','2014-04-01 00:00:00','2014-06-30 00:00:00'),(201415,1,'Y','FY 2014-15','2014-04-01 00:00:00','2015-03-31 00:00:00'),(201415,2,'H','H2 2014-15','2014-10-01 00:00:00','2015-03-31 00:00:00'),(201415,2,'Q','Q2 2014-15','2014-07-01 00:00:00','2014-09-30 00:00:00'),(201415,3,'Q','Q3 2014-15','2014-10-01 00:00:00','2014-12-03 00:00:00'),(201415,4,'Q','Q4 2014-15','2015-01-01 00:00:00','2015-03-31 00:00:00'),(201516,1,'H','H1 2015-16','2015-04-01 00:00:00','2015-09-30 00:00:00'),(201516,1,'Q','Q1 2015-16','2015-04-01 00:00:00','2015-06-30 00:00:00'),(201516,1,'Y','FY 2015-16','2015-04-01 00:00:00','2016-03-31 00:00:00'),(201516,2,'H','H2 2015-16','2015-10-01 00:00:00','2016-03-31 00:00:00'),(201516,2,'Q','Q2 2015-16','2015-07-01 00:00:00','2015-09-30 00:00:00'),(201516,3,'Q','Q3 2015-16','2015-10-01 00:00:00','2015-12-03 00:00:00'),(201516,4,'Q','Q4 2015-16','2016-01-01 00:00:00','2016-03-31 00:00:00'),(201617,1,'H','H1 2016-17','2016-04-01 00:00:00','2016-09-30 00:00:00'),(201617,1,'Q','Q1 2016-17','2016-04-01 00:00:00','2016-06-30 00:00:00'),(201617,1,'Y','FY 2016-17','2016-04-01 00:00:00','2017-03-31 00:00:00'),(201617,2,'H','H2 2016-17','2016-10-01 00:00:00','2017-03-31 00:00:00'),(201617,2,'Q','Q2 2016-17','2016-07-01 00:00:00','2016-09-30 00:00:00'),(201617,3,'Q','Q3 2016-17','2016-10-01 00:00:00','2016-12-03 00:00:00'),(201617,4,'Q','Q4 2016-17','2017-01-01 00:00:00','2017-03-31 00:00:00'),(201718,1,'H','H1 2017-18','2017-04-01 00:00:00','2017-09-30 00:00:00'),(201718,1,'Q','Q1 2017-18','2017-04-01 00:00:00','2017-06-30 00:00:00'),(201718,1,'Y','FY 2017-18','2017-04-01 00:00:00','2018-03-31 00:00:00'),(201718,2,'H','H2 2017-18','2017-10-01 00:00:00','2018-03-31 00:00:00'),(201718,2,'Q','Q2 2017-18','2017-07-01 00:00:00','2017-09-30 00:00:00'),(201718,3,'Q','Q3 2017-18','2017-10-01 00:00:00','2017-12-03 00:00:00'),(201718,4,'Q','Q4 2017-18','2018-01-01 00:00:00','2018-03-31 00:00:00'),(201819,1,'H','H1 2018-19','2018-04-01 00:00:00','2018-09-30 00:00:00'),(201819,1,'Q','Q1 2018-19','2018-04-01 00:00:00','2018-06-30 00:00:00'),(201819,1,'Y','FY 2018-19','2018-04-01 00:00:00','2019-03-31 00:00:00'),(201819,2,'H','H2 2018-19','2018-10-01 00:00:00','2019-03-31 00:00:00'),(201819,2,'Q','Q2 2018-19','2018-07-01 00:00:00','2018-09-30 00:00:00'),(201819,3,'Q','Q3 2018-19','2018-10-01 00:00:00','2018-12-03 00:00:00'),(201819,4,'Q','Q4 2018-19','2019-01-01 00:00:00','2019-03-31 00:00:00'),(201920,1,'H','H1 2019-20','2019-04-01 00:00:00','2019-09-30 00:00:00'),(201920,1,'Q','Q1 2019-20','2019-04-01 00:00:00','2019-06-30 00:00:00'),(201920,1,'Y','FY 2019-20','2019-04-01 00:00:00','2020-03-31 00:00:00'),(201920,2,'H','H2 2019-20','2019-10-01 00:00:00','2020-03-31 00:00:00'),(201920,2,'Q','Q2 2019-20','2019-07-01 00:00:00','2019-09-30 00:00:00'),(201920,3,'Q','Q3 2019-20','2019-10-01 00:00:00','2019-12-03 00:00:00'),(201920,4,'Q','Q4 2019-20','2020-01-01 00:00:00','2020-03-31 00:00:00'),(202021,1,'H','H1 2020-21','2020-04-01 00:00:00','2020-09-30 00:00:00'),(202021,1,'Q','Q1 2020-21','2020-04-01 00:00:00','2020-06-30 00:00:00'),(202021,1,'Y','FY 2020-21','2020-04-01 00:00:00','2021-03-31 00:00:00'),(202021,2,'H','H2 2020-21','2020-10-01 00:00:00','2021-03-31 00:00:00'),(202021,2,'Q','Q2 2020-21','2020-07-01 00:00:00','2020-09-30 00:00:00'),(202021,3,'Q','Q3 2020-21','2020-10-01 00:00:00','2020-12-03 00:00:00'),(202021,4,'Q','Q4 2020-21','2021-01-01 00:00:00','2021-03-31 00:00:00'),(202122,1,'H','H1 2021-22','2021-04-01 00:00:00','2021-09-30 00:00:00'),(202122,1,'Q','Q1 2021-22','2021-04-01 00:00:00','2021-06-30 00:00:00'),(202122,1,'Y','FY 2021-22','2021-04-01 00:00:00','2022-03-31 00:00:00'),(202122,2,'H','H2 2021-22','2021-10-01 00:00:00','2022-03-31 00:00:00'),(202122,2,'Q','Q2 2021-22','2021-07-01 00:00:00','2021-09-30 00:00:00'),(202122,3,'Q','Q3 2021-22','2021-10-01 00:00:00','2021-12-03 00:00:00'),(202122,4,'Q','Q4 2021-22','2022-01-01 00:00:00','2022-03-31 00:00:00'),(202223,1,'H','H1 2022-23','2022-04-01 00:00:00','2022-09-30 00:00:00'),(202223,1,'Q','Q1 2022-23','2022-04-01 00:00:00','2022-06-30 00:00:00'),(202223,1,'Y','FY 2022-23','2022-04-01 00:00:00','2023-03-31 00:00:00'),(202223,2,'H','H2 2022-23','2022-10-01 00:00:00','2023-03-31 00:00:00'),(202223,2,'Q','Q2 2022-23','2022-07-01 00:00:00','2022-09-30 00:00:00'),(202223,3,'Q','Q3 2022-23','2022-10-01 00:00:00','2022-12-03 00:00:00'),(202223,4,'Q','Q4 2022-23','2023-01-01 00:00:00','2023-03-31 00:00:00'),(202324,1,'H','H1 2023-24','2023-04-01 00:00:00','2023-09-30 00:00:00'),(202324,1,'Q','Q1 2023-24','2023-04-01 00:00:00','2023-06-30 00:00:00'),(202324,1,'Y','FY 2023-24','2023-04-01 00:00:00','2024-03-31 00:00:00'),(202324,2,'H','H2 2023-24','2023-10-01 00:00:00','2024-03-31 00:00:00'),(202324,2,'Q','Q2 2023-24','2023-07-01 00:00:00','2023-09-30 00:00:00'),(202324,3,'Q','Q3 2023-24','2023-10-01 00:00:00','2023-12-03 00:00:00'),(202324,4,'Q','Q4 2023-24','2024-01-01 00:00:00','2024-03-31 00:00:00'),(202425,1,'H','H1 2024-25','2024-04-01 00:00:00','2024-09-30 00:00:00'),(202425,1,'Q','Q1 2024-25','2024-04-01 00:00:00','2024-06-30 00:00:00'),(202425,1,'Y','FY 2024-25','2024-04-01 00:00:00','2025-03-31 00:00:00'),(202425,2,'H','H2 2024-25','2024-10-01 00:00:00','2025-03-31 00:00:00'),(202425,2,'Q','Q2 2024-25','2024-07-01 00:00:00','2024-09-30 00:00:00'),(202425,3,'Q','Q3 2024-25','2024-10-01 00:00:00','2024-12-03 00:00:00'),(202425,4,'Q','Q4 2024-25','2025-01-01 00:00:00','2025-03-31 00:00:00'),(202526,1,'H','H1 2025-26','2025-04-01 00:00:00','2025-09-30 00:00:00'),(202526,1,'Q','Q1 2025-26','2025-04-01 00:00:00','2025-06-30 00:00:00'),(202526,1,'Y','FY 2025-26','2025-04-01 00:00:00','2026-03-31 00:00:00'),(202526,2,'H','H2 2025-26','2025-10-01 00:00:00','2026-03-31 00:00:00'),(202526,2,'Q','Q2 2025-26','2025-07-01 00:00:00','2025-09-30 00:00:00'),(202526,3,'Q','Q3 2025-26','2025-10-01 00:00:00','2025-12-03 00:00:00'),(202526,4,'Q','Q4 2025-26','2026-01-01 00:00:00','2026-03-31 00:00:00'),(202627,1,'H','H1 2026-27','2026-04-01 00:00:00','2026-09-30 00:00:00'),(202627,1,'Q','Q1 2026-27','2026-04-01 00:00:00','2026-06-30 00:00:00'),(202627,1,'Y','FY 2026-27','2026-04-01 00:00:00','2027-03-31 00:00:00'),(202627,2,'H','H2 2026-27','2026-10-01 00:00:00','2027-03-31 00:00:00'),(202627,2,'Q','Q2 2026-27','2026-07-01 00:00:00','2026-09-30 00:00:00'),(202627,3,'Q','Q3 2026-27','2026-10-01 00:00:00','2026-12-03 00:00:00'),(202627,4,'Q','Q4 2026-27','2027-01-01 00:00:00','2027-03-31 00:00:00'),(202728,1,'H','H1 2027-28','2027-04-01 00:00:00','2027-09-30 00:00:00'),(202728,1,'Q','Q1 2027-28','2027-04-01 00:00:00','2027-06-30 00:00:00'),(202728,1,'Y','FY 2027-28','2027-04-01 00:00:00','2028-03-31 00:00:00'),(202728,2,'H','H2 2027-28','2027-10-01 00:00:00','2028-03-31 00:00:00'),(202728,2,'Q','Q2 2027-28','2027-07-01 00:00:00','2027-09-30 00:00:00'),(202728,3,'Q','Q3 2027-28','2027-10-01 00:00:00','2027-12-03 00:00:00'),(202728,4,'Q','Q4 2027-28','2028-01-01 00:00:00','2028-03-31 00:00:00'),(202829,1,'H','H1 2028-29','2028-04-01 00:00:00','2028-09-30 00:00:00'),(202829,1,'Q','Q1 2028-29','2028-04-01 00:00:00','2028-06-30 00:00:00'),(202829,1,'Y','FY 2028-29','2028-04-01 00:00:00','2029-03-31 00:00:00'),(202829,2,'H','H2 2028-29','2028-10-01 00:00:00','2029-03-31 00:00:00'),(202829,2,'Q','Q2 2028-29','2028-07-01 00:00:00','2028-09-30 00:00:00'),(202829,3,'Q','Q3 2028-29','2028-10-01 00:00:00','2028-12-03 00:00:00'),(202829,4,'Q','Q4 2028-29','2029-01-01 00:00:00','2029-03-31 00:00:00'),(202930,1,'H','H1 2029-30','2029-04-01 00:00:00','2029-09-30 00:00:00'),(202930,1,'Q','Q1 2029-30','2029-04-01 00:00:00','2029-06-30 00:00:00'),(202930,1,'Y','FY 2029-30','2029-04-01 00:00:00','2030-03-31 00:00:00'),(202930,2,'H','H2 2029-30','2029-10-01 00:00:00','2030-03-31 00:00:00'),(202930,2,'Q','Q2 2029-30','2029-07-01 00:00:00','2029-09-30 00:00:00'),(202930,3,'Q','Q3 2029-30','2029-10-01 00:00:00','2029-12-03 00:00:00'),(202930,4,'Q','Q4 2029-30','2030-01-01 00:00:00','2030-03-31 00:00:00'),(203031,1,'H','H1 2030-31','2030-04-01 00:00:00','2030-09-30 00:00:00'),(203031,1,'Q','Q1 2030-31','2030-04-01 00:00:00','2030-06-30 00:00:00'),(203031,1,'Y','FY 2030-31','2030-04-01 00:00:00','2031-03-31 00:00:00'),(203031,2,'H','H2 2030-31','2030-10-01 00:00:00','2031-03-31 00:00:00'),(203031,2,'Q','Q2 2030-31','2030-07-01 00:00:00','2030-09-30 00:00:00'),(203031,3,'Q','Q3 2030-31','2030-10-01 00:00:00','2030-12-03 00:00:00'),(203031,4,'Q','Q4 2030-31','2031-01-01 00:00:00','2031-03-31 00:00:00'),(203132,1,'H','H1 2031-32','2031-04-01 00:00:00','2031-09-30 00:00:00'),(203132,1,'Q','Q1 2031-32','2031-04-01 00:00:00','2031-06-30 00:00:00'),(203132,1,'Y','FY 2031-32','2031-04-01 00:00:00','2032-03-31 00:00:00'),(203132,2,'H','H2 2031-32','2031-10-01 00:00:00','2032-03-31 00:00:00'),(203132,2,'Q','Q2 2031-32','2031-07-01 00:00:00','2031-09-30 00:00:00'),(203132,3,'Q','Q3 2031-32','2031-10-01 00:00:00','2031-12-03 00:00:00'),(203132,4,'Q','Q4 2031-32','2032-01-01 00:00:00','2032-03-31 00:00:00'),(203233,1,'H','H1 2032-33','2032-04-01 00:00:00','2032-09-30 00:00:00'),(203233,1,'Q','Q1 2032-33','2032-04-01 00:00:00','2032-06-30 00:00:00'),(203233,1,'Y','FY 2032-33','2032-04-01 00:00:00','2033-03-31 00:00:00'),(203233,2,'H','H2 2032-33','2032-10-01 00:00:00','2033-03-31 00:00:00'),(203233,2,'Q','Q2 2032-33','2032-07-01 00:00:00','2032-09-30 00:00:00'),(203233,3,'Q','Q3 2032-33','2032-10-01 00:00:00','2032-12-03 00:00:00'),(203233,4,'Q','Q4 2032-33','2033-01-01 00:00:00','2033-03-31 00:00:00'),(203334,1,'H','H1 2033-34','2033-04-01 00:00:00','2033-09-30 00:00:00'),(203334,1,'Q','Q1 2033-34','2033-04-01 00:00:00','2033-06-30 00:00:00'),(203334,1,'Y','FY 2033-34','2033-04-01 00:00:00','2034-03-31 00:00:00'),(203334,2,'H','H2 2033-34','2033-10-01 00:00:00','2034-03-31 00:00:00'),(203334,2,'Q','Q2 2033-34','2033-07-01 00:00:00','2033-09-30 00:00:00'),(203334,3,'Q','Q3 2033-34','2033-10-01 00:00:00','2033-12-03 00:00:00'),(203334,4,'Q','Q4 2033-34','2034-01-01 00:00:00','2034-03-31 00:00:00'),(203435,1,'H','H1 2034-35','2034-04-01 00:00:00','2034-09-30 00:00:00'),(203435,1,'Q','Q1 2034-35','2034-04-01 00:00:00','2034-06-30 00:00:00'),(203435,1,'Y','FY 2034-35','2034-04-01 00:00:00','2035-03-31 00:00:00'),(203435,2,'H','H2 2034-35','2034-10-01 00:00:00','2035-03-31 00:00:00'),(203435,2,'Q','Q2 2034-35','2034-07-01 00:00:00','2034-09-30 00:00:00'),(203435,3,'Q','Q3 2034-35','2034-10-01 00:00:00','2034-12-03 00:00:00'),(203435,4,'Q','Q4 2034-35','2035-01-01 00:00:00','2035-03-31 00:00:00');
/*!40000 ALTER TABLE `Periods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'Aletheia'
--
/*!50003 DROP PROCEDURE IF EXISTS `AL_GetStockActualsData` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `AL_GetStockActualsData`(
	IN_Process int,
    IN_Month int,
    IN_Year int
)
BEGIN
/* ====================================================================
-Create Date 	: 30-11-2018
- Created By 	: Abhilash Kamble
- Parameters 	: Condition, month number, year
- Description	: To get Stock data for each month
- Modifications	:  
- Sample Call 	: Call AL_GetStockActualsData (1,3,2018);
=======================================================================*/
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
SHOW ERRORS LIMIT 1 ; 
END;

SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;

IF (IN_Process = 1 ) THEN /* Stock Actual data last 4 month */
 BEGIN
	SELECT 
		HD.PeriodID, 
		HD.PeriodIdx, 
		HD.Mode, 
		CASE HD.ElementType
			WHEN 'S' THEN 'Stocks'
            WHEN 'SG' THEN 'Government Controlled'
		END as Stocks,
		HD.Value,
		RG.RegionName,
		HD.ReportedDate
	FROM IEA_HistoricMacroElementsData HD
	LEFT OUTER JOIN Regions RG
	ON HD.RegionID = RG.RegionID
	WHERE TableType = '4'
	AND MONTH(ReportedDate) = IN_Month 
	AND YEAR(ReportedDate) = IN_Year
	AND IsTotal = 1
	AND PeriodIdx != (select MAX(PeriodIdx) from IEA_HistoricMacroElementsData where TableType = '4'
	AND MONTH(ReportedDate) = IN_Month 
	AND YEAR(ReportedDate) = IN_Year)

	UNION

	SELECT 
		HD.PeriodID, 
		HD.PeriodIdx, 
		HD.Mode, 
		CASE HD.ElementType
			WHEN 'S' THEN 'Stocks'
            WHEN 'SG' THEN 'Government Controlled'
		END as Stocks,
		HD.Value,
		RG.RegionName,
		HD.ReportedDate
	FROM IEA_HistoricMacroElementsData HD
	LEFT OUTER JOIN Regions RG
	ON HD.RegionID = RG.RegionID
	WHERE TableType = '4'
	AND MONTH(ReportedDate) = IN_Month 
	AND YEAR(ReportedDate) = IN_Year
	AND IsTotal = 1
	AND PeriodID != (select MAX(PeriodID) from IEA_HistoricMacroElementsData where TableType = '4'
	AND MONTH(ReportedDate) = IN_Month 
	AND YEAR(ReportedDate) = IN_Year)
	ORDER BY PeriodId DESC, PeriodIdx DESC
	;
 END;
 END IF;
 
 IF (IN_Process = 2 ) THEN /* Stock Actual data last 1 month */
 BEGIN
	select * from (
		SELECT 
			HD.PeriodID, 
			HD.PeriodIdx, 
			HD.Mode, 
			CASE HD.ElementType
				WHEN 'S' THEN 'Stocks'
				WHEN 'SG' THEN 'Government Controlled'
			END as Stocks,
			HD.Value,
			RG.RegionName,
			HD.ReportedDate
		FROM IEA_HistoricMacroElementsData HD
		LEFT OUTER JOIN Regions RG
		ON HD.RegionID = RG.RegionID
		WHERE TableType = '4'
		AND MONTH(ReportedDate) = IN_Month 
		AND YEAR(ReportedDate) = IN_Year
		AND IsTotal = 1
		AND PeriodID = (select MIN(PeriodID) from IEA_HistoricMacroElementsData where TableType = '4'
		AND MONTH(ReportedDate) = IN_Month 
		AND YEAR(ReportedDate) = IN_Year)) al
		where PeriodIdx = (select MIN(PeriodIdx) from IEA_HistoricMacroElementsData where TableType = '4'
		AND MONTH(ReportedDate) = IN_Month 
		AND YEAR(ReportedDate) = IN_Year
		AND IsTotal = 1
		AND PeriodID = (select MIN(PeriodID) from IEA_HistoricMacroElementsData where TableType = '4'
		AND MONTH(ReportedDate) = IN_Month
		AND YEAR(ReportedDate) = IN_Year)) 
		ORDER BY PeriodId DESC, PeriodIdx DESC;
 END;
 END IF;
 
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `BMIndexHistory` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `BMIndexHistory`()
BEGIN 

	SELECT IM.BM_IndexName, date_format(IH.DateOfAddition,'%Y-%m-%d') as Date, 	IH.PriceClose as Close, 	IH.Volume as Volume
	FROM IndexHistory as IH 
	INNER JOIN IndexMaster as IM on IM.RIC = IH.RIC
    ORDER BY IM.BM_IndexName, Date
    ;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `BMStockHistory` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `BMStockHistory`()
BEGIN 

	Select date_format(SH.DateOfAddition,'%Y-%m-%d') as Date, 
    ROUND(SH.PriceOpen, 2) as Open, ROUND(SH.PriceHigh, 2) as High, ROUND(SH.PriceLow, 2) as Low,
	ROUND(SH.PriceClose, 2) as Close, ROUND(SH.PriceClose, 2) as 'Adj Close', 
    REPLACE(SM.BBSymbol, ' Equity', '') as Ticker
	FROM StockHistory as SH
	INNER JOIN StockMaster as SM on SM.RIC = SH.RIC
	WHERE SM.IsHistoryParsed = 1
    ORDER BY Ticker, Date Desc
	;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CalcPricePerf` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `CalcPricePerf`()
BEGIN 

	CREATE TEMPORARY TABLE IF NOT EXISTS t_pp (
	  `RIC` varchar(10) DEFAULT NULL,
	  `BBSymbol` varchar(20) DEFAULT NULL,
	  `TradingCurrency` varchar(10) DEFAULT NULL,
	  `ReferenceIndex` varchar(10) DEFAULT NULL,
 	  `IndexName` varchar(50) DEFAULT NULL,     
	  `LatestDate` datetime DEFAULT NULL,
	  `LatestClose` decimal(22,4) DEFAULT NULL,
	  `LatestIndexClose` decimal(22,4) DEFAULT NULL,
      `LatestCloseUSD` decimal(22,4) DEFAULT NULL,
	  `OneMthDate` datetime DEFAULT NULL,
	  `OneMthClose` decimal(22,4) DEFAULT NULL,
	  `OneMthIndexClose` decimal(22,4) DEFAULT NULL,
      `OneMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `ThreeMthDate` datetime DEFAULT NULL,
	  `ThreeMthClose` decimal(22,4) DEFAULT NULL,
	  `ThreeMthIndexClose` decimal(22,4) DEFAULT NULL,
      `ThreeMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `TwelveMthDate` datetime DEFAULT NULL,
	  `TwelveMthClose` decimal(22,4) DEFAULT NULL,
	  `TwelveMthIndexClose` decimal(22,4) DEFAULT NULL,
      `TwelveMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `YTDDate` datetime DEFAULT NULL,
	  `YTDClose` decimal(22,4) DEFAULT NULL,
	  `YTDIndexClose` decimal(22,4) DEFAULT NULL,
      `YTDCloseUSD` decimal(22,4) DEFAULT NULL
	);

	CREATE TEMPORARY TABLE IF NOT EXISTS t_latest AS (
	SELECT RIC, date_sub(DateOfAddition, Interval 1 day) as LatestDate
	FROM StockHistory as SH 
	WHERE RIC IN (SELECT DISTINCT(RIC) FROM StockMaster as SM WHERE SM.IsHistoryParsed = 1
    )
	GROUP BY RIC
	-- HAVING DateOfAddition = MAX(DateofAddition)
	);

	-- SELECT * FROM t_latest;
    
	INSERT INTO t_pp (
	SELECT SM.RIC, SM.BBSymbol, SM.TradingCurrency, SM.ReferenceIndex , IM.BM_IndexName, 
	T1.LatestDate, SH.PriceClose as LatestClose,  IH.PriceClose as LatestIndexClose, SH.PriceClose / CH.Price as LatestCloseUSD,
	NULL as OneMthDate, NULL as OneMthClose,  NULL as OneMthIndexClose, NULL as OneMthCloseUSD, 
	NULL as ThreeMthDate, NULL as ThreeMthClose,  NULL as ThreeMthIndexClose, NULL as ThreeMthCloseUSD,
	NULL as TwelveMthDate, NULL as TwelveMthClose,  NULL as TwelveMthIndexClose, NULL as TwelveMthCloseUSD, 
	NULL as YTDDate, NULL as YTDClose,  NULL as YTDIndexClose, NULL as YTDCloseUSD
	FROM StockHistory as SH 
	INNER JOIN t_latest as T1 on T1.RIC = SH.RIC and T1.LatestDate = SH.DateOfAddition
	INNER JOIN StockMaster as SM on SM.RIC = SH.RIC
	INNER JOIN IndexMaster as IM on IM.RIC = SM.ReferenceIndex
	LEFT OUTER JOIN IndexHistory as IH on IH.RIC = IM.RIC and IH.DateofAddition = SH.DateOfAddition
    INNER JOIN CurrencyMaster as CM on CM.CurrencyCode = SM.TradingCurrency
    LEFT OUTER JOIN CurrencyHistory as CH on CH.RIC = CM.RIC and CH.DateOfAddition = SH.DateOfAddition
	);

	DROP TEMPORARY TABLE t_latest;
    
    -- SELECT COUNT(*) FROM t_pp;

	UPDATE t_pp
	SET OneMthDate = date_sub(LatestDate, interval 1 month),
			ThreeMthDate = date_sub(LatestDate, interval 3 month),
			TwelveMthDate = date_sub(LatestDate, interval 12 month),
			YTDDate = '2018-01-01'
            WHERE RIC is not null
	;
	SET @nbr_attempts = 1;

	-- 1mth

	UPDATE t_pp
	INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.OneMthDate
	SET t_pp.OneMthClose = SH.PriceClose
	WHERE OneMthClose is NULL
	;

	WHILE @nbr_attempts < 5  DO
    

			SELECT COUNT(*) INTO @rCount FROM t_pp 
            WHERE OneMthClose is NULL
            ;
            
            IF @rCount = 0 THEN
				SET @nbr_attempts = 5;
                
			ELSE
            
				UPDATE t_pp 
				SET OneMthDate = date_add(OneMthDate, interval 1 day)
				WHERE OneMthClose is NULL
				;

				UPDATE t_pp
				INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.OneMthDate
				SET t_pp.OneMthClose = SH.PriceClose
				WHERE OneMthClose is NULL
				;
                SET @nbr_attempts = @nbr_attempts + 1;

			END IF;
	END WHILE;
	UPDATE t_pp
	INNER JOIN IndexHistory as IH ON IH.RIC = t_pp.ReferenceIndex AND IH.DateOfAddition = t_pp.OneMthDate
	SET t_pp.OneMthIndexClose = IH.PriceClose
	WHERE t_pp.OneMthIndexClose is NULL
	;
    UPDATE t_pp
	INNER JOIN CurrencyMaster as CM on CM.CurrencyCode = t_pp.TradingCurrency
	INNER JOIN CurrencyHistory as CH ON CH.RIC = CM.RIC AND CH.DateOfAddition = t_pp.OneMthDate
	SET t_pp.OneMthCloseUSD = t_pp.OneMthClose / CH.Price
	WHERE t_pp.OneMthCloseUSD is NULL
	;

	-- 3mth

	UPDATE t_pp
	INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.ThreeMthDate
	SET t_pp.ThreeMthClose = SH.PriceClose
	WHERE ThreeMthClose is NULL
	;
    
	SET @nbr_attempts = 1;
    
	WHILE @nbr_attempts  <  5  DO
    

			SELECT COUNT(*) INTO @rCount FROM t_pp 
            WHERE ThreeMthClose is NULL
            ;
            
            IF @rCount = 0 THEN
				SET @nbr_attempts = 5;
                
			ELSE
				UPDATE t_pp 
				SET ThreeMthDate = date_add(ThreeMthDate, interval 1 day)
				WHERE ThreeMthClose is NULL
				;

				UPDATE t_pp
				INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.ThreeMthDate
				SET t_pp.ThreeMthClose = SH.PriceClose
				WHERE ThreeMthClose is NULL
				;
                
                SET @nbr_attempts = @nbr_attempts + 1;


			END IF;
	END WHILE;
	UPDATE t_pp
	INNER JOIN IndexHistory as IH ON IH.RIC = t_pp.ReferenceIndex AND IH.DateOfAddition = t_pp.ThreeMthDate
	SET t_pp.ThreeMthIndexClose = IH.PriceClose
	WHERE t_pp.ThreeMthIndexClose is NULL
	;
    UPDATE t_pp
	INNER JOIN CurrencyMaster as CM on CM.CurrencyCode = t_pp.TradingCurrency
	INNER JOIN CurrencyHistory as CH ON CH.RIC = CM.RIC AND CH.DateOfAddition = t_pp.ThreeMthDate
	SET t_pp.ThreeMthCloseUSD = t_pp.ThreeMthClose / CH.Price
	WHERE t_pp.ThreeMthCloseUSD is NULL
	;

	-- 12mth
	UPDATE t_pp
	INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.TwelveMthDate
	SET t_pp.TwelveMthClose = SH.PriceClose
	WHERE TwelveMthClose is NULL
	;
    
	SET @nbr_attempts = 1;
    
	WHILE @nbr_attempts < 5 DO
    

			SELECT COUNT(*) INTO @rCount FROM t_pp 
            WHERE TwelveMthClose is NULL
            ;
            
            IF @rCount = 0 THEN
				SET @nbr_attempts = 5;
                
			ELSE
				UPDATE t_pp 
				SET TwelveMthDate = date_add(TwelveMthDate, interval 1 day)
				WHERE TwelveMthClose is NULL
				;

				UPDATE t_pp
				INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.TwelveMthDate
				SET t_pp.TwelveMthClose = SH.PriceClose
				WHERE TwelveMthClose is NULL
				;
                SET @nbr_attempts = @nbr_attempts + 1;

			END IF;
		END WHILE;
		UPDATE t_pp
		INNER JOIN IndexHistory as IH ON IH.RIC = t_pp.ReferenceIndex AND IH.DateOfAddition = t_pp.TwelveMthDate
		SET t_pp.TwelveMthIndexClose = IH.PriceClose
		WHERE t_pp.TwelveMthIndexClose is NULL
		;
		UPDATE t_pp
		INNER JOIN CurrencyMaster as CM on CM.CurrencyCode = t_pp.TradingCurrency
		INNER JOIN CurrencyHistory as CH ON CH.RIC = CM.RIC AND CH.DateOfAddition = t_pp.TwelveMthDate
		SET t_pp.TwelveMthCloseUSD = t_pp.TwelveMthClose / CH.Price
		WHERE t_pp.TwelveMthCloseUSD is NULL
		;       

	-- ytd
	UPDATE t_pp
	INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.YTDDate
	SET t_pp.YTDClose = SH.PriceClose
	WHERE YTDClose is NULL
	;
	SET @nbr_attempts = 1;
    
	WHILE @nbr_attempts  <  5 DO
    

			SELECT COUNT(*) INTO @rCount FROM t_pp 
            WHERE YTDClose is NULL
            ;
            
            IF @rCount = 0 THEN
				SET @nbr_attempts = 5;
                
			ELSE
				UPDATE t_pp 
				SET YTDDate = date_add(YTDDate, interval 1 day)
				WHERE YTDClose is NULL
				;

				UPDATE t_pp
				INNER JOIN StockHistory as SH ON SH.RIC = t_pp.RIC and SH.DateOfAddition = t_pp.YTDDate
				SET t_pp.YTDClose = SH.PriceClose
				WHERE YTDClose is NULL
				;
                SET @nbr_attempts = @nbr_attempts + 1;

			END IF;
	END WHILE;
	UPDATE t_pp
	INNER JOIN IndexHistory as IH ON IH.RIC = t_pp.ReferenceIndex AND IH.DateOfAddition = t_pp.YTDDate
	SET t_pp.YTDIndexClose = IH.PriceClose
	WHERE t_pp.YTDIndexClose is NULL
	;
	UPDATE t_pp
	INNER JOIN CurrencyMaster as CM on CM.CurrencyCode = t_pp.TradingCurrency
	INNER JOIN CurrencyHistory as CH ON CH.RIC = CM.RIC AND CH.DateOfAddition = t_pp.YTDDate
	SET t_pp.YTDCloseUSD = t_pp.YTDClose / CH.Price
	WHERE t_pp.YTDCloseUSD is NULL
	;  

-- 	SELECT 
-- 	REPLACE(BBSymbol, ' Equity', '') as PricingSymbol, 
-- 	ROUND((LatestClose / OneMthClose  -1 )* 100, 0) AS Performance_Absolute_1M, 
-- 	ROUND((LatestClose / ThreeMthClose  -1) * 100, 0) AS Performance_Absolute_3M, 
-- 	ROUND((LatestClose / TwelveMthClose  -1) * 100, 0) AS Performance_Absolute_12M, 
-- 	ROUND((LatestClose / YTDClose - 1) * 100, 0) AS Performance_Absolute_YTD, 
--     
-- 	ROUND(( (LatestClose / LatestIndexClose)  / (OneMthClose / OneMthIndexClose ) -1 ) * 100, 0) AS Performance_Relative_1M, 
-- 	ROUND(( (LatestClose / LatestIndexClose) / (ThreeMthClose / ThreeMthIndexClose ) -1 ) * 100, 0) AS Performance_Relative_3M, 
-- 	ROUND(( (LatestClose / LatestIndexClose) / (TwelveMthClose / TwelveMthIndexClose )  -1 ) * 100, 0)  AS Performance_Relative_12M, 
-- 	ROUND(( (LatestClose / LatestIndexClose) / (YTDClose / YTDIndexClose ) -1 ) * 100, 0)  AS Performance_Relative_YTD, 
--     
-- 	ROUND((LatestCloseUSD / OneMthCloseUSD - 1)*100, 0) AS Performance_Absolute_US_1M, 
-- 	ROUND((LatestCloseUSD / ThreeMthCloseUSD - 1) *100, 0) AS Performance_Absolute_US_3M, 
-- 	ROUND((LatestCloseUSD / TwelveMthCloseUSD -1)*100, 0) AS Performance_Absolute_US_12M, 
-- 	ROUND((LatestCloseUSD / YTDCloseUSD - 1) *100 , 0) AS Performance_Absolute_US_YTD
-- 	FROM t_pp
-- 	;
    SELECT * FROm t_pp;
	DROP TEMPORARY TABLE t_pp;
   
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CalcPricePerf_New` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `CalcPricePerf_New`()
BEGIN 
	
	DROP TEMPORARY TABLE IF EXISTS t_latest;
    
	CREATE TEMPORARY TABLE IF NOT EXISTS t_latest AS (
	SELECT RIC, Max(DateOfAddition) as LatestDate
	FROM StockHistory as SH 
	WHERE RIC IN (SELECT DISTINCT(RIC) FROM StockMaster as SM WHERE SM.IsHistoryParsed = 1
    )
	GROUP BY RIC
	-- HAVING DateOfAddition = MAX(DateofAddition)
	); 
    
    /*SELECT * FROM t_latest;*/
    
    DROP TEMPORARY TABLE IF EXISTS t_pp;
    CREATE TEMPORARY TABLE IF NOT EXISTS t_pp (
	  `RIC` varchar(10) DEFAULT NULL,
	  `BBSymbol` varchar(20) DEFAULT NULL,
	  `TradingCurrency` varchar(10) DEFAULT NULL,
	  `ReferenceIndex` varchar(10) DEFAULT NULL,
 	  `IndexName` varchar(50) DEFAULT NULL,     
	  `LatestDate` datetime DEFAULT NULL,
	  `LatestClose` decimal(22,4) DEFAULT NULL,
	  `LatestIndexClose` decimal(22,4) DEFAULT NULL,
      `LatestCloseUSD` decimal(22,4) DEFAULT NULL,
	  `OneMthDate` datetime DEFAULT NULL,
	  `OneMthClose` decimal(22,4) DEFAULT NULL,
	  `OneMthIndexClose` decimal(22,4) DEFAULT NULL,
      `OneMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `ThreeMthDate` datetime DEFAULT NULL,
	  `ThreeMthClose` decimal(22,4) DEFAULT NULL,
	  `ThreeMthIndexClose` decimal(22,4) DEFAULT NULL,
      `ThreeMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `TwelveMthDate` datetime DEFAULT NULL,
	  `TwelveMthClose` decimal(22,4) DEFAULT NULL,
	  `TwelveMthIndexClose` decimal(22,4) DEFAULT NULL,
      `TwelveMthCloseUSD` decimal(22,4) DEFAULT NULL,
	  `YTDDate` datetime DEFAULT NULL,
	  `YTDClose` decimal(22,4) DEFAULT NULL,
	  `YTDIndexClose` decimal(22,4) DEFAULT NULL,
      `YTDCloseUSD` decimal(22,4) DEFAULT NULL
	);
    
    INSERT INTO t_pp (
	SELECT SM.RIC, SM.BBSymbol, SM.TradingCurrency, SM.ReferenceIndex , IM.BM_IndexName, 
		T1.LatestDate, SH.PriceClose as LatestClose, IH.PriceClose as LatestIndexClose, SH.PriceClose / CH.Price as LatestCloseUSD,
		NULL as OneMthDate, NULL as OneMthClose,  NULL as OneMthIndexClose, NULL as OneMthCloseUSD, 
		NULL as ThreeMthDate, NULL as ThreeMthClose,  NULL as ThreeMthIndexClose, NULL as ThreeMthCloseUSD,
		NULL as TwelveMthDate, NULL as TwelveMthClose,  NULL as TwelveMthIndexClose, NULL as TwelveMthCloseUSD, 
		NULL as YTDDate, NULL as YTDClose,  NULL as YTDIndexClose, NULL as YTDCloseUSD
	FROM StockHistory as SH 
	INNER JOIN t_latest as T1 on T1.RIC = SH.RIC and T1.LatestDate = SH.DateOfAddition
	INNER JOIN StockMaster as SM on SM.RIC = SH.RIC
	LEFT OUTER JOIN IndexMaster as IM on IM.RIC = SM.ReferenceIndex
	LEFT OUTER JOIN IndexHistory as IH on IH.RIC = IM.RIC and IH.DateofAddition = SH.DateOfAddition
    LEFT OUTER JOIN CurrencyMaster as CM on CM.CurrencyCode = SM.TradingCurrency
    LEFT OUTER JOIN CurrencyHistory as CH on CH.RIC = CM.RIC and CH.DateOfAddition = SH.DateOfAddition    
	);
      
    DROP TEMPORARY TABLE IF EXISTS t_latest;
	/*SELECT * FROM t_pp;*/

	DROP TEMPORARY TABLE IF EXISTS SH_OneMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS SH_OneMonth
	SELECT ST.RIC,IJ.OneMOnthOld, Min(ST.DateOfAddition) OneMonthDate
	FROM StockHistory ST
	INNER JOIN 
	(
		SELECT RIC, LatestDate, DATE_SUB(LatestDate, INTERVAL 1 MONTH) OneMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON ST.RIC=IJ.RIC
	WHERE ST.DateOfAddition >= IJ.OneMOnthOld 
	GROUP BY ST.RIC
	HAVING DATEDIFF(MIN(ST.DateOfAddition), IJ.OneMOnthOld  ) <= 15;
 
	DROP TEMPORARY TABLE IF EXISTS SH_ThreeMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS SH_ThreeMonth
    SELECT ST.RIC,IJ.ThreeMOnthOld, Min(ST.DateOfAddition) ThreeMonthDate
	FROM StockHistory ST
	INNER JOIN 
	(
		SELECT RIC, LatestDate, DATE_SUB(LatestDate, INTERVAL 3 MONTH) ThreeMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    ) IJ ON ST.RIC=IJ.RIC
	WHERE ST.DateOfAddition >= IJ.ThreeMOnthOld 
	GROUP BY ST.RIC
	HAVING datediff(Min(ST.DateOfAddition), IJ.ThreeMOnthOld  ) <= 15;

	DROP TEMPORARY TABLE IF EXISTS SH_TwelveMonth;	
	
    CREATE TEMPORARY TABLE IF NOT EXISTS SH_TwelveMonth    
	SELECT ST.RIC,IJ.TwelveMOnthOld, Min(ST.DateOfAddition) TwelveMonthDate
	FROM StockHistory ST
	INNER JOIN 
	(
		SELECT RIC, LatestDate, DATE_SUB(LatestDate, INTERVAL 12 MONTH) TwelveMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    ) IJ ON ST.RIC=IJ.RIC
    WHERE ST.DateOfAddition >= IJ.TwelveMOnthOld 
	GROUP BY ST.RIC
	HAVING datediff(Min(ST.DateOfAddition), IJ.TwelveMOnthOld  ) <= 15;


	UPDATE t_pp TP
	LEFT OUTER JOIN 
	(	
		SELECT OM.RIC, OM.OneMonthDate,ST.PriceClose OneMonthPrice
		FROM SH_OneMonth  OM 
		INNER JOIN StockHistory ST ON OM.RIC = ST.RIC AND OM.OneMonthDate = ST.DateOfAddition
	) OD ON TP.RIC = OD.RIC 
	LEFT OUTER JOIN 
	(
		SELECT SM.RIC, SM.ThreeMonthDate,ST.PriceClose ThreeMonthPrice
		FROM SH_ThreeMonth SM 
		INNER JOIN StockHistory ST ON SM.RIC = ST.RIC AND SM.ThreeMonthDate = ST.DateOfAddition
	) TD ON TP.RIC=TD.RIC
	LEFT OUTER JOIN 
	(
		SELECT SW.RIC, SW.TwelveMonthDate,ST.PriceClose TwelveMonthPrice
		FROM SH_TwelveMonth SW 
		INNER JOIN StockHistory ST ON SW.RIC = ST.RIC AND SW.TwelveMonthDate = ST.DateOfAddition
	)  TM ON TP.RIC = TM.RIC
	LEFT OUTER JOIN
	(
		SELECT SH.RIC, ST.YTDDate, SH.PriceClose AS YTDPrice
		FROM StockHistory SH
		INNER JOIN 
		(
			SELECT RIC, MIN(DateOfAddition) YTDDate
			FROM  StockHistory 
			WHERE DateOfAddition >= DATE_FORMAT(Current_Date() ,'%Y-01-01') 
			GROUP BY RIC
		) ST ON SH.RIC =ST.RIC AND SH.DateOfAddition = ST.YTDDate
	) YD ON TP.RIC = YD .RIC 
	SET TP.OneMthDate    = OD.OneMonthDate,
		TP.OneMthClose   = OD.OneMonthPrice, 
		TP.ThreeMthDate  = TD.ThreeMonthDate, 
		TP.ThreeMthClose = TD.ThreeMonthPrice, 
		TP.TwelveMthDate = TM.TwelveMonthDate, 
		TP.TwelveMthClose= TM.TwelveMonthPrice,
		TP.YTDDate 		 = YD.YTDDate,
		TP.YTDClose		 = YD.YTDPrice;

	/* Index History */
	/*Select * From t_pp;*/
	
	DROP TEMPORARY TABLE IF EXISTS IH_OneMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS IH_OneMonth
	SELECT IJ.RIC, IJ.ReferenceIndex, IJ.OneMOnthOld , MIN(IH.DateOfAddition) As OneMonthOldDate
		FROM IndexHistory IH
		INNER JOIN 
		(
			SELECT RIC,ReferenceIndex, LatestDate, DATE_SUB(LatestDate, INTERVAL 1 MONTH) OneMOnthOld
			FROM t_pp TP 
			WHERE RIC IS NOT NULL 
		) IJ ON IH.RIC=IJ.ReferenceIndex
	WHERE IH.DateOfAddition >= IJ.OneMOnthOld 
	GROUP BY IJ.RIC, IJ.ReferenceIndex
	HAVING DATEDIFF(MIN(IH.DateOfAddition), IJ.OneMOnthOld  ) <= 15;
    
	DROP TEMPORARY TABLE IF EXISTS IH_ThreeMonth;   
	CREATE TEMPORARY TABLE IF NOT EXISTS IH_ThreeMonth
	SELECT IJ.RIC, IJ.ReferenceIndex, IJ.ThreeMonthOld, MIN(IH.DateOfAddition) As ThreeMonthOldDate
	FROM IndexHistory IH
	INNER JOIN 
	(
		SELECT RIC,ReferenceIndex, LatestDate, DATE_SUB(LatestDate, INTERVAL 3 MONTH) ThreeMonthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON IH.RIC=IJ.ReferenceIndex
	WHERE IH.DateOfAddition >= IJ.ThreeMonthOld 
	GROUP BY IJ.RIC, IJ.ReferenceIndex
	HAVING DATEDIFF(MIN(IH.DateOfAddition), IJ.ThreeMonthOld  ) <= 15;
  
	DROP TEMPORARY TABLE IF EXISTS IH_TwelveMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS IH_TwelveMonth
	SELECT IJ.RIC, IJ.ReferenceIndex, IJ.TwelveMonthOld, MIN(IH.DateOfAddition) As TwelveMonthOldDate
	FROM IndexHistory IH
	INNER JOIN 
	(
		SELECT RIC,ReferenceIndex, LatestDate, DATE_SUB(LatestDate, INTERVAL 12 MONTH) TwelveMonthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON IH.RIC=IJ.ReferenceIndex
	WHERE IH.DateOfAddition >= IJ.TwelveMonthOld 
	GROUP BY IJ.RIC, IJ.ReferenceIndex
	HAVING DATEDIFF(MIN(IH.DateOfAddition), IJ.TwelveMonthOld  ) <= 15;
       
	/*Select * From t_pp;*/

	UPDATE  t_pp TP
	LEFT OUTER JOIN 
	(	SELECT OM.RIC, OM.ReferenceIndex,OM.OneMOnthOld,IH.PriceClose OneMonthPrice
		FROM IH_OneMonth  OM
		INNER JOIN IndexHistory IH ON OM.ReferenceIndex = IH.RIC AND OM.OneMOnthOldDate = IH.DateOfAddition
	) OD ON TP.RIC = OD.RIC 
	LEFT OUTER JOIN 
	(
		SELECT OM.RIC, OM.ReferenceIndex,OM.ThreeMonthOld,IH.PriceClose ThreeMonthPrice
		FROM IH_ThreeMonth  OM
		INNER JOIN IndexHistory IH ON OM.ReferenceIndex = IH.RIC AND OM.ThreeMonthOldDate = IH.DateOfAddition
	) TD ON TP.RIC=TD.RIC
	LEFT OUTER JOIN 
	(
		SELECT OM.RIC, OM.ReferenceIndex,OM.TwelveMonthOld,IH.PriceClose TwelveMonthPrice
		FROM IH_TwelveMonth  OM
		INNER JOIN IndexHistory IH ON OM.ReferenceIndex = IH.RIC AND OM.TwelveMonthOldDate = IH.DateOfAddition
	)  TM ON TP.RIC = TM.RIC
	LEFT OUTER JOIN
	(
		SELECT IH.RIC, IY.YTDDate, IH.PriceClose AS YTDPrice
		FROM IndexHistory IH
		INNER JOIN 
		(
			SELECT RIC, MIN(DateOfAddition) YTDDate
			FROM  IndexHistory 
			WHERE DateOfAddition >=  DATE_FORMAT(Current_Date() ,'%Y-01-01') 
			GROUP BY RIC
		) IY ON IY.RIC =IH.RIC AND IH.DateOfAddition = IY.YTDDate
    ) YD ON TP.ReferenceIndex = YD .RIC 
	SET TP.OneMthIndexClose    = OD.OneMonthPrice,
		TP.ThreeMthIndexClose = TD.ThreeMonthPrice, 
		TP.TwelveMthIndexClose= TM.TwelveMonthPrice,
		TP.YTDIndexClose		 = YD.YTDPrice;
 
	/*Select * From t_pp;*/
    DROP TEMPORARY TABLE IF EXISTS CH_OneMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS CH_OneMonth
	SELECT IJ.RIC,CM.RIC as RICCurCode ,CM.CurrencyCode, IJ.OneMOnthOld, Min(CH.DateOfAddition) OneMonthDate
	FROM CurrencyHistory CH
    INNER JOIN CurrencyMaster CM ON CH.RIC = CM.RIC 
	INNER JOIN 
	(
		SELECT RIC, TradingCurrency , LatestDate, DATE_SUB(LatestDate, INTERVAL 1 MONTH) OneMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON CM.CurrencyCode=IJ.TradingCurrency 
	WHERE CH.DateOfAddition >= IJ.OneMOnthOld 
	GROUP BY IJ.RIC
	HAVING DATEDIFF(MIN(CH.DateOfAddition), IJ.OneMOnthOld  ) <=15;
    
    
	DROP TEMPORARY TABLE IF EXISTS CH_ThreeMonth;
	CREATE TEMPORARY TABLE IF NOT EXISTS CH_ThreeMonth
	SELECT IJ.RIC,CM.RIC as RICCurCode,CM.CurrencyCode, IJ.ThreeMOnthOld, Min(CH.DateOfAddition) ThreeMonthDate
	FROM CurrencyHistory CH
    INNER JOIN CurrencyMaster CM ON CH.RIC = CM.RIC 
	INNER JOIN 
	(
		SELECT RIC, TradingCurrency , LatestDate, DATE_SUB(LatestDate, INTERVAL 3 MONTH) ThreeMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON CM.CurrencyCode=IJ.TradingCurrency 
	WHERE CH.DateOfAddition >= IJ.ThreeMOnthOld 
	GROUP BY IJ.RIC
	HAVING DATEDIFF(MIN(CH.DateOfAddition), IJ.ThreeMOnthOld  ) <= 15;

	DROP TEMPORARY TABLE IF EXISTS CH_TwelveMonth;	
	CREATE TEMPORARY TABLE IF NOT EXISTS CH_TwelveMonth    
	SELECT IJ.RIC,CM.RIC as RICCurCode,CM.CurrencyCode, IJ.TwelveMOnthOld, Min(CH.DateOfAddition) TwelveMonthDate
	FROM CurrencyHistory CH
    INNER JOIN CurrencyMaster CM ON CH.RIC = CM.RIC 
	INNER JOIN 
	(
		SELECT RIC, TradingCurrency , LatestDate, DATE_SUB(LatestDate, INTERVAL 12 MONTH) TwelveMOnthOld
		FROM t_pp TP 
		WHERE RIC IS NOT NULL 
    
	) IJ ON CM.CurrencyCode=IJ.TradingCurrency 
	WHERE CH.DateOfAddition >= IJ.TwelveMOnthOld 
	GROUP BY IJ.RIC
	HAVING DATEDIFF(MIN(CH.DateOfAddition), IJ.TwelveMOnthOld  ) <= 15;
    
    /*    Select * From t_pp; */
    
	UPDATE t_pp TP
	LEFT OUTER JOIN 
	(	SELECT OM.RIC, OM.CurrencyCode,OM.OneMonthOld,CH.Price OneMonthPrice
		FROM CH_OneMonth  OM
		INNER JOIN CurrencyHistory CH ON OM.RICCurCode = CH.RIC AND OM.OneMonthDate = CH.DateOfAddition
	) OD ON TP.RIC = OD.RIC 
	LEFT OUTER JOIN 
	(	
		SELECT OM.RIC, OM.CurrencyCode,OM.ThreeMonthOld,CH.Price ThreeMonthPrice
		FROM CH_ThreeMonth  OM
		INNER JOIN CurrencyHistory CH ON OM.RICCurCode = CH.RIC AND OM.ThreeMonthDate = CH.DateOfAddition
	) TD ON TP.RIC=TD.RIC
	LEFT OUTER JOIN 
	(
		SELECT OM.RIC, OM.CurrencyCode,OM.TwelveMonthOld,CH.Price TwelveMonthPrice
		FROM CH_TwelveMonth  OM
		INNER JOIN CurrencyHistory CH ON OM.RICCurCode = CH.RIC AND OM.TwelveMonthDate = CH.DateOfAddition
	)  TM ON TP.RIC = TM.RIC
	LEFT OUTER JOIN
	(
		SELECT CM.CurrencyCode, IY.YTDDate, CH.Price AS YTDPrice
		FROM CurrencyHistory CH
		INNER JOIN CurrencyMaster CM ON CH.RIC = CM.RIC
		INNER JOIN 
		(
			SELECT CH.RIC, MIN(DateOfAddition) YTDDate
			FROM  CurrencyHistory CH 
			WHERE DateOfAddition >=  DATE_FORMAT(Current_Date() ,'%Y-01-01') 
			GROUP BY  CH.RIC
		) IY ON IY.RIC =CH.RIC AND CH.DateOfAddition = IY.YTDDate
	) YD ON TP.TradingCurrency = YD.CurrencyCode
	SET TP.OneMthCloseUSD    = OneMthClose/OD.OneMonthPrice,
		TP.ThreeMthCloseUSD = ThreeMthClose/TD.ThreeMonthPrice, 
		TP.TwelveMthCloseUSD= TwelveMthClose/TM.TwelveMonthPrice,
		TP.YTDCloseUSD		 = YTDClose/YD.YTDPrice;

	Select *  FROM t_pp;
    
	SELECT 
	REPLACE(BBSymbol, ' Equity', '') as PricingSymbol, 
	ROUND((LatestClose / OneMthClose  -1 )* 100, 0) AS Performance_Absolute_1M, 
	ROUND((LatestClose / ThreeMthClose  -1) * 100, 0) AS Performance_Absolute_3M, 
	ROUND((LatestClose / TwelveMthClose  -1) * 100, 0) AS Performance_Absolute_12M, 
	ROUND((LatestClose / YTDClose - 1) * 100, 0) AS Performance_Absolute_YTD, 
    
	ROUND(( (LatestClose / LatestIndexClose)  / (OneMthClose / OneMthIndexClose ) -1 ) * 100, 0) AS Performance_Relative_1M, 
	ROUND(( (LatestClose / LatestIndexClose) / (ThreeMthClose / ThreeMthIndexClose ) -1 ) * 100, 0) AS Performance_Relative_3M, 
	ROUND(( (LatestClose / LatestIndexClose) / (TwelveMthClose / TwelveMthIndexClose )  -1 ) * 100, 0)  AS Performance_Relative_12M, 
	ROUND(( (LatestClose / LatestIndexClose) / (YTDClose / YTDIndexClose ) -1 ) * 100, 0)  AS Performance_Relative_YTD, 
    
	ROUND((LatestCloseUSD / OneMthCloseUSD - 1)*100, 0) AS Performance_Absolute_US_1M, 
	ROUND((LatestCloseUSD / ThreeMthCloseUSD - 1) *100, 0) AS Performance_Absolute_US_3M, 
	ROUND((LatestCloseUSD / TwelveMthCloseUSD -1)*100, 0) AS Performance_Absolute_US_12M, 
	ROUND((LatestCloseUSD / YTDCloseUSD - 1) *100 , 0) AS Performance_Absolute_US_YTD
	FROM t_pp
	;

    DROP TEMPORARY TABLE IF EXISTS t_latest;
    DROP TEMPORARY TABLE IF EXISTS t_pp;
    DROP TEMPORARY TABLE IF EXISTS t_latest;
    DROP TEMPORARY TABLE IF EXISTS SH_OneMonth;
    DROP TEMPORARY TABLE IF EXISTS SH_ThreeMonth;
    DROP TEMPORARY TABLE IF EXISTS SH_TwelveMonth;	
    DROP TEMPORARY TABLE IF EXISTS IH_OneMonth;
    DROP TEMPORARY TABLE IF EXISTS IH_ThreeMonth;   
    DROP TEMPORARY TABLE IF EXISTS IH_TwelveMonth;
    DROP TEMPORARY TABLE IF EXISTS CH_OneMonth;
    DROP TEMPORARY TABLE IF EXISTS CH_ThreeMonth;
    DROP TEMPORARY TABLE IF  EXISTS CH_TwelveMonth;

   
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DailyPricing` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `DailyPricing`()
BEGIN 
	SELECT 
	REPLACE(SM.BBSymbol, ' Equity', '') as TICKER, 
	date_format(SH.DateOfAddition,'%Y-%m-%d') as DATE, 
	ROUND(SH.PriceClose, 2) as PRICE,
	ROUND(SH.Volume, 0) as AVG_DLY_VOL
	FROM StockHistory as SH
	INNER JOIN StockMaster as SM on SM.RIC = SH.RIC 
	WHERE SM.IsHistoryParsed = 1
	AND DATE(DATE_SUB(SM.LastParsedDate, INTERVAL 1 DAY)) = DATE(SH.DateOfAddition)
    ORDER BY Ticker, Date Desc
	;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DP_IEAReportDataPopulation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `DP_IEAReportDataPopulation`()
BEGIN
	DROP TABLE IF EXISTS TotalSummaryReport_1;

	Create table TotalSummaryReport_1
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, RG.DisplayName As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM IEA_HistoricMacroElementsData_tab1_tab2b IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN Regions RG ON IE.RegionID = RG.RegionID
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.RegionID IS NOT NULL AND TableType IN ('1')

	UNION

	SELECT Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, CN.CountryName As Country
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx    
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM IEA_HistoricMacroElementsData_tab1_tab2b IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN Country CN ON IE.CountryID = CN.CountryID
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.CountryID IS NOT NULL AND TableType IN ('1')

	UNION
	Select Case 
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'

				 END As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx        
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period    
		, Value
			,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	From IEA_HistoricMacroElementsData_tab1_tab2b  IE 
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate
	LEFT OUTER JOIN Groups GR ON IE.GroupID1 = GR.GroupID
	LEFT OUTER JOIN Groups GR1 ON IE.GroupID2 = GR1.GroupID
	Where IE.TableType = '1' AND IE.GroupID1 IN (5,6) And IE.Mode IN ('Q','Y')
	UNION

	Select  CASE WHEN IE.PH1= 1 AND PH2 = 1 AND PH3 IS NULL AND PH4 IS NULL THEN 'Crude'
				 WHEN IE.PH1= 1 AND PH2 = 2 AND PH3 IS NULL AND PH4 IS NULL THEN 'NGL'
				 END
	 As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx         
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period  
		, Value
			,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		,IE.ReportedDate
	From IEA_HistoricMacroElementsData_tab1_tab2b  IE 
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate
	LEFT OUTER JOIN Groups GR ON IE.GroupID1 = GR.GroupID
	LEFT OUTER JOIN Groups GR1 ON IE.GroupID2 = GR1.GroupID
	Where IE.TableType = '1' AND  IE.PH1= 1 AND IE.PH2 IN ( 1,2) AND IE.PH3 IS NULL AND IE.PH4 IS NULL And IE.Mode IN ('Q','Y')
	UNION
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM IEA_HistoricMacroElementsData_tab1_tab2b IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType

	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.IsTotal  = 1 AND IE.TableType IN ('1')  AND PH2 IS NULL AND PH3 IS NULL AND PH4 IS NULL
	;

	DROP TABLE IF EXISTS ReportFor2b_1;

	Create table  ReportFor2b_1
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, CN.CountryName As Country
		, RG.DisplayName  As RegionName    
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM IEA_HistoricMacroElementsData_tab1_tab2b IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('2b') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN Country CN ON IE.CountryID = CN.CountryID AND CN.ProviderID = 1
	INNER JOIN Regions RG ON CN.RegionID = RG.RegionID AND RG.ProviderID  =1 
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.CountryID IS NOT NULL AND TableType IN ('2b') And IE.IsTotal = 1;

	DROP TABLE IF EXISTS ReportFor3;

	Create table ReportFor3
	SELECT Case When IE.ElementType = 'S' Then 'Supply'

	END As ElementType
	, CN.CountryName As Country
	, RG.DisplayName As RegionName 
	, IE.PeriodID
	, IE.Mode
	, IE.PeriodIdx
	, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
	, Value
	,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN NULL
	WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
	WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
	WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
	END As Groups
	, IE.ReportedDate
	FROM IEA_HistoricMacroElementsData_3 IE
	INNER JOIN
	(
	SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
	From IEA_HistoricMacroElementsData_3
	WHERe TableType IN ('3') And Mode IN ('Q','Y')
	Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN RegionCountryMapping RC ON IE.CountryID = RC.CountryID AND RC.RegionID= IE.RegionID AND RC.ProviderID = 1
	INNER JOIN Country CN ON RC.CountryID = CN.CountryID 
	INNER JOIN Regions RG ON RC.RegionID = RG.RegionID AND RG.ProviderID = 1
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y') AND TableType IN ('3') ;


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Test_IEAReportDataPopulation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `Test_IEAReportDataPopulation`()
BEGIN
	DROP TABLE IF EXISTS AletheiaParsing.TotalSummaryReport_1;

	Create table AletheiaParsing.TotalSummaryReport_1
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, RG.DisplayName As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM AletheiaParsing.IEA_HistoricMacroElementsData IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From AletheiaParsing.IEA_HistoricMacroElementsData
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN Regions RG ON IE.RegionID = RG.RegionID
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.RegionID IS NOT NULL AND TableType IN ('1')

	UNION

	SELECT Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, CN.CountryName As Country
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx    
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM AletheiaParsing.IEA_HistoricMacroElementsData IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From AletheiaParsing.IEA_HistoricMacroElementsData
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN Country CN ON IE.CountryID = CN.CountryID
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.CountryID IS NOT NULL AND TableType IN ('1')

	UNION
	Select Case 
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'

				 END As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx        
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period    
		, Value
			,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	From AletheiaParsing.IEA_HistoricMacroElementsData  IE 
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode , Max(ReportedDate) ReportedDate
		From IEA_HistoricMacroElementsData_tab1_tab2b
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate
	LEFT OUTER JOIN Groups GR ON IE.GroupID1 = GR.GroupID
	LEFT OUTER JOIN Groups GR1 ON IE.GroupID2 = GR1.GroupID
	Where IE.TableType = '1' AND IE.GroupID1 IN (5,6) And IE.Mode IN ('Q','Y')
	UNION

	Select  CASE WHEN IE.PH1= 1 AND PH2 = 1 AND PH3 IS NULL AND PH4 IS NULL THEN 'Crude'
				 WHEN IE.PH1= 1 AND PH2 = 2 AND PH3 IS NULL AND PH4 IS NULL THEN 'NGL'
				 END
	 As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx         
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period  
		, Value
			,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		,IE.ReportedDate
	From AletheiaParsing.IEA_HistoricMacroElementsData  IE 
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode , Max(ReportedDate) ReportedDate
		From AletheiaParsing.IEA_HistoricMacroElementsData
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate
	LEFT OUTER JOIN Groups GR ON IE.GroupID1 = GR.GroupID
	LEFT OUTER JOIN Groups GR1 ON IE.GroupID2 = GR1.GroupID
	Where IE.TableType = '1' AND  IE.PH1= 1 AND IE.PH2 IN ( 1,2) AND IE.PH3 IS NULL AND IE.PH4 IS NULL And IE.Mode IN ('Q','Y')
	UNION
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, NULL As RegionName
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM AletheiaParsing.IEA_HistoricMacroElementsData IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From AletheiaParsing.IEA_HistoricMacroElementsData
		WHERe TableType IN ('1') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType

	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.IsTotal  = 1 AND IE.TableType IN ('1')  AND PH2 IS NULL AND PH3 IS NULL AND PH4 IS NULL
	;

	DROP TABLE IF EXISTS AletheiaParsing.ReportFor2b_1;

	Create table  AletheiaParsing.ReportFor2b_1
	SELECT  Case When IE.ElementType = 'S' Then 'Supply' 
				 When IE.ElementType = 'D' Then 'Demand' 
				 WHEN IE.ElementType ='S' THEN 'Industry Stocks' 
				 WHEN IE.ElementType ='SG' THEN 'Government Controlled'
				 WHEN IE.GroupID1 = 5  THEN 'Processing Gains'
				 WHEN IE.GroupID1 = 6  THEN 'Global Biofuels'
				 END As ElementType
		, CN.CountryName As Country
		, RG.DisplayName  As RegionName    
		, IE.PeriodID
		, IE.Mode
		, IE.PeriodIdx
		, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
		, Value
		,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN  NULL
			 WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
			 WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
		END As Groups
		, IE.ReportedDate
	FROM AletheiaParsing.IEA_HistoricMacroElementsData IE
	INNER JOIN
	(
		SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
		From AletheiaParsing.IEA_HistoricMacroElementsData
		WHERe TableType IN ('2b') And Mode IN ('Q','Y')
		Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND  IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN RegionCountryMapping RC ON IE.CountryID = RC.CountryID AND RC.RegionID= IE.RegionID AND RC.ProviderID = 1
	INNER JOIN Country CN ON RC.CountryID = CN.CountryID 
	INNER JOIN Regions RG ON RC.RegionID = RG.RegionID AND RG.ProviderID = 1
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y')   And IE.CountryID IS NOT NULL AND TableType IN ('2b') And IE.IsTotal = 1;

	DROP TABLE IF EXISTS AletheiaParsing.ReportFor3;

	Create table AletheiaParsing.ReportFor3
	SELECT Case When IE.ElementType = 'S' Then 'Supply'

	END As ElementType
	, CN.CountryName As Country
	, RG.DisplayName As RegionName 
	, IE.PeriodID
	, IE.Mode
	, IE.PeriodIdx
	, Concat(IE.PeriodID,'-',Case WHEN IE.Mode = 'Y' THEN '' ELSE IE.PeriodIdx END, IE.Mode) As Period
	, Value
	,Case WHEN GR.Description IS NULL AND GR1.Description IS NULL THEN NULL
	WHEN GR.Description IS NULL AND GR1.Description IS NOT NULL THEN GR1.Description
	WHEN GR.Description IS NOT NULL AND GR1.Description IS NULL THEN GR.Description
	WHEN GR.Description IS NOT NULL AND GR1.Description IS NOT NULL THEN Concat(GR.Description,'-',GR1.Description)
	END As Groups
	, IE.ReportedDate
	FROM AletheiaParsing.IEA_HistoricMacroElementsData IE
	INNER JOIN
	(
	SELECT PeriodID, PeriodIdx,Mode, ElementType , Max(ReportedDate) ReportedDate
	From AletheiaParsing.IEA_HistoricMacroElementsData
	WHERe TableType IN ('3') And Mode IN ('Q','Y')
	Group By PeriodID,PeriodIdx, Mode, ElementType
	) IE1 ON IE.PeriodID = IE1.PeriodID AND IE.PeriodIdx =IE1.PeriodIdx AND IE.Mode=IE1.Mode AND IE.ReportedDate =IE1.ReportedDate AND IE.ElementType = IE1.ElementType
	INNER JOIN RegionCountryMapping RC ON IE.CountryID = RC.CountryID AND RC.RegionID= IE.RegionID AND RC.ProviderID = 1
	INNER JOIN Country CN ON RC.CountryID = CN.CountryID 
	INNER JOIN Regions RG ON RC.RegionID = RG.RegionID AND RG.ProviderID = 1
	Left outer join Groups GR ON GR.GroupID = IE.GroupID1 
	Left outer join Groups GR1 ON GR1.GroupID = IE.GroupID2
	Where IE.Mode IN ('Q','Y') AND TableType IN ('3') ;


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `VD_IEAReportDataValidation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `VD_IEAReportDataValidation`()
BEGIN
	Select CLS.GroupID1,CLS.PeriodID,CLS.PeriodIdx, CLS.Mode, CLS.Value, ATS.Value,
	IF(ATS.Value-CLS.Value>0.5,"FAIL","PASS") 
	FROM
	(
	SELECT GroupID1,PeriodID,PeriodIdx, Mode, Sum(Value) Value
	FROM Aletheia.IEA_HistoricMacroElementsData_tab1_tab2b 
	where tabletype = '1' 
	and ReportedDate = '2017-03-15 00:00:00' 
	and GroupID1 = 1 and IsTotal Is NULL
	Group by GroupID1, PeriodID, PeriodIdx, Mode

	) CLS 
	INNER JOIN
	(
	SELECT GroupID1,PeriodID,PeriodIdx, Mode, Value
	FROM Aletheia.IEA_HistoricMacroElementsData_tab1_tab2b 
	where tabletype = '1' 
	and ReportedDate = '2017-03-15 00:00:00' 
	and GroupID1 = 1 and IsTotal =1 

	) ATS ON CLS.GroupID1= ATS.GroupID1 AND CLS.PeriodID = ATS.PeriodID AND CLS.PeriodIdx=ATS.PeriodIDx AND CLS.Mode = ATS.Mode
	WHERE IF(ATS.Value-CLS.Value>0.5,"FAIL","PASS") = 'FAIL'
	;
    
        
    Select CLS.GroupID1,CLS.PeriodID,CLS.PeriodIdx, CLS.Mode, CLS.Value, ATS.Value, ATS.PeriodID, ATS.PeriodIDx, ATS.Mode,
	((ATS.Value/CLS.Value)-1)*100 as Result,
	IF((ATS.Value/CLS.Value-1)*100 > 0.05 or (ATS.Value/CLS.Value-1)*100 < -0.05,"FAIL","PASS")
	FROM
	(
	SELECT GroupID1,PeriodID,PeriodIdx, Mode,SUM(Value) Value
	FROM Aletheia.IEA_HistoricMacroElementsData_tab1_tab2b 
	where tabletype = '1' 
	and ReportedDate = '2017-03-15 00:00:00' 
	Group by GroupID1, PeriodID, PeriodIdx, Mode
	) CLS 
	INNER JOIN
	(
	SELECT GroupID1,PeriodID,PeriodIdx, Mode, SUM(Value) Value
	FROM Aletheia.IEA_HistoricMacroElementsData_tab1_tab2b 
	where tabletype = '1' 
	and ReportedDate = '2017-03-15 00:00:00' 
	Group by GroupID1, PeriodID, PeriodIdx, Mode
	) ATS ON CLS.GroupID1= ATS.GroupID1 AND CLS.PeriodID = ATS.PeriodID-1 AND CLS.PeriodIdx=ATS.PeriodIDx AND CLS.Mode = ATS.Mode
	WHERE IF((ATS.Value/CLS.Value-1)*100 > 0.05 or (ATS.Value/CLS.Value-1)*100 < -0.05,"FAIL","PASS") = 'FAIL'
    ;
    
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

-- Dump completed on 2019-08-23 17:24:41

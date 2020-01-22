import mysql.connector
from openpyxl import load_workbook

def dumpdata(tablename):
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='ZeusDB',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            print((cursor.fetchall()[0][0]))
            #for master tables query
            #LOAD DATA LOCAL INFILE 'csvpath' INTO TABLE TABLENAME;
            #https://stackoverflow.com/questions/6750146/mysql-bulk-insert-on-duplicate-key-update-via-load-data-infile
            sqlquery = "CREATE TABLE %s"%tablename
            cursor.execute(sqlquery)
    except Exception as e:
        print(e)


tablename = "`Attribute` (`AttID` smallint(6) NOT NULL,`TypeID` smallint(6) NOT NULL,`AttType` varchar(50) NOT NULL,`Display` varchar(100) NOT NULL,PRIMARY KEY (`TypeID`,`AttID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Calendar` (`DateID` int(11) NOT NULL,`Date` date NOT NULL,PRIMARY KEY (`DateID`),KEY`Ix_Calendar` (`DateID`,`Date`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`CoAttribute` (`SecurityID` bigint(20) NOT NULL,`CompSecInfoID` bigint(20) NOT NULL,`CoID` int(11) NOT NULL,`CurID` smallint(6) NOT NULL,`UnitID` smallint(6) NOT NULL,`ModeID` smallint(6) NOT NULL,`SectorID` smallint(6) DEFAULT NULL,PRIMARY KEY (`SecurityID`,`CompSecInfoID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Company` (`CoID` int(11) NOT NULL,`CoName` varchar(100) DEFAULT NULL,`Description` varchar(8000) DEFAULT NULL,`CountryID` smallint(6) DEFAULT NULL,`IntGICSID` int(11) DEFAULT NULL,`ExtGICSID` int(11) DEFAULT NULL,`CoTypeID` smallint(6) NOT NULL,`StatusID` smallint(6) DEFAULT NULL,`InclusionDID` int(11) DEFAULT NULL,PRIMARY KEY (`CoID`),KEY `id_Company` (`CoID`,`CountryID`,`StatusID`),FULLTEXT KEY `id_Company_Name` (`CoName`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`CoSecurity` (`SecurityID` bigint(20) NOT NULL,`CoID` int(11) DEFAULT NULL,`Ticker` varchar(20) DEFAULT NULL,`ISIN` varchar(20) DEFAULT NULL,`CUSIP` varchar(20) DEFAULT NULL,`SEDOL` varchar(20) DEFAULT NULL,`CIK` varchar(50) DEFAULT NULL,`CoCIK` bigint(20) DEFAULT NULL,`STTicker` varchar(20) DEFAULT NULL, `MCaps` smallint(6) DEFAULT '63',`IsPrimary` bit(1) DEFAULT NULL, `ListTypeID` smallint(6) DEFAULT NULL, `ExchangeID` smallint(6) DEFAULT NULL,  `DepReceipt` smallint(6) DEFAULT NULL,PRIMARY KEY (`SecurityID`),KEY `id_CoSecurity` (`CoID`,`Ticker`),FULLTEXT KEY `Idx_Ticker` (`Ticker`),CONSTRAINT `FK_CoSecurity_Company` FOREIGN KEY (`CoID`) REFERENCES `Company` (`CoID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Country` (`CountryID` smallint(6) NOT NULL,`Name` varchar(100) DEFAULT NULL,`Abbreviation` varchar(3) DEFAULT NULL,`NativeLang` varchar(50) DEFAULT NULL,`IsMultipleLang` bit(1) DEFAULT NULL,`DatabaseName` varchar(25) DEFAULT NULL,`ServerIP` varchar(45) DEFAULT NULL,`UserName` varchar(25) DEFAULT NULL,`Password` varchar(25) DEFAULT NULL,`Provider` varchar(50) DEFAULT NULL, PRIMARY KEY (`CountryID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Currency` (`CurID` smallint(6) NOT NULL,`CurCode` varchar(3) NOT NULL,`CountryID` smallint(6) DEFAULT NULL,`Description` varchar(50) DEFAULT NULL,`IsActive` bit(1) NOT NULL,`Divisor` float DEFAULT NULL,PRIMARY KEY (`CurID`))"
dumpdata(tablename)
tablename = "`Exchange` (  `ExchangeID` smallint(6) NOT NULL,  `Name` varchar(50) NOT NULL,  `Description` varchar(50) DEFAULT NULL,`XigniteSymbol` varchar(10) DEFAULT NULL,`XigniteSuffix` varchar(10) DEFAULT NULL,`CountryID` smallint(6) DEFAULT NULL,`CurID` smallint(6) DEFAULT NULL,`StartTID` int(11) DEFAULT NULL, `EndTID` int(11) DEFAULT NULL,PRIMARY KEY (`ExchangeID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`GICS` (`GICSID` smallint(6) NOT NULL,`GICSCode` int(11) NOT NULL,`GICSTypeID` smallint(6) NOT NULL,`ParentCode` int(11) DEFAULT NULL,`ParentType` smallint(6) DEFAULT NULL,`Description` varchar(255) DEFAULT NULL,PRIMARY KEY (`GICSID`), UNIQUE KEY `UK_GICS` (`GICSCode`,`GICSTypeID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Time` (`TimeID` int(11) NOT NULL,`Value` time NOT NULL,PRIMARY KEY (`TimeID`), KEY `Ix_Time` (`TimeID`,`Value`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`Unit` (`UnitID` smallint(6) NOT NULL,`Description` varchar(50) NOT NULL,`Value` int(11) DEFAULT NULL, PRIMARY KEY (`UnitID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdata(tablename)
tablename = "`XbrlGlobalElement` (`GXbrlEleID` bigint(20) NOT NULL,`Taxonomy` varchar(300) NOT NULL,`FormID` smallint(6) DEFAULT NULL,`PeriodTypeID` smallint(6) DEFAULT NULL,`DataID` smallint(6) DEFAULT NULL,`SrIdx` int(11) DEFAULT NULL,`GICSID` int(11) DEFAULT NULL,`ParentGXbrlEleID` bigint(20) DEFAULT NULL,`Depth` smallint(6) DEFAULT NULL, `HistFormula` varchar(800) DEFAULT NULL, `EstFormula` varchar(800) DEFAULT NULL,`YHistFormula` varchar(800) DEFAULT NULL,`YHiddenFormula` varchar(800) DEFAULT NULL,`TransformID` smallint(6) DEFAULT NULL,`IsOI` bit(1) DEFAULT NULL,PRIMARY KEY (`GXbrlEleID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;"
dumpdata(tablename)

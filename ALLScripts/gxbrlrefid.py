import mysql.connector
from pymongo import MongoClient
from openpyxl import load_workbook
from datetime import date


#
# def colnum_string(n):
#     string = ""
#     while n > 0:
#         n, remainder = divmod(n - 1, 26)
#         string = chr(65 + remainder) + string
#     return string

def dumpdataStarSchema():
    try:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.DWHDB
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DWHDB',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            # print((cursor.fetchall()[0][0]))
            globalelement = (list(db.GlobalElement.find({})))
            for val in (globalelement):
                print(val['GXbrlEleID'],val['Description'])
                try:
                #             # print(gxbls[0])
                    updateQuery = "update DWElement set RefEleDescription = '%s' where EleRefID = %s" %(str(val['Description']),val['GXbrlEleID'])
                    cursor.execute(updateQuery)
                    connection.commit()
                    print('query executed')
                except Exception as e:
                    pass
                    print(e)


    except Exception as e:
        print(e)






# tablename = "`StarSchema1` (`FactID` smallint(6) NOT NULL, `UID` smallint(6) NOT NULL,  `PeriodID` varchar(50) NOT NULL,  `ReportedDateID` varchar(256) DEFAULT NULL,  `Value` int(11) DEFAULT NULL,  PRIMARY KEY (`FactID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
# dumpdataStarSchema()
# tablename = "`PeriodwiseSchema1` (`FactID` smallint(6) NOT NULL,`ReportedDateID` varchar(256) DEFAULT NULL,`DWHID` int (23), PRIMARY KEY (`FactID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
# dumpPeriodSchema()
# # tablename = "`UIDwiseSchema1` (`FactID` smallint(6) NOT NULL,`PeriodID` varchar(50) NOT NULL, `ReportedDateID` varchar(256) DEFAULT NULL,  PRIMARY KEY (`FactID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
dumpdataStarSchema ()




import mysql.connector
from pymongo import MongoClient
from openpyxl import load_workbook
from datetime import date
try:
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.DWHDB
    # print(db)
    # print(db.list_collection_names());
    connection = mysql.connector.connect(host='192.168.10.13',
                                         database='DWHDB',
                                         user='root',
                                         password='Bluecrest')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        cursor = connection.cursor(buffered=True)
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)
        regiocountryMapping = (list(db.RegionCountryMapping.find({})))

        for r in regiocountryMapping:
            regionid = r['RegionID']
            countryid = r['CountryID']
            findQuery = "select DWHGeoID from DWGeography where RefID = %s and Type = 2"
            cursor.execute(findQuery,(regionid,))
            reg = cursor.fetchone()[0]
            findQueryCountry = "select DWHGeoID from DWGeography where RefID = %s and Type = 3"
            cursor.execute(findQueryCountry, (countryid,))
            country =  cursor.fetchone()[0]
            # print(reg,country)
            insertQueyMapping = "insert into DWGeographyMapping (MappingID,CountryID,MappingType,Description) values\
                            ('%s','%s','%s','%s')" %(reg,country,'2','Region')
            cursor.execute(insertQueyMapping)
            connection.commit()
except Exception as e:
    print("Error while connecting to MySQL",e)

finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
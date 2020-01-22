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
        regions = (list(db.Region.find({})))
        dwhgeoid = 0

        for re in regions:
            dwhgeoid = dwhgeoid + 1
            type = 2
            desc = re['RegionName']
            refID = re['RegionID']
            # print(re['RegionID'],re['RegionName'])
            insertQuery = "insert into DWGeography (DWHGeoID,Type,Description,RefID) value('%s','%s','%s','%s')"%(dwhgeoid,type,desc,refID)
            cursor.execute(insertQuery)
            connection.commit()

except Exception as e:
    print("Error while connecting to MySQL",e)

finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from openpyxl import load_workbook
from datetime import date
import pandas as pd

def starschemamultiple():
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DWHDB1',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)

            extractdata = "select * from DWEleIDSchema1 where DWCoID = 32994"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            print(re)
            # df = (pd.DataFrame(re))
            # for val in range(2,10):
            #     for index,rows in df.iterrows():
            #         multiple = val * rows[3]
            #         addition = val + rows[4]
            #         print(rows[0], rows[1], rows[2], multiple,addition)
            #         insertQuery = "insert into DWEleIDSchema1(DWID,PeriodID,ReportedDateID,Value,DWCoID) values(%s,%s,%s,%s,%s)"%(rows[0],rows[1],\
            #                                                                                                                     rows[2],multiple,addition)
            #         cursor.execute(insertQuery)
            #         connection.commit()
            #         print("query executed")
                    # break

    except Exception as e:
        print("Error while connecting to MySQL",e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def DWIDSchema():
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DWHDB1',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)

            extractdata = "select * from DWEleIDSchema1 where DWCoID = 32994"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            df = (pd.DataFrame(re))


            # for val in range(1, 10):
            #     for index, rows in df.iterrows():
            #         multiple = val * rows[3]
            #         addition = val + rows[4]
            #         print(rows[0], rows[1], rows[2], multiple, addition)
            #         insertQuery = "insert into DWEleIDSchema1(PeriodID,ReportedDateID,Value,DWCoID) values(%s,%s,%s,%s,%s)" % (
            #         rows[0], rows[1], \
            #         rows[2], multiple, addition)
            #         cursor.execute(insertQuery)
            #         connection.commit()
            #         print("query executed")
                    # break

    except Exception as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def StockStarSchema():
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DWHDB1',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)

            extractdata = "select * from DWStockStarSchema where DWCoID = 32994"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            # print(re)
            df = (pd.DataFrame(re))
            print(df)
            for val in range(31, 100):
                for index, rows in df.iterrows():
                    multiple = val * rows[3]
                    addition = val + rows[4]
                    print(rows[0], rows[1], rows[2], multiple, addition)
                    insertQuery = "insert into DWStockStarSchema(DWID,PeriodID,ReportedDateID,Value,DWCoID) values(%s,%s,%s,%s,%s)" % (
                    int(rows[0]), rows[1], \
                    rows[2], multiple, int(addition))
                    cursor.execute(insertQuery)
                    connection.commit()
                    print("query executed")


    except Exception as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



# DWIDSchema()
DWIDSchema()
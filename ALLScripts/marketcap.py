import os
import re
import csv
import mysql.connector
from openpyxl import load_workbook
from datetime import date
try:
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
        # result = cursor.execute("select * from DWHMainQuery")
        # print(result)

        periodIDQuery = "select distinct(PeriodID) from StarSchema"
        cursor.execute(periodIDQuery)
        re = cursor.fetchall()
        coid = 10657
        for period in re:
            revenue = "select * from StarSchema where DWHID = 5 and PeriodID = %s and DWHCoID = %s "
            cursor.execute(revenue,(period[0],coid,))
            try:
                periodRevenue = cursor.fetchone()[3]
            except Exception as e:
                print("Error ", e)
                periodRevenue = None
                pass
            sharesOutstanding = "select * from StarSchema where DWHID = 215 and PeriodID = %s and DWHCoID = %s"
            cursor.execute(sharesOutstanding, (period[0],coid,))
            try:
                periodsharesOutstanding = cursor.fetchall()[0][3]
            except Exception as e:
                print("Error ", e)
                periodsharesOutstanding = None
                pass
            stockPrice = "select * from StarSchema where DWHID = 214 and PeriodID = %s and DWHCoID = %s"
            cursor.execute(stockPrice, (period[0],coid,))
            try:
                periodstockPrice = cursor.fetchall()[0][3]
            except Exception as e:
                print("Error ", e)
                periodstockPrice = None
                pass
            print(periodRevenue,periodsharesOutstanding,periodstockPrice)
            if(periodsharesOutstanding != None and periodstockPrice != None ):
                marketcap = periodsharesOutstanding * periodstockPrice

                try:
                    DWHID = '179'
                    ReportedDateID = '20191106'
                    insertQuery = "INSERT INTO StarSchema (DWHID,PeriodID,ReportedDateID,Value,DWHCoID) VALUES (%s,%s,%s,%s,%s)"%(DWHID,period[0],ReportedDateID,marketcap,coid)
                    cursor.execute(insertQuery)
                    connection.commit()
                    print("ecexuted succesfully")


                except Exception as e:
                    print("Error ", e)

            else:
                pass




except Exception as e:
    print("Error while connecting to MySQL",e)
    pass

finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
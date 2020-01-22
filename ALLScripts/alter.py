import mysql.connector
from openpyxl import load_workbook
from datetime import date
from pymongo import MongoClient


#
# def colnum_string(n):
#     string = ""
#     while n > 0:
#         n, remainder = divmod(n - 1, 26)
#         string = chr(65 + remainder) + string
#     return string

def DWStarSchema():
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
            print((cursor.fetchall()[0][0]))

            for i in range(310,362):
                print(i)
                altertable = "alter table DWEleIDSchema1 add `%s` double null"
                cursor.execute(altertable,(i,))
                connection.commit()




    except Exception as e:
        print(e)






DWStarSchema()





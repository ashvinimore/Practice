# import pandas as pd
# datelist = pd.date_range(pd.datetime.today(), periods=10000).tolist()
# for val in datelist:
#    val = str(val)
#    print(val.split(' ')[0])

import mysql.connector
from openpyxl import load_workbook


import datetime
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

    start = datetime.datetime.strptime("01-01-1995", "%d-%m-%Y")
    end = datetime.datetime.strptime("31-12-2050", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    for date in date_generated:
        yydate =  (date.strftime("%Y-%m-%d"))
        standarddate = str (date.strftime("%d-%m-%Y"))
        print(standarddate)
        dateid =  (date.strftime("%Y%m%d"))
        # print(dateid)
        insertQuery = "insert into CalendarDate(DateID,Date,StandardDateFormat)  values('%s','%s','%s')" % ((dateid, yydate, standarddate,))
        try:
            cursor.execute(insertQuery)
            print("query excuted successfully")
            connection.commit()
        except Exception as e:
            print(e)



except Exception as e:
    print("Error while connecting to MySQL",e)


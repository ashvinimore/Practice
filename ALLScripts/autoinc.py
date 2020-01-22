import mysql.connector
from openpyxl import load_workbook
from datetime import date


def PrevValueDump():
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
            count = 0
            try:
                SelectQuery = "Select * from StockStarSchema"
                cursor.execute(SelectQuery)
                re = (cursor.fetchall())
                print(re)

                for result in re:
                    count = count + 1
                    print(result,count)
                    try:
                        UpdateQuery = "Update StockStarSchema set FactID = %s where DWID = %s and PeriodID = %s and DWCoID = %s" %(count,str(result[0]),str(result[1]),str(result[4]))
                        cursor.execute(UpdateQuery)
                        connection.commit()
                        print("executed")
                        # break
                    except Exception as e:
                        print(e)

                # for val in range(1,7049):
                #     UpdateQuery  = "Update StockStarSchema set FactID = %s where "%val
                #     cursor.execute(UpdateQuery)
                #     connection.commit()
                #     print("executed")

            except Exception as e:
                print(e)


    except Exception as e:
        print(e)

PrevValueDump()
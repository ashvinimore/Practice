import mysql.connector
from datetime import date

def PeriodUpdate():
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

            Eleschema = "select * from DWEleIDSchema11"
            cursor.execute(Eleschema)
            re = cursor.fetchall()
            # print(re)

            for period in re:
                periodtable = "select PeriodIDPri from CalendarPeriod where PeriodID = %s"%str(period[0])
                cursor.execute(periodtable)
                print(period[0])
                try:
                    periodre = cursor.fetchall()
                    try:
                        updateQuery = "Update DWEleIDSchema11 set PeriodID = %s where PeriodID = %s"%(str(periodre[0][0]),str(period[0]))
                        cursor.execute(updateQuery)
                        connection.commit()
                        print("query executed")
                        # break
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print("error",e)





    except Exception as e:
        print(e)
PeriodUpdate()
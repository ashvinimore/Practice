import mysql.connector
import pandas as pd
import sqlalchemy

def sample():
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

            SearchQuery = "select *  from DWStocksStarSchema where DWCoID = 11569 and DWID = 281"
            cursor.execute(SearchQuery)
            searchres = cursor.fetchall()
            for i,res in enumerate(searchres):
                j = i-1
                if (j < 0):
                    pass
                else:
                    print(i,j,searchres[i][1],searchres[j][3])
                    try:
                        updateQuery = "Update DWStocksStarSchema set PrevValue = %s where DWCoID = 11569 and DWID = 281 and PeriodID = %s" %(str(searchres[j][3]),str(searchres[i][1]))
                        cursor.execute(updateQuery)
                        print("executed")
                    except Exception as e:
                        print("Error", e)

           # insertQuery = "insert into DWDerStocksStarSchema (DWID,PeriodID,ReportedDateID,Value,DWCoID) values \
           #     (%s,%s,%s,%s,%s)"

    except Exception as e:
        print("Error while connecting to MySQL", e)
    #
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

sample()
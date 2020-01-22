import mysql.connector
import pandas as pd
import sqlalchemy


def starshema():
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB')
    df = pd.read_sql_table('DWStarSchema', engine)

    try:
        #
        frame = df.to_sql('DWStarSchemaMultipleCompany', engine, if_exists='append',index=False);

        #
    except ValueError as vx:

        print(vx)

    except Exception as ex:

      print(ex)



def period():
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

            dwcoid = "select DWCoID from DWDerivedCompany where Ticker IS Not NULL and DWCOID != 9 limit 1000";
            cursor.execute(dwcoid)
            res = cursor.fetchall()

            for coid in res:
                print(coid[0])
                insertmultiple = "Insert into DWStarSchemaMultipleCompany (DWID, PeriodID, ReportedDateID, Value, DWCoID)\
Select DWID, PeriodID, ReportedDateID, Value*05, %s From DWStarSchema Where DWCoID = 9"%str(coid[0])
                cursor.execute(insertmultiple)
                connection.commit()
                print("execute")
                # break
    except Exception as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# starshema()
period()


import mysql.connector
import pandas as pd
import sqlalchemy
import random

def sample():
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

            extractdata = "select * from DWStarStockSchema where DWCoID = 9"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            df = pd.DataFrame(re)
            # df[4] = (df[4]) + 1
            # df[3] = (df[3]) * 0.2
            print(df)


            # try:
            # #
            #     frame = df.to_sql('DWStarSchemaPanda', connection, if_exists='fail');
            # #
            # except ValueError as vx:
            #
            #     print(vx)
            #
            # except Exception as ex:
            #
            #     print(ex)
            #
            # else:
            #     tableName = 'DWStarSchemaPanda'
            #     print("Table %s created successfully." % tableName);


    except Exception as e:
        print("Error while connecting to MySQL", e)
    #
    # finally:
    #     # closing database connection.
    #     if (connection.is_connected()):
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")

# sample()



def starshema():
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB1')
    df = pd.read_sql_table('DWStarSchema', engine)
    for i in range(101 ,103):
        df['DWCoID'] = df['DWCoID'] + i
        # print (df['DWCoID'])
        df['Value'] = df['Value'] * i
    # print(df['Value'])
        print(df)
        try:
            #
            frame = df.to_sql('DWStarSchema1', engine, if_exists='append',index=False);

            #
        except ValueError as vx:

            print(vx)

        except Exception as ex:

          print(ex)



def periodschema():

    multiple = []
    # print("period")
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB')
    df = pd.read_sql_table('DWPeriodSchemaExtract', engine)
    dwcoid  = "select DWCoID from DWDerivedCompany where Ticker IS Not NULL and DWCOID not in(9,11569,3545,6918,9020) limit 5000 "
    with engine.connect() as con:
        res = list(con.execute(dwcoid))
    # print(res)
        # for i in res:
        #     print(random.random())

    for i in res:
        df['DWCoID'] = i[0]
        no = random.random()
        multiple.append(no)

        for col in df.columns:
            col = col.replace('P','')
            if(col.isdigit() == True):
                col = 'P' + col
                df[col] = (df[col]) * no

        try:
            frame = df.to_sql('DWPeriodSchemaMultiple', engine, if_exists='append', index=False)

        except ValueError as vx:
            print(vx)

        except Exception as ex:
            print(ex)


    print(multiple)
    return multiple


        #
        #



def DWIDSchema():
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB')
    df = pd.read_sql_table('DWPeriodSchemaExtract', engine)
    dwcoid = "select DWCoID from DWDerivedCompany where Ticker IS Not NULL and DWCOID not in(9,11569,3545,6918,9020) limit 5000 "
    with engine.connect() as con:
        res = list(con.execute(dwcoid))
    # print(res)
    # for i in res:
    #     print(random.random())

    for i in res:
        df['DWCoID'] = i[0]
        no = random.random()
        for col in df.columns:
            col = col.replace('P', '')
            if (col.isdigit() == True):
                col = 'P' + col
                df[col] = (df[col]) * no
        print(no)
        try:
            frame = df.to_sql('DWPeriodSchemaMultiple', engine, if_exists='append', index=False)

        except ValueError as vx:
            print(vx)

        except Exception as ex:
            print(ex)


# starshema()
mul = periodschema()
print(mul)
# DWIDSchema()

# sample()
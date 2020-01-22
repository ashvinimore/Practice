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

            extractdata = "select * from DWStarSchema1 where DWCoID = 9"
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


def DWIStarSchemaMultiple():
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

            extractdata = "select * from DWStarSchema1 where DWCoID = 9"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            df = (pd.DataFrame(re))


            for val in range(11, 101):
                for index, rows in df.iterrows():
                    multiple = val * rows[3]
                    addition = val + rows[4]
                    print(rows[0], rows[1], rows[2], multiple, addition)
                    insertQuery = "insert into DWStarSchema1(DWID,PeriodID,ReportedDateID,Value,DWCoID) values(%s,%s,%s,%s,%s)" % (
                    rows[0], rows[1], \
                    rows[2], multiple, addition)
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

            # extractdata = "select * from DWStockStarSchema where DWCoID = 32994"
            # cursor.execute(extractdata)
            # re = cursor.fetchall()
            # # print(re)
            # df = (pd.DataFrame(re))
            # print(df)
            # for val in range(100, 131):
            #     for index, rows in df.iterrows():
            #         multiple = val * rows[3]
            #         addition = val + rows[4]
            #         print(rows[0], rows[1], rows[2], multiple, addition)
            #         insertQuery = "insert into DWStockStarSchema(DWID,PeriodID,ReportedDateID,Value,DWCoID) values(%s,%s,%s,%s,%s)" % (
            #         int(rows[0]), rows[1], \
            #         rows[2], multiple, int(addition))
            #         cursor.execute(insertQuery)
            #         connection.commit()
            #         print("query executed")


    except Exception as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def DWIDSchemaMultiple():
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

            extractdata = "SELECT * FROM DWEleIDSchema11 where DWCoID = 3545"
            cursor.execute(extractdata)
            re = cursor.fetchall()
            df = (pd.DataFrame(re))
            # print(df)
            for val in range(2,10):
                print(val)
                for index,rows in df.iterrows():
                    addition = int(val + rows[295])
                    print(int(rows[0]), int(rows[1]),addition,int(rows[295]))
                    try:
                        searchQuery = "select * from DWEleIDSchema11 where DWCoID = %s and PeriodID = %s" % (
                        addition, int(rows[0]))
                        cursor.execute(searchQuery)
                        reexist = cursor.fetchall()

                        if reexist != []:
                            print("reexist", reexist)
                        else:
                            print("noo")
                            insertQuery = "insert into DWEleIDSchema11(PeriodID,ReportedDateID,DWCoID) values (%s,%s,%s)"%(int(rows[0]), int(rows[1]),addition)
                            cursor.execute(insertQuery)
                            for i in range(1,362):
                                if i == 295:
                                    print(i)
                                    pass
                                else:
                                    multiple = int(val * rows[i])
                                    try:
                                        updatequery = "Update DWEleIDSchema11 set `%s` = %s where DWCoID = %s and PeriodID = %s"
                                        cursor.execute(updatequery, (i, multiple, addition, int(rows[0])))
                                        connection.commit()
                                        # print("query executed updatesss")
                                        connection.commit()
                                    except Exception as e:
                                        print(e)
                                        pass
                            print("query executed")
                    except Exception as e:
                        print("Error", e)



    except Exception as e:
        print("Error while connecting to MySQL",e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def DWPeriodMultiple():
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
            dfvalues = []
            df = pd.read_sql("SELECT * FROM DWPeriodSchema1 where DWCoID = 9020", con=connection)
            coid = 9

            #insrert rows for companies DWHIDwise
                   #
            #

            for coids in range(2,3):
                coid = coid + coids
                reporteddate = '20191122'
                for dwhid in range(1,360):
                    try:
                        searchQuery = "select * from DWPeriodSchema1 where DWID = %s and DWCoID = %s"%(dwhid,coid)
                        cursor.execute(searchQuery)
                        re = cursor.fetchall()
                        if re != []:
                            print(re[0][0])
                            for period in (list(df.columns.values)):
                                if (period.isdigit() == True):
                                    print(period)
                                    val = df.iloc[dwhid][period]  * coids
                                    updateQuery = "Update DWPeriodSchema1 set `%s` = %s where DWCoID = %s and DWID = %s"%(period,val,coid,dwhid)
                                    cursor.execute(updateQuery)
                                    connection.commit()
                                    # print("updated")
                            # break
                        else:

                            insertQuery = "insert into DWPeriodSchema1 (DWID,ReportedDateID,DWCoID) Values(%s,%s,%s)"\
                                                                                    %(dwhid,reporteddate,coid)
                            cursor.execute(insertQuery)
                            connection.commit()
                            print("executed")
                    except Exception as e:
                        print("Error", e)

            # for period in (list(df.columns.values)):
            #     if(period.isdigit() == True):
            #         print(period)
                    # for i in range(1,35):
                    #     print(period,i,df.iloc[i][period])
                        # insertQuery =
                    # break



            # extractdata = "SELECT * FROM DWPeriodSchema1 where DWCoID = 3545"
            # cursor.execute(extractdata)
            # re = cursor.fetchall()
            # df = (pd.DataFrame(re))
            # print(df.head())

            # for val in range(2,3):
            #     print(val)
            #     for index,rows in df.iterrows():
            #         addition = int(val + rows[777])
            #         print(int(rows[0]), int(rows[1]),addition,int(rows[777]))
            #         try:
            #             searchQuery = "select * from DWPeriodSchema1 where DWCoID = %s and DWID = %s"%(addition,int(rows[0]))
            #             cursor.execute(searchQuery)
            #             reexist = cursor.fetchall()
            #             print("reexist",reexist)
            #         except Exception as e:
            #             print("Error", e)
            #
            #         if reexist != []:
            #             print("found")
            #             multiple = int(val * rows[i])
            #             try:
            #                 updatequery = "Update DWPeriodSchema1 set `%s` = %s where DWCoID = %s and PeriodID = %s"
            #                 cursor.execute(updatequery, (i, multiple, addition, int(rows[0])))
            #                 connection.commit()
            #                 # print("query executed updatesss")
            #                 connection.commit()
            #             except Exception as e:
            #                 print(e)
            #                 pass
            #         else:
            #             insertQuery = "insert into DWPeriodSchema1(DWID,ReportedDateID,DWCoID) values (%s,%s,%s)"%(int(rows[0]), int(rows[1]),addition)
            #             cursor.execute(insertQuery)
            #             connection.commit()
            #             print('inserted')

                                #
                        # print("query executed")


    except Exception as e:
        print("Error while connecting to MySQL",e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# DWIDSchema()
DWIStarSchemaMultiple()
# DWIDSchemaMultiple()
# DWPeriodMultiple()
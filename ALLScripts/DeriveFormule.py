import mysql.connector
from openpyxl import load_workbook
from datetime import date


def YoYQoQStarSchema():
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

            try:

                reporteddate = 20191216
                # dereleid = 46

                # starstockYoy = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultipleAll P1 INNER JOIN DWStarSchemaMultipleAll P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID -10000 where P1.DWID = 319 and P1.DWCoID < 500"
                #
                # cursor.execute(starstockYoy)
                # growthyoy = (cursor.fetchall())
                # for yoy in growthyoy:
                #     print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                #     try:
                #         insertQueryYoy = "INSERT INTO DWDerEleStarMultiple1 (DWDerEleID,PeriodID,ReportedDateID,Value,DWCoID) VALUES (%s,%s,%s,%s,%s)" % (
                #         dereleid, yoy[0], reporteddate, yoy[5], yoy[2])
                #         cursor.execute(insertQueryYoy)
                #         connection.commit()
                #         print("Yoy inserted")
                #
                #
                #     except Exception as e:
                #         print(e)

                # for QoQ
                dereleid = 45
                starstockQoQ = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultipleAll P1 INNER JOIN DWStarSchemaMultipleAll P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID - 1 where P1.DWID = 319 "
                cursor.execute(starstockQoQ)
                growthqoq = (cursor.fetchall())
                for yoy in growthqoq:
                    print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                    try:
                        insertQueryYoy = "INSERT INTO DWDerEleStarMultiple1(DWDerEleID,PeriodID,ReportedDateID,Value,DWCoID) VALUES (%s,%s,%s,%s,%s)" % (
                            dereleid, yoy[0], reporteddate, yoy[5], yoy[2])
                        cursor.execute(insertQueryYoy)
                        connection.commit()
                        print("Yoy inserted")
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)


    except Exception as e:
        print(e)


def PrevValueDump(DWCoid):
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

            try:
                today = date.today()
                reporteddatequery = "select * from CalendarDate where YYYYMMDD = %s"
                cursor.execute(reporteddatequery, (today,))
                reporteddate = cursor.fetchall()
                reporteddate = reporteddate[0][0]
                print(reporteddate)

                for coid in DWCoid:
                    starstock = "select * from StocksStarSchema1 where DWCoID = %s and DWID = 363" %coid
                    cursor.execute(starstock)
                    re = cursor.fetchall()
                    print(re)
                    for i, val in enumerate(re):
                        # print(val)
                        j = i - 1
                        if (j == -1):
                            val = 0
                        else:
                            val = re[j][3]
                            print(i, re[i][1], re[i][3], re[j][3])
                        try:
                            prevval = "Update StocksStarSchema1 set PrevValue = %s,ReportedDateID = %s where PeriodID = %s and DWCoID = %s and DWID = 363 " % (
                            str(val), str(re[i][2]),coid, str(re[i][1]))
                            cursor.execute(prevval)
                            connection.commit()
                            print("executed")
                            # break
                        except Exception as e:
                            print(e)

            except Exception as e:
                print(e)


    except Exception as e:
        print(e)


def DailyReturnsStocks(DWCoid):
    print("d")
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

            try:
                # today = date.today()
                # reporteddatequery = "select * from CalendarDate where YYYYMMDD = %s"
                # cursor.execute(reporteddatequery, (today,))
                # reporteddate = cursor.fetchall()
                # reporteddate = reporteddate[0][0]
                # print(reporteddate)
                reporteddate = 20191129
                dereleid = 4
                # DWCoID = 1101
                count = 0
                for coid in DWCoid:
                    DailyQuery = "select t2.PeriodID,t2.value ,t2.DWCoID as DWCoID ,(Select t1.Value From StockStarSchema1 t1 Where t1.DWID = t2.DWID and t1.DWCoID = t2.DWCoID\
                     And t1.PeriodID < t2.PeriodID Order by t1.PeriodID desc limit 1 )as PREVAL, (t2.value - (Select t1.Value From StockStarSchema1 t1 Where t1.DWID = t2.DWID and t1.DWCoID = t2.DWCoID And t1.PeriodID < t2.PeriodID Order by t1.PeriodID desc limit 1 )+0)/(Select t1.Value \
                     From StockStarSchema1 t1 Where t1.DWID = t2.DWID and t1.DWCoID = t2.DWCoID And t1.PeriodID < t2.PeriodID Order by t1.PeriodID desc limit 1 ) as DailyRet \
                     from StockStarSchema1 t2 where t2.DWID = 363  and t2.DWCoID = %s;"%(coid)
                    cursor.execute(DailyQuery)
                    daily = cursor.fetchall()

                    # print(len(daily))
                    for val in daily:
                        try:
                            count = count + 1
                            value = (str(val[4]).format(1.4))
                            try:
                                insertQueryDailyReturns = "INSERT INTO DWDerEleStarSchema1 (DWDerEleID,PeriodID,ReportedDateID,Value,DWCoID) VALUES (%s,%s,%s,%s,%s)" % (
                                    dereleid, val[0], reporteddate, value, coid)
                                cursor.execute(insertQueryDailyReturns)
                                connection.commit()
                                print("Daily returns inserted")
                                # break
                            except Exception as e:
                                print(e,value)
                        except Exception as e:
                            print(e)
                    print(count)


            except Exception as e:
                print(e)

    except Exception as e:
        print(e)


def YoYQoQDWIDSchema():
    print("ID")
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

            try:

                reporteddate = 20190912
                # dereleid = 46
                #
                # starstockYoy = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultiple P1 INNER JOIN DWStarSchemaMultiple P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID -10000 where P1.DWID = 319 "
                #
                # cursor.execute(starstockYoy)
                # growthyoy = (cursor.fetchall())
                # for yoy in growthyoy:
                #     print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                #     try:
                #         insertQueryYoy = "INSERT INTO DWDerEleDWIDSchemaMultiple (PeriodID,ReportedDateID,DE46,DWCoID) VALUES (%s,%s,%s,%s)" % (
                #          yoy[0], reporteddate, yoy[5], yoy[2])
                #         cursor.execute(insertQueryYoy)
                #         connection.commit()
                #         print("Yoy inserted")
                #
                #
                #     except Exception as e:
                #         print(e)

                # for QoQ
                dereleid = 45
                starstockQoQ = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultiple P1 INNER JOIN DWStarSchemaMultiple P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID - 1 where P1.DWID = 319 "
                cursor.execute(starstockQoQ)
                growthqoq = (cursor.fetchall())
                for yoy in growthqoq:
                    print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                    try:
                        UpdateQueryYoy = "Update DWDerEleDWIDSchemaMultiple set DE45 = %s where DWCoID = %s and PeriodID = %s and ReportedDateID = %s"%( yoy[5],yoy[2],yoy[0],reporteddate)
                        cursor.execute(UpdateQueryYoy)
                        connection.commit()
                        print("Yoy updated")
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)


    except Exception as e:
        print(e)


def YoYQoQPeriodSchema():
    print("Period")

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

            try:

                reporteddate = 20190912
                dereleid = 46

                starstockYoy = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultiple P1 INNER JOIN DWStarSchemaMultiple P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID -10000 where P1.DWID = 319 "

                cursor.execute(starstockYoy)
                growthyoy = (cursor.fetchall())
                for yoy in growthyoy:
                    print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                    try:
                        selectQuery = "select DWCoID from DWDerElePeriodMultiple where  DWCoID = %s and DWDerEleID = %s and ReportedDateID = %s"%(yoy[2],dereleid,reporteddate)
                        cursor.execute(selectQuery)
                        re = cursor.fetchall()
                        print((re))
                        if re == []:
                            insertQueryYoy = "INSERT INTO DWDerElePeriodMultiple (DWDerEleID,ReportedDateID,DWCoID) VALUES (%s,%s,%s)" % (
                             dereleid,reporteddate, yoy[2])
                            cursor.execute(insertQueryYoy)
                            connection.commit()
                            print("Yoy inserted")
                        else:
                            period = 'P' + str(yoy[0])
                            UpdateQuery = "Update DWDerElePeriodMultiple set `%s` = %s where DWCoID = %s and DWDerEleID = %s and ReportedDateID = %s" %(period, yoy[5],yoy[2],dereleid,reporteddate)
                            cursor.execute(UpdateQuery)
                            connection.commit()
                            print("Yoy updated")


                    except Exception as e:
                        print(e)

                # for QoQ
                dereleid = 45
                starstockQoQ = "Select P2.PeriodID, P2.Value as CurrentValue, P2.DWCoID,  P1.PeriodID as PrevPeriod,P1.Value as PrevValue , ((P2.Value/P1.Value) -1) * 100 As ' Growth in %' From DWStarSchemaMultiple P1 INNER JOIN DWStarSchemaMultiple P2 ON P1.DWCoID = P2.DWCoID AND P1.DWID = P2.DWID AND P1.PeriodID = P2.PeriodID - 1 where P1.DWID = 319 "
                cursor.execute(starstockQoQ)
                growthqoq = (cursor.fetchall())
                for yoy in growthqoq:
                    print(dereleid, yoy[0], reporteddate, yoy[2], yoy[5])
                    try:
                        selectQuery = "select DWCoID from DWDerElePeriodMultiple where  DWCoID = %s and DWDerEleID = %s and ReportedDateID = %s" % (
                        yoy[2], dereleid, reporteddate)
                        cursor.execute(selectQuery)
                        re = cursor.fetchall()
                        print((re))
                        if re == []:
                            insertQueryYoy = "INSERT INTO DWDerElePeriodMultiple (DWDerEleID,ReportedDateID,DWCoID) VALUES (%s,%s,%s)" % (
                                dereleid, reporteddate, yoy[2])
                            cursor.execute(insertQueryYoy)
                            connection.commit()
                            print("Yoy inserted")
                        else:
                            period = 'P' + str(yoy[0])
                            UpdateQuery = "Update DWDerElePeriodMultiple set `%s` = %s where DWCoID = %s and DWDerEleID = %s and ReportedDateID = %s" % (
                            period, yoy[5], yoy[2], dereleid, reporteddate)
                            cursor.execute(UpdateQuery)
                            connection.commit()
                            print("Yoy updated")

                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)


    except Exception as e:
        print(e)




YoYQoQStarSchema()
# YoYQoQDWIDSchema()
# YoYQoQPeriodSchema()
# DWCoID = []
# PrevValueDump(DWCoid)
# DWCoid = [3545]
# DailyReturnsStocks(DWCoid)

import mysql.connector
from openpyxl import load_workbook

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
        lenval = 0
        valuelen = 0

        # ticker = '%' + 'CDEV'
        GxbrlEleID = ['GXbrleleID', 'GXBRL ID']
        SegmentID = ['DivID', 'SegmentID', 'IsSegment', "io", "90","70",'000']
        ProductID = ['IsActive', 'ProductID']
        GeoID = ['Geography', 'IsHidden']
        GicID = ['CyCalcType', 'GICSID']
        OtherElementID = ['Other ElementID', 'RefElementID']
        SubElementID = ['TransformID', 'SubelementID','9090']
        NewKey = ['1', '2', '3', '4', '5', '6']
        parameters = {'GXbrlEleID': GxbrlEleID, 'SegmentID': SegmentID, 'ProductID': ProductID,
                      'GeoID': GeoID, 'GicID': GicID, 'OtherElementID': OtherElementID, 'SubElementID': SubElementID,
                      'NewKey': NewKey,"nonmatchingkey":['00']}
        # print(parameters)
except Exception as e:
    print("Error while connecting to MySQL", e)


def fetch():

            tablename = 'ColumnSearchMapping'
            alternatenames = []

            #extract column names
            sql1 = "SELECT  COLUMN_NAME FROM  INFORMATION_SCHEMA.COLUMNS   WHERE TABLE_NAME = N'%s'" % tablename;
            cursor.execute(sql1)
            records = cursor.fetchall()
            for val in records:
                alternatenames.append(val[0])
            # print(parameters)

            #table empty or not
            try:
                tableempty = "select * from `%s`"%tablename
                cursor.execute(tableempty)
                rr = cursor.fetchall()

                if rr:
                    for key, value in parameters.items():
                        for val in rr:
                            if val[0]:
                                # print(val[0])
                                flag = 0
                                if key == val[0]:
                                    print("matching values",val[0])
                                    flag = 0
                                    count = 0
                                    for val in value :
                                        count = (count + 1)
                                        col = ('AlternateName' + str(count))
                                        print(col,val,key)
                                        #update column if exists
                                        try:
                                            updatequery = "update ColumnSearchMapping set `%s` = %s where `ColumnNames` = %s"
                                            cursor.execute(updatequery,(col,val,key,))
                                            print("query  successfully")
                                            connection.commit()
                                        except Exception as e:
                                            # add column if not exists
                                            addcolumn = "alter table ColumnSearchMapping add %s varchar(256)"
                                            try:
                                                cursor.execute(addcolumn, (col,))
                                                print("column added  successfully")
                                                connection.commit()
                                                updatequery = "update ColumnSearchMapping set` %s` = %s where `ColumnNames` = %s"
                                                cursor.execute(updatequery, (col,val, key,))
                                                print("query  successfully")
                                                connection.commit()
                                            except Exception as e:
                                                print(e)
                                    break
                                else:
                                    flag = 1
                    if flag == 1:
                        print(flag)
                        insertQuery = "insert into ColumnSearchMapping(ColumnNames) values(" \
                                                  "'%s')" % key
                        try:
                            cursor.execute(insertQuery)
                            print("query excuted successfully")
                            connection.commit()

                        except Exception as e:
                            print(e)
                            # #         count = 0
                            # #         for val in value :
                            # #             count = (count + 1)
                            # #             col = str('AlternateName' + str(count))
                            # #             col = col.replace("'",'')
                            # #             print(col,val,key)
                            # #             #update column if exists
                            # #             try:
                            # #                 updatequery = "update ColumnSearchMapping set `%s` = %s where `ColumnNames` = %s"
                            # #                 cursor.execute(updatequery,(col,val,key,))
                            # #                 print("query  successfully")
                            # #                 connection.commit()
                            # #             except Exception as e:
                            # #                 #add column if not exists
                            # #                 # addcolumn = "alter table ColumnSearchMapping add `%s` varchar(256)"
                            # #                 # try:
                            # #                 #     cursor.execute(addcolumn, (col,))
                            # #                 #     print("column added  successfully")
                            # #                 #     connection.commit()
                            # #                 #     updatequery = "update ColumnSearchMapping set `%s` = %s where `ColumnName` = %s"
                            # #                 #     cursor.execute(updatequery, (col,val, key,))
                            # #                 #     print("query  successfully")
                            # #                 #     connection.commit()
                            # #                 # except Exception as e:
                            # #                     print(e)
                            #     else:
                            #         #insert query
                            #         insertQuery = "insert into ColumnSearchMapping(ColumnNames) values(" \
                            #                       "'%s')" % key
                            #         try:
                            #             cursor.execute(insertQuery)
                            #             print("query excuted successfully")
                            #             connection.commit()
                            #
                            #         except Exception as e:
                            #             print(e)

        #when table is empty insert column
                else:
                    #insert key
                    for key, value in parameters.items():
                        insertQuery = "insert into ColumnSearchMapping(ColumnNames) values(" \
                                      "'%s')" % key
                        try:
                            cursor.execute(insertQuery)
                            print("query excuted successfully when table is empty")
                            connection.commit()

                        except Exception as e:
                            print(e)
            except Exception as e:
                print("Error", e)





fetch()

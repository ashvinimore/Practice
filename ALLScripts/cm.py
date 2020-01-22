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
        SegmentID = ['DivID', 'SegmentID', 'IsSegment']
        ProductID = ['IsActive', 'ProductID']
        GeoID = ['Geography', 'IsHidden']
        GicID = ['CyCalcType', 'GICSID']
        OtherElementID = ['Other ElementID', 'RefElementID']
        SubElementID = ['TransformID', 'SubelementID','9090']
        NewKey = ['1', '2', '3', '4', '5', '6']
        parameters = {'GXbrlEleID': GxbrlEleID, 'SegmentID': SegmentID, 'ProductID': ProductID,
                      'GeoID': GeoID, 'GicID': GicID, 'OtherElementID': OtherElementID, 'SubElementID': SubElementID,
                      'NewKey': NewKey}
        # print(parameters)
except Exception as e:
    print("Error while connecting to MySQL", e)


def fetch():

            tablename = 'ColumnSearchMapping'
            alternatenames = []
            parameters = {'GXbrlEleID': GxbrlEleID, 'SegmentID': SegmentID, 'ProductID': ProductID,
                          'GeoID': GeoID, 'GicID': GicID, 'OtherElementID': OtherElementID,
                          'SubElementID': SubElementID,
                          'NewKey': NewKey}
            #extract column names
            sql1 = "SELECT  COLUMN_NAME FROM  INFORMATION_SCHEMA.COLUMNS   WHERE TABLE_NAME = N'%s'" % tablename;
            cursor.execute(sql1)
            records = cursor.fetchall()
            for val in records:
                alternatenames.append(val[0])
            print(alternatenames)
            for key,pairs in parameters.items():
                for pair in pairs:
                    # print(pair)
                    try:
                        sqlquery = "select * from ColumnSearchMapping where ColumnName = %s  and %s in (Alternate1,Alternate2,Alternate3,Alternate4) ;";
                        cursor.execute(sqlquery,(key,pair,))
                        res = cursor.fetchall()
                        if res:
                            pass
            #                 # print(res)
                        else:
                            sqlquerynotfound = "select * from ColumnSearchMapping where ColumnName = %s  and ColumnName in (Alternate1,Alternate2,Alternate3,Alternate4) IS NULL;";
                            cursor.execute(sqlquerynotfound,(key,))
                            result = cursor.fetchall()
            #                 #
                            if result:
                                length = result[0]
                                listresult = list(length)
                                print(listresult)
                                lengths = (len(list(length)))
            #                     # print(lengths)
                                for i in range(1,lengths):
                                    if (listresult[i] == None):
                                        name = ('Alternate' + str(i))
                                        updatequery = "update ColumnSearchMapping set `{}` = %s where `ColumnName` =%s".format(name)
                                        cursor.execute(updatequery,(pair,key,))
                                        connection.commit()
                                        break
            #                 else:
            #                     countcolumns = "select * from ColumnSearchMapping where ColumnName = %s"
            #                     cursor.execute(countcolumns, (key,))
            #                     resultcount = cursor.fetchall()
            #                     resultcount  = list(resultcount)
                                # print(resultcount)





                    except Exception as e:
                        print(e)

                # for val in res:
                #     for i in range(1,len(val)):
                #         if val[i] == None:
                #             column = ('Alternate'+str(i))
                #             updatequery = "Update ColumnSearchMapping set `%s` = %s "
                #             cursor.execute(updatequery,(column,))



            # else:
            # select * from ColumnSearchMapping where ColumnName in(Alternate1,Alternate2,Alternate3) IS NULL;




def columnmapping():
    try:
        tableempty = "select ColumnNames from ColumnSearchMapping"
        cursor.execute(tableempty)
        resultempty = cursor.fetchall()
        length = 0
        # print((resultempty))
        if len(resultempty) <= 0 :
            for key,value in parameters.items():
                if key:
                    insertquery = "insert into ColumnSearchMapping(ColumnNames)  values(" \
                                                  "'%s')" % ((key,))
                    cursor.execute(insertquery)
                    connection.commit()
                    l = length
                    length = len(value)
                    if length > l:
                        l = length
            print(l)
            if l:
                l = l + 1
                for i in range(1,l):
                    name = 'Alternate' + str(i)
                    try:
                        addcolumn = "Alter table ColumnSearchMapping add  %s varchar(250)"%name
                        cursor.execute(addcolumn)
                        connection.commit()
                    except Exception as e:
                        print(e)
                    pass
            for key, value in parameters.items():
                keysearch = "select ColumnNames from ColumnSearchMapping where ColumnNames = '%s' "%key
                cursor.execute(keysearch)
                r = cursor.fetchall()
                print(r)




        else:
            for key in parameters.keys():
                for col in resultempty:
                    flag = 0
                    if col[0] == key:
                        print(col[0])
                        break
                    else:
                        flag = 1
                if flag == 1:
                    print(key)

    except Exception as e:
        print(e)

    # try:
    #     ColumnSearchMapping  = []
    #     tablename = 'ColumnSearchMapping'
    #     sql1 = "SELECT  COLUMN_NAME FROM  INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'%s'" % tablename;
    #     cursor.execute(sql1)
    #     records = cursor.fetchall()
    #     for val in records:
    #         ColumnSearchMapping.append(val[0])
    #     print(len(ColumnSearchMapping))
    #
    #     try:
    #         key = "select ColumnNames from ColumnSearchMapping"
    # except Exception as e:
    #     print(e)





columnmapping()

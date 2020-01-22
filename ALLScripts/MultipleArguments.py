import mysql.connector
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
def foo(TableName,**ColumnName):
    # Arguments = (list(therest))
    # print(Arguments)
    # for val in Arguments:
    #     print(val)
    if(TableName == 'Company'):
        print("And all the rest... %s" %(dict(ColumnName)))
# foo(TableName = "Company",a = "12",b = "23")


def parsing(tablename):
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DataWarehouse',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = "select * from SyncDetails where PrimaryKeyCol IS NOT NULL"
            cursor.execute(query)
            records = cursor.fetchall()
            records = (list(records))
            modifieddate = records[0][2]
            tablename = records[0][1]
            tabletoinsert = 'AttributeDWH'
            if (modifieddate == None):
                query1 = "select * from %s"%tablename
                cursor.execute(query1)
                records = cursor.fetchall()
                records = (list(records))
                sql1 = "SELECT  COLUMN_NAME FROM  INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'%s'"%tablename;
                cursor.execute(sql1)
                records = cursor.fetchall()
                records = (list(records))
                print(records)
            else:
                print("none")
    except Exception as e:
        print(e)




parsing("SyncDetails")
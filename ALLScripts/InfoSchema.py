import mysql.connector
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
def foo(TableName,**ColumnName):
    # Arguments = (list(therest))
    # print(Arguments)
    # for val in Arguments:
    #     print(val)
    # if(TableName == 'Company'):
    print("And all the rest... %s" %(dict(ColumnName)))



def parsing():
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='Zeus',
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
            for data in records:
                if (data[2] == None):
                    print("null")
                else:
                    print("not null",data[2])

                    sql1 = "SELECT  COLUMN_NAME FROM  INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'%s'" % data[1];
                    cursor.execute(sql1)
                    recordcol = cursor.fetchall()
                    recordscol = (list(recordcol))
                    # print(records)
                    l = []
                    for val in recordscol:
                        l.append(val[0])
                    l = str(l)
                    l = l.replace('[', '').replace(']', '')
                    foo(TableName=data[1], l=l)

    except Exception as e:
        print(e)




parsing()
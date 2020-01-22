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
                                             database='DWHDB',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            print((cursor.fetchall()[0][0]))
            #for master tables query
            #LOAD DATA LOCAL INFILE 'csvpath' INTO TABLE TABLENAME;
            #https://stackoverflow.com/questions/6750146/mysql-bulk-insert-on-duplicate-key-update-via-load-data-infile
            coid = 11795
            try:
                cursor.callproc('DerivedCompany')
                SelectQuery = "Select count(*) from DerivedCompany"
                findQuery = "select * from DerivedCompany"
                cursor.execute(findQuery)
                result = (cursor.fetchall())
                for re in result:
                    # print(re)
                    CoID = re[0]
                    CoName = re[1]
                    Description = re[2]
                    CountryID = re[3]
                    IntGICSID = re[4]
                    ExtGICSID = re[5]
                    CoAttID = re[6]
                    CurID = re[7]
                    UnitID = re[8]
                    ExchangeID = re[10]
                    coid = coid + 1
                    try:
                        findQuery = "select DWCoID,CoID from DerivedCompany where CoID = %s and Ticker IS NULL "
                        cursor.execute(findQuery,(CoID,))
                        result = cursor.fetchall()
                        if result == []:
                            print("queryyy")
                            insertQuery = "INSERT INTO DerivedCompany(CoID, CoName, CountryID, IntGICSID, ExtGICSID,CoAttID,CurID,UnitID,ExchangeID,DWCoID) values (%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s)"%(CoID,CoName,CountryID,IntGICSID,ExtGICSID,CoAttID,CurID,UnitID,ExchangeID,coid)
                            cursor.execute(insertQuery)
                            connection.commit()
                        else:
                            print("result")
                    except Exception as e:
                        print(e)
                        pass
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)



parsing()
import os
import re
import csv
import mysql.connector

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
        print("Your connected to - ", record)
        cursor.execute("select * from period")
        file_name = '/home/pavan/Music/Data Warehouse/GE/RatioCountryGics_LiveExported_19082019.csv'
        try:
            result = []
            with open(file_name) as file:
                reader = csv.reader(file)
                reader = list(reader)
                reader.pop(0)
                for row in reader:
                    print(row)
                    SegmentID = row[0]
                    GicsID = row[1]
                    IsActive = row[2]

                    insertQuery = "insert into RatioCountry(TemplateID,CountryID,GicsID)  values( \
                                  %s,%s,%s)"
                    val = (SegmentID,GicsID,IsActive)
                    try:
                        cursor.execute(insertQuery,val)
                    except Exception as e:
                        print(e)

            # print(result)
            connection.commit()
            # return result
        except Exception as e:
            raise e

except Exception as e:
    print("Error while connecting to MySQL",e)

finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# def read_csv_file(file_name):
#     try:
#         result = []
#         with open(file_name) as file:
#             reader = csv.reader(file)
#             # print(list(reader))
#             for row in reader:
#                 print(row[0])

        # print(result)
    #
    #     # return result
    # except Exception as e:
    #     raise e

# read_csv_file('/home/pavan/Music/Data Warehouse/GE/GlobalElement_LiveExported_19082019.csv')
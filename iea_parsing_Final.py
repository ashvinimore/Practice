import os
import re
import csv
import pymysql
import PyPDF2, re
import datetime

from tabula import read_pdf
from Common.log import logging
from Common.config import MYSQL_ALETHEIA, PDF_PATH, CSV_PATH


class IEABase:

    def __init__(self):
        try:
            self.sqlconn = pymysql.connect(host=MYSQL_ALETHEIA["HOST"], port=MYSQL_ALETHEIA["PORT"], user=MYSQL_ALETHEIA["USER"],
                                           passwd=MYSQL_ALETHEIA["PASSWORD"], db=MYSQL_ALETHEIA["DB_NAME"], autocommit=True)
            self.cursor = self.sqlconn.cursor()
        except Exception as e:
            logging.error(e)


    def __del__(self):
        try:
            self.cursor.close()
        except Exception as e:
            raise e

        try:
            self.sqlconn.close()
        except Exception as e:
            raise e

    def get_pdf_list(self):
        """
        :return: PDF files from folder
        """
        try:
            pdf_files = [f for f in os.listdir(PDF_PATH+'.') if os.path.isfile(PDF_PATH+f) and f.endswith('.pdf')]
            return pdf_files
        except Exception as e:
            logging.error(e)
            raise e

    def find_table_contents(self,pdf_list,table_name):
        page_numbers = {}
        pdf_value = {}
        flag = 0

        for pdf in pdf_list:
            pdf = pdf.replace(' ', '')
            Xfile = open((PDF_PATH + pdf), 'rb')
            pdfDoc = PyPDF2.PdfFileReader(Xfile, "rb")
            if flag == 1:
                try:
                    for i in range(0, 10):
                        content = ""
                        content += (pdfDoc.getPage(i).extractText() + "\n")
                        content1 = content.encode('ascii', 'ignore').lower()
                        content1 = content1.decode('utf-8')
                        ResSearch = re.search(table_name, content1)
                        if ResSearch is not None:
                            PageFound = i
                            content += (pdfDoc.getPage(PageFound).extractText() + "\n")
                            content1 = content.encode('ascii', 'ignore').lower()
                            content1 = content1.decode('utf-8')
                            ResSearch = re.search('tables', content1)
                            if ResSearch is not None:
                                pageObj1 = pdfDoc.getPage(PageFound)
                                pagecontent = pageObj1.extractText()
                                pagecontent.replace('.', '')
                                f = open("error page.txt", "w")
                                f.write(pagecontent)
                                try:
                                    f = open("error page.txt", "r")
                                    read = f.read()
                                    l = (read.replace('.', ' ').split())
                                    for i in l:
                                        if 'TABLES' in i:
                                            index = int((l.index(i)) + 1)
                                            last = len(l) + 1
                                            for page in range(index, last):
                                                page_number = l[page]
                                                if page_number.isdigit():
                                                    page_numbers[pdf] = page_number
                                                    break

                                except Exception as e:
                                    print(e)
                except Exception as e:
                    print(e)
            else:
                page_numbers[pdf] = '1'
        return page_numbers

    def find_page_number_1(self,pdf_list, table_name):
        page_numbers = {}
        for pdf, value in pdf_list.items():
            value = int(value)
            try:
                pdf = pdf.replace(' ', '')

                Xfile = open((PDF_PATH + pdf), 'rb')
                pdfDoc = PyPDF2.PdfFileReader(Xfile, "rb")

                for i in range(value, pdfDoc.getNumPages()):
                    content = ""
                    content += (pdfDoc.getPage(i).extractText() + "\n")
                    content1 = content.encode('ascii', 'ignore').lower()
                    content1 = content1.decode('utf-8')

                    if table_name == 'table2b':
                        name = 'OIL DEMAND IN SELECTED OECD COUNTRIES'.lower()
                        name1 = 'OIL DEMAND AND % GROWTH IN'.lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i + 1
                            page_numbers[pdf] = PageFound
                            break
                        else:
                            ResSearch = re.search(name1, content1)
                            if ResSearch is not None:
                                PageFound = i + 1
                                page_numbers[pdf] = PageFound
                                break
                    if (table_name == 'table1'):
                        name = "WORLD OIL SUPPLY AND DEMAND".lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i
                            page_numbers[pdf] = PageFound
                            break
                    if (table_name == 'table3'):
                        name = "WORLD OIL PRODUCTION".lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i + 1
                            page_numbers[pdf] = PageFound
                            break
                    if (table_name == 'table4'):
                        name = "OECD INDUSTRY STOCKS".lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i + 1
                            page_numbers[pdf] = PageFound
                            break
                    if (table_name == 'table2'):
                        name = "Summary of Global Oil Demand".lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i + 1
                            page_numbers[pdf] = PageFound
                            break
                    if (table_name == 'table2a'):
                        name = "OECD REGIONAL OIL DEMAND".lower()
                        ResSearch = re.search(name, content1)
                        if ResSearch is not None:
                            PageFound = i + 1
                            page_numbers[pdf] = PageFound
                            # print(page_numbers)
                            break
            except Exception as e:
                f = open("pdf.txt", "a")
                f.write(pdf + '\n')
                f.write(str(e))
                pass

        return page_numbers

    def conert_pdf_to_csv(self, pdf_name, csv_name, page_number):
        """
        Converts pdf page to csv file
        :param pdf_name: Existing PDF name
        :param csv_name: Expected CSV name
        :param page_number: PDF page number to be converted into CSV file(mostly table page)
        :return:
        """
        try:
            with open(csv_name, "w") as f:
                data = read_pdf(pdf_name, output_format="csv", pages=page_number)
                data.to_csv(f)
            return 1
        except Exception as e:
            logging.error(e)
            raise e

    def get_month_id(self,month_name):
        """
        get month number in integer
        :param monthName:
        :return:
        """
        try:
            month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            count = 1
            for month in month_list:
                if month == month_name:
                    return count
                count += 1
        except Exception as e:
            logging.error(e)
            raise e

    def clean_string(self, string):
        """
        remove numeric and symbols from string
        :param string:
        :return:
        """
        try:
            new_string = re.sub('[0-9.,:*]+','',string)
            return new_string.strip()
        except Exception as e:
            logging.error(e)
            raise e

    def get_period_year(self, number):
        try:
            if number > 80:
                return 1900+number
            else:
                return 2000+number
        except Exception as e:
            logging.error(e)
            raise e

    def convert_to_period_data(self, row, allow_all=False):
        """
        convert csv rows into period_id, period_idx, mode format
        :param row:
        :param allow_all:
        :return:
        """
        try:
            year_row = {}
            inner_count = 0
            for r in row:
                if inner_count == 12:
                    if allow_all == True:
                        if "Q" in r:
                            v = str(r).split("Q")
                            year_row[inner_count] = {
                                "PeriodID": self.get_period_year(number=int(v[1].split(".")[0])),
                                "PeriodIdx": int(v[0]),
                                "Mode": "Q"
                            }
                        else:
                            v1 = str(r).split(" ")
                            if len(v1) > 1:
                                year_row[inner_count] = {
                                    "PeriodID": self.get_period_year(number=int(v1[1].split(".")[0])),
                                    "PeriodIdx": self.get_month_id(v1[0]),
                                    "Mode": "M"
                                }
                            else:
                                year_row[inner_count] = {
                                    "PeriodID": v1[0].split(".")[0],
                                    "PeriodIdx": 1,
                                    "Mode": "Y"
                                }
                else:
                    if "Q" in r:
                        v = str(r).split("Q")
                        year_row[inner_count] = {
                            "PeriodID": self.get_period_year(number=int(v[1].split(".")[0])),
                            "PeriodIdx": int(v[0]),
                            "Mode": "Q"
                        }
                    else:
                        v1 = str(r).split(" ")
                        if len(v1) > 1:
                            year_row[inner_count] = {
                                "PeriodID": self.get_period_year(number=int(v1[1].split(".")[0])),
                                "PeriodIdx": self.get_month_id(v1[0]),
                                "Mode": "M"
                            }
                        else:
                            year_row[inner_count] = {
                                "PeriodID": v1[0].split(".")[0],
                                "PeriodIdx": 1,
                                "Mode": "Y"
                            }

                inner_count += 1
            return year_row
        except Exception as e:
            logging.error(e)
            raise e

    def format_changer_for_table1(self, rows):
        try:
            final_result = []
            for row_id in range(len(rows)):
                inner_row = []
                if row_id == 0:
                    col_count = 0
                    for column in rows[row_id]:
                        if col_count >= 1:
                            if "Unna" not in column:
                                col_list = column.split(" ")
                                for col in col_list:
                                    if col:
                                        inner_row.append(col)
                        else:
                            inner_row.append(column)
                        col_count += 1
                    final_result.append(inner_row)

                else:
                    for column in rows[row_id][2:]:
                        col_split = column.split(" ")
                        for cols in col_split:
                            if cols:
                                inner_row.append(cols)
                    inner_row = rows[row_id][:2] + inner_row
                    final_result.append(inner_row)
            return final_result
        except Exception as e:
            logging.error(e)
            f = open("error files.txt", "a")
            f.write(str(e))
            raise e

    def convert_to_period_data_table_4(self, row):
        try:
            result = []
            for col in row:

                if "Q" in col:
                    seprate = col.split("Q")
                    result.append({
                        "PeriodID": seprate[-1],
                        "PeriodIdx": seprate[0],
                        "Mode": 'Q'
                    })
                else:
                    result.append({
                        "PeriodID": col[3:7],
                        "PeriodIdx": self.get_month_id(col[:3]),
                        "Mode": 'M'
                    })
            return result

        except Exception as e:
            logging.error(e)
            raise e

    def format_changer_table2a(self, list_of_list):
        """
        pdf format chaged before 2010/06
        :return:
        """
        try:
            raw_data = []
            r1 = []
            r2 = []
            rows = []
            quartrs = {
                'First Quarter': '1Q',
                'Second Quarter': '2Q',
                'Third Quarter': '3Q',
                'Fourth Quarter': '4Q'
            }
            for li in list_of_list:
                raw_data.append(li)

            list_of_list = raw_data
            for i in range(len(list_of_list)):
                if i == 0:
                    for lol in list_of_list[i]:
                        if lol and "Unnamed" not in lol:
                            r1.append(lol)
                    rows.append(r1)

                if i == 1:
                    count1 = 0
                    for data in list_of_list[i]:
                        x = data.split(" ")
                        for x1 in x:
                            if count1 > 1:
                                if x1:
                                    r2.append(x1.replace(".0", ""))
                            else:
                                r2.append(x1.replace(".0", ""))
                        count1 += 1
                    rows.append(r2)

                if i > 1:
                    var = []
                    counts = 0
                    for data in list_of_list[i]:
                        if counts == 1:
                            var.append(data)
                        else:
                            x = data.split(" ")
                            for x1 in x:
                                if x1:
                                    var.append(x1)
                        counts += 1
                    rows.append(var)

            second_index = 2
            for month_id in range(len(r1)):
                counter = 0
                for year_id in range(5):
                    month = r1[month_id]
                    year = r2[second_index]
                    if year == '%':
                        year = '2050'
                    get_quarter = quartrs.get(month)
                    if get_quarter:
                        all_year = get_quarter + year[2:]
                    else:
                        all_year = month[:3] + " " + year[2:]

                    r2[second_index] = all_year
                    second_index += 1
                    counter += 1
                    if counter == 3:
                        break
            rows[1] = r2
            return rows
        except Exception as e:
            logging.error(e)
            print(e)


    def string_seperator(self, string, decimal_places=1):
        try:
            numbers = []
            space_count = str(string).count(" ")
            if space_count == 0:
                digit_count = str(string).count(".")
                if digit_count > 0:
                    for i in range(digit_count):
                        data = str(string).index(".")
                        numbers.append(string[:data + decimal_places + 1])
                        string = string[data + decimal_places + 1:]
                else:
                    numbers.append(string)
            else:
                space_sep = str(string).split(" ")
                for sp in space_sep:
                    if sp:
                        numbers.append(sp)
            return numbers
        except Exception as e:
            logging.error(e)
            raise e

    def read_csv_file(self, file_name):
        try:
            result = []
            with open(file_name) as file:
                reader = csv.reader(file)
                for row in reader:
                    result.append(row)

            return result
        except Exception as e:
            logging.error(e)
            raise e

    def format_changer_for_table2(self, rows):
        try:
            final_result = []
            for row_id in range(len(rows)):
                inner_row = []
                if row_id == 0:
                    col_count = 0
                    for column in rows[row_id]:
                        if col_count > 1:
                            if "Unna" not in column:
                                col_list = column.split(" ")
                                for col in col_list:
                                    if col:
                                        inner_row.append(col)
                        else:
                            inner_row.append(column)
                        col_count += 1
                    final_result .append(inner_row)

                else:
                    for column in rows[row_id][2:]:
                        col_split = column.split(" ")
                        for cols in col_split:
                            if cols:
                                inner_row.append(cols)
                    inner_row = rows[row_id][:2]+inner_row
                    final_result.append(inner_row)
            return final_result
        except Exception as e:
            logging.error(e)
            raise e

    def table_3_prior_formatting(self, row):
        try:
            new_row = []
            count = 0
            for col in row:
                col = col.replace("*","")
                if "f" in col and "Feb" not in col:
                    col = col.replace("f","").strip()

                if count > 1:
                    if "Q" in col:
                        if len(col) == 6:
                            col = col[:2]+col[-2:]
                        elif len(col) == 4:
                            if col[0] == "Q":
                                col = col[1:2]+"Q"+col[-2]

                    if str(col[2]).isalpha() and str(col[3]).isdigit():
                        col = col[:3]+' '+col[-2:]
                count += 1
                new_row.append(col)
            return new_row
        except Exception as e:
            logging.error(e)
            raise e


class IEADataProcessing(IEABase):

    def __init__(self):
        try:
            IEABase.__init__(self)
        except Exception as e:
            logging.error(e)

    def insert_table2_data(self, file_name, sub_table):
        """
        insert table 2a and table 2b data
        :param file_name:
        :param sub_table: table2a_ or table2b_
        :return:
        """
        try:
            year_row = {}
            start_col = 2
            country = ""
            is_total = "null"
            table_type = "2a"
            if sub_table != "table2a_":
                table_type = "2b"

            rows = self.read_csv_file(file_name=file_name)
            check = 1

            version_id = str(file_name.split("/")[-1]).replace(".csv", "").replace(sub_table, "").replace("-", "")
            if int(version_id) < 20100713:
                rows = self.format_changer_table2a(rows)

            provided_date = str(file_name.split("/")[-1]).replace(".csv", "").replace(sub_table, "")
            reported_date = provided_date + " 00:00:00"
            print(reported_date)
            country_id = 'null'
            region_id = 'null'

            query = "delete from IEA_HistoricMacroElementsData where ReportedDate = %s and TableType = %s"
            try:
                result = self.cursor.execute(query, (reported_date, table_type,))
            except Exception as e:
                logging.error(e)

            for n in range(len(rows)):
                if n == check:
                    if rows[n][2] and rows[n][3]:
                        year_row = self.convert_to_period_data(row=rows[n])
                    else:
                        check += 1
                if n > check:
                    if (int(version_id) < 20100713 and len(rows[n]) > 1) or (rows[n][2] and rows[n][3]):
                        element = self.clean_string(rows[n][1])
                        country = self.clean_string(element)

                        if sub_table == "table2a_":
                            if "OECD" in country:
                                region_id = "null"
                                country_id = "null"
                            else:
                                region_id_query = "select RegionID from Regions where RegionName='%s' and ProviderID = '1' " % (
                                    country)
                                self.cursor.execute(region_id_query)
                                country_res = self.cursor.fetchall()
                                if country_res and len(country_res) > 0 and country_res[0][0] != None:
                                    region_id = country_res[0][0]
                                    country_id = 'null'
                                else:
                                    if (element == 'Jet/Kerosene'):
                                        element = 'Jet and kerosene'
                                    element = element.replace(' ', '')
                                    get_ph_heirarchy = "select PH1ID, PH2ID, PHID from ProductHR3 where upper(replace(Description,' ','')) = upper('%s')" % element
                                    self.cursor.execute(get_ph_heirarchy)
                                    ph_result = self.cursor.fetchall()
                                    if ph_result and len(ph_result) > 0:
                                        ph1 = ph_result[0][0]
                                        ph2 = ph_result[0][1]
                                        ph3 = ph_result[0][2]
                                        is_total = "null"
                                    else:
                                        ph1 = "null"
                                        is_total = "null"
                                        if element == "Total":
                                            ph1 = 1
                                            is_total = 1
                                        ph2 = "null"
                                        ph3 = "null"
                        else:
                            if (element == 'Jet/Kerosene'):
                                element = 'Jet and kerosene'
                            element = element.replace(' ', '')
                            get_ph_heirarchy = "select PH1ID, PH2ID, PHID from ProductHR3 where upper(replace(Description,' ','')) = upper('%s')" % element
                            self.cursor.execute(get_ph_heirarchy)
                            ph_result = self.cursor.fetchall()
                            if ph_result and len(ph_result) > 0:
                                ph1 = ph_result[0][0]
                                ph2 = ph_result[0][1]
                                ph3 = ph_result[0][2]
                                is_total = "null"
                            else:
                                ph1 = "null"
                                is_total = "null"
                                if element == "Total":
                                    ph1 = 1
                                    is_total = 1
                                else:
                                    pattern = country.replace(' ', '') + "%"
                                    country_id_query = "select CountryID from Country where upper(replace(CountryName,' ','')) LIKE  '%s'" % (
                                        pattern)
                                    self.cursor.execute(country_id_query)
                                    res = self.cursor.fetchall()
                                    if res and len(res) > 0:
                                        country_id = str(res[0][0])
                                    else:
                                        country_id = "null"
                                    region_id_query = "select RegionID from RegionCountryMapping where CountryID='%s'" % (
                                        country_id)
                                    self.cursor.execute(region_id_query)
                                    res = self.cursor.fetchall()
                                    if res and len(res) > 0:
                                        region_id = res[0][0]

                                    else:
                                        region_id = "null"

                                ph2 = "null"
                                ph3 = "null"

                        elemCount = start_col
                        for fr in rows[n][start_col:]:
                            value = fr
                            if value and elemCount != 12:
                                res = year_row.get(elemCount)
                                periodID = res.get("PeriodID")
                                periodIdx = res.get("PeriodIdx")
                                mode = res.get("Mode")
                                insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                              "%s, %s, '%s', 'D', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', %s, %s, 1, null, null, 1.0, current_timestamp(), %s, '%s', 1, '%s')" % (
                                                  periodID, periodIdx, mode, ph1, ph2, ph3, value, country_id,
                                                  region_id, is_total, provided_date, table_type
                                              )

                                try:
                                    if int(periodID) != 2050:
                                        self.cursor.execute(insertQuery)
                                except Exception as e:
                                    logging.error(e)
                            elemCount += 1
                    else:
                        element = (rows[n][1])
                        # print(element)
                        country = self.clean_string(element)

                        if sub_table == "table2a_":
                            region_id_query = "select RegionID from Regions where RegionName='%s' and ProviderID = '1' " % (
                                country)
                            self.cursor.execute(region_id_query)
                            country_res = self.cursor.fetchall()
                            if country_res and len(country_res) > 0 and country_res[0][0] != None:
                                region_id = country_res[0][0]
                                country_id = 'null'
                            else:
                                country_id = 'null'
                                region_id = 'null'

                        else:
                            pattern = country.replace(' ', '') + "%"
                            country_id_query = "select CountryID from Country where upper(replace(CountryName,' ','')) LIKE  '%s'" % (
                                pattern)
                            self.cursor.execute(country_id_query)
                            res = self.cursor.fetchall()
                            if res and len(res) > 0:
                                country_id = str(res[0][0])
                            else:
                                country_id = "null"
                            region_id_query = "select RegionID from RegionCountryMapping where CountryID='%s'" % (
                                country_id)
                            self.cursor.execute(region_id_query)
                            res = self.cursor.fetchall()
                            if res and len(res) > 0:
                                region_id = res[0][0]
                            else:
                                region_id = "null"

        except Exception as e:
            logging.error(e)

            query = "update RefTables set parsing = 13 where ReportedDate = %s and TableType = %s"
            try:
                result = self.cursor.execute(query, (reported_date, table_type))
            except Exception as e:
                logging.error(e)
        os.remove(file_name)
        print("file removed", file_name)

    def insert_table4_data(self, file_name, sub_table=None):
        version_id = str(file_name.split("/")[-1]).replace(".csv", "").replace("table4_", "").replace("-", "")
        provided_date = str(file_name.split("/")[-1]).replace(".csv", "").replace(sub_table, "")
        reported_date = provided_date + " 00:00:00"
      #  print(reported_date)
        
        query = "delete from IEA_HistoricMacroElementsData_2_issue where ReportedDate = %s and TableType = '4'"
        try:
            result = self.cursor.execute(query, (reported_date,))
        except Exception as e:
            logging.error(e)
        query = "delete from RefTable where ReportedDate = %s and TableType = '4'"
        try:
            result = self.cursor.execute(query, (reported_date,))
            # print(result)
        except Exception as e:
            logging.error(e)
            # print(e, file_name)

     #   
        query = "insert into RefTable(ReportedDate,TableType,Flag) values(" \
                "'%s','4','1')" % (reported_date,)
        try:
            result = self.cursor.execute(query)
            # print(result)
        except Exception as e:
            logging.error(e)

        query = "select max(ReportedDate) from IEA_HistoricMacroElementsData_2_issue where TableType = 4"
        try:
            result = self.cursor.execute(query,)
            if result > 1:
                max_date = str(self.cursor.fetchone())
                max_date = (max_date.strip("(datetime.datetime(,)").replace('', '')[0:12])
                max_date = max_date.split(',')
                y = int(max_date[0])
                m = int(max_date[1])
                d = int(max_date[2])
                dates = str(datetime.date(y, m, d))
                dates = dates.replace('-', '')
      #          print((dates))
            else:
                dates = 000
        except Exception as e:
            logging.error(e)

        if int(dates) != int(version_id):
            try:
                period_data = []
                is_total = "null"
                govenrment_controlled = "S"
                region = ""
                region_id = "null"
                rows = self.read_csv_file(file_name=file_name)

                count = 0
                for index in range(len(rows)):
                    if index > 1:
                        temp_row = []
                        for col_index in range(len(rows[index])):
                            if col_index > 1:
                                d = self.string_seperator(string=rows[index][col_index])
                                temp_row.extend(d)

                            else:
                                temp_row.append(rows[index][col_index])
                        rows[index] = temp_row

                get_period_data = True

                for row_count in range(len(rows)):
                    count = count + 1
                    if row_count == 2 or get_period_data == True:
                        period_data = self.convert_to_period_data_table_4(rows[row_count])
                        get_period_data = False

                    if row_count > 2:
                        if is_total == 1:
                            region_id = "null"

                        if "Million" in rows[row_count]:
                            get_period_data = True
                            govenrment_controlled = "SG"

                        if rows[row_count][1]:
                            if rows[row_count][1] and "OECD" in rows[row_count][1]:
                                # print(rows[row_count][1])
                                region = self.clean_string(rows[row_count][1])
                                #  region =
                                region = region.strip("OECD").strip()
                                check_region_id = "select RegionID from Regions where upper(RegionName)=upper('%s')" % region
                                self.cursor.execute(check_region_id)
                                region_res = self.cursor.fetchall()
                                if region_res and len(region_res) > 0:
                                    region_id = region_res[0][0]
                                else:
                                    region_id = "null"

                            else:
                                element = self.clean_string(rows[row_count][1])
                                if "TOTAL" in element.upper() and "PRODUCTS" not in element.upper():
                                    is_total = 1

                                element = self.clean_string(rows[row_count][1])
                                get_ph_heirarchy = "select PH1ID, PH2ID, PHID from ProductHR3 where upper(Description) = upper('%s')" % element
                                self.cursor.execute(get_ph_heirarchy)
                                ph_result = self.cursor.fetchall()
                                if ph_result and len(ph_result) > 0:
                                    ph1 = ph_result[0][0]
                                    ph2 = ph_result[0][1]
                                    ph3 = ph_result[0][2]
                                else:
                                    if "TOTAL" in element.upper():
                                        is_total = 1
                                        if str(region_id).upper() == "Null".upper():
                                            region = self.clean_string(rows[row_count][1])
                                            is_total = 1
                                            check_region_id = "select RegionID from Regions where upper(RegionName)=upper('%s')" % region
                                            self.cursor.execute(check_region_id)
                                            region_res = self.cursor.fetchall()
                                            if region_res and len(region_res) > 0:
                                                region_id = region_res[0][0]
                                            else:
                                                region_id = "null"
                                    else:

                                        is_total = "null"
                                        region = self.clean_string(rows[row_count][1])
                                        check_region_id = "select RegionID from Regions where upper(RegionName)=upper('%s')" % region
                                        self.cursor.execute(check_region_id)
                                        region_res = self.cursor.fetchall()
                                        if region_res and len(region_res) > 0:
                                            region_id = region_res[0][0]
                                        else:
                                            region_id = "null"

                                    ph1 = 1
                                    ph2 = "null"
                                    ph3 = "null"

                                check_count = 0
                                for col_count in range(len(rows[row_count])):
                                    if rows[row_count][col_count] and col_count > 1:
                                        period_id = period_data[col_count].get("PeriodID")
                                        period_idx = period_data[col_count].get("PeriodIdx")
                                        mode = period_data[col_count].get("Mode")
                                        if mode != "Q":
                                            insert_query = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal,  ReportedDate, ProviderID, TableType) values(" \
                                                           "%s, %s, '%s', '%s', %s, %s, %s, null, %s, 'V', 'MBPM', 'USD', null, %s, 1, null, null, 1.0, current_timestamp(), %s, '%s', 1, '4')" % (
                                                               period_id, period_idx, mode, govenrment_controlled, ph1,
                                                               ph2, ph3, rows[row_count][col_count], region_id,
                                                               is_total, reported_date
                                                           )

                                            try:
                                                self.cursor.execute(insert_query)
                                                check_count += 1

                                                if check_count == 5:
                                                    break

                                            except Exception as e:
                                                logging.error(e)



            except Exception as e:
                logging.error(e)
              #  print(e)
                query = "update RefTables set flag = 2 where ReportedDate = %s and TableType = '4'"
                try:
                    result = self.cursor.execute(query, (reported_date,))
                except Exception as e:
                    logging.error(e)
                    print(e)

    def insert_table1_data(self, file_name, sub_table=None):
        flag = 0
        total_nonopec = 0
        provided_date = str(file_name.split("/")[-1]).replace("table1_", "").replace(".csv", "")
        reported_date = provided_date + " 00:00:00"
        query = "delete from IEA_HistoricMacroElementsData where ReportedDate = %s and TableType = '1'"
        try:
            result = self.cursor.execute(query, (reported_date,))
        except Exception as e:
            logging.error(e)

        try:
            period_data = {}
            start = False
            ph1 = 1
            ph2 = "null"
            ph3 = "null"
            gr = ''
            gr2 = ''
            provided_date = str(file_name.split("/")[-1]).replace("table1_", "").replace(".csv", "")

            data = self.read_csv_file(file_name=file_name)
            rows = self.format_changer_for_table1(rows=data)
            for row_id in range(len(rows)):
                row = rows[row_id]
                if row_id == 0:
                    period_data = self.convert_to_period_data(row=row, allow_all=True)
                # print("period data",period_data)
                else:
                    if start == True:

                        get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % gr
                        self.cursor.execute(get_group_query)
                        group_res = self.cursor.fetchall()
                        if group_res and len(group_res) > 0:
                            group_id = group_res[0][0]
                        else:
                            group_id = "null"
                        is_total = "null"
                        region_id_query = "select RegionID from Regions where RegionName='%s' and ProviderID=1" % self.clean_string(
                            row[1])
                        self.cursor.execute(region_id_query)
                        res = self.cursor.fetchall()
                        if res and len(res) > 0:
                            region_id = res[0][0]
                            country_id = "null"
                        else:
                            region_id = "null"
                            pattern = row[1].replace(' ', '') + "%"
                            country_id_query = "select CountryID from Country where upper(replace(CountryName,' ','')) LIKE  '%s'" % (
                                pattern)
                            self.cursor.execute(country_id_query)
                            res = self.cursor.fetchall()
                            if res and len(res) > 0:
                                country_id = str(res[0][0])
                                region_id_query = "select RegionID from RegionCountryMapping where CountryID='%s'" % (
                                    country_id)
                                self.cursor.execute(region_id_query)
                                res = self.cursor.fetchall()
                                if res and len(res) > 0:
                                    region_id = res[0][0]

                                else:
                                    region_id = "null"

                            else:
                                country_id = "null"

                        if "TOTAL" in row[1].upper():
                            is_total = 1
                        for val_id in range(2, len(row)):
                            value = row[val_id]
                            # print("value", value)
                            dict_id = (val_id - 1)
                            # print(dict_id)
                            peri_data = period_data.get(dict_id)
                            period_id = peri_data.get("PeriodID")
                            period_idx = peri_data.get("PeriodIdx")
                            mode = peri_data.get("Mode")

                            insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                          "%s, %s, '%s', 'D', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', %s, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                              period_id, period_idx, mode, ph1, ph2, ph3, value, country_id, region_id,
                                              group_id,
                                              is_total, provided_date
                                          )

                            try:
                                self.cursor.execute(insertQuery)
                            except Exception as e:
                                logging.error(e)

                        if self.clean_string(row[1]).upper() == "TOTAL NON-OECD":
                            total_demand = row_id
                            start = False

                    elif start == False:
                        if self.clean_string(row[1]).upper() == "OECD DEMAND".upper() or self.clean_string(
                                row[1]).upper() == "DEMAND".upper():
                            start = True
                            gr = 'OECD'

                    if "Total OECD".upper() == self.clean_string(row[1]).upper():
                        gr = "Non-OECD"

                    if "TOTAL DEMAND".upper() == self.clean_string(row[1]).upper():
                        oecd_supply = row_id
                        print("total demand")
                        for val_id in range(2, len(row)):
                            value = row[val_id]
                            print("value", value)
                            dict_id = (val_id - 1)
                            peri_data = period_data.get(dict_id)
                            period_id = peri_data.get("PeriodID")
                            period_idx = peri_data.get("PeriodIdx")
                            mode = peri_data.get("Mode")
                            is_total = 1
                            ph1 = 1
                            ph2 = "null"
                            ph3 = "null"
                            region_id = "null"
                            group_id = "null"
                            group_id_2 = "null"
                            insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                          "%s, %s, '%s', 'D', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                              period_id, period_idx, mode, ph1, ph2, ph3, value, region_id, group_id,
                                              is_total, provided_date
                                          )

                            try:
                                self.cursor.execute(insertQuery)
                            except Exception as e:
                                logging.error(e)
                        break

            #     # for supply
            supply_start = False
            for row_id in range(oecd_supply, len(rows)):
                row = rows[row_id]
                if supply_start == True:
                    if self.clean_string(row[1]).upper() == "PROCESSING GAINS":
                        supply_start = False
                        flag = 1
                    else:
                        get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % gr
                        self.cursor.execute(get_group_query)
                        group_res = self.cursor.fetchall()
                        if group_res and len(group_res) > 0:
                            group_id = group_res[0][0]
                        else:
                            group_id = "null"
                        get_group_query_2 = "select GroupID from Groups where upper(Description) = upper('%s')" % gr2
                        self.cursor.execute(get_group_query_2)
                        group_res = self.cursor.fetchall()
                        if group_res and len(group_res) > 0:
                            group_id_2 = group_res[0][0]
                        else:
                            group_id_2 = "null"

                        is_total = "null"

                        region_id_query = "select RegionID from Regions where RegionName='%s' and ProviderID=1" % self.clean_string(
                            row[1])
                        self.cursor.execute(region_id_query)
                        res = self.cursor.fetchall()
                        if res and len(res) > 0:
                            region_id = res[0][0]
                            country_id = "null"
                        else:
                            region_id = "null"
                            pattern = row[1].replace(' ', '') + "%"
                            country_id_query = "select CountryID from Country where upper(replace(CountryName,' ','')) LIKE  '%s'" % (
                                pattern)
                            self.cursor.execute(country_id_query)
                            res = self.cursor.fetchall()
                            if res and len(res) > 0:
                                country_id = str(res[0][0])
                                region_id_query = "select RegionID from RegionCountryMapping where CountryID='%s'" % (
                                    country_id)
                                self.cursor.execute(region_id_query)
                                res = self.cursor.fetchall()
                                if res and len(res) > 0:
                                    region_id = res[0][0]

                                else:
                                    region_id = "null"
                            else:
                                country_id = "null"

                        if "TOTAL" in row[1].upper():
                            is_total = 1
                        for val_id in range(2, len(row)):
                            value = row[val_id]
                            dict_id = (val_id - 1)
                            peri_data = period_data.get(dict_id)
                            period_id = peri_data.get("PeriodID")
                            period_idx = peri_data.get("PeriodIdx")
                            mode = peri_data.get("Mode")
                            ph1 = 1
                            ph2 = "null"
                            ph3 = "null"
                            if (
                                    ph1 == "null" and ph2 == "null" and region_id == "null" and is_total == "null" and group_id == "null" and group_id_2 == "null"):
                                break
                            else:

                                insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                              "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', %s, %s, %s, %s, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                                  period_id, period_idx, mode, ph1, ph2, ph3, value, country_id,
                                                  region_id, group_id, group_id_2, is_total, provided_date
                                              )

                                try:
                                    self.cursor.execute(insertQuery)
                                except Exception as e:
                                    logging.error(e)

                        if "Total OECD".upper() == self.clean_string(row[1]).upper():
                            gr = "Non-OPEC"
                            gr2 = 'Non-OECD'

                        if self.clean_string(row[1]).upper() == "TOTAL NON-OECD":
                            supply_start = False

                        if self.clean_string(row[1]).upper() == "TOTAL NON-OPEC":
                            supply_start = False
                            total_nonopec = 1

                if "PROCESSING GAINS".upper() == self.clean_string(row[1]).upper() or flag == 1:
                    supply_start = False
                    total_nonopec == 1
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        row[1]).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]
                    else:
                        group_id = "null"
                    region_id = "null"
                    is_total = "null"
                    #
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        print("value processing gains", value)
                        dict_id = (val_id - 1)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"
                        if (
                                ph1 == "null" and ph2 == "null" and region_id == "null" and is_total == "null" and group_id == "null" and group_id_2 == "null"):
                            break
                        else:
                            insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                          "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                              period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                              group_id,
                                              is_total, provided_date
                                          )
                            try:
                                self.cursor.execute(insertQuery)
                            except Exception as e:
                                logging.error(e)

                if "BIOFUELS" in self.clean_string(row[1]).upper():
                    global_bio = "global biofuels"
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        global_bio).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]
                    else:
                        group_id = "null"
                    # print("Group_id",group_id)
                    region_id = "null"
                    is_total = "null"
                    #
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        dict_id = (val_id - 1)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"

                        insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                      "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                          period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                          group_id,
                                          is_total, provided_date
                                      )
                        try:
                            self.cursor.execute(insertQuery)
                        except Exception as e:
                            logging.error(e)

                if "TOTAL NON-OPEC".upper() in self.clean_string(row[1]).upper() or total_nonopec == 1:
                    non_opec = 'NON-OPEC'
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        non_opec).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]
                    else:
                        group_id = "null"
                    region_id = "null"
                    is_total = 1
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        print("value non opec", value)
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"
                        if (
                                ph1 == "null" and ph2 == "null" and region_id == "null" and is_total == "null" and group_id == "null" and group_id_2 == "null"):
                            break
                        else:
                            insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                          "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                              period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                              group_id,
                                              is_total, provided_date
                                          )
                            try:
                                self.cursor.execute(insertQuery)
                            except Exception as e:
                                logging.error(e)

                    total_nonopec = 0

                if "OPEC" == self.clean_string(row[1]).upper():
                    pass
                if "CRUDE" in self.clean_string(row[1]).upper():
                    opec = "OPEC"
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        opec).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]
                    else:
                        group_id = "null"
                    # print("Group_id",group_id)
                    region_id = "null"
                    is_total = 1
                    get_group_query = "select * from ProductHR2 where upper(Description) = upper('%s')" % self.clean_string(
                        'Oil').upper()
                    self.cursor.execute(get_group_query)
                    ph_res = self.cursor.fetchall()
                    # print(ph_res)
                    if ph_res and len(ph_res) > 0:
                        ph1 = ph_res[0][2]
                        ph2 = ph_res[0][0]
                    else:
                        ph_id = "null"
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        print("value crude", value)
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")

                        insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                      "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                          period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                          group_id,
                                          is_total, provided_date
                                      )
                        try:
                            self.cursor.execute(insertQuery)
                        except Exception as e:
                            logging.error(e)

                    ph1 = 1
                    ph2 = "null"
                    ph3 = "null"
                if "NGL" in self.clean_string(row[1]).upper():
                    print("ngl")
                    opec = "OPEC"
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        opec).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]

                    else:
                        group_id = "null"

                    region_id = "null"
                    is_total = 1
                    get_group_query = "select * from ProductHR2 where upper(Description) = upper('%s')" % self.clean_string(
                        'Gas').upper()
                    self.cursor.execute(get_group_query)
                    ph_res = self.cursor.fetchall()
                    # print(ph_res)
                    if ph_res and len(ph_res) > 0:
                        ph1 = ph_res[0][2]
                        ph2 = ph_res[0][0]

                    else:
                        ph_id = "null"
                    for val_id in range(2, len(row)):
                        if (
                                ph1 == "null" and ph2 == "null" and region_id == "null" and is_total == "null" and group_id == "null" and group_id_2 == "null"):
                            break
                        else:
                            value = row[val_id]
                            # print("value ngls", value)
                            dict_id = (val_id - 1)
                            # print(dict_id)
                            peri_data = period_data.get(dict_id)
                            period_id = peri_data.get("PeriodID")
                            period_idx = peri_data.get("PeriodIdx")
                            mode = peri_data.get("Mode")

                            insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                          "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                              period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                              group_id,
                                              is_total, provided_date
                                          )
                            try:
                                self.cursor.execute(insertQuery)
                            except Exception as e:
                                logging.error(e)

                    ph1 = 1
                    ph2 = "null"
                    ph3 = "null"
                if 'TOTAL OPEC' == self.clean_string(row[1]).upper():
                    # print("total opec")
                    opec = "OPEC"
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        opec).upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]

                    else:
                        group_id = "null"
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        # print("value", value)
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        is_total = 1
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"
                        region_id = "null"

                        insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                      "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                          period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                          group_id,
                                          is_total, provided_date
                                      )

                        try:
                            self.cursor.execute(insertQuery)
                        except Exception as e:
                            logging.error(e)

                if "NON-OPEC EXCL ANGOLA" == self.clean_string(
                        row[1]).upper() or "OPEC INCL ANGOLA" in self.clean_string(row[1]).upper():
                    print("exclusddding angola")
                    get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        'NON - OPEC EXCL ANGOLA').upper()
                    self.cursor.execute(get_group_query)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id = group_res[0][0]

                    else:
                        group_id = "null"
                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        # print("value", value)
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        is_total = "null"
                        ph1 = "null"
                        ph2 = "null"
                        ph3 = "null"
                        region_id = "null"
                        try:
                            if (
                                    ph2 == "null" and region_id == "null" and is_total == "null" and group_id == "null"):
                                f = open("error files.txt", "a")
                                f.write(str(row[1] + '\t'))
                                f.write(str(value + '\t'))
                                f.write(file_name + '\t')
                                f.write('\n')
                                break
                        except Exception as e:
                            logging.error(e)
                            f = open("error files.txt", "a")
                            f.write(file_name)
                            f.write(str(e))
                            print(e, file_name)

                if 'HISTORICAL COMPOSITION' in self.clean_string(row[1]).upper():
                    ph1 = 1
                    ph2 = "null"
                    ph3 = "null"
                    print("HISTORIACALLLLLLL")
                    if 'NON-OPEC HISTORICAL COMPOSITION' in self.clean_string(row[1]).upper():
                        get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                            'Non-OPEC').upper()
                        self.cursor.execute(get_group_query)
                        group_res = self.cursor.fetchall()
                        if group_res and len(group_res) > 0:
                            group_id = group_res[0][0]

                        else:
                            group_id = "null"
                    else:

                        get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                            'OPEC').upper()
                        self.cursor.execute(get_group_query)
                        group_res = self.cursor.fetchall()
                        if group_res and len(group_res) > 0:
                            group_id = group_res[0][0]

                        else:
                            group_id = "null"

                    # print("group id",group_id)
                    get_group_query2 = "select GroupID from Groups where upper(Description) = upper('%s')" % self.clean_string(
                        'Historical Composition').upper()
                    self.cursor.execute(get_group_query2)
                    group_res = self.cursor.fetchall()
                    if group_res and len(group_res) > 0:
                        group_id_2 = group_res[0][0]

                    else:
                        group_id_2 = "null"

                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        # print("value", value)
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        is_total = 1
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"
                        region_id = "null"

                        insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                      "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, %s, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                          period_id, period_idx, mode, ph1, ph2, ph3, value, region_id,
                                          group_id, group_id_2,
                                          is_total, provided_date
                                      )

                        try:
                            self.cursor.execute(insertQuery)
                        except Exception as e:
                            logging.error(e)

                if 'TOTAL SUPPLY' == self.clean_string(row[1]).upper():
                    ph1 = 1
                    ph2 = "null"
                    ph3 = "null"
                    region_id = "null"
                    group_id = "null"
                    group_id_2 = "null"

                    for val_id in range(2, len(row)):
                        value = row[val_id]
                        dict_id = (val_id - 1)
                        # print(dict_id)
                        peri_data = period_data.get(dict_id)
                        period_id = peri_data.get("PeriodID")
                        period_idx = peri_data.get("PeriodIdx")
                        mode = peri_data.get("Mode")
                        is_total = 1
                        ph1 = 1
                        ph2 = "null"
                        ph3 = "null"
                        region_id = "null"
                        group_id = "null"

                        insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                      "%s, %s, '%s', 'S', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '1')" % (
                                          period_id, period_idx, mode, ph1, ph2, ph3, value, region_id, group_id,
                                          is_total, provided_date
                                      )

                        try:
                            self.cursor.execute(insertQuery)
                        except Exception as e:
                            logging.error(e)
                            f = open("error files.txt", "a")
                            f.write(file_name)
                            f.write(str(e))
                    break
                #
                elif supply_start == False:
                    if self.clean_string(row[1]).upper() == "SUPPLY" or self.clean_string(
                            row[1]).upper() == "OECD SUPPLY":
                        # print("cse truee")
                        supply_start = True
                        gr = 'Non-OPEC'
                        gr2 = 'OECD'
        except Exception as e:
            logging.error(e)
            print(e)
            query = "update RefTables set start = 13 where ReportedDate = %s and TableType = '1'"
            try:
                result = self.cursor.execute(query, (reported_date,))
            except Exception as e:
                logging.error(e)

        os.remove(file_name)
        print("file removed", file_name)


    def insert_table2(self, file_name, sub_table=None):
        provided_date = str(file_name.split("/")[-1]).replace("table1_", "").replace(".csv", "")
        reported_date = provided_date + " 00:00:00"
        version_id = str(file_name.split("/")[-1]).replace(".csv", "").replace(sub_table, "").replace("-", "")
        query = "delete from RefTable where ReportedDate = %s and TableType = '1'"
        try:
            result = self.cursor.execute(query, (reported_date))
            # print(result)
        except Exception as e:
            logging.error(e)
            # print(e, file_name)

        # Mongo Query
        query = "insert into RefTable(ReportedDate,TableType,Flag) values(" \
                "'%s','2','1')" % (reported_date,)
        try:
            result = self.cursor.execute(query)
            # print(result)
        except Exception as e:
            logging.error(e)
        dates = 000
        query = "select max(ReportedDate) from IEA_HistoricMacroElementsData_2_issue where TableType = 2"
        try:
            result = self.cursor.execute(query)
            if result > 1:
                max_date = str(self.cursor.fetchone())
                max_date = (max_date.strip("(datetime.datetime(,)").replace('', '')[0:12])
                max_date = max_date.split(',')
                y = int(max_date[0])
                m = int(max_date[1])
                d = int(max_date[2])
                dates = str(datetime.date(y, m, d))
                dates = dates.replace('-', '')
               # print((dates))
            else:
                dates = 000
        except Exception as e:
            logging.error(e)

        if int(dates) != int(version_id):
            try:
                period_data = {}
                start = False
                ph1 = 1
                ph2 = "null"
                ph3 = "null"
                gr = ''
                provided_date = str(file_name.split("/")[-1]).replace("table2_","").replace(".csv","")

                data = self.read_csv_file(file_name=file_name)
                rows = self.format_changer_for_table2(rows=data)
                for row_id in range(len(rows)):
                    row = rows[row_id]
                    if row_id == 0:
                        period_data = self.convert_to_period_data(row=row, allow_all=True)
                    else:
                        if start == True:

                            get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % gr
                            self.cursor.execute(get_group_query)
                            group_res = self.cursor.fetchall()
                            if group_res and len(group_res) > 0:
                                group_id = group_res[0][0]
                            else:
                                group_id = "null"

                            is_total = "null"
                            region_id_query = "select RegionID from Regions where RegionName='%s' and ProviderID=1"%self.clean_string(row[1])
                            self.cursor.execute(region_id_query)
                            res = self.cursor.fetchall()
                            if res and len(res) > 0:
                                region_id = res[0][0]
                            else:
                                region_id = "null"

                            if "TOTAL" in row[1].upper():
                                is_total = 1

                            for val_id in range(2, len(row)):
                                value = row[val_id]
                                peri_data = period_data.get(val_id)
                                period_id = peri_data.get("PeriodID")
                                period_idx = peri_data.get("PeriodIdx")
                                mode = peri_data.get("Mode")

                                insertQuery = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                              "%s, %s, '%s', 'D', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', null, %s, %s, null, null, 1.0, current_timestamp(), %s, '%s', 1, '2')" % (
                                                period_id, period_idx, mode, ph1, ph2, ph3, value, region_id, group_id,
                                                  is_total, provided_date
                                              )

                                try:
                                    self.cursor.execute(insertQuery)
                                except Exception as e:
                                    logging.error(e)

                            if self.clean_string(row[1]).upper() == "TOTAL NON-OECD":
                                break
                        elif start == False:
                            if self.clean_string(row[1]).upper() == "Demand (mb/d)".upper():
                                start = True
                                gr = 'OECD'

                        if "Total OECD".upper() == self.clean_string(row[1]).upper():
                            gr = "Non-OECD"


            except Exception as e:
                logging.error(e)
                query = "delete from IEA_HistoricMacroElementsData_2_issue where ReportedDate = %s and TableType = '2'"
                try:
                    result = self.cursor.execute(query, (reported_date,))
                except Exception as e:
                    logging.error(e)

                query = "update RefTable set flag = 2 where ReportedDate = %s and TableType = '2'"
                try:
                    result = self.cursor.execute(query, (reported_date,))
                except Exception as e:
                    logging.error(e)


    def convert_pdf_to_csv(self, pdf_list,csv_folder_list):
        """
        converts all pdf from folder into csv
        :param pdf_list:
        :param csv_folder_list:
        :return:
          page"""
        page_numbers = {}
        try:
            for pdf_file in pdf_list:

                try:
                    for folder in csv_folder_list:

                        provided_date = pdf_file.replace(".pdf", "") + " 00:00:00"
                        if folder == 'table1':
                            version_id = pdf_file.replace(".pdf", "").replace("-", "")
                            print(pdf_file)
                            page_numbers [pdf_file] = '1'
                            print(page_numbers)
                            tabletype = '1'
                        # elif folder == 'table2b':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     # page_numbers[pdf_file] = '5'
                        #     tabletype = '2b'
                        #
                        # elif folder == 'table3':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     # page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     tabletype = '3'
                        #     page_numbers[pdf_file] = '6'
                        #
                        # elif folder == 'table4':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     print(page_numbers)
                        #     tabletype = '4'
                        #
                        # elif folder == 'table2':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     # print(table_contents)
                        #     page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     tabletype = '2'
                        #
                        # elif folder == 'table2a':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     # print(table_contents)
                        #     page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     tabletype = '2a'
                        #
                        # elif folder == 'table2b':
                        #     version_id = pdf_file.replace(".pdf", "").replace("-", "")
                        #     # print(table_contents)
                        #     page_numbers = iea_obj.find_page_number_1(table_contents, folder)
                        #     tabletype = '2b'



                        if bool(page_numbers):
                            for pdf, value in page_numbers.items():
                                if pdf == pdf_file:
                                    csv_name = folder + "_" + pdf_file.replace(".pdf", ".csv")
                                    page_number = int(value)  #
                                    con_tab_1 = iea_obj.conert_pdf_to_csv(
                                        pdf_name=PDF_PATH + pdf_file,
                                        csv_name=CSV_PATH + folder + "/" + csv_name,
                                        page_number=page_number)
                                    if con_tab_1 == 1:
                                        os.remove(PDF_PATH + pdf_file)
                                        iea_obj.insert_csv_data(csv_folder_list=csv_folder_list)
                        else:
                            query = "UPDATE RefTable SET flag = '2' where ReportedDate = %s and TableType = '%s"
                            try:
                                result = self.cursor.execute(query, (provided_date, tabletype,))

                            except Exception as e:
                                logging.error(e)

                except Exception as e:
                    logging.error(e)

        except Exception as e:
            logging.error(e)
            raise e



    def insert_csv_data(self, csv_folder_list):
        """
        call insert function of every table data
        :param csv_folder_list:
        :return:
        """
        try:
            for csv_folder in csv_folder_list:
                csv_list = [f for f in os.listdir(CSV_PATH + csv_folder + '/.') if
                            os.path.isfile(CSV_PATH + csv_folder + '/' + f) and f.endswith('.csv')]
                for csv_name in csv_list:

                    try:
                        if csv_folder[-1].isalpha():
                            folder_name = csv_folder
                            function_name = csv_folder[:-1]
                        else:
                            folder_name = csv_folder
                            function_name = csv_folder

                        if folder_name == "table2":
                            data = ""
                        else:
                            data = "_data"
                        eval(
                            "iea_obj.insert_" + function_name + data+"(file_name='" + CSV_PATH + folder_name + "/" + csv_name + "', sub_table='" + folder_name + "_')")
                    except Exception as e:
                        logging.error(e)
            #            print(e)
        except Exception as e:
            logging.error(e)
            raise e

    def insert_table3_data(self, file_name, sub_table=None):
        version_id = str(file_name.split("/")[-1]).replace(".csv", "").replace("table3_", "").replace("-", "")
        provided_date = str(file_name.split("/")[-1]).replace(".csv", "").replace(sub_table, "")
        reported_date = provided_date + " 00:00:00"
     #   print(reported_date)
        query = "delete from RefTable where ReportedDate = %s and TableType = 3"
        try:
            result = self.cursor.execute(query, (reported_date,))
      #      print(result)
        except Exception as e:
            logging.error(e)
       #     print(e)


        # Mongo Query
        query = "insert into RefTable(ReportedDate,TableType,Flag) values(" \
                "'%s','3','1')" % (reported_date,)
        try:
            result = self.cursor.execute(query)
        #    print(result)
        except Exception as e:
            logging.error(e)
        dates = 000
        query = "select max(ReportedDate) from IEA_HistoricMacroElementsData where TableType = 3"
        try:
            result = self.cursor.execute(query, (reported_date,))
            if result > 1:
                max_date = str(self.cursor.fetchone())
                max_date = (max_date.strip("(datetime.datetime(,)").replace('', '')[0:12])
                max_date = max_date.split(',')
                y = int(max_date[0])
                m = int(max_date[1])
                d = int(max_date[2])
                dates = str(datetime.date(y, m, d))
                dates = dates.replace('-', '')
         #       print((dates))
            else:
                dates = 000
        except Exception as e:
            logging.error(e)

        if int(dates) != int(version_id):
          #  print(version_id)

            try:
                rows = self.read_csv_file(file_name=file_name)
                category_list = ["OPEC", "NON-OPEC"]
                exclude_list = ["OECD", "NON-OECD", "PROCESSING GAINS", "GLOBAL BIOFUELS"]
                # exclude_list = ["PROCESSING GAINS","GLOBAL BIOFUELS"]

                specific_country = {
                    "UAE": 'United Arab Emirates',
                    "Congo": 'Congo (Rep. of)',
                    "UK": 'United Kingdom',
                    "Russia": 'Russian Federation'
                }
                res = {}
                country_id = "null"
                region_id = "null"
                group_id = "null"
                group_2_id = "null"

                reported_date = str(file_name.split("/")[-1]).replace(".csv", "").replace("table3_", "")
                versionID = reported_date.replace(".csv", "").replace("-", "").replace("table3_", "")
                for count in range(len(rows)):
                    d = rows[count]
                    if count == 0:
                        if int(versionID) < 19990209:
                            d = self.table_3_prior_formatting(d)
                        periods = self.convert_to_period_data(d, allow_all=True)

                    if count == 1:
                        name = self.clean_string(d[1])
                        if name.upper() in category_list:
                            group_2_id = "null"
                            get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % name
                            self.cursor.execute(get_group_query)
                            group_res = self.cursor.fetchall()
                            if group_res and len(group_res) > 0:
                                group_id = group_res[0][0]
                            else:
                                group_id = "null"

                    if count > 2:
                        # print(res)
                        name = self.clean_string(d[1])
                        name = name.replace(' ', '')
           #             print(name)
                        val1 = specific_country.get(name)
                        if val1:
                            name = val1

                        is_total = "null"
                        ph1 = 1
                        ph2 = 1
                        ph3 = "null"
                        ph4 = "null"

                        if name.upper() == "NGLS":
                            is_total = 1
                            ph1 = 1
                            ph2 = 2
                            ph3 = "null"
                            is_total = "null"

                        if name == 'ProcessingGains':
                            # print("in processing bgainsssss")
                            ph1 = 1;
                            ph2 = "null"
                            ph3 = "null"
                            is_total = "null"
                            group_2_id = "null"
                            get_group_query = "select GroupID from Groups where  upper(Description) ='Processing Gains'"
                            self.cursor.execute(get_group_query)
                            group_res = self.cursor.fetchall()
                            if group_res and len(group_res) > 0:
                                group_id = group_res[0][0]
                            else:
                                group_id = "null"
                        if "TOTAL" in name.upper():
                            is_total = 1
                            ph1 = 1
                            ph2 = "null"
                            ph3 = "null"
                            ph4 = "null"
                            country_id = "null"
                            region_id = "null"
                            name = name.replace("Total", "").strip()
                            name = name.replace("TOTAL", "").strip()
                            if name.upper() == "CRUDE OIL":
                                ph1 = 1
                                ph2 = 1
                                ph3 = "null"
                            elif name.upper() == "NGLS":
                                ph1 = 1
                                ph2 = 2
                                ph3 = "null"


                            elif name.upper() in category_list:
                                ph1 = 1
                                ph2 = "null"
                                ph3 = "null"
                                group_2_id = "null"

                        elif name.upper() in exclude_list:
                            get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % name
                            self.cursor.execute(get_group_query)
                            group_res = self.cursor.fetchall()
                            if group_res and len(group_res) > 0:
                                group_2_id = group_res[0][0]
                            else:
                                group_2_id = "null"

                        elif name.upper() in category_list:
                            get_group_query = "select GroupID from Groups where upper(Description) = upper('%s')" % name
                            self.cursor.execute(get_group_query)
                            group_res = self.cursor.fetchall()
                            if group_res and len(group_res) > 0:  # to make groupid2 null condition
                                group_id = group_res[0][0]
                            else:
                                group_id = "null"
                        else:
                            name = name.replace(' ', '')
                            check_region_name = "select RegionID from Regions where ProviderID = '1' and upper(replace(RegionName,' ',''))=upper('%s')" % name
                            self.cursor.execute(check_region_name)
                            region_res = self.cursor.fetchall()
                            if region_res and len(region_res) > 0:
                                region_id = region_res[0][0]
                                country_id = "null"
                            else:
                                name = name.replace(' ', '')
                                if (name == 'Others'):
                                    region_id = region_id
                                    country_id = "null"

                                else:
                                    name = name.replace(' ', '')
                                    country_id_query = "select CountryID from Country where upper(replace(CountryName,' ','')) ='%s'" % self.clean_string(
                                        name)
                                    self.cursor.execute(country_id_query)
                                    res = self.cursor.fetchall()
                                    if res and len(res) > 0:
                                        country_id = str(res[0][0])
                                    else:
                                        country_id = "null"

                                    region_id_query = "select RegionID from RegionCountryMapping where CountryID = '%s'" % (
                                        country_id)
                                    self.cursor.execute(region_id_query)
                                    res = self.cursor.fetchall()
                                    if res and len(res) > 0:
                                        region_id = str(res[0][0])
                                    else:
                                        region_id = "null"


                        if name != "Neutral Zone" or "gains" in name or "Biofuels" in name:
                            if name.upper() == "SUPPLY":
                                group_id = "null"
                                group_2_id = "null"
                            if name.upper() == "Processing gains" and "Global Biofuels" in name:
                                group_2_id = "null"

                        elemCount = 2
                        for dvalue in d[2:]:
                            if dvalue:
                                p1 = periods.get(elemCount)
                                periodID = p1.get("PeriodID")
                                periodIdx = p1.get("PeriodIdx")
                                mode = p1.get("Mode")
                                ElementType = 'S'
                                insert_query = "insert into IEA_HistoricMacroElementsData(PeriodID, PeriodIdx, Mode, ElementType, PH1, PH2, PH3, PH4, Value, ValueType, ValueUnit, Currency, CountryID, RegionID, GroupID1, GroupID2, GroupID3, VersionID, LastModifiedDate, IsTotal, ReportedDate, ProviderID, TableType) values(" \
                                               "%s, %s, '%s', '%s', %s, %s, %s, null, %s, 'V', 'MBPD', 'USD', %s, %s, %s, %s, null, 1.0, current_timestamp(), %s, '%s', 1,'3')" % (
                                                   periodID, periodIdx, mode, ElementType, ph1, ph2, ph3, dvalue,
                                                   country_id, region_id, group_id, group_2_id, is_total, reported_date
                                               )
                                try:
                                    self.cursor.execute(insert_query)
                                except Exception as e:
                                    logging.error(e)

                            elemCount += 1

            except Exception as e:
                logging.error(e)


                query = "update RefTable set flag = 2 where ReportedDate = %s and TableType = '3'"
                try:
                    result = self.cursor.execute(query, (reported_date,))
                except Exception as e:
                    logging.error(e)

if __name__ == '__main__':
    try:
        iea_obj = IEADataProcessing()
        csv_folder_list = ["table1"]
        pdf_list = iea_obj.get_pdf_list()
        print(pdf_list)
        # table_name = 'contents'
        # table_contents = iea_obj.find_table_contents(pdf_list, table_name)
        # print(table_contents)
        iea_obj.convert_pdf_to_csv(pdf_list=pdf_list, csv_folder_list=csv_folder_list)

    except Exception as e:
        logging.error(e)
        raise e

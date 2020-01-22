import mysql.connector
import pandas as pd
import sqlalchemy
import random
def starstockmultiple():
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB')
    df = pd.read_sql_query('select * from StocksStarSchemaNew where DWCoID = 9', engine)
    # print(df)
    dwcoid = "select DWCoID from DWDerivedCompany where Ticker IS Not NULL and DWCOID not in(9,11569,3545,6918,9020) limit 5000 "
    with engine.connect() as con:
        res = list(con.execute(dwcoid))

    for val in res:
        dwcoid = (val[0])
        df['DWCoID'] = dwcoid
        no = random.random()
        old = df['Value']
        df['Value']  = df['Value'] * no
        # for val,newval in zip(old,new):
        #     print(val,newval,no)

        try:
            frame = df.to_sql('StocksStarSchemaMultiple1', engine, if_exists='append', index=False)

        except ValueError as vx:
            print(vx)

        except Exception as ex:
            print(ex)

        # break

        # df['Value'] = df['Value'] * no




starstockmultiple()
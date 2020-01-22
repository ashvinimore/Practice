import psycopg2
try:
    con=psycopg2.connect(dbname= 'dwh', host='52.41.146.155',
    port= 5439, user= 'warehouse', password= 'Dwh!virtua1')
    print(con)
except Exception as e:
    print(e)
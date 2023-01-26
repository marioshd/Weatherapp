import pymysql

conn = pymysql.connect(host = '127.0.0.1', #add host
                       user = 'master', #add user
                       password = 'sysadmin', #add password
                       db = 'weather') #add database

def latestForecast():
    with conn.cursor() as cur:
        cur.execute('SELECT latitude,longitude,datetime,temperature FROM forecast WHERE datetime IN (SELECT MAX(datetime) FROM forecast GROUP BY DATE(datetime),latitude,longitude);')
        queryResult = cur.fetchall()
        for row in queryResult:          
                print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')
        
def averageTemp():
    with conn.cursor() as cur:
        cur.execute('SELECT tbl.latitude,tbl.longitude,DATE(tbl.datetime) AS Date,ROUND(AVG(tbl.temperature),5) AS AverageTemperature FROM (WITH forecast AS (SELECT latitude,longitude,datetime,temperature,ROW_NUMBER() OVER (PARTITION BY latitude,longitude,date(datetime) ORDER BY datetime DESC) row_num FROM forecast) SELECT row_num,latitude,longitude,datetime,temperature FROM forecast WHERE row_num <= 3) tbl GROUP BY DATE(datetime),latitude,longitude;')
        queryResult = cur.fetchall()
        for row in queryResult:
                print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')
                
def topLocation(topN): #topNumber should be a numeric value
    with conn.cursor() as cur:
        cur.execute('SELECT latitude,longitude,datetime,MAX(temperature) FROM forecast GROUP BY latitude,longitude,datetime ORDER BY MAX(temperature) DESC  LIMIT %s;',(topN))
        queryResult = cur.fetchall()
        for row in queryResult:   
                print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')
    return topN
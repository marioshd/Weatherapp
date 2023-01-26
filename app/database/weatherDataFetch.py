import meteomatics.api as api
import datetime as dt
import pymysql

conn = pymysql.connect(host='127.0.0.1', #add host
                       user='master', #add user
                       password='sysadmin', #add password
                       db='weather') #add database

MeteomUsername = 'username' #add meteomatics username
MeteomPassword = 'password' #add meteomatics password

coordList = [(35.112657,33.319656),
           (35.130608,33.370146),
           (35.157861,33.341800)] #Create a list of 3 locations
i = 0 #required from row 16 onwards

for i in [0,1,2]: #Create a loop to request the 3 locations one at a time
    coords = [coordList[i]]
    startdate = dt.datetime(year=2023, month=1, day=24, hour=22)
    enddate = dt.datetime(year=2023, month=1, day=31, hour=21) #select the start/end date by indication the year,month,day and hour
    interval = dt.timedelta(hours=1) #will fetch data every 1 hour starting from the startdate until enddate
    parameters = ['t_2m:C'] #As per meteomatics parameters, this is the Instantaneous temperature at 2m above ground in degrees Celsius (C)
    df = api.query_time_series(coords,startdate,enddate,interval,parameters,MeteomUsername,MeteomPassword)
    df = df.reset_index() #dataframe has no index, hence created one as I will need it later in row 26
    df.rename(columns={"t_2m:C": "temp"}, inplace=True) #In row 28, I was getting an error when I was writting row.t_2m:C, hence renamed the field

    cursor = conn.cursor()
    for index, row in df.iterrows():
        sql = "INSERT INTO forecast (datetime,latitude,longitude,temperature) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE temperature=VALUES(temperature)"
        cursor.execute(sql, (row.validdate, row.lat, row.lon, row.temp)) #read the dataframe and insert the records one at a time in the table
    i+=1 #start with the first element of the coordList, then go to the second and finally to the third
    conn.commit()
cursor.close()

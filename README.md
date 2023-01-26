# Weatherapp

Required Installations:
Python: meteomatics, pymysql packages

Go to database folder and create the MySQL table included in the weatherForecast_Queries.sql.
Run the weatherDataFetch.py to fetch the data from meteomatics and insert them into the corresponding table in the database.
Go to function folder and run the weatherForecastApp.py.

Function can be called with the below way, once the script is run:
latestForecast()
averageTemp()
topLocation(n)

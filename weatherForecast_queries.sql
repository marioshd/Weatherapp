#Task 1#
SELECT latitude,longitude,datetime,temperature FROM forecast WHERE datetime IN (SELECT MAX(datetime) FROM forecast GROUP BY DATE(datetime),latitude,longitude);

#Task 2#
SELECT tbl.latitude,tbl.longitude,DATE(tbl.datetime) AS Date,ROUND(AVG(tbl.temperature),5) AS AverageTemperature FROM (
WITH forecast
AS (SELECT latitude,longitude,datetime,temperature,
       ROW_NUMBER() OVER (PARTITION BY latitude,longitude,date(datetime) ORDER BY datetime DESC) row_num
    FROM forecast)
SELECT row_num,latitude,longitude,datetime,temperature
FROM forecast WHERE row_num <= 3) tbl GROUP BY DATE(datetime),latitude,longitude;

#Task 3#
select * from forecast;
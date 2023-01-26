#SHOW CREATE TABLE#
CREATE TABLE forecast2 (
   recordId int NOT NULL AUTO_INCREMENT,
   datetime datetime NOT NULL,
   latitude decimal(9,6) DEFAULT NULL,
   longitude decimal(9,6) DEFAULT NULL,
   temperature double DEFAULT NULL,
   PRIMARY KEY (recordId),
   UNIQUE KEY dateLoc (datetime,latitude,longitude)
 ) ENGINE=InnoDB AUTO_INCREMENT=5041 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
SELECT latitude,longitude,datetime,MAX(temperature) FROM forecast GROUP BY latitude,longitude,datetime ORDER BY MAX(temperature) DESC LIMIT 3;
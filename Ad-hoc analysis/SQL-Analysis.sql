-- Question 1- Payment Method Performance
-- Do Card and Cash trips differ in trip volume, average fare and total fare revenue?
SELECT
 CASE
 WHEN payment_type = 1 THEN 'Credit Card'
 WHEN payment_type = 2 THEN 'Cash'
 END AS payment_method,
 COUNT(*) AS total_trips,
 ROUND(AVG(fare_amount), 2) AS avg_fare,
 ROUND(SUM(fare_amount), 2) AS total_fare_revenue
FROM taxi_trips
WHERE payment_type IN (1, 2)
 AND fare_amount > 0
GROUP BY payment_type
ORDER BY avg_fare DESC;

-- Question 2- Trip Distance Analysis
-- How does fare performance change across short, medium and long trips?
SELECT
 CASE
 WHEN trip_distance < 2 THEN 'Short (<2 miles)'
 WHEN trip_distance < 5 THEN 'Medium (2-5 miles)'
 ELSE 'Long (5+ miles)'
 END AS distance_group,
 COUNT(*) AS total_trips,
 ROUND(AVG(trip_distance), 2) AS avg_distance,
 ROUND(AVG(fare_amount), 2) AS avg_fare,
 ROUND(SUM(fare_amount), 2) AS total_fare_revenue
FROM taxi_trips
WHERE trip_distance > 0
 AND fare_amount > 0
GROUP BY distance_group
ORDER BY avg_distance;

-- Question 3- Trip Duration Analysis
--  Do longer trips generate higher average fares?
SELECT
 CASE
 WHEN TIMESTAMPDIFF(MINUTE,
 tpep_pickup_datetime,
 tpep_dropoff_datetime) < 10 THEN 'Short (<10 min)'
 WHEN TIMESTAMPDIFF(MINUTE,
 tpep_pickup_datetime,
 tpep_dropoff_datetime) < 30 THEN 'Medium (10-29 min)'
 ELSE 'Long (30+ min)' END AS duration_group,
 COUNT(*) AS total_trips,
 ROUND(AVG(fare_amount), 2) AS avg_fare,
 ROUND(SUM(fare_amount), 2) AS total_fare_revenue
FROM taxi_trips
WHERE fare_amount > 0
 AND tpep_dropoff_datetime > tpep_pickup_datetime
GROUP BY duration_group
ORDER BY avg_fare;

-- Question 4- Peak Revenue Hours
-- Which pickup hours generate the most trips and fare revenue?
SELECT
 HOUR(tpep_pickup_datetime) AS pickup_hour,
 COUNT(*) AS total_trips,
 ROUND(AVG(fare_amount), 2) AS avg_fare,
 ROUND(SUM(fare_amount), 2) AS total_fare_revenue
FROM taxi_trips
WHERE fare_amount > 0
GROUP BY HOUR(tpep_pickup_datetime)
ORDER BY total_fare_revenue DESC;

-- Question 5-  Passenger Count Analysis
-- How do trip volume and fare change with the number of passengers?
SELECT
 passenger_count,
 COUNT(*) AS total_trips,
 ROUND(AVG(fare_amount), 2) AS avg_fare,
 ROUND(SUM(fare_amount), 2) AS total_fare_revenue
FROM taxi_trips
WHERE passenger_count BETWEEN 1 AND 5
 AND fare_amount > 0
GROUP BY passenger_count
ORDER BY passenger_count;

-- Question 6- Revenue Efficiency by Payment Method
--  Which payment method has the higher average fare earned per mile?
SELECT
 CASE
 WHEN payment_type = 1 THEN 'Card'
 WHEN payment_type = 2 THEN 'Cash'
 END AS payment_method,
 COUNT(*) AS total_trips,
 ROUND(AVG(fare_amount / trip_distance), 2)
 AS avg_fare_per_mile
FROM taxi_trips
WHERE payment_type IN (1, 2)
 AND fare_amount > 0
 AND trip_distance > 0
GROUP BY payment_type
ORDER BY avg_fare_per_mile DESC;


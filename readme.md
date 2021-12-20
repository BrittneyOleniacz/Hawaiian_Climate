# Climate Analysis: Hawaii

## Climate Analysis and Exploration
I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. I used SQLAlchemy ORM queries, Pandas, and Matplotlib to complete the following analyses. 

* Use SQLAlchemy `create_engine` to connect to your sqlite database.
* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis
* I created a query to retrieve the `data` and `prcp` values from the last 12 months of the precipitation data.
* Query results were put into a Pandas DataFrame and the index set to the date column.
* The DataFrame was sorted by the `date` values. 
* Results plotted using the DataFrame `plot` method.
* The summary statistics for the precipitation data printed via Pandas.

### Station Analysis
* Design a query:
  * to calculate the total number of stations.
  * to find the most active stations.
    * List the stations and observation counts in descending order.
    * Which station has the highest number of observations?
* Design a query:
  * to retrieve the last 12 months of temperature observation data (TOBS).
    * Used the highest number of observations to filter the stations.
    * Plotted the results as a histogram with `bins=12`.

- - -

## Climate App
Using the queries I just developed I designed a Flask API. 

### Routes
* `/`
  * Home page.
  * List all routes that are available.
* `/api/v1.0/precipitation`
  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of your dictionary.
* `/api/v1.0/stations`
  * Return a JSON list of stations from the dataset.
* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  * Return a JSON list of temperature observations (TOBS) for the previous year.
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

## Additional Analyses

### June v. December Temperatures
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.
* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?
_Across all the stations, the mean temperatures in June and December temperature in years 2010-2017 differ by 3.9 degrees Fahrenheit. An unpaired t-test was conducted, and with an extremely low p-value, the difference is deemed statistically significant. 
_
### Calculating Temperatures
* I used a function called `calc_temps` that accepts a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.
* The min, avg, and max temperature from the query is plotted as a bar chart using:
  * the average temperature as the bar height.
  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

### Daily Rainfall Average
* Calculate the:
* rainfall per weather station using the previous year's matching dates.
* daily normals. Normals are the averages for the min, avg, and max temperatures.
* The function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.
* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.
* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Then, Pandas let me area plot (`stacked=False`) for the daily normals.

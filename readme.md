# Climate Analysis: Hawaii

## Climate Analysis and Exploration
I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. I used SQLAlchemy ORM queries, Pandas, and Matplotlib to complete the following analyses. 

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
    * List the stations and observation counts in descending order to determine the station with the highest number of observations?

* Design a query:
  * to retrieve the last 12 months of temperature observation data (Tobs).
    * Used the highest number of observations to filter the stations.
    * Plotted the results as a histogram with `bins=12`.


## Additional Analyses

### June v. December Temperatures
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.
* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Calculating Temperatures
* I used a function called `calc_temps` that accepts a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.
* The min, avg, and max temperature from the query is plotted as a bar chart using:
  * the average temperature as the bar height.
  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

### Daily Rainfall Average
* Calculated the:
  * rainfall per weather station using the previous year's matching dates.
  * the Daily normals as the averages for the min, avg, and max temperatures.
* The function called `daily_normals` will calculate the daily normals for a specific date. This date string will be in the format `%m-%d` and will use historic TOBS that match that date string.
* Create a list of dates for your trip in the format `%m-%d`.
* Using the `daily_normals` function, calculate the normals for each date string and append the results to a list.
* Convert list of daily normals into a Pandas DataFrame with the index set to the date.
* Then, area plot (`stacked=False`) for the daily normals with Pandas.

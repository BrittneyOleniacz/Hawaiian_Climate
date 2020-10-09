#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


import datetime as dt


# ### Reflect Tables into SQLAlchemy ORM

# In[5]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[6]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[7]:


# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect = True)


# In[8]:


# We can view all of the classes that automap found
base.classes.keys()


# In[9]:


# Save references to each table
m = base.classes.measurement
s = base.classes.station


# In[10]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[11]:


station_cols = s.__table__.columns
print(station_cols)


# In[12]:


meas_cols = m.__table__.columns
print(meas_cols)


# ## Exploratory Climate Analysis

# In[13]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results
max_date = session.query(func.max(m.date)).all()
max_date_index = max_date[0][0]
print(max_date)


# In[14]:


# Calculate the date 1 year ago from the last data point in the database
datetime_object = dt.datetime.strptime(max_date_index, '%Y-%m-%d')
datetime_object_past = datetime_object - dt.timedelta(days = 365)
datetime_object_past


# In[15]:


# Perform a query to retrieve the data and precipitation scores
prcp_result = session.query(m.date, m.prcp).filter(m.date > datetime_object_past).all()


# In[16]:


# Save the query results as a Pandas DataFrame...
prcp_result_df = pd.DataFrame(prcp_result)

#...and set the index to the date column
# Sort the dataframe by date
prcp_result_df = prcp_result_df.set_index("date").sort_values(by = "date")
prcp_result_df = prcp_result_df.dropna()
prcp_result_df


# In[17]:


with plt.style.context("seaborn-white"):
    plt.rcParams["axes.grid"]=True
    prcp_result_df.plot(rot=35, figsize=(20,10), linewidth=3, color="darkblue", legend=False)
    plt.title("Precipitation Observations (2016-08-24 to 2017-08-19)", fontsize=25)
    plt.xlabel("Date", fontsize=22)
    plt.xticks(fontsize=20)
    plt.ylabel("Precipitation", fontsize=22)
    plt.yticks(fontsize=20)
    plt.ylim(0,7)
plt.savefig("Temperature Observations")


# In[18]:


# Use Pandas to calcualte the summary statistics for the precipitation data
prcp_result_df.describe()


# In[19]:


# Design a query to show how many stations are available in this dataset?
stations = session.query(func.count(s.station)).all()
stations


# In[20]:


#number of records 
records = session.query(func.count(m.station)).group_by(m.station).all()
records


# In[21]:


# What are the most active stations? (i.e. what stations have the most rows)?
session.query(m.station, func.count(m.station)).group_by(m.station).all()


# In[22]:


# List the stations and the counts in descending order.
station_records = session.query(m.station, func.count(m.station)).group_by(m.station).order_by(func.count(m.station).desc()).all()
station_records


# In[23]:


# Using the station id from the previous query, calculate the lowest temperature recorded, 
#highest temperature recorded, and average temperature of the most active station?
session.query(m.station, func.max(m.tobs), func.avg(m.tobs), func.min(m.tobs)).filter(m.station == "USC00519281").all()


# In[24]:


# Choose the station with the highest number of temperature observations.
most_tobs = session.query(m.station, func.max(m.tobs))

# Query the last 12 months of temperature observation data for this station...
temp_obs = session.query(m.date, m.tobs).filter(m.date > datetime_object_past).filter(m.station == "USC00519281").all()
temp_obs_df =  pd.DataFrame(temp_obs)
temp_obs_df = temp_obs_df.set_index("date")
temp_obs_df


# In[25]:


#...and plot the results as a histogram
temp_obs_df.plot(kind = "hist", figsize=(20,10), color="darkred", legend=False).set_facecolor("white")
plt.title("Station USC00519281: Temperature Observations (2016-08-24 to 2017-08-19)", fontsize = 25)
plt.xlabel("Frequency", fontsize = 22)
plt.xticks(rotation="horizontal", fontsize = 20)
plt.ylabel("Temperature", fontsize = 22)
plt.yticks(rotation="horizontal", fontsize=20)
plt.show()
plt.savefig("Temperature Observations")


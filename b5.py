
import pandas
import matplotlib.pyplot as plt 

data = pandas.read_csv("weather_year.csv")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
                
# g) What is the maximum temperature in New York? 
print(data['date'][data['events']=='Rain'].count())

#h) What was the average speed of the wind during the month? 

print ("Average Windspeed is", data['max_wind'].mean())


data.mean_temp.hist()
plt.show()
#data.max_temp.plot() # Without Labelled Axis

ax = data.max_temp.plot(title="Min and Max Temperatures")
data.min_temp.plot(style="green", ax=ax)
ax.set_ylabel("Temperature (F)")

plt.show()

data.max_temp.tail(8).plot()
plt.show()


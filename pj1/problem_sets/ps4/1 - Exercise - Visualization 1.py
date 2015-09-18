from pandas import *
from ggplot import *
import pandasql
import datetime

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    df = turnstile_weather[['DATEn','Hour','ENTRIESn_hourly','rain']]
    df.is_copy = False
    
    df['date'] = pandas.to_datetime(df['DATEn'])
    # df['date'] = datetime.datetime.strptime(turnstile_weather['DATEn'], '%y-%m-%d')
    
    # strftime('%w', date)
    # q = """
    # SELECT strftime('%w', date), avg(cast (ENTRIESn_hourly as integer)) FROM df GROUP BY strftime('%w', date)
    # """
    q = """
    SELECT Hour, avg(cast (ENTRIESn_hourly as integer)) as AVG_ENTRIESn_hourly FROM df GROUP BY Hour
    """
    
    #Execute your SQL command against the pandas frame
    mean_entries_per_hour = pandasql.sqldf(q.lower(), locals())
    # print mean_entries_per_hour
    # print df
    
    # dayofweek
    # f = lambda x: datetime.strptime(x, "%Y-%m-%d").strftime('%A') 
    # df['dayofweek'] = df['DATEn'].apply(f)

    # Ridership by time of day
    plot = ggplot(mean_entries_per_hour,aes('Hour','avg_entriesn_hourly')) + \
    geom_bar(fill = 'steelblue', stat='bar') + \
    scale_x_continuous(limits=[0,23]) + \
    scale_y_continuous(limits=[0,2700]) + \
    ggtitle('Average entries by time of day') + \
    xlab('Hour') + \
    ylab('Entries')

    # geom_line(color='steelblue', size=5) + \
    # geom_point(color='steelblue', size=100) + \
    
    # or day of week
    # plot = ggplot(df,aes('dayofweek','ENTRIESn_hourly')) + \
    # geom_bar(fill = 'steelblue', stat='bar') + \
    # ggtitle('Entries by day of week') + xlab('Day of week') + ylab('Entries')
    
    return plot

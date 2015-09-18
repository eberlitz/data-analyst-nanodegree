import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    # plt.xlabel('Residuals')
    # plt.ylabel('Frequency')
    # plt.title('Histogram of the residuals')
    
    # residual = turnstile_weather['ENTRIESn_hourly'] - predictions
    # plt.xlabel('Fitted Value')
    # plt.ylabel('Residual')
    # plt.title('Residuals versus fits')
    # plt.plot(predictions, residual, 'ro')
    #plt.plot(turnstile_weather['ENTRIESn_hourly'],predictions, 'b')
    
    #(turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=100)
    #plt.plot(turnstile_weather['ENTRIESn_hourly'] - predictions, 'b') 
    #plt.plot(predictions, 'b')
    

    
    # Probability Plot
    stats.probplot(turnstile_weather['ENTRIESn_hourly'] - predictions, plot=plt)
    plt.show()
    return plt
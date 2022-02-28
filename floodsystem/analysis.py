import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
from floodsystem.stationdata import update_water_levels

def polyfit(dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    #shift x values
    p_coeff = np.polyfit(x-x[0],y,p) 
    poly = np.poly1d(p_coeff)
    d0 = matplotlib.dates.date2num(dates[0])

    return poly, d0

def predict_max(station, dates, levels, order, future_days):
    low, high = station.typical_range
    poly, d0 = polyfit(dates, levels, order)
    predicted = max(poly(np.arange(0, future_days, 10)))
    predicted_relative = (predicted - low) / (high - low)
    print(predicted_relative)
    return predicted_relative
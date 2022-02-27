import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
from floodsystem.stationdata import update_water_levels
from matplotlib.dates import date2num 

#Finds least-squares fit of a polynomial of degree p to water level data
def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x-x[0],y,p) #shift x values
    poly = np.poly1d(p_coeff)
    d0 = matplotlib.dates.date2num(dates[0])

    return poly, d0
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
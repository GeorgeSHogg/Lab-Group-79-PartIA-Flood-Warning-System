from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import most_at_risk_stations
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations= build_station_list()
    update_water_levels(stations)
    highest_level_stations = most_at_risk_stations(stations, 10)
    
    stations_used = []
    n = 5
 
    for station in highest_level_stations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt = timedelta(days=2))
        if len(dates) > 3:
            stations_used.append(station[0])
            n -= 1
        else:
            print("Station ", station[0].name, "does not have sufficient recent data to plot")
        if not n:
            break

    for station in stations_used:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        plot_water_level_with_fit(station, dates, levels, 4)
        
if  __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import most_at_risk_stations
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations= build_station_list()
    update_water_levels(stations)
    high_risk_stations = most_at_risk_stations(stations, 5)
  
    for station, _ in high_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        try:
            graph = plot_water_level_with_fit(station, dates, levels, 4)
        except:
            print('No data')
        
if  __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
# Write your solution here

import math

def get_station_data(filename: str) -> dict:
    # Read names and locations of all stations in a dict
    with open(filename) as new_file:
        station_data = {}
        for row in new_file:
            parts = row.split(";")
            if parts[0] == "Longitude":
                continue
            station_name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            station_data[station_name] = (longitude, latitude)
    return station_data

def distance(stations: dict, station1: str, station2: str) -> float:
    # Return the distance between the two stations
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance_for_one_station(stations: dict, station_names: list, station_name: str) -> tuple:
    # Return a tuple where the first two elements are the names of
    # the two stations (with one station fixed for comparison) and
    # the third element is the distance between the them.
    start_index = station_names.index(station_name)+1
    remaining_stations = station_names[start_index:]
    max_distance = 0
    station1 = ""
    station2 = ""
    for station in remaining_stations:
        if max_distance < distance(stations, station_name, station):
            max_distance = distance(stations, station_name, station)
            station1 = station_name
            station2 = station
    return (station1, station2, max_distance)

def greatest_distance(stations: dict) -> tuple:
    # Return a tuple where the first two elements are the names of
    # the two stations, and the third element is the distance
    # between them.
    station_names = list(stations.keys())
    max_distance = 0
    station1 = ""
    station2 = ""
    for station_name in station_names:
        stationA, stationB, distance = greatest_distance_for_one_station(stations, station_names, station_name)
        if max_distance < distance:
            max_distance = distance
            station1 = stationA
            station2 = stationB
    return (station1, station2, max_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

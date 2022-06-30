#zadnie 1
class GeoPoint:
    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude

    def longitude(self):
        return self.longitude

    def latitude(self):
        return self.latitude
    
    def __eq__(self, other):
        return (
            self.longitude == other.longitude and self.latitude == other.latitude)
    
    def __str__(self):
        return f'{{lat: {self.latitude}, lon: {self.longitude}}}.'
    
def task_1():
    point_1 = GeoPoint(51.21782, 22.54583)
    point_2 = GeoPoint(51.21782, 22.54583)
    
    print(point_1 == point_2)
    print(point_1, point_2)

#zadnie 2
from math import radians, cos, sin, asin, sqrt

class GeoPoint:
    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude
        
    def longitude(self):
        return self.longitude
    
    def latitude(self):
        return self.latitude

    def haversine(lon1: float, lat1: float, lon2: float, lat2: float):
        """Calculate the great circle distance between two points on the earth (specified in decimal degrees) """
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))

        meters = 6371000 * c
        return meters
    
    def print_geoPoint_list(geo_point_list: list):
        for point in geo_point_list:
            print(f'{point.longitude: .5f}, {point.latitude :.5f}')
            
    def sort_geoPoint_list(geo_point_list: list, point_sorted_by):
        geo_point_list.sort(key=lambda x: GeoPoint.haversine(x.longitude, x.latitude, point_sorted_by.longitude, point_sorted_by.latitude))
        
    def __eq__(self, other):
        return (self.longitude == other.longitude and self.latitude == other.latitude)
    
    def __str__(self):
        return f'{{lat: {self.latitude}, lon: {self.longitude}}}.'
    
    def __repr__(self):
        return f'{self.longitude} {self.latitude}'
    
def task_2():
    point_1 = GeoPoint(51.21782, 22.54583)
    point_2 = GeoPoint(51.21353, 22.54142)
    point_3 = GeoPoint(51.21483, 22.52527)
    point_4 = GeoPoint(51.22352, 22.55640)
    
    point_sorted_by = GeoPoint(51.21167, 22.5222)
    points_list = [point_1, point_2, point_3, point_4]
    GeoPoint.sort_geoPoint_list(points_list, point_sorted_by)
    GeoPoint.print_geoPoint_list(points_list)

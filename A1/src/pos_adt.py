## @file pos_adt.py
#  @author Jay Mody
#  @brief Provides the GPosT ADT class for representing latitude/longitude points on Earth.
#  @date 19/01/20 (dd/mm/yy)

from math import cos, sin, asin, atan2, radians
from date_adt import DateT

## @brief An ADT ...
class GPosT:
    ## Earth's radius in km
    __R = 6731

    ## @brief Constructor for GPosT objects.
    #  @
    #  @param lat
    #  @param long
    #  @throws ValueError
    def __init__(self, lat, long):
        if not (-180 <= long and long <= 180):
            raise ValueError("long (longitude) must be between -180 and 180")
        if not (-90 <= lat and lat <= 90):
            raise ValueError("lat (latitude) must be between -90 and 90")

        self.__lat = lat
        self.__long = long

    ## @brief ?
    #  @return ?
    def lat(self):
        return self.__lat

    ## @brief ?
    #  @return ?
    def long(self):
        return self.__long

    ## @brief ?
    #  @param p
    #  @return ?
    def west_of(self, p):
        return self.__long < p.__long

    ## @brief ?
    #  @param p
    #  @return ?
    def north_of(self, p):
        return self.__lat > p.__lat

    ## @brief ?
    #  @param p
    #  @return ?
    def equal(self, p):
        distance = self.distance(p)
        return distance < 1.0

    ## @brief ?
    #  @param b
    #  @param d
    def move(self, b, d):
        b = radians(b)
        lat = radians(self.__lat)
        long = radians(self.__long)

        angular_dist = d / self.__R
        target_lat = asin(sin(lat) * cos(angular_dist) + cos(lat) * sin(angular_dist) * sin(b))
        y = sin(b) * sin(angular_dist) * cos(lat)
        x = cos(angular_dist) - sin(lat) * target_lat
        target_long = long + atan2(y, x)

        self.__lat = target_lat
        self.__long = target_long

    ## @brief ?
    #  @return ?
    def distance(self, p):
        lat = radians(self.__lat)
        long = radians(self.__long)

        delta_long = p.__long - long
        delta_lat = p.__lat - lat
        a = sin(0.5 * delta_lat)**2 + cos(lat) * cos(p.__lat) * sin(0.5 * delta_long)
        c = 2 * atan2(a**0.5, (1-a)**0.5)
        distance = self.__R * c
        return distance

    ## @brief ?
    #  @param p
    #  @param d
    #  @param s
    #  @return ?
    def arrival_date(self, p, d, s):
        distance = self.distance(p)
        days = distance / s
        return d.add_days(days=days)

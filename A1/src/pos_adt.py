## @file pos_adt.py
#  @author Jay Mody
#  @brief ?
#  @date ?

from math import cos, sin, asin, atan2, radians

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

        self.__lat = radians(lat)
        self.__long = radians(long)

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
    #  @return ?
    def distance(self, p):
        delta_long = p.__long - self.__long
        delta_lat = p.__lat - self.__lat
        a = sin(0.5 * delta_lat)**2 + cos(self.__lat) * cos(p.__lat) * sin(0.5 * delta_long)
        c = 2 * atan2(a**0.5, (1-a)**0.5)
        distance = self.__R * c
        return distance

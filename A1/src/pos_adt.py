## @file pos_adt.py
#  @author Jay Mody
#  @brief Provides the GPosT ADT class for representing latitude/longitude points on Earth.
#  @date 19/01/20 (dd/mm/yy)

from math import cos, sin, asin, atan2, radians, degrees
from date_adt import DateT

## @brief An ADT that represents latitude/longitude positions.
#  @details An ADT for signed decimal degree latiitude and longitude GPS positions on Earth, assuming Earth's radius to be 6371km.
class GPosT:
    ## Earth's radius in km
    __R = 6371

    ## @brief Constructor for GPosT objects.
    #  @param lat Latitude as a signed decimal degree (float from -90 to 90), with + as north and - as south.
    #  @param long Longitude as a signed decimal degree (float from -180 to 180), with + as east and - as west.
    #  @throws ValueError Thrown if longitude or latitude values are not in the correct ranges.
    def __init__(self, lat, long):
        if not (-180 <= long and long <= 180):
            raise ValueError("long (longitude) must be between -180 and 180")
        if not (-90 <= lat and lat <= 90):
            raise ValueError("lat (latitude) must be between -90 and 90")

        self.__lat = radians(lat)
        self.__long = radians(long)

    ## @brief Get's the latitude (as a signed decimal degree).
    #  @return The latitude.
    def lat(self):
        return degrees(self.__lat)

    ## @brief Get's the longitude (as a signed decimal degree).
    #  @return The longitude.
    def long(self):
        return degrees(self.__long)

    ## @brief Determins if this position is west of position p.
    #  @param p A GPosT object.
    #  @return  A boolean that is True if this position is west of p, else False.
    def west_of(self, p):
        return self.__long < p.__long

    ## @brief Determines if this position is north of position p.
    #  @param p A GPosT object.
    #  @return  A boolean that is True if this position is north of p, else False.
    def north_of(self, p):
        return self.__lat > p.__lat

    ## @brief Determines if this position equal (within 1km distance) to position p.
    #  @param p A GPosT object.
    #  @return  A boolean that is True if this position is equal to p, else False.
    def equal(self, p):
        distance = self.distance(p)
        return distance < 1.0

    ## @brief Moves the current position by d distance at b bearing.
    #  @param b The bearing of the move, as a signed decimal degree.
    #  @param d The distance (in km) to move.
    def move(self, b, d):
        b = radians(b)

        angular_dist = d / self.__R
        target_lat = asin(sin(self.__lat) * cos(angular_dist) + cos(self.__lat) * sin(angular_dist) * sin(b))

        y = sin(b) * sin(angular_dist) * cos(self.__lat)
        x = cos(angular_dist) - sin(self.__lat) * target_lat
        target_long = self.__long + atan2(y, x)

        self.__lat = target_lat
        self.__long = target_long

    ## @brief Gets the distance (in km) between this position and position p.
    #  @return The distance (in km)
    def distance(self, p):
        delta_lat = p.__lat - self.__lat
        delta_long = p.__long - self.__long

        a = sin(0.5 * delta_lat)**2 + cos(self.__lat) * cos(p.__lat) * sin(0.5 * delta_long)**2
        c = 2 * atan2(a**0.5, (1-a)**0.5)
        distance = self.__R * c
        return distance

    ## @brief Calculates the arrival date to get to position p from this position, given a start date and speed.
    #  @param p The target position (as a GPosT object).
    #  @param d The start date (as a DateT object).
    #  @param s The speed (in km/day).
    #  @return The arrival date (as a DateT object).
    def arrival_date(self, p, d, s):
        distance = self.distance(p)
        days = distance / s
        return d.add_days(days=days)

## @file pos_adt.py
#  @title pos_adt
#  @author Reneuel Dela Cruz
#  @date 2020-01-20

import math
from date_adt import DateT

## @brief An ADT for representing global position coordinates.
#  @details This class creates an ADT for global position coordinates using 
#  latitude and longitude as signed decimal degrees.
class GPosT:

    ## @brief Constructor for GPosT.
    #  @details Constructor accepts two parameters to initialize the global position coordinate.
    #  @param latitude Float for the latitude in signed decimal degrees.
    #  @param longitude Float for the longitude in signed decimal degrees.
    #  @throws ValueError Error if the latitude or longitude exceeds the maximum possible values.
    def __init__(self, latitude, longitude):
        if abs(latitude) > 90 or abs(longitude) > 180:
            raise ValueError("ERROR: Maximum latitude or longitude values exceeded")

        self.__latitude = latitude
        self.__longitude = longitude
    
    ## @brief This function gets the position's latitude.
    #  @return Float value for latitude.
    def lat(self):
        return self.__latitude
    
    ## @brief This function gets the position's longitude.
    #  @return Float value for longitude.
    def long(self):
        return self.__longitude
    
    ## @brief Checks if current position is west of another position.
    #  @details Checks if current longitude is less than another position's, since navigation
    #  convention has negative longitudes for the western hemisphere and positive for the eastern.
    #  @return True if the current longitude is west of the other longitude; false otherwise.
    def west_of(self, other):
        return self.__longitude < other.__longitude
    
    ## @brief Checks if current position is north of another position.
    #  @details Checks if current latitude is more than another position's, since navigation
    #  convention has positive latitudes for the northern hemisphere and negative for the southern.
    #  @return True if the current latitude is north of the other latitude; false otherwise.
    def north_of(self, other):
        return self.__latitude > other.__latitude

    ## @brief Special method to represent a GPosT object as a string.
    #  @return String of the coordinate formatted as [latitude, longitude].
    def __str__(self):
        return '[{}, {}]'.format(self.__latitude, self.__longitude)

    ## @brief Special method to compare two GPosT objects.
    #  @return True if both positions are within 1 km of each other; false otherwise.
    def __eq__(self, other):
        return self.equal(other)

    ## @brief Checks if two GPosT objects are equal.
    #  @return True if the coordinates have less than 1 km of distance between each other.
    def equal(self, other):
        if self.distance(other) <= 1:
            return True

        return False

    ## @brief Calculates distance between two coordinates.
    #  @details Calculates the distance between two GPosT objects 
    #  in km using the Haversine Formula.
    #  @return Float distance between the two positions in km.
    def distance(self, other):
        """
        Haversine Formula:
        a = sin(delta_lat/2)^2 + cos lat1 * cos lat2 * sin(delta_long/2)^2
        c = 2 * atan2(sqrt(a),sqrt(1-a))
        d = R * c

        Cited from: https://www.movable-type.co.uk/scripts/latlong.html
        """

        #Degrees changed to radians to work with math library
        lat1 = math.radians(self.__latitude)
        lat2 = math.radians(other.__latitude)
        delta_lat = math.radians(other.__latitude - self.__latitude)
        delta_long = math.radians(other.__longitude - self.__longitude)

        a = math.sin(delta_lat/2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long/2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        #Average radius of the Earth is 6371 km according to www.movable-type.co.uk
        return 6371 * c

    ## @brief Moves a GPosT object in a specified direction and distance.
    #  @details This function changes the longitude and latitude of a GPosT object towards a
    #  degrees bearing direction over a specified distance in km.
    #  @param bearing Number representing the bearing direction in degrees.
    #  @param distance Number for the distance to travel in km.
    #  @throws ValueError Error if the bearing exceeds 360 degrees
    #  @throws ValueError Error if the distance is negative
    def move(self, bearing, distance):
        if abs(bearing) > 360:
            raise ValueError("ERROR: Bearing cannot exceed 360 degrees")
        if distance < 0:
            raise ValueError("ERROR: Distance travelled cannot be negative")

        """
        Destination Using Bearing and Distance:
        lat2 = asin(sin lat1 * cos d + cos lat1 * sin d * cos b)
        long2 = long1 + atan2(sin b * sin d * cos lat1, cos d - sin lat1 * sin lat2)

        Cited from: https://www.movable-type.co.uk/scripts/latlong.html
        """
        latitude = math.radians(self.__latitude)
        longitude = math.radians(self.__longitude)
        angular_dist = distance / 6371
        bearing = math.radians(bearing)

        new_lat = math.asin(math.sin(latitude) * math.cos(angular_dist) + math.cos(latitude) * math.sin(angular_dist) * math.cos(bearing))
        new_long = longitude + math.atan2(math.sin(bearing) * math.sin(angular_dist) * math.cos(latitude),
                                          math.cos(angular_dist) - math.sin(latitude) * math.sin(new_lat))

        self.__latitude = math.degrees(new_lat)
        self.__longitude = math.degrees(new_long)

    ## @brief Determines the arrival date based on starting point and speed.
    #  @details This function calculates the date of arrival to a specified position given the
    #  starting date and the speed of travel in km/day.
    #  @param position GPosT object for the destination.
    #  @param date DateT object for the starting date.
    #  @param speed Travelling speed in km/day.
    #  @throws ValueError Error if speed is negative.
    #  @throws ZeroDivisionError Error if speed is zero which will cause division by zero.
    #  @return DateT object representing date of arrival.
    def arrival_date(self, position, date, speed):
        if speed < 0:
            raise ValueError("ERROR: Speed cannot be negative")
        if speed == 0:
            raise ZeroDivisionError("ERROR: Speed cannot be zero")
        
        #Distance in km
        distance = self.distance(position)
        #Fractional days are rounded up
        num_of_days = math.ceil(distance/speed)
        return date.add_days(num_of_days)

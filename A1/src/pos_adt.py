## @file pos_adt.py
#  @author Jay Mody
#  @brief ?
#  @date ?

## @brief An ADT ...
class GPosT:

    ## @brief Constructor for GPosT objects.
    #  @
    #  @param lat
    #  @param long
    #  @throws ValueError
    def __init__(self, lat, long):
        if not (-180 <= long and long <= 180):
            raise ValueError("long (longitude) must be between -180 and 180")
        if not (-90 <= lat and lat <= 90)
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
    #  @return ?
    def west_of(self, p):
        return self.__long < p.__long

    ## @brief ?
    #  @return ?
    def north_of(self, p):
        return self.__lat > p.__lat

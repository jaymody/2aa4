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
  def __init__(self, lat, long):
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

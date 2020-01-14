## @file date_adt.py
#  @author Jay Mody
#  @brief ?
#  @date ?

import datetime

# assumptions
# - no leap years
# - months follow this number of day schedule [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# - year may be positive

## @brief An ADT ...
class DateT:

  ## @brief Constructor for DateT objects.
  #  @
  #  @param d
  #  @param m
  #  @param y
  def __init__(self, d, m, y):
    self.__date = datetime.date(y, m, d)

  ## @brief ?
  #  @return ?
  def day(self):
    return self.__date.day
  
  ## @brief ?
  #  @return ?
  def month(self):
    return self.__date.month

  ## @brief ?
  #  @return ?
  def year(self):
    return self.__date.year

  ## @brief ?
  #  @return ?
  def next(self):
    pass

  ## @brief ?
  #  @return ?
  def prev(self):
    pass

  ## @brief ?
  #  @return ?
  def before(self):
    pass

  ## @brief ?
  #  @return ?
  def after(self):
    pass

  ## @brief ?
  #  @return ?
  def equal(self):
    pass

  ## @brief ?
  #  @return ?
  def add_days(self):
    pass

  ## @brief ?
  #  @return ?
  def days_between(self):
    pass

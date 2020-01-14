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
    return self.__date + datetime.timedelta(days=1)

  ## @brief ?
  #  @return ?
  def prev(self):
    return self.__date - datetime.timedelta(days=1)

  ## @brief ?
  #  @return ?
  def before(self, d):
    return self.__date < d

  ## @brief ?
  #  @return ?
  def after(self, d):
    return d < self.__date

  ## @brief ?
  #  @return ?
  def equal(self, d):
    return self.__date == d

  ## @brief ?
  #  @return ?
  def add_days(self, n):
    return self.__date + datetime.timedelta(days=n)

  ## @brief ?
  #  @return ?
  def days_between(self, d):
    # ask about whether to consider negative number of days, days from which to which?
    return abs((self.__date - d).days)

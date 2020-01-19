## @file date_adt.py
#  @author Jay Mody
#  @brief Provides the DateT ADT class for representing dates.
#  @date 15/01/20 (dd/mm/yy)

import datetime

## @brief An ADT that represents a date.
#  @details An ADT for an idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect.
class DateT:

    ## @brief Constructor for DateT objects.
    #  @param d The day of the month (integer from 1-31)
    #  @param m The month of the year (integer from 1-12)
    #  @param y The year
    def __init__(self, d, m, y):
        self.__date = datetime.date(y, m, d)

    ## @brief Gets the day of the month.
    #  @return The day of the month.
    def day(self):
        return self.__date.day

    ## @brief Gets the month of the year.
    #  @return The month of the year.
    def month(self):
        return self.__date.month

    ## @brief Gets the year.
    #  @return The year.
    def year(self):
        return self.__date.year

    ## @brief Returns a date that is 1 day ahead.
    #  @return A DateT object that is 1 day ahead.
    def next(self):
        new_date = self.__date + datetime.timedelta(days=1)
        return DateT(new_date.day, new_date.month, new_date.year)

    ## @brief Returns a date that is 1 day behind.
    #  @return A DateT object that is 1 day behind.
    def prev(self):
        new_date = self.__date - datetime.timedelta(days=1)
        return DateT(new_date.day, new_date.month, new_date.year)

    ## @brief Determines if this date comes before date d.
    #  @param d A DateT object.
    #  @return A boolean that is True if this date comes before date d, else False.
    def before(self, d):
        return self.__date < d.__date

    ## @brief Determines if this date comes after date d.
    #  @param d A DateT object.
    #  @return A boolean that is True if this date comes after date d, else False.
    def after(self, d):
        return self.__date > d.__date

    ## @brief Determines if this date and date d are equal.
    #  @param d A DateT object.
    #  @return A boolean that is True if this date and date d are equal, else False.
    def equal(self, d):
        return self.__date == d.__date

    ## @brief Returns a date that is n days ahead.
    #  @param n An integer representing the number of days to skip ahead.
    #  @return A date that is n days ahead.
    def add_days(self, n):
        new_date = self.__date + datetime.timedelta(days=n)
        return DateT(new_date.day, new_date.month, new_date.year)

    ## @brief Returns the number of days between this day and date d.
    #  @param d A DateT object.
    #  @return The number of days between this day and date d (negative if d comes before this date).
    def days_between(self, d):
        return (d.__date - self.__date).days

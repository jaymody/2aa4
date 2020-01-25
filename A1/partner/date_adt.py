## @file date_adt.py
#  @title date_adt
#  @author Reneuel Dela Cruz
#  @date 2020-01-20

from datetime import date, timedelta

## @brief An ADT for date-related comparisons and calculations.
#  @details This class creates an ADT for date-related comparisons and
#  calculations given the day, month, and year as integers.
class DateT:

    ## @brief Constructor for DateT.
    #  @details Constructor accepts three parameters to initialize the date.
    #  @param d Integer for the day of the month.
    #  @param m Integer representing the month.
    #  @param y Integer representing the year.
    #  @throws ValueError Error if the date entered cannot exist in a calendar, such as negative dates.
    #  @throws TypeError Error if the date values are not integers.
    def __init__(self, d, m, y):
        try:
            """
            Single-line in if statement to check all() parameters for int by Cory Kramer
            Cited from: https://stackoverflow.com/questions/25297272/how-to-make-sure-if-parameter-is-a-list-of-numbers-python
            """
            nums = [d, m, y]
            if not all(isinstance(i, int) for i in nums):
                raise TypeError ("ERROR: Date values can only be integers")
            
            #Creates datetime.date object into self.__date
            self.__date = date(y, m, d)
        except ValueError:
            raise ValueError("ERROR: Entered date values cannot exist together")

    ## @brief This function gets the day of the month.
    #  @return Integer value for the day.
    def day(self):
        return self.__date.day

    ## @brief This function gets the numeric value of the month.
    #  @return Integer value for the month.
    def month(self):
        return self.__date.month

    ## @brief This function returns the numeric year value.
    #  @return Integer value for the year.
    def year(self):
        return self.__date.year

    ## @brief Private function that converts a datetime object into a DateT object.
    #  @param d Datetime object that will be converted from.
    #  @return Converted DateT object.
    def __convert_datetime_to_DateT(self, d):
        return DateT(d.day, d.month, d.year)

    ## @brief Gets the immediate date after the current date in question.
    #  @return DateT object of the day after current date.
    def next(self):
        next_date = self.__date + timedelta(days=1)
        return self.__convert_datetime_to_DateT(next_date)

    ## @brief Gets the date immediately before the current date in question.
    #  @return DateT object of the day before current date.
    def prev(self):
        prev_date = self.__date - timedelta(days=1)
        return self.__convert_datetime_to_DateT(prev_date)

    ## @brief Checks if current date in question is before another date.
    #  @return True if the date is before the other date; false otherwise.
    def before(self, other):
        return self.__date < other.__date

    ## @brief Checks if current date in question is after another date.
    #  @return True if the date is after the other date; false otherwise.
    def after(self, other):
        return self.__date > other.__date

    ## @brief Special method to represent a DateT object as a string.
    #  @return String of the date formatted as DD/MM/YYYY.
    def __str__(self):
        """
        date.strftime(format)
        Cited from: https://docs.python.org/3/library/datetime.html#module-datetime
        """
        return self.__date.strftime("%d/%m/%Y")

    ## @brief Special method to compare if two DateT objects are the same.
    #  @return True if both objects have the same day, month, and year; false otherwise.
    def __eq__(self, other):
        return self.equal(other)

    ## @brief Determines if two DateT objects are equal.
    #  @return True if the objects have the same numeric day, month, and year.
    def equal(self, other):
        return self.__date == other.__date

    ## @brief Adds a specified number of days to a given DateT object.
    #  @param n Integer used to determine the number of days to add.
    #  @throws ValueError Error if added days is a negative number.
    #  @return DateT object after the specified number of days from current date.
    def add_days(self, n):
        if n < 0:
            raise ValueError("ERROR: Days to add cannot be a negative number")

        future_date = self.__date + timedelta(days=n)
        return self.__convert_datetime_to_DateT(future_date)

    ## @brief Calculates the number of days between two DateT objects.
    #  @return Integer of total number of days between the specified dates.
    def days_between(self, other):
        """
        timedelta = date1 - date2
        Cited from: https://docs.python.org/3/library/datetime.html#module-datetime
        """
        return abs((self.__date - other.__date).days)

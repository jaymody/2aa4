## @file Set.py
#  @author Jay Mody
#  @brief Provides generic template module for Sets.
#  @date 08/02/20 (dd/mm/yy)

from Equality import Equality

## @brief A generic module for Sets.
class Set(Equality):

    ## @brief Constructor for Set objects.
    #  @return A list of input elements.
    def __init__(self, s):
        self.__set = set(s)

    ## @brief Adds an element to the set.
    #  @param e The element to add.
    def add(self, e):
        self.__set.add(e)

    ## @brief Removes an element from the set.
    #  @param e The element to remove.
    #  @throws ValueError Thrown if e is not in the set.
    def rm(self, e):
        try:
            self.__set.remove(e)
        except KeyError:
            raise ValueError("Element {} is not in set.".format(e))

    ## @brief Checks if an element exists in the set.
    #  @param e The element to check if it is a member of the set.
    #  @returns A boolean that is True if e is a member of set, else False
    def member(self, e):
        return e in self.__set

    ## @brief Gets the size of the set.
    #  @returns An integer for the number of elements in the set (size).
    def size(self):
        return len(self.__set)

    ## @brief Checks if this set is equivalent to set R.
    #  @param R The set to compare if this set is equal to it.
    def equals(self, R):
        return self.__set == R.__set and self.size() == R.size()

    ## @brief Returns a sequence of the set.
    #  @details The order of the elements in the sequence are not guarenteed to be consitent as a set is unordered.
    #  @returns A list of the elements in set.
    def to_seq(self):
        return list(self.__set)

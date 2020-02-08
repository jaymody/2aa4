## @file Set.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

from Equality import Equality

class Set(Equality):
    def __init__(self, s):
        self.__set = set(s)

    def add(self, e):
        self.__set.add(e)

    def rm(self, e):
        try:
            self.__set.remove(e)
        except KeyError:
            raise ValueError("Element {} is not in set.".format(e))

    def member(self, e):
        return e in self.__set

    def size(self):
        return len(self.__set)

    def equals(self, R):
        return self.__set == R.__set and self.size() == R.size()

    def to_seq(self):
        return list(self.__set)

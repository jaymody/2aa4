## @file Set.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

class Set:
    def __init__(self, sequence):
        self.__set = set(sequence)

    def add(self, element):
        self.__set.add(element)

    def rm(self, element):
        try:
            self.__set.remove(element)
        except KeyError:
            raise ValueError("Element {} is not in set.".format(element))

    def member(self, element):
        return element in self.__set

    def size(self):
        return len(self.__set)

    def to_seq(self):
        return list(self.__set)

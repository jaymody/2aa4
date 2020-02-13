## @file Equality.py
#  @author Jay Mody
#  @brief Provides generic interface module for equality.
#  @date 08/02/20 (dd/mm/yy)

## @brief A generic interface for modules with equality properties.
class Equality:
    ## @brief Determines if this object is equivalent to object T.
    #  @param T The object to be compared with.
    #  @returns A boolean that is True if T is equivalent to this object, else False
    def equals(self, T):
        raise NotImplementedError

    ## @brief Allows equivalency comparisons via ==
    #  @details If A and B are objects that implement Equality, then this function makes A == B the same as A.equals(B).
    #  @returns A boolean that is True if T is equivalent to this object, else False
    def __eq__(self, T):
        return self.equals(T)

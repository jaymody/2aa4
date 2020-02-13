## @file Equality.py
#  @author Jay Mody
#  @brief Provides generic interface module for equality.
#  @date 08/02/20 (dd/mm/yy)

class Equality:
    def equals(self, T):
        raise NotImplementedError

    def __eq__(self, T):
        return self.equals(T)

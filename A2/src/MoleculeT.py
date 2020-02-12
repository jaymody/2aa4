## @file MoleculeT.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

from ChemEntity import ChemEntity
from ChemTypes import ElementT
from Equality import Equality
from ElmSet import ElmSet

class MoleculeT(ChemEntity, Equality):
    def __init__(self, n, e):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a non-zero positive integer")
        if not isinstance(e, ElementT):
            raise ValueError("e must be of type ElementT")
        self.__num = n
        self.__elm = e

    def get_num(self):
        return self.__num

    def get_elm(self):
        return self.__elm

    def num_atoms(self, e):
        return self.__num if e == self.__elm else 0

    def constit_elems(self):
        return ElmSet([self.__elm])

    def equals(self, m):
        return self.get_elm() == m.get_elm() and self.get_num() == m.get_num()

    def __hash__(self):
        return hash((self.__num, self.__elm))

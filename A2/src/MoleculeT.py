## @file MoleculeT.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet

class MoleculeT(ChemEntity, Equality):
    def __init__(self, n, e):
        self.__num = n
        self.__elm = e

    def get_num(self):
        return self.__num

    def get_elm(self):
        return self.__elm

    def num_atoms(self, e):
        return self.__num if e == self.__elm else 0

    def constit_elems(self):
        return ElmSet(self.__elm)

    def equals(self, m):
        return self.get_elm() == m.get_elm() and self.get_num() == m.get_num()

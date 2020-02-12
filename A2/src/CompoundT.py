## @file CompoundT.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet

class CompoundT(ChemEntity, Equality):
    def __init__(self, m):
        self.__c = m

    def get_molec_set(self):
        return self.__c

    def num_atoms(self, e):
        return sum([m.num_atoms(e) for m in self.get_molec_set().to_seq()])

    def constit_elems(self):
        return ElmSet([m.get_elm() for m in self.get_molec_set().to_seq()])

    def equals(self, D):
        return self.get_molec_set().equals(D.get_molec_set())

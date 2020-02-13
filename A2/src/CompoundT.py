## @file CompoundT.py
#  @author Jay Mody
#  @brief Provides module for chemical compounds.
#  @date 08/02/20 (dd/mm/yy)

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet
from MolecSet import MolecSet

import copy

## @brief A module for chemical compounds.
#  @details A module for chemical compounds, defined by a MolecSet.
class CompoundT(ChemEntity, Equality):

    ## @brief Constructor for CompoundT objects.
    #  @param m A MolecSet that defines the compound.
    #  @throws ValueError Thrown if m is not of type MolecSet.
    def __init__(self, m):
        if not isinstance(m, MolecSet):
            raise ValueError("m must be of type MolecSet")
        self.__c = copy.deepcopy(m)

    ## @brief Gets the MolecSet of this compound.
    #  @return m The MolecSet object for this compound.
    def get_molec_set(self):
        return self.__c

    ## @brief Gets the number of atoms of a given type in this molecule.
    #  @param e An ElementT atom to count for in the compound.
    #  @returns The number of atoms of type e in this compound.
    def num_atoms(self, e):
        return sum([m.num_atoms(e) for m in self.get_molec_set().to_seq()])

    ## @brief Gets the set of all elements that constitute this molecule.
    #  @return An ElmSet of all the ElementT's in this entity.
    def constit_elems(self):
        return ElmSet([m.get_elm() for m in self.get_molec_set().to_seq()])

    ## @brief Determines if this compound is equivalent to a compound D.
    #  @details A compound is considered equivalent to another if their MolecSets are equal.
    #  @param The CompoundT object to compare to this one.
    #  @return A boolean that is True if D is equivalent to this compound, else False.
    def equals(self, D):
        return self.get_molec_set().equals(D.get_molec_set())

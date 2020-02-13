## @file MoleculeT.py
#  @author Jay Mody
#  @brief Provides module for molecules consisting of a single element.
#  @date 08/02/20 (dd/mm/yy)

from ChemEntity import ChemEntity
from ChemTypes import ElementT
from Equality import Equality
from ElmSet import ElmSet

## @brief A module for single element molecules.
#  @details A module for molecules that are only made up of a single type of element (e.g. O2, N2, C7).
class MoleculeT(ChemEntity, Equality):

    ## @brief Constructor for MoleculeT objects.
    #  @param n The number of atoms (must be an integer greater than 0)
    #  @param e The single ElementT that makes up this atom.
    #  @throws ValueError Thrown if e is not of type ElementT or n is not within the valid range and type.
    def __init__(self, n, e):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a non-zero positive integer")
        if not isinstance(e, ElementT):
            raise ValueError("e must be of type ElementT")
        self.__num = n
        self.__elm = e

    ## @brief Gets the number of atoms in the molecule.
    #  @returns An integer for the number of atoms in the molecule.
    def get_num(self):
        return self.__num

    ## @brief Gets the element that makes up this molecule.
    #  @returns An ElementT object representing the element that makes up this molecule.
    def get_elm(self):
        return self.__elm

    ## @brief Gets the number of atoms of a given type in this molecule.
    #  @details Note, since MoleculeT objects are comprised of only one element type, the only non-zero value that is returned occurs when e == self.__elm.
    #  @param e An ElementT atom to count in the molecule.
    #  @returns The number of atoms of type e in this molecule.
    def num_atoms(self, e):
        return self.__num if e == self.__elm else 0

    ## @brief Gets the set of all elements that constitute this molecule.
    #  @details Note, since MoleculeT objects are comprised of only one element type, this function returns a Set of size 1 containing just self.__elm.
    #  @return An ElmSet of all the ElementT's in this entity.
    def constit_elems(self):
        return ElmSet([self.__elm])

    ## @brief Determines if this molecule is equivalent to a molecule m.
    #  @details A molecule is considered equivalent to another if they are made up of the same element, and have the same number of atoms.
    #  @param The MoleculeT object to compare to this one.
    #  @return A boolean that is True if m is equivalent to this molecule, else False.
    def equals(self, m):
        return self.get_elm() == m.get_elm() and self.get_num() == m.get_num()

    ## @brief A function that allows MoleculeT objects to be hashed for Sets, Dicts, etc ...
    #  @details The hash for a molecule is a function of its element and number of atoms (so the hash for equivalent molecules would be the same).
    #  @return The hash signature of the molecule.
    def __hash__(self):
        return hash((self.__num, self.__elm))

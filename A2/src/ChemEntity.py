## @file ChemEntity.py
#  @author Jay Mody
#  @brief Provides module interface for chemical entities (molecules, compounds, etc ...).
#  @date 08/02/20 (dd/mm/yy)

## @brief A module interface for chemical entities.
#  @details A module interface for chemical entities like molecules and compounds.
class ChemEntity:

    ## @brief Counts the number of atoms of a specific element.
    #  @param e The ElementT atom to count.
    #  @return An integer for the number of atoms e.
    def num_atoms(self, e):
        raise NotImplementedError

    ## @brief Gets the set of all elements that constitute this entity.
    #  @return An ElmSet of all the ElementT's in this entity.
    def constit_elems(self):
        raise NotImplementedError

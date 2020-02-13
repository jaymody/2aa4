## @file ChemEntity.py
#  @author Jay Mody
#  @brief Provides module interface for chemistry entities (molecules, compounds, etc ...).
#  @date 08/02/20 (dd/mm/yy)

class ChemEntity:
    def num_atoms(self, e):
        raise NotImplementedError

    def constit_elems(self):
        raise NotImplementedError

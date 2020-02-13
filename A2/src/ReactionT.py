## @file ReactionT.py
#  @author Jay Mody
#  @brief todo
#  @date 08/02/20 (dd/mm/yy)

import math
import collections
import numpy as np

class ReactionT:
    def __init__(self, l, r):
        self.__lhs = l
        self.__rhs = r

        # find matrix of elements x compounds
        cols = len(l)+len(r)
        count = collections.defaultdict(lambda: [0]*cols)
        for i, compound in enumerate(l+r):
            for molec in compound.get_molec_set().to_seq():
                count[molec.get_elm()][i] = molec.get_num()

        # check if solution is unique
        rows = len(count)
        if cols-1 > rows:
            raise ValueError("There exists multiple independent solutions for reaction.")

        # linear algebra solve for coefficients
        mat = np.array(list(count.values()))
        lmat = mat[:,:len(l)]
        rmat = -1 * mat[:,len(l):-1]
        x = np.hstack((lmat, rmat))
        y =  mat[:,-1]
        soln = np.linalg.solve(x, y)

        # convert coefficients to whole numbers
        soln = np.append(soln, 1)
        for i in range(1,100):
            whole_soln = i*soln
            if all(int(n) == n for n in whole_soln):
                soln = whole_soln
                break

        self.__lhs_coeff = list(soln[:len(l)])
        self.__rhs_coeff = list(soln[len(l):])

    def get_lhs(self):
        return self.__lhs

    def get_rhs(self):
        return self.__rhs

    def get_lhs_coeff(self):
        return self.__lhs_coeff

    def get_rhs_coeff(self):
        return self.__rhs_coeff

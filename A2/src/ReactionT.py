## @file ReactionT.py
#  @author Jay Mody
#  @brief Provides module for chemical reactions.
#  @date 08/02/20 (dd/mm/yy)

import math
import collections
import numpy as np

## @brief A module to represent and balance chemical reactions.
class ReactionT:

    ## @brief Constructor for a ReactionT object.
    #  @details Constructs a chemical reaction and computes the correct coefficients for the reaction after being balanced by solving a linear system of equations.
    #  @param l A list of CompoundT objects that make up the left hand side of the equation.
    #  @param r A list of CompoundT objects that make up the right hand side of the equation.
    #  @throws ValueError Thrown if there are an infinite number of linearly independent solutions.
    #  @cite https://www.nyu.edu/classes/tuckerman/adv.chem/lectures/lecture_2/node3.html
    #  @cite https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
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

    ## @brief Gets the left hand side of the equation.
    #  @return m A list of CompoundT objects that represent the left hand side of the equation.
    def get_lhs(self):
        return self.__lhs

    ## @brief Gets the right hand side of the equation.
    #  @return m A list of CompoundT objects that represent the right hand side of the equation.
    def get_rhs(self):
        return self.__rhs

    ## @brief Gets the coefficients for each compound on the left hand side of the equation.
    #  @details The compounds and coefficients are index related, so self.get_lhs_coeff()[i] would be the coefficient for compound self.get_lhs()[i].
    #  @return m A list of integers that represent the coefficients for the left hand side of the equation.
    def get_lhs_coeff(self):
        return self.__lhs_coeff

    ## @brief Gets the coefficients for each compound on the right hand side of the equation.
    #  @details The compounds and coefficients are index related, so self.get_rhs_coeff()[i] would be the coefficient for compound self.get_rhs()[i].
    #  @return m A list of integers that represent the coefficients for the right hand side of the equation.
    def get_rhs_coeff(self):
        return self.__rhs_coeff

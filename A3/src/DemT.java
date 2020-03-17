/**
 * @file DemT.java
 * @author Jay Mody
 * @brief Seq2D for Integers.
 * @date 16/03/20 (dd/mm/yy)
 */

package src;

import java.util.ArrayList;

import src.Seq2D;

/**
 * @brief Template module for Seq2D with Integers.
 */
public class DemT extends Seq2D<Integer> {

    /**
     * @brief Constructor for DemT.
     * @param S ArrayList of ArrayList of Integers to initialize the matrix. S and it's first element must be non-empty and each row must have the same number of columns.
     * @param scl Scale value of a cell. Must a non-zero postive real number.
     * @thows IllegalArgumentException Thrown if scl or S are not valid arguments according to the stated restrictions.
     */
    public DemT(ArrayList<ArrayList<Integer>> S, double scl){
        super(S, scl);
    }

    public int total() {
        int total = 0;

        for (ArrayList<Integer> r : this.s)
            for (Integer e : r)
                total += e;

        return total;
    }

    public int max() {
        int max = Integer.MIN_VALUE;

        for (ArrayList<Integer> r : this.s)
            for (Integer e : r)
                if (e > max)
                    max = e;

        return max;
    }

    public boolean ascendingRows() {
        return false;
    }
}

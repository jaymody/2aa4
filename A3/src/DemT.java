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

    /**
     * @brief Calculates the integer total of all the elements.
     * @returns The integer total.
     */
    public int total() {
        int total = 0;

        for (ArrayList<Integer> r : this.s)
            for (Integer e : r)
                total += e;

        return total;
    }

    /**
     * @brief Gets the max value.
     * @returns The mav value.
     */
    public int max() {
        int max = Integer.MIN_VALUE;

        for (ArrayList<Integer> r : this.s)
            for (Integer e : r)
                if (e > max)
                    max = e;

        return max;
    }

    /**
     * @brief Determines of the sum of each row is greater than the sum of the one before it.
     * @returns A boolean thats true if the above holds, else false.
     */
    public boolean ascendingRows() {
        int prev = this.sumRow(0);

        for (int i = 1; i < this.nRow; i++) {
            int cur = this.sumRow(1);
            if (cur < prev)
                return false;
            prev = cur;
        }
        return true;
    }

    private int sumRow(int r) {
        int sum = 0;
        for (int e : this.s.get(r))
            sum += e;
        return sum;
    }
}

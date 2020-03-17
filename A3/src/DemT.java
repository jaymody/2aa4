// @file DemT.py
// @author Jay Mody
// @brief
// @date 16/03/20 (dd/mm/yy)

package src;

import java.util.ArrayList;

import src.Seq2D;

public class DemT extends Seq2D<Integer> {
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
        return 0;
    }
}

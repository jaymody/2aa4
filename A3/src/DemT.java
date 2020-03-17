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
      return 0;
   }
}

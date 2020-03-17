/**
 * @file LanduseMapT.java
 * @author Jay Mody
 * @brief Seq2D for LuT (land use).
 * @date 16/03/20 (dd/mm/yy)
 */

package src;

import java.util.ArrayList;

import src.Seq2D;
import src.LuT;

public class LanduseMapT extends Seq2D<LuT> {
    public LanduseMapT(ArrayList<ArrayList<LuT>> S, double scl){
	    super(S, scl);
    }
}

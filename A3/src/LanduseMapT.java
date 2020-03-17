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

/**
 * @brief Template module for Seq2D with LuT (land use).
 */
public class LanduseMapT extends Seq2D<LuT> {
    /**
     * @brief Constructor for LanduseMapT.
     * @param S ArrayList of ArrayList of LuT to initialize the matrix. S and it's first element must be non-empty and each row must have the same number of columns.
     * @param scl Scale value of a cell. Must a non-zero postive real number.
     * @thows IllegalArgumentException Thrown if scl or S are not valid arguments according to the stated restrictions.
     */
    public LanduseMapT(ArrayList<ArrayList<LuT>> S, double scl){
	    super(S, scl);
    }
}

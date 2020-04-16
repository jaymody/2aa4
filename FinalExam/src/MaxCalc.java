package src;

import java.util.Collections;
import java.util.ArrayList;

public class MaxCalc implements TieHandler {
    @Override
    public double rCalc(ArrayList<Integer> s) {
        return Collections.max(s);
    }
}

package src;

import java.util.Collections;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class Seq1D<T extends Comparable> {
    private ArrayList<T> s;
    public ArrayList<T> sorted;
    private TieHandler tieHandler;

    public Seq1D(ArrayList<T> S) {
        this.s = S;
        this.sorted = new ArrayList<T>(S);
        Collections.sort(this.sorted);
    }

    public Seq1D(ArrayList<T> S, TieHandler t) {
        this.tieHandler = t;
        this.s = S;
        this.sorted = new ArrayList<T>(S);
        Collections.sort(this.sorted);
    }

    public void setTieHandler(TieHandler t) {
        this.tieHandler = t;
    }

    public double rank(T p) throws IllegalArgumentException {
        try {
            ArrayList<Integer> iset = this.indexSet(p, this.sorted);
            return this.tieHandler.rCalc(iset);
        } catch (NoSuchElementException e) {
            throw new IllegalArgumentException("argument p not found in the seq.");
        }
    }

    private ArrayList<Integer> indexSet(T i, ArrayList<T> B) {
        ArrayList<Integer> out = new ArrayList<Integer>();
        for (int n = 0; n < B.size(); n++)
            if (B.get(n).compareTo(i) == 0)
                out.add(n);
        return out;
    }
}

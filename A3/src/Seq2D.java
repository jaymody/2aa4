// @file Seq2D.py
// @author Jay Mody
// @brief
// @date 16/03/20 (dd/mm/yy)

package src;

import java.util.ArrayList;

public class Seq2D<T> {
    private ArrayList<ArrayList<T>> s;
    private double scale;
    private int nRow;
    private int nCol;

    public Seq2D(ArrayList<ArrayList<T>> S, double scl) throws IllegalArgumentException {
        if (scl < 0)
            throw new IllegalArgumentException("scl must be > 0");
        if (S.size() == 0)
            throw new IllegalArgumentException("|S| must be > 0 (S must not be empty)");
        if (S[0].size() == 0)
            throw new IllegalArgumentException("|S[0]| must be > 0 (first row of S may not be empty)");
        for (ArrayList<T> r : S)
            if r.size() != S[0].size()
                throw new IllegalArgumentException("Number of columns in each row must be the same");

        // copy contents to S rather than point to the object
        this.s = new ArrayList<ArrayList<T>>();
        for (ArrayList<T> r : S) {
            ArrayList<T> row = new ArrayList<T>();
            for (T e : r)
                row.add(e);
            this.s.add(row);
        }

        this.scale = scl;
        this.nRow = this.s.size();
        this.nCol = this.s[0].size();
    }

    public void set(PointT p, T v) throws IndexOutOfBoundsException {
        if (!this.validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        this.s[p.row()][p.col()] = v;
    }

    public T get(PointT p) throws IndexOutOfBoundsException {
        if (!validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        return this.s[p.row()][p.col()];
    }

    public int getNumRow() {
        return this.nRow;
    }

    public int getNumCol() {
        return this.nCol;
    }

    public double getScale() {
        return this.scale;
    }

    public int count(T t) {
        int count = 0;

        for (ArrayList<T> r : this.s)
            for (T e : r)
                if (e == t)
                    count++;

        return count;
    }

    public int countRow(T t, int i) {
        if (!this.validRow(i))
            throw new IllegalArgumentException("i must be < nRow");

        count = 0;

        for (T e : this.s[i])
            if (e == t)
                count++;

        return count;
    }

    public double area(T t) {
        return this.count(t) * this.scale;
    }

    private boolean validRow(int n) {
        return 0 <= n && n <= (this.nRow-1);
    }

    private boolean validCol(int n) {
        return 0 <= n && n <= (this.nCol-1);
    }

    private boolean validPoint(PointT p) {
        return this.validRow(p.row()) && this.validCol(p.col());
    }
}

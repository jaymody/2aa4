/**
 * @file Seq2D.java
 * @author Jay Mody
 * @brief Generic Template Module for 2D Matrices.
 * @date 16/03/20 (dd/mm/yy)
 */
package src;

import java.util.ArrayList;

/**
 * @brief Generic template module for 2D matrices.
 */
public class Seq2D<T> {
    protected ArrayList<ArrayList<T>> s;
    protected double scale;
    protected int nRow;
    protected int nCol;

    /**
     * @brief Constructor for Seq2D.
     * @param S ArrayList of ArrayList of T to initialize the matrix. S and it's first element must be non-empty and each row must have the same number of columns.
     * @param scl Scale value of a cell. Must a non-zero postive real number.
     * @thows IllegalArgumentException Thrown if scl or S are not valid arguments according to the stated restrictions.
     */
    public Seq2D(ArrayList<ArrayList<T>> S, double scl) throws IllegalArgumentException {
        if (scl < 0)
            throw new IllegalArgumentException("scl must be > 0");
        if (S.size() == 0)
            throw new IllegalArgumentException("|S| must be > 0 (S must not be empty)");
        if (S.get(0).size() == 0)
            throw new IllegalArgumentException("|S[0]| must be > 0 (first row of S may not be empty)");
        for (ArrayList<T> r : S)
            if (r.size() != S.get(0).size())
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
        this.nCol = this.s.get(0).size();
    }

    public void set(PointT p, T v) throws IndexOutOfBoundsException {
        if (!this.validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        this.s.get(p.row()).set(p.col(), v);
    }

    public T get(PointT p) throws IndexOutOfBoundsException {
        if (!validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        return this.s.get(p.row()).get(p.col());
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

        int count = 0;

        for (T e : this.s.get(i))
            if (e == t)
                count++;

        return count;
    }

    public double area(T t) {
        return this.count(t) * this.scale;
    }

    protected boolean validRow(int n) {
        return 0 <= n && n <= (this.nRow-1);
    }

    protected boolean validCol(int n) {
        return 0 <= n && n <= (this.nCol-1);
    }

    protected boolean validPoint(PointT p) {
        return this.validRow(p.row()) && this.validCol(p.col());
    }
}

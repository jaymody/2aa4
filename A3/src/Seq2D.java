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
     * @param S ArrayList of ArrayList of T to initialize Seq2D. S and it's first element must be non-empty and each row must have the same number of columns.
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

    /**
     * @brief Sets the value at a PointT p.
     * @param p Point in Seq2D to set value.
     * @param v Value to set.
     * @thows IndexOutOfBoundsException Thrown if p is not a valid point in Seq2D.
     */
    public void set(PointT p, T v) throws IndexOutOfBoundsException {
        if (!this.validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        this.s.get(p.row()).set(p.col(), v);
    }

    /**
     * @brief Gets the value at a PointT p.
     * @param p Point in Seq2D to get value.
     * @returns Value at the point.
     */
    public T get(PointT p) throws IndexOutOfBoundsException {
        if (!validPoint(p))
            throw new IllegalArgumentException("Point p must be within the bounds of nRow and nCol");

        return this.s.get(p.row()).get(p.col());
    }

    /**
     * @brief Gets the number of rows in Seq2D.
     * @returns An integer representing the number of rows.
     */
    public int getNumRow() {
        return this.nRow;
    }

    /**
     * @brief Gets the number of columns in Seq2D.
     * @returns An integer representing the number of columns.
     */
    public int getNumCol() {
        return this.nCol;
    }

    /**
     * @brief Gets the scale value of Seq2D.
     * @returns The scale as a double.
     */
    public double getScale() {
        return this.scale;
    }

    /**
     * @brief Gets the number of times t occurs in Seq2D.
     * @param t The value to count in Seq2D.
     * @returns The number of times t occured in Seq2D.
     */
    public int count(T t) {
        int count = 0;

        for (ArrayList<T> r : this.s)
            for (T e : r)
                if (e == t)
                    count++;

        return count;
    }

    /**
     * @brief Gets the number of times t occurs at a specified row.
     * @param t The value to count in the row.
     * @param i Index of the row.
     * @returns The number of times t occured in row i.
     */
    public int countRow(T t, int i) {
        if (!this.validRow(i))
            throw new IllegalArgumentException("i must be < nRow");

        int count = 0;

        for (T e : this.s.get(i))
            if (e == t)
                count++;

        return count;
    }

    /**
     * @brief Calculates the total area occupied by a value t.
     * @param t The value to measure the area.
     * @returns The area as a double.
     */
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

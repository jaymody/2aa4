/**
 * @file PointT.java
 * @author Jay Mody
 * @brief Template Module for 2D Integer Vectors.
 * @date 25/03/20 (dd/mm/yy)
 */

package src;

/**
 * @brief Module for 2D integer vectors (cartesian coordinates).
 */
public class PointT {
    private int r;
    private int c;

    /**
     * @brief Constructor for PointT.
     * @param row "x" or "row" coordinate of the point.
     * @param col "y" or "column" coordinate of the point.
     */
    public PointT(int row, int col) {
        this.r = row;
        this.c = col;
    }

    /**
     * @brief Gets the row value.
     * @returns The row or "x" coordinate.
     */
    public int row() {
        return this.r;
    }

    /**
     * @brief Gets the column value.
     * @returns The columns or "y" coordinate.
     */
    public int col() {
        return this.c;
    }

    /**
     * @brief Gets a new point that is translated in the x direction by dr, and the y direction by dc.
     * @param dr Value to translate by in the x direction.
     * @param dc Value to translate by in the y direction.
     * @returns A new PointT at the translated point.
     */
    public PointT translate(int dr, int dc) {
        return new PointT(this.r + dr, this.c + dc);
    }

    /**
     * @brief Checks if a PointT p is equal to this one (that is there rows and columns values are equal).
     * @param p PointT to compare to this one.
     * @return A boolean thats true if the points are equal, else false.
     */
    public boolean equals(PointT p) {
        return this.r == p.row() && this.c == p.col();
    }
}

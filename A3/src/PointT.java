/**
 * @file PointT.java
 * @author Jay Mody
 * @brief Module for 2D Integer Vectors.
 * @date 16/03/20 (dd/mm/yy)
 */

package src;

/**
 * @brief Module for 2D integer vectors (cartesian coordinates).
 */
public class PointT
{
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

    public int row() {
        return this.r;
    }

    public int col() {
        return this.c;
    }

    public PointT translate(int dr, int dc) {
        return new PointT(this.r + dr, this.c + dc);
    }

    public boolean eq(PointT p) {
        return this.r == p.row() && this.c == p.col();
    }
}

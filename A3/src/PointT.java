// @file PointT.java
// @author Jay Mody
// @brief
// @date 16/03/20 (dd/mm/yy)

package src;

public class PointT
{
    private int r;
    private int c;

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

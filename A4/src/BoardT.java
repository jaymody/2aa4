/**
 * @file BoardT.java
 * @author Jay Mody
 * @brief Template module for the Dots game board.
 * @date 25/03/20 (dd/mm/yy)
 */

package src;

import java.util.Random;
import src.DotT;

/**
 * @brief Template Module for BoardT objects (game boards for Dots).
 */
public class BoardT {
    private DotT[][] board;
    private int nRow;
    private int nCol;
    private int seed;
    private Random r;

    /**
     * @brief Constructor for BoardT.
     * @param height
     * @param width
     * @param seed
     * @throws
     */
    public BoardT(int height, int width, int seed) throws IllegalArgumentException {
        if (height <= 0 || width <= 0)
            throw new IllegalArgumentException("Height and width must be greater than 0.");

        this.nRow = height;
        this.nCol = width;
        this.seed = seed;
        this.r = new Random(this.seed);
        this.board = new DotT[this.nRow][this.nCol];

        this.shuffleBoard();
    }

    /**
     * @brief TODO.
     * @param p
     * @returns TODO.
     */
    public DotT get(PointT p) {
        return this.board[p.row()][p.col()];
    }

    /**
     * @brief TODO.
     * @returns TODO.
     */
    public DotT[][] board() {
        DotT[][] boardcopy = new DotT[this.nRow][this.nCol];
        for (int i = 0; i < this.board.length; i++)
            for (int j = 0; j < this.board[0].length; j++)
                boardcopy[i][j] = this.board[i][j];
        return boardcopy;
    }

    /**
     * @brief TODO.
     * @returns TODO.
     */
    public int height() {
        return this.nRow;
    }

    /**
     * @brief TODO.
     * @returns TODO.
     */
    public int width() {
        return this.nCol;
    }

    /**
     * @brief TODO.
     * @returns TODO.
     */
    public int seed() {
        return this.seed;
    }

    /**
    * @brief Removes point p and let's the dots above it "fall" (shuffles the topmost entry).
    * @returns TODO.
    * @throws IllegalArgumentException Thrown if p is not a valid point in the board.
    */
    public void remove(PointT p) throws IllegalArgumentException {
        if (!validPoint(p))
            throw new IllegalArgumentException("PointT p must be a valid point in the board.");

        for (int i = p.row(); i > 0; i++)
            this.board[i][p.col()] = this.board[i-1][p.col()];
        shufflePoint(new PointT(0, p.col()));
    }

    /**
     * @brief TODO.
     * @returns TODO.
     * @throws IllegalArgumentException Thrown if p is not a valid point in the board.
     */
    public void shuffleBoard() {
        for (int i = 0; i < this.nRow; i++)
            for (int j = 0; j < this.nCol; j++)
                shufflePoint(new PointT(i, j));
    }

    /**
     * @brief TODO.
     * @param p
     * @throws IllegalArgumentException Thrown if p is not a valid point in the board.
     */
    public DotT shufflePoint(PointT p) {
        if (!validPoint(p))
            throw new IllegalArgumentException("PointT p must be a valid point in the board.");

        int x = this.r.nextInt(DotT.class.getEnumConstants().length);
        board[p.row()][p.col()] = DotT.class.getEnumConstants()[x];
        return DotT.class.getEnumConstants()[x];
    }

    /**
     * @brief TODO.
     * @param p
     * @returns TODO.
     */
    public boolean validPoint(PointT p) {
        return validRow(p) && validCol(p);
    }

    /**
     * @brief TODO.
     * @param p
     * @returns TODO.
     */
    private boolean validRow(PointT p) {
        return p.col() >= 0 && p.col() < this.nCol;
    }

    /**
     * @brief TODO.
     * @param p
     * @returns TODO.
     */
    private boolean validCol(PointT p) {
        return p.row() >= 0 && p.row() < this.nRow;
    }

    /**
     * @brief TODO.
     * @returns TODO.
     */
    public String toString() {
        String s = "";
        for (int i = 0; i < this.nRow; i++) {
            for (int j = 0; j < this.nCol; j++)
                s += this.board[i][j] + " ";
            s += "\n";
        }
        return s;
    }
}

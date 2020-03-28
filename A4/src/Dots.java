/**
 * @file Dots.java
 * @author Jay Mody
 * @brief Controller and view of the Dots game.
 * @date 25/03/20 (dd/mm/yy)
 */

package src;

import java.util.Random;
import src.DotT;
import src.BoardT;
import src.ConnectionT;


/**
 * @brief Template Module for BoardT objects (game boards for Dots).
 */
public class Dots {
    public final static int BOARD_HEIGHT = 6;
    public final static int BOARD_WIDTH = 6;
    public final static int DEFAULT_SEED = 1234;
    public final static int DEFAULT_OBJECTIVENUM = 10;
    public final static int DEFAULT_MAXMOVES = 10;


    private BoardT gameboard;
    private int moves;
    private int maxMoves;
    private DotT objectiveColor;
    private int objectiveNum;
    private int seed;

    /**
     * @brief Constructor for Dots.
     */
    public Dots() {
        this.gameboard = new BoardT(BOARD_HEIGHT, BOARD_WIDTH, DEFAULT_SEED);
        this.moves = 0;
        this.seed = DEFAULT_SEED;
        this.objectiveNum = DEFAULT_OBJECTIVENUM;
        this.maxMoves = DEFAULT_MAXMOVES;
        this.newObjective();
    }

    /**
     * @brief Constructor for Dots.
     * @param seed
     */
    public Dots(int seed) {
        this.gameboard = new BoardT(BOARD_HEIGHT, BOARD_WIDTH, DEFAULT_SEED);
        this.moves = 0;
        this.seed = seed;
        this.objectiveNum = DEFAULT_OBJECTIVENUM;
        this.maxMoves = DEFAULT_MAXMOVES;
        this.newObjective();
    }

    /**
     * @brief TODO
     * @param c
     * @throws
     */
    public void move(ConnectionT c) {
    }

    private void newObjective() {
        Random r = new Random(this.seed);

        int x = r.nextInt(DotT.class.getEnumConstants().length);
        this.objectiveColor = DotT.class.getEnumConstants()[x];
    }
}

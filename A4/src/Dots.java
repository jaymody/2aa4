/**
 * @file Dots.java
 * @author Jay Mody
 * @brief Controller and view of the Dots game.
 * @date 25/03/20 (dd/mm/yy)
 */

package src;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

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

    public Dots() {
        this.gameboard = new BoardT(BOARD_HEIGHT, BOARD_WIDTH, DEFAULT_SEED);
        this.seed = DEFAULT_SEED;
    }

    public Dots(int seed) {
        this.gameboard = new BoardT(BOARD_HEIGHT, BOARD_WIDTH, DEFAULT_SEED);
        this.seed = seed;
    }

    public boolean newGame() throws InterruptedException {
        // setup
        Random r = new Random(this.seed);
        int x = r.nextInt(DotT.class.getEnumConstants().length);
        this.objectiveColor = DotT.class.getEnumConstants()[x];
        this.objectiveNum = DEFAULT_OBJECTIVENUM;
        this.maxMoves = DEFAULT_MAXMOVES;
        this.moves = 0;

        // shuffle board
        this.gameboard.shuffleBoard();

        // welcome message
        System.out.println("Welcome to Dots!");
        System.out.println("----------------");
        System.out.println("Enter two integers seperated by a comma at the prompt.");
        System.out.println("Once at least two points are entered, press enter to");
        System.out.println("make the connection between the points. The topleft");
        System.out.println("corner of the board is the point 0,0. Enter q in the");
        System.out.println("prompt to exit the game.");
        System.out.println();

        // main game loop
        while (true) {
            if (step())
                this.moves++;

            // win
            if (this.objectiveNum <= 0) {
                System.out.println("You've won!");
                return true;
            }

            // lose
            if (this.moves > this.maxMoves) {
                System.out.println("Ran out of moves, game over.");
                return false;
            }
        }
    }

    private boolean step() throws InterruptedException {
        System.out.println(
            "objective dot: " + objectiveColor +
            ", dots left: " + objectiveNum +
            ", moves left: " + (this.maxMoves - this.moves)
        );
        System.out.println(this.gameboard);

        Scanner in = new Scanner(System.in);
        ArrayList<PointT> points = new ArrayList<PointT>();
        boolean valid = true;
        int count = 0;

        while (true) {
            if (valid)
                System.out.print("Enter point: ");
            String line = in.nextLine();
            String[] values = line.split(",");

            // enter
            if (line.isEmpty()) {
                // less than 2 points were entered
                if (count < 2) {
                    System.out.print("Must input at least 2 points: ");
                    valid = false;
                    continue;
                }
                System.out.println();
                System.out.println();
                System.out.println("Connection completed, make another connection.");
                break;
            }
            // quit
            if (line.equalsIgnoreCase("q")) {
                this.moves = this.maxMoves;
                throw new InterruptedException("Game quit.");
            }


            // more than 1 comma
            if (values.length != 2) {
                System.out.print("Invalid input: ");
                valid = false;
                continue;
            }

            try {
                int x = Integer.parseInt(values[0]);
                int y = Integer.parseInt(values[1]);

                // point outside board
                PointT p = new PointT(x, y);
                if (!this.gameboard.validPoint(p)) {
                    System.out.print("Point must be inside game board: ");
                    valid = false;
                    continue;
                }

                points.add(p);
            } // input not integers
            catch (NumberFormatException e) {
                System.out.print("Input must be integers: ");
                valid = false;
                continue;
            }

            count++;
            valid = true;
        }

        // make move
        try {
            // not all same color
            if (!this.move(new ConnectionT(points))) {
                System.out.println("Connection did not contain dots of the same color, try again.");
                return false;
            }
        } // connection is invalid
        catch (IllegalArgumentException e) {
            System.out.println(e.getMessage() + ", try again.");
            return false;
        }

        // move was made succsefully
        return true;
    }

    public boolean move(ConnectionT c) {
        DotT color = null;

        for (PointT p : c.pointsSet()) {
            // System.out.println(p);
            if (!this.gameboard.validPoint(p))
                throw new IllegalArgumentException("One of the points in the connection was not a valid point in the board");
            else if (color != null && color != this.gameboard.get(p))
                return false;
            color = this.gameboard.get(p);
        }

        for (PointT p : c.pointsSet()) {
            this.gameboard.remove(p);
            this.objectiveNum--;
        }

        return true;
    }
}

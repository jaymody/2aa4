/**
 * @file TestDots.java
 * @author Jay Mody
 * @brief Test module for the Dots game.
 * @date 25/03/20 (dd/mm/yy)
 */

import java.util.Random;

import src.Dots;

public class Main {
    public static void main(String[] args)  {
        // 3,0
        // 5,0
        //
        // 4,3
        // 4,5
        //
        // 1,2
        // 2,2
        // 2,3

        Dots game = new Dots();
        try {
            game.newGame();
        } catch (InterruptedException e) {

        }

        // DotT[] arr = new DotT[20];
        // Random r = new Random(100);
        // for (int i = 0; i < 20; i++)
        //     arr[i] = DotT.class.getEnumConstants()[r.nextInt(DotT.class.getEnumConstants().length)];
        // for (DotT d : arr)
        //     System.out.println(d);

        // test for remove function
        // BoardT b = new BoardT(4, 4, 100);
        // System.out.println(b);
        // b.remove(new PointT(3,1));
        // System.out.println(b);
        // b.remove(new PointT(0,0));
        // System.out.println(b);
        // b.remove(new PointT(2,3));
        // System.out.println(b);
    }
}

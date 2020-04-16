package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.NoSuchElementException;

public class TestSeq1D {
    Seq1D<Integer> s1;
    Seq1D<Integer> s2;
    Seq1D<Integer> s3;
    Seq1D<Integer> s4;
    Seq1D<Integer> s5;

    @Before
    public void setUp() {
        s1 = new Seq1D<Integer>(new ArrayList<Integer>(Arrays.asList()));
        s2 = new Seq1D<Integer>(new ArrayList<Integer>(Arrays.asList(
            0
        )));
        s3 = new Seq1D<Integer>(new ArrayList<Integer>(Arrays.asList(
            -1,-1,-1,-1,-1,-1,-1,-1
        )));
        s4 = new Seq1D<Integer>(new ArrayList<Integer>(Arrays.asList(
            3,-2,-2,-5,9,9
        )));
        s5 = new Seq1D<Integer>(new ArrayList<Integer>(Arrays.asList(
            3,2,6,5,4,7,1,0,9,8
        )));
    }

    @After
    public void tearDown() {
        s1 = null;
        s2 = null;
        s3 = null;
        s4 = null;
        s5 = null;
    }

    @Test(expected = IllegalArgumentException.class)
    public void testEmptySeqMax() {
        s1.setTieHandler(new MaxCalc());
        s1.rank(2);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testEmptySeqMin() {
        s1.setTieHandler(new MinCalc());
        s1.rank(2);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testIllegalArgumentMax() {
        s2.setTieHandler(new MaxCalc());
        s2.rank(1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testIllegalArgumentMin() {
        s2.setTieHandler(new MinCalc());
        s2.rank(1);
    }

    @Test
    public void testMaxCalc() {
        s2.setTieHandler(new MaxCalc());
        s3.setTieHandler(new MaxCalc());
        s4.setTieHandler(new MaxCalc());
        s5.setTieHandler(new MaxCalc());

        // s2
        assertEquals(0, s2.rank(0), 0);

        // s3
        assertEquals(7, s3.rank(-1), 0);

        // s4
        assertEquals(0, s4.rank(-5), 0);
        assertEquals(2, s4.rank(-2), 0);
        assertEquals(3, s4.rank(3), 0);
        assertEquals(5, s4.rank(9), 0);

        // s5
        assertEquals(0, s5.rank(0), 0);
        assertEquals(1, s5.rank(1), 0);
        assertEquals(2, s5.rank(2), 0);
        assertEquals(3, s5.rank(3), 0);
        assertEquals(4, s5.rank(4), 0);
        assertEquals(5, s5.rank(5), 0);
        assertEquals(6, s5.rank(6), 0);
        assertEquals(7, s5.rank(7), 0);
        assertEquals(8, s5.rank(8), 0);
        assertEquals(9, s5.rank(9), 0);
    }

    @Test
    public void testMinCalc() {
        s2.setTieHandler(new MinCalc());
        s3.setTieHandler(new MinCalc());
        s4.setTieHandler(new MinCalc());
        s5.setTieHandler(new MinCalc());

        // s2
        assertEquals(0, s2.rank(0), 0);

        // s3
        assertEquals(0, s3.rank(-1), 0);

        // s4
        assertEquals(0, s4.rank(-5), 0);
        assertEquals(1, s4.rank(-2), 0);
        assertEquals(3, s4.rank(3), 0);
        assertEquals(4, s4.rank(9), 0);

        // s5
        assertEquals(0, s5.rank(0), 0);
        assertEquals(1, s5.rank(1), 0);
        assertEquals(2, s5.rank(2), 0);
        assertEquals(3, s5.rank(3), 0);
        assertEquals(4, s5.rank(4), 0);
        assertEquals(5, s5.rank(5), 0);
        assertEquals(6, s5.rank(6), 0);
        assertEquals(7, s5.rank(7), 0);
        assertEquals(8, s5.rank(8), 0);
        assertEquals(9, s5.rank(9), 0);
    }
}

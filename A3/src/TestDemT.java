/**
 * Author: S. Smith
 * Revised: Feb 23, 2020
 *
 * Description: Testing DemT Class
 */

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

import src.PointT;
import src.DemT;

public class TestDemT {
    private DemT pos;
    private DemT neg;

    @Before
    public void setUp() {
        ArrayList<ArrayList<Integer>> posarr = new ArrayList<ArrayList<Integer>>();
        posarr.add(new ArrayList<Integer>(Arrays.asList(1,2,3)));
        posarr.add(new ArrayList<Integer>(Arrays.asList(4,5,6)));
        pos = new DemT(posarr, 1.0);

        ArrayList<ArrayList<Integer>> negarr = new ArrayList<ArrayList<Integer>>();
        negarr.add(new ArrayList<Integer>(Arrays.asList(1,2)));
        negarr.add(new ArrayList<Integer>(Arrays.asList(-3,-4)));
        negarr.add(new ArrayList<Integer>(Arrays.asList(5,5)));
        neg = new DemT(negarr, 3.0);
    }

    @After
    public void tearDown() {
        pos = null;
        neg = null;
    }

    @Test
    public void testGetScale() {
        assertEquals(pos.getScale(), 1.0, 0.0);
        assertEquals(neg.getScale(), 3.0, 0.0);
    }

    @Test
    public void testGetNumRow() {
        assertEquals(pos.getNumRow(), 2);
        assertEquals(neg.getNumRow(), 3);
    }

    @Test
    public void testGetNumCol() {
        assertEquals(pos.getNumCol(), 3);
        assertEquals(neg.getNumCol(), 2);
    }

    @Test
    public void testGet() {
        assertEquals((int)pos.get(new PointT(0, 0)), 1);
        assertEquals((int)neg.get(new PointT(2, 1)), 5);
    }

    @Test
    public void testSet() {
        pos.set(new PointT(0, 0), -100);
        neg.set(new PointT(2, 1), 0);

        assertEquals((int)pos.get(new PointT(0, 0)), -100);
        assertEquals((int)neg.get(new PointT(2, 1)), 0);
    }

    @Test
    public void testCount() {
        assertEquals(pos.count(-1), 0);
        assertEquals(pos.count(4), 1);
        assertEquals(neg.count(3), 0);
        assertEquals(neg.count(5), 2);
    }

    @Test
    public void testCountRow() {
        assertEquals(pos.countRow(-1, 0), 0);
        assertEquals(pos.countRow(1, 0), 1);
        assertEquals(neg.countRow(-3, 1), 1);
        assertEquals(neg.countRow(5, 2), 2);
    }

    @Test
    public void testArea() {
        assertEquals(pos.area(1), 1.0, 0.00000001);
        assertEquals(pos.area(7), 0.0, 0.00000001);
        assertEquals(neg.area(5), 6.0, 0.00000001);
        assertEquals(neg.area(6), 0.0, 0.00000001);
    }

    @Test
    public void testTotal() {
        assertEquals(pos.total(), 21);
        assertEquals(neg.total(), 6);
    }

    @Test
    public void testMax() {
        assertEquals(pos.max(), 6);
        assertEquals(neg.max(), 5);
    }

    @Test
    public void testAscendingRows() {
    }
}

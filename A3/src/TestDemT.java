/**
 * @file TestDemT.java
 * @author Jay Mody
 * @brief Unit Tests for DemT.
 * @date 16/03/20 (dd/mm/yy)
 */

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

import src.PointT;
import src.DemT;

public class TestDemT {
    private DemT dem1;
    private DemT dem2;

    @Before
    public void setUp() {
        ArrayList<ArrayList<Integer>> dem1arr = new ArrayList<ArrayList<Integer>>();
        dem1arr.add(new ArrayList<Integer>(Arrays.asList(1,2,3)));
        dem1arr.add(new ArrayList<Integer>(Arrays.asList(4,5,6)));
        dem1 = new DemT(dem1arr, 1.0);

        ArrayList<ArrayList<Integer>> dem2arr = new ArrayList<ArrayList<Integer>>();
        dem2arr.add(new ArrayList<Integer>(Arrays.asList(1,2)));
        dem2arr.add(new ArrayList<Integer>(Arrays.asList(-3,-4)));
        dem2arr.add(new ArrayList<Integer>(Arrays.asList(5,5)));
        dem2 = new DemT(dem2arr, 3.0);
    }

    @After
    public void tearDown() {
        dem1 = null;
        dem2 = null;
    }

    @Test
    public void testGetScale() {
        assertEquals(dem1.getScale(), 1.0, 0.0);
        assertEquals(dem2.getScale(), 3.0, 0.0);
    }

    @Test
    public void testGetNumRow() {
        assertEquals(dem1.getNumRow(), 2);
        assertEquals(dem2.getNumRow(), 3);
    }

    @Test
    public void testGetNumCol() {
        assertEquals(dem1.getNumCol(), 3);
        assertEquals(dem2.getNumCol(), 2);
    }

    @Test
    public void testGet() {
        assertEquals((int)dem1.get(new PointT(0, 0)), 1);
        assertEquals((int)dem2.get(new PointT(2, 1)), 5);
    }

    @Test
    public void testSet() {
        dem1.set(new PointT(0, 0), -100);
        dem2.set(new PointT(2, 1), 0);

        assertEquals((int)dem1.get(new PointT(0, 0)), -100);
        assertEquals((int)dem2.get(new PointT(2, 1)), 0);
    }

    @Test
    public void testCount() {
        assertEquals(dem1.count(-1), 0);
        assertEquals(dem1.count(4), 1);
        assertEquals(dem2.count(3), 0);
        assertEquals(dem2.count(5), 2);
    }

    @Test
    public void testCountRow() {
        assertEquals(dem1.countRow(-1, 0), 0);
        assertEquals(dem1.countRow(1, 0), 1);
        assertEquals(dem2.countRow(-3, 1), 1);
        assertEquals(dem2.countRow(5, 2), 2);
    }

    @Test
    public void testArea() {
        assertEquals(dem1.area(1), 1.0, 0.00000001);
        assertEquals(dem1.area(7), 0.0, 0.00000001);
        assertEquals(dem2.area(5), 6.0, 0.00000001);
        assertEquals(dem2.area(6), 0.0, 0.00000001);
    }

    @Test
    public void testTotal() {
        assertEquals(dem1.total(), 21);
        assertEquals(dem2.total(), 6);
    }

    @Test
    public void testMax() {
        assertEquals(dem1.max(), 6);
        assertEquals(dem2.max(), 5);
    }

    @Test
    public void testAscendingRows() {
    }
}

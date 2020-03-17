/**
 * @file LanduseMapT.java
 * @author Jay Mody
 * @brief Unit Tests for LanduseMapT.
 * @date 16/03/20 (dd/mm/yy)
 */

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

import src.LuT;
import src.LanduseMapT;
import src.PointT;

public class TestLanduseMapT {
    private LanduseMapT map1;

    @Before
    public void setUp() {
        ArrayList<ArrayList<LuT>> map1arr = new ArrayList<ArrayList<LuT>>();
        map1arr.add(new ArrayList<LuT>(Arrays.asList(LuT.R, LuT.C, LuT.R)));
        map1arr.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.A, LuT.A)));
        map1 = new LanduseMapT(map1arr, 1.5);
    }

    @After
    public void tearDown() {
        map1 = null;
    }

    @Test
    public void testGetScale() {
        assertEquals(map1.getScale(), 1.5, 0.0);
    }

    @Test
    public void testGetNumRow() {
        assertEquals(map1.getNumRow(), 2);
    }

    @Test
    public void testGetNumCol() {
        assertEquals(map1.getNumCol(), 3);
    }

    @Test
    public void testGet() {
        assertEquals((LuT)map1.get(new PointT(0, 0)), LuT.R);
    }

    @Test
    public void testSet() {
        map1.set(new PointT(0, 0), LuT.C);

        assertEquals((LuT)map1.get(new PointT(0, 0)), LuT.C);
    }

    @Test
    public void testCount() {
        assertEquals(map1.count(LuT.A), 2);
        assertEquals(map1.count(LuT.C), 1);
    }

    @Test
    public void testCountRow() {
        assertEquals(map1.countRow(LuT.A, 0), 0);
        assertEquals(map1.countRow(LuT.A, 1), 2);
    }

    @Test
    public void testArea() {
        assertEquals(map1.area(LuT.A), 3.0, 0.00000001);
        assertEquals(map1.area(LuT.T), 1.5, 0.00000001);
    }
}

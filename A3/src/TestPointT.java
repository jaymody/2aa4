/**
 * @file TestPointT.java
 * @author Jay Mody
 * @brief Unit Tests for PointT.
 * @date 16/03/20 (dd/mm/yy)
 */

import org.junit.*;
import static org.junit.Assert.*;
import src.PointT;

public class TestPointT {
    private PointT o;
    private PointT p;
    private PointT q;
    private PointT r;

    @Before
    public void setUp() {
        o = new PointT(0,0);
        p = new PointT(2,3);
        q = new PointT(2,-5);
        r = new PointT(-1,-1);
    }

    @After
    public void tearDown() {
        o = null;
        p = null;
        q = null;
        r = null;
    }

    @Test
    public void testRow() {
        assertEquals(o.row(), 0);
        assertEquals(p.row(), 2);
        assertEquals(q.row(), 2);
        assertEquals(r.row(), -1);
    }

    @Test
    public void testCol() {
        assertEquals(o.col(), 0);
        assertEquals(p.col(), 3);
        assertEquals(q.col(), -5);
        assertEquals(r.col(), -1);
    }

    @Test
    public void testTranslate() {
        assertTrue(o.translate(p.row(), p.col()).eq(p));
        assertTrue(p.translate(p.row(), p.col()).eq(new PointT(4, 6)));
        assertTrue(q.translate(r.row(), r.col()).eq(new PointT(1, -6)));
        assertTrue(r.translate(1, 1).eq(o));
    }
}

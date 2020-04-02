/**
 * @file ConnectionT.java
 * @author Jay Mody
 * @brief Template Module to model connections between PointT objects.
 * @date 25/03/20 (dd/mm/yy)
 */


package src;

import java.util.ArrayList;
import java.util.HashSet;

import src.PointT;

/**
 * @brief Template Module for ConnectionT objects that model connections between PointT objects.
 */
public class ConnectionT {
    private ArrayList<PointT> p;
    private HashSet<PointT> s;

    /**
     * @brief Constructor for ConnectionT.
     * @param points A List of PointT objects in order of the connenction path.
     * @throws IllegalArgumentException Thrown if the sequence of points does
     * fails to meet the requirements to be a valid connection. That is,
     * adjacent connections must be a straight vertical or horizontal line.
     */
    public ConnectionT(ArrayList<PointT> points) throws IllegalArgumentException {
        if (points.size() < 2)
            throw new IllegalArgumentException("Number of points must be 2 or more");
        else if (points.get(0).equals(points.get(1)))
            throw new IllegalArgumentException("A connection with only 2 points may not be the same point");

        for (int i = 1; i < points.size(); i++)
            if (!isValid(points.get(i), points.get(i-1)))
                throw new IllegalArgumentException("Adjacent points do not form horizontal/vertical lines");

        this.p = points;
        this.s = new HashSet<PointT>();

        PointT a, b;
        a = points.get(0);
        for (int i = 1; i < points.size(); i++) {
            b = points.get(i);

            int xmin = Math.min(a.row(), b.row());
            int xmax = Math.max(a.row(), b.row());
            int ymin = Math.min(a.col(), b.col());
            int ymax = Math.max(a.col(), b.col());

            for (int x = xmin; x < xmax; x++)
                for (int y = ymin; y < ymax; y++)
                    s.add(new PointT(x, y));

            a = b;
        }
    }

    /**
     * @brief Gets the sequence of points.
     * @returns ArrayList of PointT objects.
     */
    public ArrayList<PointT> pointsSeq() {
        ArrayList<PointT> pointscopy = new ArrayList<PointT>();
        for (PointT point : this.p)
            pointscopy.add(new PointT(point.row(), point.col()));
        return pointscopy;
    }

    /**
     * @brief Gets the HashSet of points in the connection.
     * @returns HashSet of PointT objects.
     */
    public HashSet<PointT> pointsSet() {
        HashSet<PointT> HashSetcopy = new HashSet<PointT>();
        for (PointT point : this.s)
            HashSetcopy.add(new PointT(point.row(), point.col()));
        return HashSetcopy;
    }

    private boolean isValid(PointT a, PointT b) {
        return isHorizontal(a, b) || isVertical(a, b);
    }

    private boolean isHorizontal(PointT a, PointT b) {
        return a.row() == b.row();
    }

    private boolean isVertical(PointT a, PointT b) {
        return a.col() == b.col();
    }
}

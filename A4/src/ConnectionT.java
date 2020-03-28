/**
 * @file ConnectionT.java
 * @author Jay Mody
 * @brief Template Module to model connections between PointT objects.
 * @date 25/03/20 (dd/mm/yy)
 */


package src;

import java.util.ArrayList;
import src.PointT;

/**
 * @brief Template Module for ConnectionT objects that model connections between PointT objects.
 */
public class ConnectionT {
    private ArrayList<PointT> p;

    /**
     * @brief Constructor for ConnectionT.
     * @param points A List of PointT objects in order of the connenction path.
     * @throws IllegalArgumentException Thrown if the sequence of points does
     * fails to meet the requirements to be a valid connection. That is,
     * adjacent connections must be a straight vertical or horizontal line.
     */
    public ConnectionT(ArrayList<PointT> points) throws IllegalArgumentException {
        if (points.size() < 2)
            throw new IllegalArgumentException("Number of points must be 2 or more.");

        for (int i = 1; i < points.size(); i++)
            if (!isValid(points.get(i), points.get(i-1)))
                throw new IllegalArgumentException("Adjacent points do not form horizontal/vertical lines.");

        this.p = points;
    }

    /**
     * @brief Gets the sequence of points.
     * @returns ArrayList of PointT objects.
     */
    public ArrayList<PointT> points() {
        ArrayList<PointT> pointscopy = new ArrayList<PointT>();
        for (PointT point : this.p)
            pointscopy.add(new PointT(point.row(), point.col()));
        return pointscopy;
    }

    private boolean isValid(PointT a, PointT b) {
        return isHorizontal(a, b) && isVertical(a, b);
    }

    private boolean isHorizontal(PointT a, PointT b) {
        return a.row() == b.row();
    }

    private boolean isVertical(PointT a, PointT b) {
        return a.col() == b.col();
    }
}

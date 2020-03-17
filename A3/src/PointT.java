// @file PointT.java
// @author Jay Mody
// @brief
// @date 16/03/20 (dd/mm/yy)

package src;

public class PointT
{

   public PointT(int row, int col)
   {
   }

   public int row()
   {
     return 0;
   }

   public int col()
   {
     return 0;
   }

   public PointT translate(int dr, int dc)
   {
     return new PointT(0, 0);
   }

   public boolean eq(PointT p)
   {
     return false;
   }

}

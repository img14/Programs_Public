public class Backpack
{
   private boolean hasScissors;
   private boolean hasGlue;
   private boolean hasPaper;
   private int numBinders;
   private String color;
   private String owner;
   
   public Backpack()
   {
      hasScissors = false;
      hasGlue = false;
      hasPaper = false;
      numBinders = 0;
      color = "Black";
      owner = "No One :(";
   }
   public Backpack(boolean hS, boolean hG, boolean hP, int nB, String c, String o)
   {
      hasScissors = hS;
      hasGlue = hG;
      hasPaper = hP;
      numBinders = nB;
      color = c;
      owner = o;
   }
   public boolean scissors()
   {
      return hasScissors;
   }
   public boolean glue()
   {
      return hasGlue;
   }
   public boolean paper()
   {
      return hasPaper;
   }
   public int binders()
   {
      return numBinders;
   }
   public String col()
   {
      return color;
   }
   public String ownedBy()
   {
      return owner;
   }
   public void setScissors(boolean s)
   {
      hasScissors = s;
   }
   public void setGlue(boolean g)
   {
      hasGlue = g;
   }
   public void setPaper(boolean p)
   {
      hasPaper = p;
   }
   public void setBinders(int b)
   {
      numBinders = b;
   }
   public void setColor(String c)
   {
      color = c;
   }
   public void setOwner(String o)
   {
      owner = o;
   }
}
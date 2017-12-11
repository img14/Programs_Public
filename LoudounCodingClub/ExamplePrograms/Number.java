public class Number
{
   private int digitOne;
   private int digitTwo;
   private int digitThree;
   private int digitFour;
   private int digitFive;
   private boolean isNegative;
   
   public Number(boolean neg, int d1, int d2, int d3, int d4, int d5)
   {
      digitOne = d1;
      digitTwo = d2;
      digitThree = d3;
      digitFour = d4;
      digitFive = d5;
      isNegative = neg;
   }
   public int number()
   {
      //Don't worry about this part yet. 
      //Just know that classes can have methods inside of them
      //This method is returning the full number.
      //Look through it and see if you understand how.
      String temp = "";
      if(isNegative)
      {
         temp = temp + "-";
      } 
      temp = temp + "" + digitOne + digitTwo + digitThree + digitFour + digitFive;
      int num = Integer.parseInt(temp);
      return num;
   }
}
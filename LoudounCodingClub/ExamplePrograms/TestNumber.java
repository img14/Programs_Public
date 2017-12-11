//Test your number class

public class TestNumber
{
   public static void main(String[] args)
   {
      //Your number class should be called Number.java. If it isn't, replace "Number" with whatever 
      //you named yours. 
      Number caseOne = new Number(false, 1, 2, 3, 4, 5);
      Number caseTwo = new Number(true, 6, 7, 8, 9, 0);
      Number caseThree = new Number(true, 2, 4, 5, 8, 1);
      Number caseFour = new Number(false, 1, 7, 3, 2, 9);
      Number caseFive = new Number(true, 7, 3, 2, 2, 6);
      
      System.out.println("caseOne should be 12345. It is: " + caseOne.number());
      System.out.println("caseTwo should be -67890. It is: " + caseTwo.number());
      System.out.println("caseThree should be -24581. It is: " + caseThree.number());
      System.out.println("caseFour should be 17329. It is: " + caseFour.number());
      System.out.println("caseFive should be -73226. It is: " + caseFive.number());

   }
}
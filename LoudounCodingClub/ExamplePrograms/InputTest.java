import java.util.*;
import javax.swing.JOptionPane;

public class InputTest
{
   public static void main(String[] args)
   {
      //There are two main ways to get user input from a program:
      
      //Using a Scanner:
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter your name:");
      String name = scan.nextLine();
      System.out.println("Hello, " + name);
      
      //Using JOptionPane (a built in java class, you have to import it at the top):
      String name2 = JOptionPane.showInputDialog(null, "Enter your name:");
      JOptionPane.showMessageDialog(null, "Hello, " + name2);
   }
}
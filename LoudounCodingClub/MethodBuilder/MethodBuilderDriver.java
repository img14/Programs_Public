import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class MethodBuilderDriver
{
   public static void main(String args[])
   {
      JOptionPane.showMessageDialog(null, "Hello! Welcome to Method Builder.");
      JOptionPane.showMessageDialog(null, "Enter the method header as specified.");
      JOptionPane.showMessageDialog(null, "Name each method \"method\".");
      JOptionPane.showMessageDialog(null, "Name the arguments whatever you want, just make sure they are in the right order.");
      int n = 0;
      try
      {
      n = Integer.parseInt(JOptionPane.showInputDialog(null, "How many times would you like to practice?"));
      }
      catch(NumberFormatException e)
      {
         JOptionPane.showMessageDialog(null, "That wasn't a number! I'm getting out of here.");
         System.exit(0);
      }
      JOptionPane.showMessageDialog(null, "Good luck!");
      JFrame frame = new JFrame("Method Builder");
      frame.setSize(1000,100);
      frame.setLocation(100,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new MethodBuilderPanel(n));
      frame.setVisible(true);
   }
}
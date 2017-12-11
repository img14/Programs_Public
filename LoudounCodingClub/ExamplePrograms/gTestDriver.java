import java.awt.image.*; 
import javax.swing.event.*;
import javax.swing.JFrame;
public class gTestDriver
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Test");
      frame.setSize(800, 800);
      frame.setLocation(0, 0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new gPanel());
      frame.setVisible(true);
   }
}
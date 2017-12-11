import java.awt.*;
import java.awt.event.*;
import java.awt.image.*; 
import javax.swing.event.*;
import javax.swing.JFrame;


public class DriverCalc
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Calc");
      frame.setSize(200, 200);
      frame.setLocation(0, 0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new calcPanel());
      frame.setVisible(true);
   
   
   }
}
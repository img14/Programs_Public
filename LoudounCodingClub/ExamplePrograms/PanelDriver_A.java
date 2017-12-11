import java.awt.image.*; 
import javax.swing.event.*;
import javax.swing.JFrame;

public class PanelDriver_A
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Test");
      frame.setSize(300, 300);
      frame.setLocation(0, 0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new PanelTimer_A());
      frame.setVisible(true);
   }
}
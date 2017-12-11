import javax.swing.JFrame;

public class UI_Test
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Test");
      frame.setSize(300, 300);
      frame.setLocation(0, 0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new GUI());
      frame.setVisible(true);
   }
}
import javax.swing.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.awt.color.*;
import javax.swing.*;
import java.io.*;
import javax.swing.JOptionPane;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*; 
import javax.swing.event.*;
public class PanelTimer extends JPanel
{
   
   private BufferedImage myImage;
   private Graphics myBuffer;
   private Timer t;
   public PanelTimer()
   {
      myImage =  new BufferedImage(700, 700, BufferedImage.TYPE_INT_RGB); //covers the size of the entire frame
      myBuffer = myImage.getGraphics();
      myBuffer.setColor(Color.BLACK);
      myBuffer.fillRect(0, 0, 700,700);
   
        
      t = new Timer(1, new Listener());
      t.start();
   }
   public void paintComponent(Graphics g)
   {
      g.drawImage(myImage, 0, 0, getWidth(), getHeight(), null);
   }
   private class Listener implements ActionListener
   {
      private int x = 0;
      public void actionPerformed(ActionEvent e)
      {
         myBuffer.setColor(Color.BLACK);    //cover the old rectangle 
         myBuffer.fillRect(0,0,700,700);
         
         drawR(x);
         if(x < 700)
         {
            x += 5;
         }
         else
         {
            x = 0;
         }
      
         repaint();
      }
      public void drawR(int x)
      {
         myBuffer.setColor(Color.BLUE);
         myBuffer.fillRect(x, 200, 100,30);
      }
   }
   
}
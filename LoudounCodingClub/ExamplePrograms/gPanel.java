import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;

public class gPanel extends JPanel
{
   private int x1 = 0;
   private int y1 = 0;
   private int x2 = 15;
   private int y2 = 0;
   private int x3 = 0;
   private int y3 = 15;
   private int x4 = 15;
   private int y4 = 15;
   private int size = 800;
   private int[][] board;
   private BufferedImage myImage;
   private Graphics myBuffer;
   private Timer t;
   
   public gPanel()
   {        
      t = new Timer(1, new Listener());
      t.start();
      board = new int[size][size];
      //setFocusable(true);
      
      for(int x = 0; x< board.length; x++)
      {
         for(int y = 0; y<board.length; y++)
         {
            board[x][y] = 0;
         }
      }
   }  
   public void paint()
   {
            
      myImage =  new BufferedImage(size, size, BufferedImage.TYPE_INT_RGB);
      myBuffer = myImage.getGraphics();
      for(int x = 0; x<board.length; x++)
      {
         for(int y = 0; y<board[x].length; y++)
         {
            if(board[x][y] == 1)
            {
               myBuffer.setColor(Color.GREEN);
            }
            else if(board[x][y] == 2)
            {  
               myBuffer.setColor(Color.RED);
            }
            else if(board[x][y] == 0)
            {  
               myBuffer.setColor(Color.BLACK);
            }
            myBuffer.fillRect(x, y, 1, 1);            
         }
      }
      myBuffer.setColor(Color.BLACK);
   
      repaint();
   }
   private class Listener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         for(int x = 0; x<board.length; x++)
         {
            for(int y = 0; y<board[x].length; y++)
            {
               int col = (int)(Math.random() * 2 + 1);
               board[x][y] = col;
            }
         }
         paint();
      }
   }
   public void paintComponent(Graphics g)
   {
      g.drawImage(myImage, 0, 0, getWidth(), getHeight(), null);
   }
}
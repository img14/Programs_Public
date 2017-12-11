import javax.swing.*;
import java.awt.color.*;
import javax.swing.*;
import java.io.*;
import javax.swing.JOptionPane;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*; 
import javax.swing.event.*;
import java.util.ArrayList;
public class PanelTimer_A extends JPanel
{
   private static BufferedImage myImage;
   private static Graphics myBuffer;
   private Timer t;
   private Timer t2;
   private Timer t3;
   private Timer t4;
   private int count;
  // private int sizex = 25;
  // private int sizey = 25;
   private int xPos = 10;
   private int yPos = 10;
   private int rPos = 10;
   private int cPos = 10;
   private int size = 25;
   private int direction = 1;
   private static int[][] matrix = new int[28][28];
   private static ArrayList<Integer> xs = new ArrayList<Integer>();
   private static ArrayList<Integer> ys = new ArrayList<Integer>();
   public PanelTimer_A()
   {
      addKeyListener(new Key());
      myImage =  new BufferedImage(700, 700, BufferedImage.TYPE_INT_RGB); //covers the size of the entire frame
      myBuffer = myImage.getGraphics();
      myBuffer.setColor(Color.BLACK);
      myBuffer.fillRect(0, 0, 700,700);
      t = new Timer(250, new Listener());
      t.start();
      t2 = new Timer(5000, new Listener2());
      t2.start();
      setFocusable(true);
      for(int x = 0; x < 28; x++)
      {
         for(int y =0; y < 28; y++)
         {
            matrix[x][y] = 0;
         }
      }
      int xRand = (int)(Math.random()*28);
      int yRand = (int)(Math.random()*28);
         
      int xRand2 = (int)(Math.random()*28);
      int yRand2 = (int)(Math.random()*28);
         
      matrix[xRand][yRand] = 1;
      matrix[xRand2][yRand2] = 2;
         
      t3 = new Timer(10000, new Listener3(xRand, yRand));
      t3.start();
      t4 = new Timer(10000, new Listener3(xRand2, yRand2));
      t4.start();
      paint();
      paint();
   }

   public void paint()
   {
      myImage =  new BufferedImage(700, 700, BufferedImage.TYPE_INT_RGB); //covers the size of the entire frame
      myBuffer = myImage.getGraphics();
      for(int i = 0; i<matrix.length; i++)
      {
         for(int j = 0; j<matrix[0].length; j++)
         {
            if(matrix[i][j] == 0)
            {
               myBuffer.setColor(Color.BLACK);
            }
            else if(matrix[i][j] == 1)
            {
               myBuffer.setColor(Color.GREEN);
            }
            else if(matrix[i][j] == 2)
            {
               myBuffer.setColor(Color.YELLOW);
            }
            else if(matrix[i][j] == 3)
            {
               myBuffer.setColor(Color.RED);
            }
            myBuffer.fillRect(i*25, j*25, 25, 25);
         }
      }
      repaint();
   }

   public void paintComponent(Graphics g)
   {
      g.drawImage(myImage, 0, 0, getWidth(), getHeight(), null);
   }

   private class Key extends KeyAdapter
   {
      public void keyPressed(KeyEvent e)
      {
         if(e.getKeyCode() == KeyEvent.VK_UP)
         {
            direction = 1;
         }
         else if(e.getKeyCode() == KeyEvent.VK_DOWN)
         {
            direction = 2;
         }
         else if(e.getKeyCode() == KeyEvent.VK_LEFT)
         {
            direction = 3;
         }
         else if(e.getKeyCode() == KeyEvent.VK_RIGHT)
         {
            direction = 4;
         }
         paint();
      
      }
   }
         
   private class Listener2 implements ActionListener
   
   {
      public void actionPerformed(ActionEvent e)
      {
         int xRand = (int)(Math.random()*28);
         int yRand = (int)(Math.random()*28);
         
         int xRand2 = (int)(Math.random()*28);
         int yRand2 = (int)(Math.random()*28);
         
         if(matrix[xRand][yRand] != 3)
         {
         matrix[xRand][yRand] = 1;
         }
         if(matrix[xRand2][yRand2] != 3)
         {
         matrix[xRand2][yRand2] = 1;
         }
         
         t3 = new Timer(10000, new Listener3(xRand, yRand));
         t3.start();
         t4 = new Timer(10000, new Listener3(xRand2, yRand2));
         t4.start();
         paint();
      }
   }
   private class Listener3 implements ActionListener
   
   {
      int myX;
      int myY;
      private Listener3(int x, int y)
      {
         myX = x;
         myY = y;
      }
      public void actionPerformed(ActionEvent e)
      {
         if(matrix[myX][myY] == 1 || matrix[myX][myY] == 2)
         {
            matrix[myX][myY] = 0;
         }
      }
   }
   private class Listener implements ActionListener
   
   {
      public void actionPerformed(ActionEvent e)
      {
         count++;
         if(count % 5 == 0)
         {
            size += 25;
         }
         int x = xPos;
         int y = yPos;
         if(direction == 1)
         {
           yPos--;
         }
         else if(direction == 2)
         {
            yPos++;
         }
         else if(direction == 3)
         {  
            xPos--; 
         }
         else if(direction == 4)
         {  
            xPos++;
         }
         if (matrix[xPos][yPos] == 3)
         {
            JOptionPane.showMessageDialog(null, "Game Over");
            System.exit(0);
         }
         if(xPos >= 27 || yPos >= 27 || xPos <= 0 || yPos <= 0)
         {
            JOptionPane.showMessageDialog(null, "Game Over");
            System.exit(0);
         }
         if (matrix[xPos][yPos] == 1)
         {
            size += 100;
         }
         if (matrix[xPos][yPos] == 2)
         {
            size = 25;
         }
         matrix[xPos][yPos] = 3;
         xs.add(xPos);
         ys.add(yPos);
         while(xs.size() > size/25 && ys.size() > size/25)
         {
            int tx = xs.remove(0);
            int ty = ys.remove(0);
            matrix[tx][ty] = 0;
               //System.out.println("out, x=" + tx + ", y=" + ty);
         }
         paint();
      
      }
   }
}
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

public class TimerTestGraphics
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Timer Test Graphics");
      frame.setSize(700, 700);
      frame.setLocation(0, 0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new PanelTimer());
      frame.setVisible(true);
   
   
   }
}
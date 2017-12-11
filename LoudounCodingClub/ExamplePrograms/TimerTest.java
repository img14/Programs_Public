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

public class TimerTest
{
   public static void main(String[] args)
   {
      Timer t = new Timer(500, new Listener());
      t.start();
   }
}
class Listener implements ActionListener
{
   public void actionPerformed(ActionEvent e)
   {
      System.out.println("Hi!");
   }
}
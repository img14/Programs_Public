import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class GUI extends JPanel
{
   private JButton button;
   private JButton button1;
   private JButton button2;
   private JButton button3;
   private JButton button4;
   private JButton button5;
   private JButton button6;
   private JButton button7;
   private JLabel label;
   public GUI()
   {
   setLayout(new GridLayout(3,3));
      button = new JButton("test");
      button.addActionListener(new Listener());
      add(button);
       button1 = new JButton("test");
      button1.addActionListener(new Listener());
      add(button1);
       button2 = new JButton("test");
      button2.addActionListener(new Listener());
      add(button2);
       button3 = new JButton("test");
      button3.addActionListener(new Listener());
      add(button3);
       button4 = new JButton("test");
      button4.addActionListener(new Listener());
      add(button4);
       button5 = new JButton("test");
      button5.addActionListener(new Listener());
      add(button5);
       button6 = new JButton("test");
      button6.addActionListener(new Listener());
      add(button6);
       button7 = new JButton("test");
      button7.addActionListener(new Listener());
      add(button7);
      
      label = new JLabel("");
      add(label);
    
   }
   private class Listener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         label.setText("Hello World!");
      }
   }
 }
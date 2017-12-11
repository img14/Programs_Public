import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class calcPanel extends JPanel
{
   private JButton b1;
   private JButton b2;
   private JButton b3;
   private JButton b4;
   public calcPanel()
   {
      setLayout(new GridLayout(2,2));
      Listener1 l = new Listener1();
      b1 = new JButton();
      b1.addActionListener(l);
      b2 = new JButton();
      b2.addActionListener(l);
      b3 = new JButton();
      b3.addActionListener(l);
      b4 = new JButton();
      b4.addActionListener(l);
      add(b1);
      add(b2);
      add(b3);
      add(b4);
      b1.setText("1");
      b2.setText("2");
      b3.setText("3");
      b4.setText("4");
   }
   private class Listener1 implements ActionListener
   {
      private int n1;
      private String o;
      private int n2;
      private int count = 0;
      public void actionPerformed(ActionEvent e)
      {//Beginning of actionPerformed
         if(e.getSource() == b1)
         {
                     
            if(count == 0)
            {
               n1 = 1;
               b1.setText("+");
               b2.setText("-");
               b3.setText("*");
               b4.setText("/");
               count++;
            }
            else if(count == 1)
            {
               o = "+";
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
               count++;
            }
            else if(count == 2)
            {
               n2 = 1;
               b1.setVisible(false);
               b1.setEnabled(false);
               b2.setVisible(false);
               b2.setEnabled(false);
               b3.setVisible(false);
               b3.setEnabled(false);
               b4.setText("=");
               count++;
            }
            else if(count == 3)
            {
               if(o == "+")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1+n2));
               } 
               else if(o == "-")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1-n2));
               } 
               else if(o == "*")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1*n2));
               }
               else if(o == "/")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1/n2));
               }
               count++;
            }
            else if(count == 4)
            {
               count = 0; 
               n1 = 0; 
               n2 = 0;
               o = "";
               b1.setEnabled(true);
               b1.setVisible(true);
               b2.setEnabled(true);
               b2.setVisible(true);
               b3.setEnabled(true);
               b3.setVisible(true);
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
            }
         
         
         }
         else if(e.getSource() == b2)
         {
         
            if(count == 0)
            {
               n1 = 2;
               b1.setText("+");
               b2.setText("-");
               b3.setText("*");
               b4.setText("/");
               count++;
            }
            else if(count == 1)
            {
               o = "-";
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
               count++;
            }
            else if(count == 2)
            {
               n2 = 2;
               b1.setVisible(false);
               b1.setEnabled(false);
               b2.setVisible(false);
               b2.setEnabled(false);
               b3.setVisible(false);
               b3.setEnabled(false);
               b4.setText("=");
               count++;
            }
            else if(count == 3)
            {
               if(o == "+")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1+n2));
               } 
               else if(o == "-")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1-n2));
               } 
               else if(o == "*")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1*n2));
               }
               else if(o == "/")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1/n2));
               }
               count++;
            }
            else if(count == 4)
            {
               count = 0; 
               n1 = 0; 
               n2 = 0;
               o = "";
               b1.setEnabled(true);
               b1.setVisible(true);
               b2.setEnabled(true);
               b2.setVisible(true);
               b3.setEnabled(true);
               b3.setVisible(true);
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
            }
         
            
         
         }
         else if(e.getSource() == b3)
         {
          
            if(count == 0)
            {
               n1 = 3;
               b1.setText("+");
               b2.setText("-");
               b3.setText("*");
               b4.setText("/");
               count++;
            
            }
            else if(count == 1)
            {
               o = "*";
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
               count++;
            
            }
            else if(count == 2)
            {
               n2 = 3;
               b1.setVisible(false);
               b1.setEnabled(false);
               b2.setVisible(false);
               b2.setEnabled(false);
               b3.setVisible(false);
               b3.setEnabled(false);
               b4.setText("=");
               count++;
            
            }
            else if(count == 3)
            {
            
               if(o == "+")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1+n2));
               } 
               else if(o == "-")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1-n2));
               } 
               else if(o == "*")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1*n2));
               }
               else if(o == "/")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1/n2));
               }
               count++;
            
            }
            else if(count == 4)
            {
               count = 0; 
               n1 = 0; 
               n2 = 0;
               o = "";
               b1.setEnabled(true);
               b1.setVisible(true);
               b2.setEnabled(true);
               b2.setVisible(true);
               b3.setEnabled(true);
               b3.setVisible(true);
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
            }         
         }
         else if(e.getSource() == b4)
         {
            if(count == 0)
            {
               n1 = 4;
               b1.setText("+");
               b2.setText("-");
               b3.setText("*");
               b4.setText("/");
               count++;
            }
            else if(count == 1)
            {
               o = "/";
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
               count++;
            }
            else if(count == 2)
            {
               n2 = 4;
               b1.setVisible(false);
               b1.setEnabled(false);
               b2.setVisible(false);
               b2.setEnabled(false);
               b3.setVisible(false);
               b3.setEnabled(false);
               b4.setText("=");
               count++;
            }
            else if(count == 3)
            {
               if(o == "+")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1+n2));
               } 
               else if(o == "-")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1-n2));
               } 
               else if(o == "*")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1*n2));
               }
               else if(o == "/")
               {
                  System.out.println(""+ n1 + o + n2 + "=" + (n1/n2));
               }
               b4.setText("Reset");
               count++;
            }
            else if(count == 4)
            {
               count = 0; 
               n1 = 0; 
               n2 = 0;
               o = "";
               b1.setEnabled(true);
               b1.setVisible(true);
               b2.setEnabled(true);
               b2.setVisible(true);
               b3.setEnabled(true);
               b3.setVisible(true);
               b1.setText("1");
               b2.setText("2");
               b3.setText("3");
               b4.setText("4");
            }
         
         }
      }
   }
}
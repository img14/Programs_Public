import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.JOptionPane;

public class MethodBuilderPanel extends JPanel
{
   private String[] returnTypes = {"nothing", "int", "String", "double", "bool", "Object"};
   private String[] scopeTypes = {"public", "private"};
   private String[] argTypes = {"int", "String", "double", "bool", "Object"};
   private String[] statOrNot = {" class", ""};
   JLabel title;
   JTextField box;
   JLabel message;
   String method;
   String headerNoArgs;
   String argss;
   int numTries;
   int numTriesSorryThisIsAVariable;
   boolean firstTry;
   int numFirstTry;
   public MethodBuilderPanel(int nt)
   {
      numTries = nt;
      numTriesSorryThisIsAVariable = nt;
      
      setLayout(new BorderLayout());
      setBackground(Color.BLACK);
      
      title = new JLabel("");
      title.setFont(new Font("Sans Serif", Font.BOLD, 16));
      title.setForeground(Color.WHITE);
      add(title, BorderLayout.NORTH);
      
      box = new JTextField(50);
      box.setFont(new Font("Courier",Font.PLAIN, 20));
      box.setForeground(Color.BLUE.darker());
      add(box, BorderLayout.CENTER);
            
      JButton b1 = new JButton("Submit");
      b1.addActionListener(new Listener());
      add(b1, BorderLayout.EAST);
      
      message = new JLabel(" ");
      message.setFont(new Font("Sans Serif", Font.BOLD, 18));
      add(message, BorderLayout.SOUTH);
      
      displayPrompt();
   }
   public void displayPrompt()
   {
      firstTry = true;
      int numArgs =  (int)(Math.random() * 5);
      
      String scope = scopeTypes[(int)(Math.random()*scopeTypes.length)];
      String stat = statOrNot[(int)(Math.random()*statOrNot.length)];
      String ret = returnTypes[(int)(Math.random()*returnTypes.length)]; 
      
      String statWord = (stat == " class") ? " static" : "";
      String retWord = (ret == "nothing") ? "void" : ret;     
      
      method = "Create a " + scope + stat + " method that returns " + ret
         + " and takes " + numArgs + " arguments: ";
       
      headerNoArgs = scope + statWord + " " + retWord + " method";
       
      argss = "";
      for(int i = 0; i<numArgs; i++)
      {
         argss += argTypes[(int)(Math.random()*argTypes.length)];
         if(i < numArgs - 1)
            argss += ", ";
      }
      
      method += argss;
      title.setText(method);
   }
   private class Listener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         String submission = box.getText();
         String regex = "^.*?(public|private|static|void|int|double|bool|object|String).*$";
         if(submission.equals(" ") || submission.equals(""))
         {
            firstTry = false;
            message.setForeground(Color.PINK);
            message.setText("At least give it a try!");
         }
         else if(submission.contains(";"))
         {
            firstTry = false;
            message.setForeground(Color.MAGENTA);
            message.setText("Remember, don't use a semicolon in a method header.");
         }
         else if(!submission.matches(regex))
         {
            message.setForeground(Color.YELLOW);
            message.setText("I don't think that's proper programming syntax.");
         }
         else
         {
            if(submission.contains(headerNoArgs))
            {
               submission = submission.replaceFirst(headerNoArgs, "");
               submission = submission.replaceAll("^[(),]+", "").replaceAll("[(),]+$", "");
               String[] ar = submission.split(" ");
               String checkArgs = "";
               for(int i = 0; i<ar.length; i++)
               {
                  if(i%2 == 0)
                     checkArgs += (ar[i]);
               }
               argss = argss.replaceAll("[, ]+","").replaceAll("[, ]+$", "");
               checkArgs = checkArgs.replace(" ","");
               boolean b = checkArgs.equals(argss);
               if(!b && checkArgs.equalsIgnoreCase(argss))
               {
                  firstTry = false;
                  message.setForeground(Color.ORANGE);
                  message.setText("Not exactly, but very close. Be careful of capitalization.");
               }
               else if(checkArgs.equals(argss))
               {
                  message.setForeground(Color.GREEN);
                  message.setText("Good job!");
                  if(firstTry)
                  {
                     numFirstTry++;
                  }
                  if(numTries > 1)
                  {
                     numTries--;
                     box.setText("");
                     displayPrompt(); 
                  }
                  else
                  {
                     message.setText(" ");
                     title.setText(" ");
                     box.setText("");
                     JOptionPane.showMessageDialog(null, "Good job! Percent Correct on first try: " + (numFirstTry*100/numTriesSorryThisIsAVariable) + "%");
                     System.exit(0);
                  }
               }
               else
               {
                  firstTry = false;
                  message.setForeground(Color.ORANGE);
                  message.setText("You don't have the arguments quite right! Try again.");
               }
            }
            else
            {
               firstTry = false;
               message.setForeground(Color.RED);
               message.setText("Not quite, try again!");
            } 
         }    
      }
   }
}
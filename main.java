import java.util.*;
import java.math.*;

public class Main{
 public static void main(String[] args){
  while (true){
   try{
    Scanner in = new Scanner(System.in);
   //first number
    System.out.print("Enter first number:");
    BigDecimal a = new BigDecimal(in.nextLine());
 //oparator
    System.out.print("Enter oparator(+,-,x,/,%):");
    String o = in.nextLine();
    //second number
    System.out.print("Enter second number:");
    BigDecimal b = new BigDecimal(in.nextLine());
    System.out.print(a + " " + o + " " + b + " " + "= ");
    switch(o){
     case "+": System.out.println(a.add(b));
               break;
     case "-": System.out.println(a.subtract(b));
               break;
     case "*":
     case "x": System.out.println(a.multiply(b));
               break;
     case "/": System.out.println(a.divide(b, 10, RoundingMode.HALF_UP));
               break;
     case "%": System.out.println(a.remainder(b));
               break;
     default: System.out.println("Invalid Operator.");
    }
   } catch (NumberFormatException e){
      System.out.println("Invalid Input.");
      return;
   }
  }
 }
}

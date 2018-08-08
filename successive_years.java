import java.time.Year;

public class successive_years {
   public static void main(String[] args) 
   {
 
      int i = 1991;
      Year y;
      System.out.println("LPG Era begins, Liberalisation, Privatisation, Globalisation for Good of India .")
      for(; i < 2050; i++)
      {
        y = Year.of(i); // Returns Int
        System.out.println("This year is :"+ y);
        // System.out.println("Current Year is "+y.getValue()+"Previous Year was"+y.isBefore(y.getValue()));
      // Year date = Year.of(2016);
      // Year date1 = Year.of(2017);
      // System.out.println(date1.isBefore(date));  
       }  // End of For Loop
    } // End of  main method
  } // End of successive_years Class

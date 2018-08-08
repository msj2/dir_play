/*
https://docs.oracle.com/javase/8/docs/api/allclasses-noframe.html has all classes in JDK 1.8

https://docs.oracle.com/javase/8/docs/api/java/time/Year.html

ALl methods of Class Year

Ok, fall to https://www.tutorialspoint.com/javatime/javatime_year.htm

https://www.programcreek.com/java-api-examples/?api=java.time.DateTimeException

https://www.programcreek.com/java-api-examples/?api=java.time.DateTimeException

https://www.programcreek.com/java-api-examples/?api=java.time.DateTimeExceptions
*/

import java.time.Year;
import java.time.MonthDay;
import java.time.DateTimeException;
public class year_1
{
  public static void main(String[] args)
  {
  Year y = Year.of(2018); // using new ives Errpr
  System.out.println(y.getValue());
  // System.out.println(y.getLong(2018));
	System.out.println("Printing Valid dates in feb 2018");
  for(int i = 1; i < 32; i++)
	{
		MonthDay m1 = MonthDay.of(2,i);
		try
		{
			boolean value = y.isValidMonthDay(m1);
			System.out.println("Can february 2018 have"+i+ "as valid day?           "+ value);
		}
		catch(DateTimeException e)
		{
		System.out.println("Exception maga, ... "+e.getMessage());
		}
	}
  }
 }

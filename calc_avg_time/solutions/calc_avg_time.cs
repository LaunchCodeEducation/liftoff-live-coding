using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    
    double time_one = calculate_time(20, 150);
    double time_two = calculate_time(25, 155);
    double time_three = calculate_time(32, 162);
    
    
    
    Console.WriteLine(time_one);
    Console.WriteLine(time_two);
    Console.WriteLine(time_three);
    
    double average_time = time_one + time_two + time_three / 3;
    
    
  }
  
  public static double calculate_time(int x, int y) {
    double time = System.Convert.ToDouble(y) / System.Convert.ToDouble(x);
    return time;
  }
  
}
using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    
    int x = 16;
    
    for(int i = 1; i <= x; i++){
      if((i % 15) == 0) {
        Console.WriteLine("fizzbuzz");
      }
      else if ((i % 3) == 0) {
        Console.WriteLine("fizz");
      }
      else if ((i % 5) == 0) {
        Console.WriteLine("buzz");
      }
      else {
        Console.WriteLine(i);
      }
    }
    
  }
  
}
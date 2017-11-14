using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    
    int[] the_array = new int[] {15, 22, 84, 14, 88, 23};
    int highest_value = the_array[0];
    int lowest_value = the_array[0];
    
    for (int i = 1; i < the_array.Length; i++) {
      if (the_array[i] > highest_value){
        highest_value = the_array[i];
      }
      if (the_array[i] < lowest_value) {
        lowest_value = the_array[i];
      }
    }
    
    Console.WriteLine(highest_value);
    Console.WriteLine(lowest_value);
    
    int the_difference = highest_value - lowest_value;
    
    Console.WriteLine(the_difference);
    
  }
  
}
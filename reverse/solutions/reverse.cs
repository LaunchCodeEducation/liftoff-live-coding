using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    string the_string = "LaunchCode";
    string reversed_string = "";
    for (int i = the_string.Length - 1; i >= 0; i--) {
      reversed_string += the_string[i];
    }
    Console.WriteLine(reversed_string);
    
  }
}
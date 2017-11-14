using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    int[] array_one = {1, 5, 2};
    int[] array_two = {3, 6, 4};
    int[] zipped_array = new int[array_one.Length + array_two.Length];
    int count = 0;
    for (int i = 0; i < zipped_array.Length; i+=2) {
      zipped_array[i] = array_one[count];
      zipped_array[i + 1] = array_two[count];
      count += 1;
    }
    
    foreach(int element in zipped_array) {
      Console.WriteLine(element);
    }
  }
}
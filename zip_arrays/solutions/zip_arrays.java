import java.util.*;
class Main {
  public static void main(String[] args) {
    
    int[] array_one = {1, 5, 2};
    int[] array_two = {3, 6, 4};
    int[] zipped_array = new int[array_one.length + array_two.length];
    
    int count = 0;
    
    for (int i = 0; i < zipped_array.length; i+=2) {
      zipped_array[i] = array_one[count];
      zipped_array[i + 1] = array_two[count];
      count += 1;
    }
    
    for (int element : zipped_array) {
      System.out.println(element);
    }
  }
}
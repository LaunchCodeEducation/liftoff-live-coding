import java.util.*;
class Main {
  public static void main(String[] args) {

    Integer[] the_array = {15, 22, 84, 14, 88, 23};
    int high_value = the_array[0];
    int low_value = the_array[0];
    
    for (int i = 1; i < the_array.length; i++) {
      if (the_array[i] > high_value) {
        high_value = the_array[i];
      }
      if (the_array[i] < low_value) {
        low_value = the_array[i];
      }
    }
    
    System.out.println(high_value);
    System.out.println(low_value);
    
    int the_difference = high_value - low_value;
    
    System.out.println(the_difference);

  }
}
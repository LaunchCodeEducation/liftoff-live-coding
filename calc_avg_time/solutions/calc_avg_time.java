import java.util.*;
class Main {
  public static void main(String[] args) {
    double time_one = calculate_time(20, 150);
    double time_two = calculate_time(25, 155);
    double time_three = calculate_time(32, 162);
    
    System.out.println(time_one);
    System.out.println(time_two);
    System.out.println(time_three);
    
    double average_time = (time_one + time_two + time_three) / 3;
    
    System.out.println(average_time);
    
  }
  public static Double calculate_time(int x, int y) {
    Double time = (double)y / (double)x;
    return time;
  }
}
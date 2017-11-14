import java.util.*;
class Letter_Usage {
  public static void main(String[] args) {

    String word = "My name is Fred";
    char[] words = word.toCharArray();
    Map<Character, Integer> letters = new HashMap<>();
    
    
    for(char letter : words){
      if (letters.containsKey(letter)){
        int amount = letters.get(letter);
        letters.put(letter, (amount + 1));
      }
      else {
        letters.put(letter, 1);
      }
      
    }
    
    System.out.println(letters);
    
  }
  

  
}
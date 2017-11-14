using System;
using System.Collections.Generic;
class MainClass {
  public static void Main (string[] args) {
    String word = "My name is Fred";
    Dictionary<char, int> letters = new Dictionary<char, int>();
    
    foreach (char letter in word){
      if (letters.ContainsKey(letter)) {
        int amount = letters[letter];
        letters[letter] += 1;
      }
      else {
        letters[letter] = 1;
      }
    }
    
    foreach (KeyValuePair<char, int> kvp in letters){
      Console.WriteLine("{0}: {1}", kvp.Key, kvp.Value);
    }
    
  }
  
}
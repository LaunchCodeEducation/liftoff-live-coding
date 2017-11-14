using System;
class MainClass {
  public static void Main (string[] args) {
    String word = "The dog jumps over the cat.";
    
    int the_first_answer = count_words(word);
    int the_second_answer = count_word(word);
    Console.WriteLine(the_first_answer);
    Console.WriteLine(the_second_answer);
    
    //Console.WriteLine(the_answer);
  }
  
  public static int count_words(string phrase){
    string[] words = phrase.Split(' ');
    return words.Length;
  }
  
  public static int count_word(string phrase){
    int num_of_words = 1;
    foreach (char letter in phrase){
      if(letter == ' ') {
        num_of_words = num_of_words + 1;
      }
    }
    return num_of_words;
  }
  
}
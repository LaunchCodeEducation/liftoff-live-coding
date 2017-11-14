using System;
class MainClass {
  public static void Main (string[] args) {
    String word = "19jfeapoihfe85";
    char[] keep = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    String new_word = "";
    foreach (char letter in word){
      foreach (char k in keep){
        if(k == letter){
          new_word = new_word + letter;
        }
      }
    }
    int the_number = Int32.Parse(new_word);
    int the_answer = the_number * word.Length;
    Console.WriteLine(new_word);
    Console.WriteLine(the_answer);
  }
}
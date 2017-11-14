class How_Many_Words{
  public static void main(String[] args) {
    char[] keep = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    String word = "The dog jumps over the cat.";
    
    Integer the_first_answer = count_words(word);
    Integer the_second_answer = count_word(word);
    
    System.out.println(the_first_answer);
    System.out.println(the_second_answer);
    
  }
  
  public static int count_words(String phrase){
    String[] words = phrase.split(" ");
    return words.length;
  }
  
  public static int count_word(String phrase){
    int num_of_words = 1;
    char[] letters = phrase.toCharArray();
    for(char l : letters){
      if (l == ' '){
        num_of_words = num_of_words + 1;
      }
    }
    return num_of_words;
  }
  
}
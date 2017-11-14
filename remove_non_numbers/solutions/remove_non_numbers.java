class Remove_Non_Numbers {
  public static void main(String[] args) {
    char[] keep = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    String word = "19jfeapoihfe85";
    char[] letters = word.toCharArray();
    String new_word = "";
    
    for(char letter : letters){
      for(char k : keep){
        if(letter == k){
          new_word = new_word + letter;
        }
      }
    }
    System.out.println(new_word);
    
    int the_number = Integer.parseInt(new_word);
    int the_answer = the_number * word.length();
    System.out.println(the_answer);
  }
}
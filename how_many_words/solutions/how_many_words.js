var word = "The dog jumps over the cat.";

var the_first_answer = words_count(word);
var the_second_answer = word_count(word);

console.log(the_first_answer);
console.log(the_second_answer);

function words_count(word){
  words = word.split(' ');
  return words.length;
}

function word_count(word){
  num_of_words = 1;
  for(var i = 0; i < word.length; i++){
    if(word[i] === ' '){
      num_of_words += 1;
    }
  }
  return num_of_words;
}
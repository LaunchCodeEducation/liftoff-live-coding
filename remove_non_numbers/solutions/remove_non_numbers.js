var word = "19jfeapoihfe85";
var keep = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
var new_word = "";

for(var i = 0;i<word.length;i++){
  keep.forEach(function(letter) {
    if(letter === word[i]){
      new_word = new_word + word[i];
    }
  });
}
console.log(new_word);
var the_answer = new_word * word.length;
console.log(the_answer);
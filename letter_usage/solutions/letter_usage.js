var word = "My name is Fred";

var letters = {};

for(var i = 0; i < word.length; i++) {
  console.log(word[i]);
  console.log(letters[word[i]]);
  if (letters[word[i]] === undefined) {
    letters[word[i]] = 1;
  }
  else {
    var amount = letters[word[i]];
    letters[word[i]] = amount + 1;
  }
}
console.log(letters);
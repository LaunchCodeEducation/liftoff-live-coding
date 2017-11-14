var the_array = [15, 22, 84, 14, 88, 23];

var highest_value = the_array[0];
var lowest_value = the_array[0];

for (var i = 1; i < the_array.length; i++) {
  if (the_array[i] > highest_value) {
    highest_value = the_array[i];
  }
  if (the_array[i] < lowest_value) {
    lowest_value = the_array[i];
  }
}

console.log(highest_value);
console.log(lowest_value);

var the_difference = highest_value - lowest_value;

console.log(the_difference);
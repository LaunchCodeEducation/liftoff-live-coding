let array_one = [1, 5, 2];
let array_two = [3, 6, 4];
let zipped_array = [];

for (let i = 0; i < array_one.length; i++) {
  zipped_array.push(array_one[i]);
  zipped_array.push(array_two[i]);
}

console.log(zipped_array);
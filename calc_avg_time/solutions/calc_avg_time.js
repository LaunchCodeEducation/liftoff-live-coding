let time_one = calculate_time(20, 150);
let time_two = calculate_time(25, 155);
let time_three = calculate_time(32, 162);

console.log(time_one);
console.log(time_two);
console.log(time_three);

let average_time = (time_one + time_two + time_three) / 3;

console.log(average_time);


function calculate_time(x, y) {
  let time = y / x;
  return time;
}
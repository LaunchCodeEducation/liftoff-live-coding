let the_string = "LaunchCode";
let reversed_string = "";

for (let i = the_string.length - 1; i >= 0; i--) {
  reversed_string += the_string[i];
}

console.log(reversed_string);
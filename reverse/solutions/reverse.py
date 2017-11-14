'''
Reverse String
Without using the built in reverse function, Write a function that will take a string in as a parameter, and return a reversed string



Example Input: "LaunchCode"

Example Output: "edoChcnuaL"
'''

def reverse_string(example_string):
    new_string = ''
    for i in range(1, len(example_string) + 1):
        new_string += example_string[(-1 * i)]

    return new_string


example_string = "LaunchCode"
print(reverse_string(example_string))


'''
Java answer:
class Main {
  public static void main(String[] args) {
    String str = "LaunchCode";
    String answer = reverse_string(str);
    System.out.println(answer);
  }
  public static String reverse_string(String example_string){
    String new_string = "";
    String[] str_array = example_string.split("");
    for(int i = str_array.length-1;i >= 0;i--){
      new_string += str_array[i];
    }
    return new_string;
  }
}

'''

'''
Remove all the vowels from a string.

Then return a new string of every other character in the string.abs

Example input: "LaunchCode"

Example output: "LcC"


Tests:
input = "L"
output = "L"

input = "LC"
output = "L"

input = "Python is great!"
output = "Ptnsgt"
output = "Ph  r!"

'''

def remove_vowels(example_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for c in example_string:
        if c.lower() not in vowels:
            new_string += c

    return new_string

def strip_every_other_character(example_string):
    new_string = ''
    odd = True
    for c in example_string:
        if odd:
            new_string += c
        odd = not odd
    return new_string

example_string = "LaunchCode"
example_string = remove_vowels(example_string)
example_string = strip_every_other_character(example_string)
print(example_string)

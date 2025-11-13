-->                               string
--> Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

def hello_name(name):
    greeting = "Hello " + name 
    return greeting
# print(hello_name("Bob"))
# print(hello_name("Alice"))
# print(hello_name("X"))

--> Given an "out" string length 4, such as "<<>>", and a word, return a new 
    string where the word is in the middle of the out string, e.g. "<<word>>".
    make_out_word('<<>>', 'Yay') → '<<Yay>>'
    make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
    make_out_word('[[]]', 'word') → '[[word]]'   

def make_out_word(out, word):
    return out[:2] + word + out[2:]
# print(make_out_word('<<>>', 'Yay'))
# print(make_out_word('<<>>', 'WooHoo'))
# print(make_out_word('[[]]', 'word'))

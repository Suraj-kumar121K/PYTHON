# Q1. Reverse a string without using [::-1].
# +++++++++++++++++++++++++++++++++++++++++
# ----> Input: "Suraj"
# ----> Output: "jaruS"
#+++++++++++++++++++++++++++++++++++++++++
def reverse_string(reverse):
    reverse_str = ""
    for char in reverse:
        reverse_str = char + reverse_str
    return reverse_str
# name = input("Enter a String: ")
# print(reverse_string(name))

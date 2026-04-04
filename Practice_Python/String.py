# 1. Print the first character of "Python"
"""text = "Python"
print(text[0])"""

# 2. Print the last character of "Python"
"""text = "Python"
print(text[-1])"""

# 3. Print the second last character of "Python"
"""text = "Python"
print(text[-3])"""

# 4. Print the first three characters of "Programming"
"""text = "Programming"
print(text[0:3])"""

# 5. Print the last three characters of "Programming"
"""text = "Programming"
print(text[-3:])"""

# 6. Print the string "Python" in reverse
"""text = "Python"
print(text[::-1])"""

# 7. Print every second character of "Python"
"""text = "Python"
print(text[0:6:2])"""

# 8. Print every third character of "PythonProgramming"
"""text = "PythonProgramming"
print(text[0:16:3])"""

# 9. Extract "thon" from "Python"
"""text = "Python"
print(text[2:6])"""

# 10. Extract "gram" from "Programming"
"""text = "Programming"
print(text[3:7])"""

# 11. Slice "DataScience" from index 4 to 8
"""text = "DataScience"
print(text[4:8])"""

# 12. Slice "MachineLearning" from index 0 to 7
"""text = "MachineLearning"
print(text[0:7])"""

# 13. Slice "ArtificialIntelligence" last 5 characters
"""text = "ArtificialIntelligence"
print(text[-5:])"""

# 14. Slice "DeepLearning" from 2nd to 8th character
"""text = "DeepLearning"
print(text[2:8])"""

# 15. Reverse "Artificial" using slicing
"""text = "Artificial"
print(text[::-1])"""

# 16. Get every 2nd character of "Analytics"
"""text = "Analytics"
print(text[::2])"""

# 17. Slice "Programming" from 3rd last to end
"""text = "Programming"
print(text[-3:])"""

# 18. Slice "PythonProgramming" first 6 characters
"""text = "PythonProgramming"
print(text[0:6])"""

# 19. Slice "PythonProgramming" last 6 characters
"""text = "PythonProgramming"
print(text[-6:])"""

# 20. Slice "PythonProgramming" characters at even indices
"""text = "PythonProgramming"
print(text[::2])"""

# 21. Convert "python" to uppercase
"""text = "python"
print(text.upper())"""

# 22. Convert "PYTHON" to lowercase
"""text = "PYTHON"
print(text.lower())"""

# 23. Capitalize "python programming"
"""text = "python programming"
print(text.capitalize())"""

# 24. Make "python programming" title case
"""text = "python programming"
print(text.title())"""

# 25. Swap case of "PyTHon ProGRAM"
"""text = "PyTHon ProGRAM"
print(text.swapcase())"""

# 26. Check if "PYTHON" is uppercase
"""text = "PYTHON"
print(text.isupper())"""

# 27. Check if "python" is lowercase
"""text = "python"
print(text.islower())"""

# 28. Convert "python programming" to title case
"""text = "python programming"
print(text.title())"""

# 29. Convert "python programming" to capitalize the first letter
"""text = "python programming"
print(text.capitalize())"""
# 30. Check if "Python" is title case
"""text = "Python"
print(text.istitle())"""

# 31. Strip whitespaces from "  Python  "
"""text = "  Python  "
print(text.strip())"""

# 32. Strip "*" from "***Python***"
"""text = "***Python***"
print(text.strip("*"))"""

# 33. Remove leading spaces from "  Python"
"""text = "  Python"
print(text.lstrip())"""

# 34. Remove trailing spaces from "Python  "
"""text = "Python  "
print(text.rstrip())"""

# 35. Replace "Python" with "Java" in "I love Python"
"""text = "I love Python"
s = text.replace("Python", "Java")
print(s)"""

# 36. Replace " " with "-" in "Python Programming"
"""text = "Python Programming"
s = text.replace(" ", "-")
print(s)"""

# 37. Replace "a" with "@" in "Data"
"""text = "Data"
ss = text.replace("a", "@")
print(ss)"""

# 38. Replace "Python" with "C++" in "Python is easy"
"""text = "Python is easy"
sk = text.replace("Python", "C++")
print(sk)"""

# 39. Replace " " with "" in "Hello World"
"""text = "Hello World"
sz = text.replace(" ", "")
print(sz)"""

# 40. Strip both leading and trailing "#" from "##Python##"
"""text = "##Python##"
print(text.strip("#"))"""

# 41. Count occurrences of "o" in "Python"
text = "Python"
print(text.count("o"))

# 42. Count occurrences of "p" in "Python Programming"
text = "Python Programming"
count_1 = text.lower().count("p")
print(count_1)

# 43. Find index of "o" in "Python"
text = "Python"
print(text.index("o"))

# 44. Find index of "Pro" in "Python Programming"
text = "Python Programming"
pri = text.index("Pro")
print(pri)

# 45. Check if "Python" starts with "Py"
text = "Python"
py = text.startswith("Py")
print(py)

# 46. Check if "Programming" ends with "ing"
text = "Programming"
px = text.endswith("ing")
print(px)

# 47. Check if "Data" is in "Data Science"
text = "Data Science"
D = "Data" in text
print(D)

# 48. Check if "AI" is in "Machine Learning"
text = "Machine Learning"
A = "AI" in text
print(A)

# 49. Find last occurrence of "n" in "Python"
text = "Python"
L = text.rfind("n")
print(L)

# 50. Count number of spaces in "Python Programming Language"
text = "Python Programming Language"
print(text.count(" "))

# 51. Check if "Python" is alphabetic
# 52. Check if "Python123" is alphabetic
# 53. Check if "12345" is digit
# 54. Check if "12a45" is digit
# 55. Check if "Python123" is alphanumeric
# 56. Check if "Python 123" is alphanumeric
# 57. Check if "   " is space
# 58. Check if "Python" is alphanumeric
# 59. Check if "123 " is space
# 60. Check if "DataScience" is alphabetic
# 61. Split "Python Programming" by space
# 62. Split "a,b,c,d" by comma
# 63. Join ["Python","Java","C++"] with ","
# 64. Join ["I","love","Python"] with "-"
# 65. Split "Python-Programming-Data" by "-"
# 66. Join ["2023","04","02"] with "/"
# 67. Split "AI|ML|DL" by "|"
# 68. Join ["Hello","World"] with space
# 69. Split "PythonPythonPython" by "Python"
# 70. Join ["Python"]*5 with ","
# 71. Format "Hello {}" with "World"
# 72. Format "{} + {} = {}" with 2,3,5
# 73. Format float 3.14159 to 2 decimals using "%.2f"
# 74. Use f-string to display "Python is fun" using variable
# 75. Format "Name: {}, Age: {}" with "Alice" and 20
# 76. Center "Python" in width 20 with "*" padding
# 77. Left justify "Python" in width 15
# 78. Right justify "Python" in width 15
# 79. Format number 50 to width 5 with zeros → "00050"
# 80. Format "Hello" in 10-character width with right alignment
# 81. Check if "Python" ends with "on"
# 82. Check if "Python" starts with "Py"
# 83. Check if " " is space
# 84. Check if "Python3" is alphanumeric
# 85. Check if "123" is numeric
# 86. Check if "PYTHON" is uppercase
# 87. Check if "python" is lowercase
# 88. Check if "Python Programming" is title case
# 89. Check if "123 " is digit
# 90. Check if "abc123" is alphanumeric
# 91. Count number of vowels in "Python Programming" (no loop → use count())
# 92. Remove all "o" in "Python" using replace()
# 93. Convert "PYTHON" to "python" using method
# 94. Convert "python" to "PYTHON"
# 95. Strip "!" from "!!!Hello!!!"
# 96. Replace " " with "-" in "Hello World Python"
# 97. Check if "123abc" is alphanumeric
# 98. Slice "PythonProgramming" first 7 characters
# 99. Slice "PythonProgramming" last 7 characters
# 100. Reverse "PythonProgramming" using slicing

# 1. Given a string, return a greeting: "Hello <name>!"
#    Function: hello_name(name)

# 2. Given two strings a and b, return 'abba' form: "Hi", "Bye" → "HiByeByeHi"
#    Function: make_abba(a, b)

# 3. Given tag and word, return HTML: "i", "Yay" → "<i>Yay</i>"
#    Function: make_tags(tag, word)

# 4. Given out string length 4 and word, put word in middle: "<<", "Hello" → "<<Hello>>"
#    Function: make_out_word(out, word)

# 5. Given string, return 3 copies of last 2 chars: "Hello" → "lololo"
#    Function: extra_end(s)

# 6. Return first 2 chars of a string, if short return all: "Hello" → "He"
#    Function: first_two(s)

# 7. Given string of even length, return first half: "WooHoo" → "Woo"
#    Function: first_half(s)

# 8. Given string, return last char + first char: "Python" → "nP"
#    Function: front_back(s)

# 9. Remove first and last char of string: "Hello" → "ell"
#    Function: without_end(s)

# 10. Repeat string n times: "Hi", 3 → "HiHiHi"
#     Function: string_times(s, n)

# 11. Return True if string starts with "hi": "hi there" → True
#     Function: start_hi(s)

# 12. Return True if first 2 and last 2 chars are same: "edited" → True
#     Function: front_again(s)

# 13. Count how many times last 2 chars appear in string: "hixxhi" → 1
#     Function: last2(s)

# 14. Return string without first 2 chars, except "ki": "kitten" → "kitten"
#     Function: without2(s)

# 15. Return new string with every other char: "Hello" → "Hlo"
#     Function: string_bits(s)

# 16. Return string with first and last char swapped: "code" → "eodc"
#     Function: front_back(s)

# 17. Return True if "cat" or "dog" appears: "my dog" → True
#     Function: cat_dog(s)

# 18. Return string without "x" at start or end: "xHix" → "Hi"
#     Function: string_x(s)

# 19. Return True if b appears in string between two a: "aba" → True
#     Function: bob_btw(s)

# 20. Return new string by doubling each char: "Hi" → "HHii"
#     Function: double_char(s)

# 21. Count number of "hi" in string: "hihi" → 2
#     Function: count_hi(s)

# 22. Count number of "co_e" pattern: "codecoze" → 2
#     Function: count_code(s)

# 23. Return True if string contains same number of "cat" and "dog": "catdogcat" → False
#     Function: cat_dog_equal(s)

# 24. Return True if string has xyx anywhere: "xxyx" → True
#     Function: xyx_check(s)

# 25. Return string with "not ... bad" replaced by "good": "This is not so bad" → "This is good"
#     Function: not_bad(s)

# 26. Return string made of chars at positions multiple of 3: "abcdefghi" → "adg"
#     Function: every_third(s)

# 27. Return string where all "x" replaced by "y": "xoxo" → "yoyo"
#     Function: replace_x(s)

# 28. Return string made of first 2 chars + last 2 chars: "spring" → "spng"
#     Function: first_last_2(s)

# 29. Return True if string length >= 2 and first 2 chars equal last 2 chars: "edited" → True
#     Function: same_first_last2(s)

# 30. Return longest prefix which is also suffix (without overlap): "ababcab" → "ab"
#     Function: longest_prefix_suffix(s)
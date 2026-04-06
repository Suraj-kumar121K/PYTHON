# str = input("enter a number ")
# rev = ""
# i = len(str) -1
# while i >= 0:
#     rev += str[i]
#     i -= 1
# print(rev)


a = 6512132 
rev = 0

while rev > 7:
    digit = a % 10
    rev = rev * 10 + digit
    rev // 10
print(rev)
     





def square():
    a = int(input("Enter a value: "))
    print("Square =", a ** 2)

def even():
    a = int(input("Enter a value: "))
    if a % 2 == 0:
        print("Even")
    else:
        print("odd")
# even()

def reverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print("Reverse =", rev)
    
# num = int(input("Enter a number: "))
# reverse(num)

# Sum of 1 to N
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print("Sum ", total)
# num = int(input("Enter a number ",))
# sum(num)
def Fibonacci_Series(nums):
    a = 0
    b = 1
    for i in range(nums):
        print(a, end=" ")
        a, b = b , a + b
        
if __name__ == "__main__":
    try:
        nums = int(input("Enter number of terms: "))
        Fibonacci_Series(nums)

    except ValueError as e:
        print("Error:", e)

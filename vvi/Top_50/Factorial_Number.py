def factorial_number(nums):
    fact = 1
    calculation = []
    for i in range(1, nums + 1):
        fact *= i
        calculation.append(str(i))
    print(f"{nums}! = {' x '.join(calculation[::-1])} = {fact}")
    return fact

if __name__ == "__main__":
    try:
        nums = int(input("Enter a Number: "))
        if nums < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial_number(nums)
    except ValueError as e:
        print("Error:", e)
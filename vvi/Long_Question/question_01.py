def Sum_Of_Digits(nums):
    total = 0

    while nums > 0:
        digit = nums % 10
        total += digit
        nums //= 10

    return total


def Count_Even_Odd(nums):
    even = 0
    odd = 0

    while nums > 0:
        digit = nums % 10

        if digit % 2 == 0:
            even += 1
        else:
            odd += 1

        nums //= 10

    return even, odd


def Reverse_Number(nums):
    reverse = 0

    while nums > 0:
        digit = nums % 10
        reverse = reverse * 10 + digit
        nums //= 10

    return reverse


def main():
    try:
        nums = int(input("Enter a Number: "))

        if nums < 0:
            print("Please enter a positive number.")
            return

        while True:
            print("\n----- Number Analysis Menu -----")
            print("1. Sum of Digits")
            print("2. Count Even and Odd Digits")
            print("3. Reverse Number")
            print("4. Show All Results")
            print("5. Exit")

            choice = input("Enter your choice: ").strip().lower()

            if choice == "1":
                print("Sum of Digits:", Sum_Of_Digits(nums))

            elif choice == "2":
                even, odd = Count_Even_Odd(nums)
                print("Even Digits Count:", even)
                print("Odd Digits Count:", odd)

            elif choice == "3":
                print("Reverse Number:", Reverse_Number(nums))

            elif choice == "4":
                print("Sum of Digits:", Sum_Of_Digits(nums))

                even, odd = Count_Even_Odd(nums)
                print("Even Digits Count:", even)
                print("Odd Digits Count:", odd)

                print("Reverse Number:", Reverse_Number(nums))

            elif choice in ("5", "exit"):
                print("Program Exited Successfully!")
                break

            else:
                print("Invalid choice! Please select 1 to 5 or type exit.")

    except ValueError as e:
        print("Please enter a valid integer.", e)


if __name__ == "__main__":
    main()
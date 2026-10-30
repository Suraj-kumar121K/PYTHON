def Smallest_Number(nums):
    smallest = nums[0]
    for i in range(len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
    print("Smallest number:", smallest)
if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter a Smallest Number: ").split()))
        Smallest_Number(nums)
        
    except ValueError as e:
        print("Error: Please enter valid integers.", e)
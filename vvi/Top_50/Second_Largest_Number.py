def Second_Largest_Number(nums:list) -> int:
    largest = float("-inf")
    second = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            second = largest
            largest = nums[i]
        elif nums[i] > second and nums[i] < largest:
            second = nums[i]
            
    if second == float("-inf"):
        print("Second largest number does not exist.")
    else:
        print("Second Largest Number:", second)
    
if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter the Second Largest: ").split()))
        Second_Largest_Number(nums)
        
    except ValueError as e:
        print("Error: Please enter valid integers.", e)
        
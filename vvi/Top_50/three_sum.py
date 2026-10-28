def three_sum(nums:list, target:int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return[i, j, k]

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter a Number: ").split()))
        target = int(input("Enter the Total Target:"))
        
        print(three_sum(nums, target))
    except Exception as e:
        print("Error:", e)
            
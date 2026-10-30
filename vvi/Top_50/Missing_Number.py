def Missing_Number(nums):
    Duplicate = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                if nums[i] not in Duplicate:
                    Duplicate.append(nums[i])
if __name__ == "__main__":
    try:
        nums = str(map(int, input("Enter the value: ").split()))
        Missing_Number(nums)
    except ValueError as e:
        print("Error", e)
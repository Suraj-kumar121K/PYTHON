def two_sum(nums:list, target:int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
if __name__ == "__main__":
    try:
        numbers = list(map(int, input("Enter numbers: ").split()))
        target = int(input("Enter the Total Target: "))

        print(two_sum(numbers, target))

    except Exception as e:
        print("Error:", e)
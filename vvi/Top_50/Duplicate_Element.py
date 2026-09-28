# Finde the First Duplicate Element in a list
def first_duplicate(numbers:list) -> int:
    moon = set()
    for num in numbers:
        if num in moon:
            return num
        moon.add(num)
if __name__ == "__main__":
    try:
        numbers = [10, 20, 30, 15, 30, 13, 5]
        print(first_duplicate(numbers))
    except Exception as e:
        print("Error", e)
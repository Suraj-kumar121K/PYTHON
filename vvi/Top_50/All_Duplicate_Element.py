# Find All Duplicate Elements in a List
def All_Duplicate_Elements(num:list) -> int:
    duplicate_value = set()
    duplicate = set()
    for number in num:
        if number in duplicate_value:
            duplicate.add(number)
        else:
            duplicate.add(number)
    return list(duplicate)
if __name__ ==  "__main__":
    try:
        num = [ 10, 20, 40, 30, 50, 20, 10, 30]
        print(All_Duplicate_Elements(num))
    except Exception as e:
        print("Error", e)
        
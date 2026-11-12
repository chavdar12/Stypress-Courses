def binary_search(items, target, left=0, right=None):
    if right is None:
        right = len(items) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    if items[middle] == target:
        return middle
    if items[middle] > target:
        return binary_search(items, target, left, middle - 1)
    return binary_search(items, target, middle + 1, right)


numbers = [1, 3, 5, 7, 9, 11]
assert [binary_search(numbers, n) for n in numbers] == list(range(6))
assert binary_search(numbers, 4) == -1 and binary_search([], 1) == -1

if __name__ == "__main__":
    print(binary_search(numbers, int(input("Search for: "))))

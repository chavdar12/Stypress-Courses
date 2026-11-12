def is_sorted(items):
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))


assert is_sorted([1, 2, 2]) and not is_sorted(["b", "a"]) and is_sorted([])

if __name__ == "__main__":
    print(is_sorted([1, 2, 2]))
    print(is_sorted(["b", "a"]))

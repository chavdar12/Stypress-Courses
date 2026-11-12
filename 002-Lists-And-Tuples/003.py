def has_duplicates(items):
    seen = []  # list, not set, so unhashable elements (e.g. lists) work too
    for item in items:
        if item in seen:
            return True
        seen.append(item)
    return False


assert has_duplicates([1, 2, 1]) and not has_duplicates([1, 2, 3]) and has_duplicates([[1], [1]])

if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 2]))

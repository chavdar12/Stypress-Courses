def unique(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


assert unique([3, 1, 3, 2, 1]) == [3, 1, 2]

if __name__ == "__main__":
    print(unique([3, 1, 3, 2, 1]))

def keys_for_value(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]


assert keys_for_value({"a": 1, "b": 2, "c": 1}, 1) == ["a", "c"]
assert keys_for_value({"a": 1}, 5) == []

if __name__ == "__main__":
    print(keys_for_value({"a": 1, "b": 2, "c": 1}, 1))

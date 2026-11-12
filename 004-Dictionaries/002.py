def histogram(text):
    result = {}
    for ch in text:
        result[ch] = result.get(ch, 0) + 1
    return result


assert histogram("brontosaurus") == {"b": 1, "r": 2, "o": 2, "n": 1, "t": 1, "s": 2, "a": 1, "u": 2}

if __name__ == "__main__":
    print(histogram(input("Text: ")))

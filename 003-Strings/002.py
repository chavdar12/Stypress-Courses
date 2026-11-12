from string import ascii_uppercase as ABC


def vigenere(text, key, decrypt=False):
    key = [ABC.index(k) for k in key.upper() if k in ABC]
    sign = -1 if decrypt else 1
    result, i = "", 0
    for ch in text.upper():
        if ch in ABC:
            result += ABC[(ABC.index(ch) + sign * key[i % len(key)]) % 26]
            i += 1
        else:
            result += ch
    return result


# example from the lecture: key LEMON
assert vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
assert vigenere("LXFOPVEFRNHR", "LEMON", decrypt=True) == "ATTACKATDAWN"

if __name__ == "__main__":
    text = input("Text: ")
    key = input("Key: ")
    print(vigenere(text, key))

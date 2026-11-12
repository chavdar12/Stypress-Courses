from string import ascii_uppercase as ABC


def caesar(text, shift):
    result = ""
    for ch in text.upper():
        result += ABC[(ABC.index(ch) + shift) % 26] if ch in ABC else ch
    return result


assert caesar("ATTACK AT DAWN", 3) == "DWWDFN DW GDZQ"
assert caesar(caesar("Hello, World", 5), -5) == "HELLO, WORLD"

if __name__ == "__main__":
    text = input("Text: ")
    shift = int(input("Shift: "))
    print(caesar(text, shift))

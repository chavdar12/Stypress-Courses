def letters(text):
    return sorted(ch for ch in text.lower() if ch.isalnum())


def are_anagrams(first, second):
    return letters(first) == letters(second)


assert are_anagrams("Vladimir Nabokov", "Vivian Darkbloom")
assert are_anagrams("rocketboys", "octobersky")
assert not are_anagrams("abc", "abd")

if __name__ == "__main__":
    print(are_anagrams(input("First: "), input("Second: ")))

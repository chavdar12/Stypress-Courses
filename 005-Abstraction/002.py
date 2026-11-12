def is_palindrome(text):
    if len(text) < 2:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])


assert is_palindrome("racecar") and is_palindrome("") and not is_palindrome("ab")

if __name__ == "__main__":
    print(is_palindrome(input("Text: ")))

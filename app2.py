def has_e(word):
    """Check if the word contains the letter 'e'."""
    for letter in word:
        if letter.lower() == 'e':
            return True
    return False

def has_any(word, letters):
    """Check if the word contains any of the specified letters."""
    if word is None or letters is None:
        return False

    letters_lower = letters.lower()

    for letter in word:
        if letter.lower() in letters_lower:
            return True
    return False

print(has_e("Hello"))  # True
print(has_e("World"))  # False
print("\n")

print(has_any("Hello", "aeiou"))  # True
print(has_any("Hello", "LO"))  # True
print(has_any("World", "aeiou"))  # True
print("\n")

print(has_any("","aeiou"))  # False
print(has_any(None, "aeiou"))  # False
print(has_any("Hello", None))  # False
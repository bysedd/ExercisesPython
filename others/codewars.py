def alphabet_position(text):
    alphabet = {chr(97 + i): i + 1 for i in range(26)}
    return ' '.join([str(alphabet[char]) for char in text.lower() if char in alphabet])


print(alphabet_position("The sunset sets at twelve o' clock."))

def palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

word = "rotimi"
if palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


def palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

<<<<<<< HEAD
word = "rotimi"
if palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
=======
word = "Mallam"
if palindrome(word):
    print("true")
else:
    print("false")

>>>>>>> d3c72c6 (Initial commit)


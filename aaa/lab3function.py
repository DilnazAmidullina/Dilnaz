def isPalindrome(word):
    reversed_word = ""
    for char in reversed(word):
        reversed_word += char
    if reversed_word == word:
        print("is palindrome")
    else:
        print("not palindrome")

my_string = input()
isPalindrome(my_string)

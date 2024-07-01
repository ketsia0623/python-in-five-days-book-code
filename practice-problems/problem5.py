# practice problem 5
'''
Write a function that converts a word to Pig Latin. The conversion rules are as follows:
 - Remove the first character of the word
 - Append the removed character to the end of the string
 - Add “ay” to the end of the string

Example Usage:
print(pigLatin("python"))  
Output: "ythonpay"
'''

# Write your code here


































# Solution

'''
def pigLatin(word: str) -> str:
    if len(word) > 1:
        return word[1:] + word[0] + "ay"
    return word + "ay"
'''

# practice problem 12
'''
Given a list of strings, return the largest string in the list

Example usage:
print(longestString(["apple", "banana", "cherry"]))  
Output: "banana"
'''

# Write your code here










































# Solution

'''
def longestString(words: List[str]) -> str:
    longest = ""
    index = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
        else:
            continue 
    return longest

# OR

def largest_string(string_list):
    return max(string_list, key=len)

'''

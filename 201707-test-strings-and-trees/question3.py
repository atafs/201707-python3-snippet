#!/usr/bin/python3

# reverse: reverts the words from a string received as a parameter
def reverseWords(text):
    lst = []
    count = 1

    for i in range(0,len(text)):
        # appending the last character to the list starts the reverse order (loops makes sure I do it for the whole string)
        lst.append(text[len(text)-count])
        count += 1

    #join the letters together without a space
    lst = ''.join(lst)
    return lst

# call the function for this text
text = "Hello there, Huckletree"
print(reverseWords(text))

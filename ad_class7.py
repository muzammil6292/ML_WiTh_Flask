string = "immortality or death"
for word in string.split():
    if len(word) > 3:  # Check if the length of the word is greater than 3
        print(word[0])  # Print the first letter of the word
# convert str to list 
list1=string.split(",")
print(list1)
strr="hellooo world"
five_letter_words = [word for word in strr.split() if len(word) == 5]
print(five_letter_words)
pyy="nana told not to judge others"
words = [word[::-1] for word in pyy.split() if len(word) == 5]
print(words)
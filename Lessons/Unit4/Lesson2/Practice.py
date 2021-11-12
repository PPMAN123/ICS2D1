# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-09

#Minds On
word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
counter = 0
for i in range(len(word)):
    if word[i].lower() in vowels:
        counter += 1
print(counter)

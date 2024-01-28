#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case. 

word = input("Please enter a word: ")

first_consonant = word[0]

length = len(word)

remaining_word = word[1:length]

if first_consonant == "a" or first_consonant == "e" or first_consonant == "i" or first_consonant == "o" or first_consonant == "u":
    new_word = word + "way"

else:
    new_word = remaining_word + first_consonant + "ay"

print(new_word.lower())
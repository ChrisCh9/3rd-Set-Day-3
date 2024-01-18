#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case. 

num = int(input("Please enter a number between 10 and 20 (inclusive): "))

if num <= 20 and num >= 10:
    print("Correct")

elif num < 10:
    print("Too low")

else:
    print("Too high")
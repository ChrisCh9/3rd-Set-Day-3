#Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1). 

rhyme = input("Please enter your rhyme: ")

length = len(rhyme)

print("Your rhyme has a length of ", length, " letters")

start = int(input("Enter a starting number"))

end = int(input("Enter an ending number"))

print(rhyme[start:end])
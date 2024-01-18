#Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together (without a space) and display the name in upper case. If the length of the first name is five or more characters, display their first name in lower case

rhyme = input("Please enter your first name: ")



surname = surname.title()

full_name = (name + " " + surname)

print(full_name)

if user_age >= 18:
    print("You can vote")

elif user_age == 17:
    print("You can learn to drive")

elif user_age == 16:
    print("You can buy a lottery ticket")

elif user_age < 16 and user_age > 0:
    print("You can go Trick or Treating")

else:
    print("Invalid age")
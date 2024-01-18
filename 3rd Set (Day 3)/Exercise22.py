#Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result. 

name = input("Please enter your first name in lowercase: ")

surname = input("Please enter your surname in lowercase: ")

name = name.title()

surname = surname.title()

full_name = (name + " " + surname)

print(full_name)
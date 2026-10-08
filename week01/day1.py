name = input("What's your name? ")
print("Hello,",name)
#we can also write this as ("Hello, " + name)

for i in range(0,6,2):
    print("Round", i)

#to strip off white spaces from left and right side that user may add by mistake
name = name.strip()

#to capitalize the first letter of the users name
#name = name.capitalize()

#to capitalize the first letter of the users names(surname as well if there
name = name.title()

#we could fit all these functions in one line of code
# name = input("What's your name? ").strip().title()

#if u want to split the first and last name and only print the last name 
# first,last = name.split(" ")

#another way to print print (f"Hello, {name}") -> formats the varibles on its own 
print (f"Hello, {name}") 
# This program is a simple exercise to practice basic Python programming concepts. Says hello and asks for my name

print('Hello, world!')
print('What is your name?') # Asks for name
myname = input('>')
print('It is good to meet you, ' + myname) # Greets user by name
print('The length of your name is:') # Tells user the length of their name
print(len(myname)) # Prints length of name 
print('What is your age?') # Asks for age
myage = input('>') # Asks for age
print('You will be ' + str(int(myage) + 1) + ' in a year.')

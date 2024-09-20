# string concatenation (how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

# youtuber = "NiceWigg" # some string variable

# ways to do this

# print("subscribe to " + youtuber) # string and then concatenate it using '+ youtuber'
# print("subscribe to {}".format(youtuber)) # this puts the value of youtuber into where the curly braces are
# print(f"subscribe to {youtuber}") # f string. This is probably the cleanest way to express string concatenation here
 
# For this demo, I'll choose to use the f string method, because it is a clean implementation of string concatenation.

adjective = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
pro_player= input("Famous person: ")

madlib = f"Apex Legends is so {adjective}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {pro_player}!"

print(madlib)

# this simple madlib is defines user input values to fill out a string. 

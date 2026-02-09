# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys.


phonebook = {
    "Benson" : "2547431233",
    "Mary" : "25476413130",
    "Stephen": "2547451133"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out benson's number
print(phonebook["Benson"])

print('==============================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (254774542, 254765344, 25476531)
    }
}
# print barcelona - the second team he played for
print(player["teams"][1])
print("The second number of messi is: ", player["more"])

# print messi second number


# research on if ... else statements in python

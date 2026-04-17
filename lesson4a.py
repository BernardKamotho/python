# Nested if Statements
# A nested if statement is an if statement that is contained within another if statement.

age = 13
weight = 46

if age > 15:
    if weight > 50:
        print("you can donate blood")
    else:
        print("you cannot donate blood because of your weight")
else:
    print("you cannot donate blood because of your age")
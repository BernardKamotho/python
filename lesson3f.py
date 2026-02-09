# Create a python program that is able to determine whether a number entered is an odd number or an even number.
# number = int(input("input the number here"))
# if number  % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# Create a python program that is able to detaermine if a person can donate blood based on the weight and and age of the person.If thhe weight is greater than 50kgs and age greater than 18 years the the person can donate,else not possible.
age = int(input("enter age"))
weight = float(input("enter weight"))

if age >= 18 and weight >=50:
    print("can donate")
else:
    print("cannot")
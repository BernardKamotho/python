# A for loop can also be used to iterate through a list, tuple, string or even adictionary..

name = "Bernard"

for letter in name:
    if letter == "n":
        print("the letter is n")
    else:
        print(letter)

print('==============================')
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print('==============================')
for county in counties:
    if "Nairobi" in counties:
        print("The county is part of the list ")
        break
    else:
        print("The county is not part of the list")
print('==============================')
# The for loop can also be used to iterate through a dictionary


player = {
    "name": "Mbappe",
    "age": 25,
    "teams": ["PSG", "Monaco", "France"],
    "nationality": "French"
}

for key in player:
    print(key)

print('==============================')
for value in player:
    print(player[value])
# print(player["name"])



print('==============================')
#  loop throught the teams the player has played for
# print(player["teams"])

for team in player["teams"]:
    print(team)
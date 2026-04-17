county = input("Enter the city to check: ")

found = False

counties = ["Nairobi", "Kisumu", "Narok", "Elgeyo Marakwet", "Lamu", "Tana River", "Machakos", "Nandi"]

for c in counties:
    if county == c:
        found = True
        break

if found:
    print("The county entered is part of the list")
else:
    print("The county entered is NOT part of the list")



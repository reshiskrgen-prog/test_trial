# the dictionary
names = {
    "Superman": "Strength", 
    "Spider Man": "Spider Sense", 
    "Flash": "Super Speed"
}
# the user's hero and power
new_name = input("What is your superhero's name? ")
power = input("What is their power? ")

# print final
names[new_name] = power

print(names)

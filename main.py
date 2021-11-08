import random

print("Python Banker Roulette - Who will pay the bill?")
names_string = input("Give me everybody's names, separated by a comma and space:\n")

names = names_string.split(", ")
num_names = len(names)
random_name = random.randint(0, num_names - 1)
person = names[random_name]

print(f"{person} should pay the bill. Program has decided! :)")

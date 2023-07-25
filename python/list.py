#! /usr/bin/python3

#List items or lements
#Indexing starts from 0
FAVOURITE_FOODS = ["fruits", "nuts", "chocolate","nuts"]
#FAVOURITE_FOODS[2] = "Cake"
#List methods
# FAVOURITE_FOODS.append("Yogurt")
# FAVOURITE_FOODS.insert(0, "Peanut")
# print(FAVOURITE_FOODS)
# FAVOURITE_FOODS.remove("fruits")
# del FAVOURITE_FOODS[0]

#print(FAVOURITE_FOODS)
# counter = 0
# while counter < len(FAVOURITE_FOODS):
#     print(FAVOURITE_FOODS[counter].upper())
#     counter += 1

# for foods in FAVOURITE_FOODS:
#     print(foods.lower())
class_uno = ["one", "two", "three"]
class_duo = ["four", "five", "six"]

class_uno.extend(class_duo)
print(class_uno)
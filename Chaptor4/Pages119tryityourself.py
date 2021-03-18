#4-10. slice
favorite_pizzas = ['hawaiian','margherita','pepperoni']
print(favorite_pizzas[:3])

print(favorite_pizzas[2:])

print(favorite_pizzas[-2:])

#4-11 My Pizza,Your Pizzas
favorite_pizzas = ['hawaiian','margherita','pepperoni']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("spare rib")
friend_pizzas.append('chicken and avo')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
#4-12 more loops:
friend_pizzas = ["chicken_and_avo"]
for friend_pizzas in friend_pizzas:
    print(friend_pizzas)
    print(f"{friend_pizzas}, I don't like avo" )

favorite_pizzas = ["spare,rib"]
for favorite_pizzas in favorite_pizzas:
    print(favorite_pizzas)
    print(f"{favorite_pizzas}, can do with some pineapple")
#4-13

menu_items = (
    'burgers', 'steak and chips', 'lamb shanks',
    'chicken salad', 'pizza',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print("- " + item)

menu_items = (
    'burgers', 'steak and chips', 'lamb shanks',
    'greek salad', 'nachos',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print("- " + item)





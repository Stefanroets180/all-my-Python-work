#p171 6-7person:
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'Johnny',
    'last_name': 'delong',
    'age': 56,
    'city': 'capetown',
}
people.append(person)

person = {
    'first_name': 'hennie',
    'last_name': 'brits',
    'age': 28,
    'city': 'johannesburg',
}
people.append(person)

person = {
    'first_name': 'ferdie',
    'last_name': 'zoelner',
    'age': 21,
    'city': 'durban',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'shark',
    'name': 'grey',
    'owner': 'danie',

}
pets.append(pet)

pet = {
    'animal type': 'parrot',
    'name': 'polly',
    'owner': 'mark',

}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'millo',
    'owner': 'bob',

}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

#6-9 Favorite Placees

favorite_places = {
    'Stevo': ['Mistickboer', 'Cape Town', 'Ponta'],
    'Burt': ['Hard_Rock_cafe', 'Durban'],
    'Rudie': ['Disnie_World', 'Burger_kink', 'Margate']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
#6-10 Favorite Numbers
favorite_numbers = {
    'Johnny': [42, 17],
    'whiehan': [42, 39, 56],
    'Coenie': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " Favorite numbers are:")
    for number in numbers:
        print("  " + str(number))

#6-11 Cities:
cities = {
    'Cape Town': {
        'country': 'South Africa',
        'population': 6158080,
        'churches': '20',
        },
    'vancouver': {
        'country': 'Canada',
        'population': 87600,
        'churches': '300',
        },
    'sydney': {
        'country': 'australia',
        'population': 1003285,
        'churches': '30',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    churches = city_info['churches'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print( 'number of', 'churches' + churches  )

#6.12

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print(pizza)
pizza['crust2'] = 'thin'
pizza['toppings2'] = 'chicken','avo'
print("Update pizza is:", pizza)
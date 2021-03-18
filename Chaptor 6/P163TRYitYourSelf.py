



glossary = {
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'value': 'An item associated with a key in a dictionary.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

rivers = {
    'vaalriver': 'vaaltriangel',
    'Tugelariveri': 'KwaZulu-Natal',
    'Breeriver': 'Westen Cape',
    'Hartsriver':'North West',
    'Olifantriver': 'Westen, Cape',
    }

for river, province in rivers.items():
    print("The " + river.title() + " flows through " + province.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(" - " + river.title())

print("\nThe following Province are included in this data set:")
for province in rivers.values():
    print("- " + province.title())


#6.6 polling
favorite_languages = {
    'frikkie': 'python',
    'martin': 'c',
    'johnny': 'ruby',
    'anton': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['frikkie', 'martin', 'johnny', 'anton', 'jp', 'dave', 'jack']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")

















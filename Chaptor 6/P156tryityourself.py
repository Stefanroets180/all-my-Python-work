#p156 6-1person:
personal_informations = {'first_name':'Stefan','last_name':'Roets','age':'33','city':'Pretoria'}
print(personal_informations)
print(personal_informations['first_name'])
print(personal_informations['last_name'])
print(personal_informations['age'])
print(personal_informations['city'])

#6-2. Favorite Numbers:
favorite_numbers = {
    'dino': 23,
    'PJ': 6,
    'Johnny': 66,
    'Frikkie': 12,
    'Rubert': 2,
    }

num = favorite_numbers['dino']
print("dino favorite number is " + str(num) + ".")

num = favorite_numbers['PJ']
print("PJ favorite number is " + str(num) + ".")

num = favorite_numbers['Johnny']
print("Johnny favorite number is " + str(num) + ".")

num = favorite_numbers['Frikkie']
print("Frikkie favorite number is " + str(num) + ".")

num = favorite_numbers['Rubert']
print("Rubert favorite number is " + str(num) + ".")
#6-3. Glossary:

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])



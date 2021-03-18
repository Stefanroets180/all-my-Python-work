magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

FriendNames = ['Johnny','Steve','anton','Mark']
for FriendName in FriendNames:
    print(f"\t{FriendName}")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Indenting Unnecessarily After The Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")

#Using the Rage() Function Numbers

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

#
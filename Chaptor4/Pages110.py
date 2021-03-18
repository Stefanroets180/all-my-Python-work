#4-3
for value in range(1,21):
    print(value)

#4-4
number = list(range(1,1000001))
print(number)

#4-5
print(min(number))

print(max(number))

print(sum(number))

#4-6
odd_numbers = list(range(3,1000001,3))
print(odd_numbers)

#4-7

threes = list(range(3, 31, 3))

for number in threes:
    print(number)

#4-8
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#4-9
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


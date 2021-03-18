try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("that's not a number idiot, I said number are you blind or can't you read. ")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")

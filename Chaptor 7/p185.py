#7-4:Pizza Topings
prompt = "\nPlease tell me a topping you would like to put " + \
    "on your pizza"
prompt += "\nFor end of the input enter 'quit': "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print ("'Okay il be adding " + topping.title(),'to your pizza!')

#7-5:Movie Ticket
prompt = "How old are you?"
prompt += "\nEnter 'exit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'exit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
#7_7
infinity_loop_name = 'stefan'
while infinity_loop_name <= 'stefan':
    print(infinity_loop_name)
    infinity_loop_name = 'stefan'
#7-6 is still in working progress
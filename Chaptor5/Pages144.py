#5-8 hello admin
usernames = ['anton', 'frikkie', 'admin', 'stan', 'martin']
for username in usernames:
    if username == 'admin':
        print("Hi there admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", why did you log in don't you have a life?")
#5-9 no users
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hi there admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", why did you log in don't you have a life?")
else:
    print("We need to find some users!")
#5-10 cheaking Usernames
current_users = ['anton', 'frikkie', 'admin', 'stan', 'martin']
new_users = ['emillo', 'rubert', 'jp', 'davie', 'zander']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
#5-11 ordinal numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

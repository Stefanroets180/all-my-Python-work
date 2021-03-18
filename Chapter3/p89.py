#3-4
guest_list = ['Tom,Delong','Frank,Senatran','Johnny,Depp']
print(guest_list)
message = f"dear guest you been invited to dinner {guest_list[0].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[1].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[2].title()}. "
print(message)
guest_list = ['Tom,Delong','Frank,Senatran','Johnny,Depp']
print(message)
del guest_list[0]
print(guest_list)
guest_list.insert(0,'Joe,Rogen')
print(guest_list)
message = f"dear guest you been invited to dinner {guest_list[0].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[1].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[2].title()}. "
print(message)
found_a_bigger_dinner_tabel = 'guest_list'
print(f"\nA {message.title()} I found a bigger dinner tabel.")
guest_list.insert(0,'David,Bowie')
print(guest_list)
guest_list.insert(2,'Charles,Manson')
print(guest_list)
guest_list.insert(5,'Tyson,Fury')
print(guest_list)
message = f"dear guest you been invited to dinner {guest_list[0].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[1].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[2].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[3].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[4].title()}. "
print(message)
message = f"dear guest you been invited to dinner {guest_list[5].title()}. "
print(message)
print(f"\nI {message.title()} can only invite two people for dinner.")
guest_list = ['David,Bowie','Joe,Rogen','Frank,Senatran','Johnny,Depp','Tyson,Fury']
print(guest_list)
last_guest = guest_list.pop()
print(f"I am sorry I can't invite you to dinner {last_guest.title()}. ")
last_guest = guest_list.pop()
print(f"I am sorry I can't invite you to dinner {last_guest.title()}. ")
last_guest = guest_list.pop()
print(f"I am sorry I can't invite you to dinner {last_guest.title()}. ")
last_guest = guest_list.pop()
print(f"I am sorry I can't invite you to dinner {last_guest.title()}. ")
message = f"dear guest you still  invited to dinner {guest_list[0].title()}. "
print(message)
del guest_list[0]
print(guest_list)
del guest_list[1]
print(guest_list)
#8-3:t-shirt
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'Baker Skateboard!')
make_shirt(message="nike.", size='medium')

#8-4:T-Shirt size
def t_shirt(shirt_size='L', printed_message='I love Python.'):
    """Print size of shirt and the message on the shirt"""
    print("\nT-shirt is of size " + shirt_size.upper() + ".")
    print("Message printed on a shirt: " + printed_message.title() + ".")

t_shirt()
t_shirt('m')
t_shirt('xl', printed_message='I am with stupid')

#8-5:cities
def describe_city(city, country='USA'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Houston')
describe_city('London', 'UK')
describe_city('New York')

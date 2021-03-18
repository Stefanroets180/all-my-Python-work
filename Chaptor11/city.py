def city_country(city, country):
    """Return a string like 'Cape Town, RSA'."""
    return f"{city.title()}, {country.title()}"

city = city_country('cape town', 'rsa')
print(city)

city = city_country('new york', 'usa')
print(city)

city = city_country('london', 'uk')
print(city)

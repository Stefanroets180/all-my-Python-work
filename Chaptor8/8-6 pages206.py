#8-6 City names
def city_country(city, country):
    """Return a string like 'Houston, USA'."""
    return f"{city.title()}, {country.title()}"

city = city_country('houston', 'usa')
print(city)

city = city_country('cape town', 'south africa')
print(city)

city = city_country('harare', 'zimbabwe')
print(city)


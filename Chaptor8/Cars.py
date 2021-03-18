def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_wrangler = make_car('jeep', 'wrangler', color='blue', tow_package=True)
print(my_wrangler)

my_old_corvette = make_car('chevrolet', 'corvette', year=1963, color='red',
        headlights='popup')
print(my_old_corvette)

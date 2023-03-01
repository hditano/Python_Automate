def city_functions(city, country, population=''):
    if population:
        return f'{city}, {country} - population {population}'
    return f'{city} {country}'

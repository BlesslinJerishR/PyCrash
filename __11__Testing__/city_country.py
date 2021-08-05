# 11.1
# To get the city info
def info(city, country, population=" "):
    if population:
        infos =f'{city}, {country} - population {population}'
    else:
        infos =f'{city}, {country}'
    return infos
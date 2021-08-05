# 8.5
def describe_city(city, country):
    """To get city and its country"""
    print(f'{city} city is in country {country}')


describe_city('chennai', 'India')
describe_city('coimbatore', 'India')

def describe_city(city, country='America'):
    """To get city and its country"""
    print(f'{city} city is in country {country}')


describe_city('Los Angeles')
describe_city('Little India', country='Singapore')
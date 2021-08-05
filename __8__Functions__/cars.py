# 8.14
def make_cars(company, manufacturer, **car_info):
    """To gather info about cars"""
    car_info['company'] = company
    car_info['manufacturer'] = manufacturer
    print(car_info)
    return car_info

if __name__ == '__main__':
    make_cars('Jaguar', 'Tata', color='Brown', type='XE' )



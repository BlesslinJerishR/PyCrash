# 9.1

class Restaurant:
    """Creating a Restaurant class"""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """assigning name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def description(self):
        """about"""
        print(f"{self.restaurant_name} is Located in chennai")
        print("Non veg is also available")

    def availability(self):
        """open"""
        print(f'{self.restaurant_name} Restaurant is open now')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served = self.number_served + increment_number_served


if __name__ == '__main__':
    ss = Restaurant('SS Hyderabad', 'Biryani')
    print(ss.restaurant_name)
    print(ss.cuisine_type)
    ss.description()
    ss.availability()

    print()

    # 9.2
    muthu = Restaurant('Muthulakshmi', 'Fast food')
    print(muthu.restaurant_name)
    print(muthu.cuisine_type)
    muthu.description()
    muthu.availability()

    print()

    padi = Restaurant('Padi Kattu Kadai', 'Maligai Samanam')
    print(padi.restaurant_name)
    print(padi.cuisine_type)
    padi.description()
    padi.availability()



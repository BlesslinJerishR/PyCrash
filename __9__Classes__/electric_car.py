# 9.9
from cars import Car


class Battery:
    def __init__(self, power=75):
        self.battery_power = power

    def battery_description(self):
        print(f'This car has a battery power of {self.battery_power} KWH')

    def battery_upgrade(self):
        if self.battery_power < 100:
            self.battery_power = 100
            print("Battery upgrade successfull")
        else:
            print("The battery is already full")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year, battery_type):
        super().__init__(manufacturer, model, year, battery_type)
        self.battery = Battery()
        self.type = 'battery'
        self.battery_size = 75

    def petrol_tank(self, type):
        if self.type == 'battery':
            print("Car runs on battery Mr.Genius")

    def battery_range(self):
        if self.battery.battery_power == 75:
            print(f"This Car can travel upto 50 kms with the battery of {self.battery.battery_power} KWH")
        elif self.battery.battery_power < 75:
            print(f"This Car can travel upto 40 kms with the battery power less than {self.battery.battery_power} KWH")

    def update_battery(self, battery_level):
        self.battery.battery_power = battery_level
        print(f"Battery level updated \nCurrent Battery level = {battery_level}")
        return battery_level

    def battery_info(self):
        print(f'This car has a battery capacity of {self.battery.battery_power} KWH')


tesla = ElectricCar('Tesla motors', 'Tesla S', 2016, 'battery')
print(f'Manufacturer : {tesla.manufacturer} \nModel : {tesla.model} \nYear : {tesla.year}')
tesla.get_descriptive_name()
tesla.battery_info()
tesla.petrol_tank('battery')
tesla.battery.battery_description()
tesla.battery_range()
tesla.update_battery(45)
tesla.battery_info()
tesla.battery_range()
tesla.battery_info()
tesla.battery.battery_upgrade()
tesla.battery_info()

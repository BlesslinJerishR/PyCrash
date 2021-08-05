class Car:
    """A simple attempt to represent a car."""
    def __init__(self, manufacturer, model, year, type):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.type = type

    def get_descriptive_name(self):
        long_name = f"{self.year} - {self.manufacturer} - {self.model}"
        print(long_name.title())
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def petrol_tank(self, petrol):
        if self.type == petrol:
            return "This car runs on petrol"


if __name__ == '__main__':
    jaguar = Car('TATA', 'Jaguar', 1990, 'petrol')
    print(f'Manufacturer : {jaguar.manufacturer} \nName : {jaguar.model} \nYear : {jaguar.year}')
    print(jaguar.petrol_tank('petrol'))

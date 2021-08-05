# 9.6
# importing
from restaurant import Restaurant
from _0_AddOns.defs import comma_remover


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, number_served, *flavours):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = flavours

    def flavours_available(self):
        flavours = []
        for flavour in self.flavours:
            flavours.append(flavour)
        print(f"Ice Cream Flavours available in {self.restaurant_name} are : ", end=" ")
        return comma_remover(flavours)


arun_ice_creams = IceCreamStand('Arun Ice Creams', 'Ice Creams and Juices', 10, 'apple', 'mango', 'orange')
arun_ice_creams.flavours_available()

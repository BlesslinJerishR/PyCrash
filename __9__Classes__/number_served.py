# 9.4

from restaurant import Restaurant

saravana_bhavan = Restaurant("Saravana Bhavan", "Vegetarian", 10)
print(f"Restaurant namer : {saravana_bhavan.restaurant_name}")
print(f"Cuisine Type : {saravana_bhavan.cuisine_type}")
print(f"Numbers served : {saravana_bhavan.number_served}")

saravana_bhavan.set_number_served(20)
print(f"After updating : {saravana_bhavan.number_served}")
saravana_bhavan.increment_number_served(5)
print(f"Numbers served after increment : {saravana_bhavan.number_served}")
print(f"Total people served in the day of business is {saravana_bhavan.number_served}")

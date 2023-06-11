# strings with embedded variable by using {}

my_name = 'Zed A. Show'
my_age = 35
my_height = 170 #cm
my_weight = 88 #kg
my_eyes = 'black'
my_teeth = 'brown'
my_hair = 'black'

print(f"Lets talk about {my_name}")
print(f"He's {my_height}cm tall.")
print(f"He's {my_weight}kg heavy.")
print(f"Actually that's not too heavy, right?")
print(f"He's got {my_eyes} eyes  and {my_hair} hair.")
print(f"His teeth {my_teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age} , {my_weight} and {my_height} I get {total}")
import temp_calc

# What would the temperature in Fahrenheit be if it were 18 degrees in celcius
cel = 18.5
# calling the function, in the other file, using a keyword argument and unpacking the tuple returned to retrieve an answer
print(f"Celsius = {cel}\nFahrenheit = {temp_calc.calculate_temperature(celsius=cel)[1]:.1f}")

fahrenheit = lambda cel: cel*(9/5)+32 # create lambda function
print(f"When celsius = {cel:.1f} then fahrenheit = {fahrenheit(cel):.1f}") # used within print because it was quicker to create in the page than reference the calculator

# Now I want to convert lists of temp values using lambda functions and list comprehensions to see them both working
# and produce a rough table that gives some key data points from celsius in fahrenheit and kelvin and converts the temperature into newtons
tuple_data_points = -20, -10, 0, 10, 20, 30, 40

tuple_fahrenheit = tuple(map(lambda c: c*(9/5)+32, tuple_data_points)) # uses lambda on a tuple
tuple_kelvin = tuple(c + 273.15 for c in tuple_data_points) # uses list comprehension on a tuple
list_newton = list(map(lambda c: c*(33/100), tuple_data_points)) # uses lambda on a list

list_headers = ["Celsius", "Fahrenheit", "Kelvin", "Newton"]

for item in list_headers:
    print(f"{item:>15s}|", end='')
for i in range(len(tuple_data_points)):
    print(f"\n|{tuple_data_points[i]:14.1f}|{tuple_fahrenheit[i]:15.1f}|{tuple_kelvin[i]:15.1f}|{list_newton[i]:15.1f}|")

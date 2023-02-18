# Revisiting a Codecademy Project - Kelvin Weather Project, Lets use **kwargs

celsius_today = 9.8855777

# A temperature calculator that can take multiple keyword arguments (**kwargs)
# and uses an invisible dictionary to store those values
def calculate_temperature(**temperature): # (**temperature) refers to several arguments that I might feed in referenced by keywords
    if "celsius" in temperature.keys(): # these arguments are stored in an invisible dictionary (that can be printed) and accessed in the same way we usually access a dictionary
        celsius = temperature["celsius"]
        return celsius, int(celsius*(9/5)+32), int(celsius + 273.15)
    elif "fahrenheit" in temperature.keys():
        fahrenheit = temperature["fahrenheit"]
        return int((fahrenheit-32)*5/9), fahrenheit, int(((fahrenheit-32)*5/9) + 273.15)
    else:
        # if given a kelvin value
        kelvin = temperature["kelvin"] - 273.15
        return int(kelvin - 273.15), int((kelvin - 273.15)*(9/5)+32), kelvin
    #returns a tuple containing (celsius, fahrenheit, kelvin)
    
# This is a cool calculator that I might want to use elsewhere so I only want to call this function if I am in this file, not if I am referencing the function from another file
if __name__ == "__main__":

# Each return in the function produces a tuple that can be unpacked
# We can use the calculator by calling the functions within the print function using {} and identify which part of the tuple to send in to the print function components.
    print(f'Today\'s temperature is {int(celsius_today)}.\nThat is {int(calculate_temperature(celsius=celsius_today)[1])} in fahrenheit.\nAnd {int(calculate_temperature(celsius=celsius_today)[2])} in kelvin.')

# test
    print("celsius", calculate_temperature(celsius=20))
    print("fahrenheit", calculate_temperature(fahrenheit=80)) # should return a tuple
    print("kelvin", calculate_temperature(kelvin=0)) # should return a tuple

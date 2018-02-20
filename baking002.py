import temperature_program002

def get_preheating_instruction(fahrenheit):
    """ (number) -> string
    
    Return instruction for preheating the oven in Fahrenheitdegrees and
    Celsius degrees.
    
    >>> get_preheating_instruction(500)
    'Preheat oven 500 degrees F (260.0 degrees C).'
    """
    
    cels = str(temperature_program002.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F ('+ cels +' degrees C).'


fahr = float(input('Enter the baking temperature in degrees Fahrenheit: '))
print(get_preheating_instruction(fahr))

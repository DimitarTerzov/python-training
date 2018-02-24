def convert_to_celsius(fahrenheit):
    """ (number) -> float
    
    Return the number of Celsius degrees equivalent  to Fahrenheit.
    
    >>> convert_to_celsius(75)
    23.88888888888889
    """
    
    return (fahrenheit - 32) * 5 / 9

def above_freezing(celsius):
    """ (number) -> bool
    
    Return TRUE iff temperature celsius degrees is above freezing.
    
    >>> above_freezing(25)
    True
    >>> above_freezing(-9)
    False
    """
    
    return celsius > 0


if __name__ == '__main__':
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print('It is above Celsius freezing.')
    else:
        print('It is below Celsius freezing.')
    
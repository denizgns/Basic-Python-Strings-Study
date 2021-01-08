"""
#Student Name: Deniz Güneş
This program converts a celsius to fahrenheit degrees.
"""

import random


def convert_celsius_to_fahrenheit(celsius):
    """
    >>> convert_celsius_to_fahrenheit(37)
    98.60
    >>> convert_celsius_to_fahrenheit(45)
    113.00
    """
    F = ((celsius * 9) / 5) + 32
    return F

def convert_fahrenheit_to_celsius(fahrenheit):
    """
    >>> convert_fahrenheit_to_celsius(32)
    0.00
    >>> convert_fahrenheit_to_celsius(97)
    36.11
    """
    C = ((fahrenheit - 32) * 5) / 9
    return C

def random_celsius():
    """
    Should return a random integer between [-273, 1000]
    """
    celsius = random.randint(-273, 1000)
    return celsius

def random_fahrenheit():
    """
    Should return a random integer between [-459, 1832]
    """
    fahrenheit = random.randint(-459, 1832)
    return fahrenheit

def celsius_or_fahrenheit():
    """
    Should return a boolean that decides which conversion will be made.
    This boolean should be used in main method to decide.
    Hint: if statements are very useful for this job.
    """
    decision = random.randint(0, 1)
    if decision == 0:
        return 'Celsius'
    if decision == 1:
        return 'Fahrenheit'

def random_convert():
    '''
    To randomly convert celcius or fahrenheit.
    Wrote this to have a more simpler main
    :return: randomly converted numbers in a proper string
    '''
    decide = celsius_or_fahrenheit()
    if decide == 'Celsius':
        print('Celsius to fahrenheit randomly selected')
        C = random_celsius()
        F = convert_celsius_to_fahrenheit(C)
        print(format(C, '.2f')  + ' celsius is ' + format(F, '.2f') + ' fahrenheit')
    elif decide == 'Fahrenheit':
        print('Fahrenheit to celsius randomly selected')
        F = random_fahrenheit()
        C = convert_fahrenheit_to_celsius(F)
        print(format(F, '.2f') + ' fahrenheit is ' + format(C, '.2f') + ' celsisus')
def main():
    print('This program randomly chooses celsius or fahrenheit and converts one to another')
    random_convert()
    print('End of program')


if __name__ == '__main__':
    main()
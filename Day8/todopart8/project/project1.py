from parser import parse
from converter import feet_to_meter

feet_inches = input('Enter the length in feet and inches: ')

print(
    f"{parse(feet_inches)['feet']} feet and {parse(feet_inches)['inches']} inches in equal to {feet_to_meter(feet_inches)} meters")

if feet_to_meter(feet_inches) < 1:
    print('The kid is too small.')
else:
    print('The kid can use the slide.')

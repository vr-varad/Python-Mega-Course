feet_inches = input('Enter the length in feet and inches: ')

def parse(feet_inches):
    length = list(map(lambda x: float(x), feet_inches.split(' ')))
    return {'feet':length[0],'inches':length[1]}


def feet_to_meter(inp):
    feet = parse(inp)['feet']
    inches = parse(inp)['inches']
    len_in_met = (feet * 30 + inches * 2.5) / 100
    return len_in_met


print('Length in meters:', feet_to_meter(feet_inches), 'm')

if feet_to_meter(feet_inches) < 1:
    print('The kid is too small.')
else:
    print('The kid can use the slide.')
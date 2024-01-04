from parser import parse

def feet_to_meter(inp):
    feet = parse(inp)['feet']
    inches = parse(inp)['inches']
    len_in_met = (feet * 30 + inches * 2.5) / 100
    return len_in_met

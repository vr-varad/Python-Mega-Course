def parse(feet_inches):
    length = list(map(lambda x: float(x), feet_inches.split(' ')))
    return {'feet': length[0], 'inches': length[1]}

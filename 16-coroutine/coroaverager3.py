from collections import namedtuple

# input dict{'girls;kg': [55,60,50,45,90], ....}

Result = namedtuple('Result', 'count average')

# the subgenerator
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

# the delegating generator
def grouper(result, key):
    while True:
        result[key] = yield from averager()

# caller
def main(data):
    result = {}
    for key, values in data.items():
        group = grouper(result, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(result)
# output report
def report(result):
    for key, value in sorted(result.items()):
        group, measure = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            value.count,
            group,
            value.average,
            measure
        ))

data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}
if __name__ == '__main__':
    main(data)



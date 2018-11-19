import re

N, S, E, W = "NORTH", "SOUTH", "EAST", "WEST"
DIRS = {N: (0, 1), S: (0, -1), E: (1, 0), W: (-1, 0)}
TURNS = {"LEFT": {DIRS[N]: DIRS[W], DIRS[S]: DIRS[E], DIRS[E]: DIRS[N], DIRS[W]: DIRS[S]},
         "RIGHT": {DIRS[N]: DIRS[E], DIRS[S]: DIRS[W], DIRS[E]: DIRS[S], DIRS[W]: DIRS[N]}}

PATTERN = re.compile(r"Head (?P<head>\w+)" +
                     r"|Take the (?P<nTurn>\d*)(?P<isNext>\w+) (?P<turnTo>LEFT|RIGHT)" +
                     r"|Go straight on for (?P<straight>[\d.]+)(?P<unit>k?m)" +
                     r"|(?P<flip>Turn around!)")


def sat_nav(directions):
    def go(d):
        return x + d * moves[0], y + d * moves[1]

    x, y, moves = 0, 0, (0, 0)
    for i in range(len(directions) - 1):
        d, m = 0, PATTERN.match(directions[i])

        if m.group('straight'):
            d = round(10 * float(m.group('straight')))
            if m.group('unit') == 'm': d //= 1000
            x, y = go(d)

        elif m.group('turnTo'):
            d = 10 * (m.group('isNext') == 'NEXT' or int(m.group('nTurn')))
            x, y = (z - z % (10 if dz > 0 else -10) for z, dz in zip(go(d), moves))
            moves = TURNS[m.group('turnTo')][moves]

        elif m.group('flip'):
            moves = -moves[0], -moves[1]
        elif m.group('head'):
            moves = DIRS[m.group('head')]

    return [x, y]


def test():
    assert [0, 0] == sat_nav([
        'Head EAST',
        'Take the 2nd LEFT',
        'Take the NEXT LEFT',
        'Take the NEXT LEFT',
        'Go straight on for 1.5km',
        'Take the NEXT RIGHT',
        'Take the 2nd RIGHT',
        'Go straight on for 1.7km',
        'Turn around!',
        'Take the NEXT LEFT',
        'Go straight on for 1.0km',
        'You have reached your destination!'
    ])
    assert [0, -1] == sat_nav([
        'Head NORTH',
        'Take the 2nd LEFT',
        'Take the 2nd LEFT',
        'Take the NEXT LEFT',
        'Go straight on for 3.5km',
        'Take the NEXT RIGHT',
        'Go straight on for 2.3km',
        'Take the NEXT RIGHT',
        'Take the NEXT RIGHT',
        'Take the NEXT LEFT',
        'Take the NEXT RIGHT',
        'Go straight on for 900m',
        'You have reached your destination!'
    ])


def main():
    test()


if __name__ == '__main__':
    main()

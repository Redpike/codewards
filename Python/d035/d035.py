directions = {
    'NORTH': [0, 1],
    'SOUTH': [0, -1],
    'WEST': [-1, 0],
    'EAST': [1, 0]
}


def sat_nav(directions):
    # Your code here!
    pass


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

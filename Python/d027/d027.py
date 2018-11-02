def rgb(r, g, b):
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b

    hex_string = hex(r).split('x')[-1].zfill(2) + hex(g).split('x')[-1].zfill(2) + hex(b).split('x')[-1].zfill(2)
    return hex_string.upper()


def test():
    assert "000000" == rgb(0, 0, 0)
    assert "010203" == rgb(1, 2, 3)
    assert "FFFFFF" == rgb(255, 255, 255)
    assert "FEFDFC" == rgb(254, 253, 252)
    assert "00FF7D" == rgb(-20, 275, 125)


def main():
    test()


if __name__ == '__main__':
    main()

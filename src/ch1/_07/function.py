def func(x: int, y: str, z: float):
    return "{x}時の{y}は{z}".format(x=x, y=y, z=z)


if __name__ == '__main__':
    x: int = 12
    y: str = "気温"
    z: float = 22.4
    result = func(x, y, z)
    print(result)

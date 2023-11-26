from geometry.figure import Area

if __name__ == '__main__':

    print(*Area(3).result)
    print(*Area(3, 4).result)
    print(*Area(3, 5, 4).result)
    print(*Area(3, 5, 5).result)

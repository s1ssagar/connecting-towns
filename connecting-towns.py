def connecting_towns():
    tc = input()
    while tc > 0:
        towns = input()
        routes = map(int, raw_input().strip().split(' '))
        prod = 1
        for x in routes:
            prod *= x
        print prod % 1234567
        tc -= 1

def main():
    connecting_towns()

if __name__ == "__main__":
    main()
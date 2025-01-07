def max3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def solve(num_of_moves, p1, p2, p3, m1, m2, m3):
    for x1 in range(num_of_moves):
        for x2 in range(num_of_moves):
            for x3 in range(num_of_moves):
                max = max3(x1, x2, x3)
                if 2*max == x1 + x2 + x3:
                    if (x1 + x2 + x3) % 2 == 0:
                        if (p1 + x1) % m1 == 0 and (p2 + x2) % m2 == 0 and (p3 + x3) % m3 == 0:
                            print(f"Solved in {round((x1+x2+x3)/2)} moves")
                            return (x1,x2,x3)
    print("Solution not found")
    return (-1, -1, -1)


def main():
    p1 = int(input("First ring's position  (p1): "))
    p2 = int(input("Second ring's position (p2): "))
    p3 = int(input("Third ring's position  (p3): "))
    print()
    m1 = int(input("First ring's cycle  (m1): "))
    m2 = int(input("Second ring's cycle (m2): "))
    m3 = int(input("Third ring's cycle  (m3): "))
    print()
    num_of_moves = int(input("Number of moves given: "))
    print()

    solution = solve(num_of_moves, p1, p2, p3, m1, m2, m3)
    print(f"solution:")
    print(f"x1: {solution[0]}")
    print(f"x2: {solution[1]}")
    print(f"x3: {solution[2]}")

if __name__ == "__main__":
    main()
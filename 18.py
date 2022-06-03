def direction(l):
    e_count = l.count("EAST")
    w_count = l.count("WEST")
    n_count = l.count("NORTH")
    s_count = l.count("SOUTH")

    d = []

    e_w = abs(e_count - w_count)
    n_s = abs(n_count - s_count)

    if e_count >= w_count:
        for i in range(e_w):
            d.append("EAST")

    else:
        for j in range(e_w):
            d.append("WEST")

    if n_count >= s_count:
        for i in range(n_s):
            d.append("NORTH")

    else:
        for j in range(n_s):
            d.append("SOUTH")

    return d

if __name__ == '__main__':
    directions = eval(input("Enter the array of directions: "))

    reduced_directions = direction(directions)

    print("New directions:", reduced_directions)

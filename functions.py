def sum_num(a, b):
    sum_ab = a + b
    return sum_ab


def max_el_list(my_list):
    max_el = max(my_list)
    return max_el


def main():
    sum_xy = sum_num(3, 2)
    print max_el_list([0, 3, 0.5, 1])
    print sum_xy
    print sum_num(3, 5)


def args_to_dict(x1, x2, y1, y2):
    rectangle = {
        'A': (x1, y1),
        'B': (x2, y1),
        'C': (x2, y2),
        'D': (x1, y2),
        'width': x2 - x1,
        'height': y2 - y1,
        'pl': (x2 - x1) * (y2 - y1),
        'ob': 2 * (x2 - x1) + 2 * (y2 - y1)
    }

    return rectangle


if __name__ == '__main__':
    main()


def sum_list(list):
    if list == []:
        return 0
    print(list[0] + sum_list(list[1:]))
    return list[0] + sum(list_list[1:])


def max_num(list):
    if list == []:
        return 0
    return list[0]


def max_list(list):
    if len(list) == 2:
        print(list[0] if list[0] > list[1] else list[1])
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_list(list[1:])
    print(list[0] if list[0] > sub_max else sub_max)
    return list[0] if list[0] > sub_max else sub_max


def main():
    max_list()

if __name__ == "__main__":
    main()

# coding=utf-8


# def reverse_print_multi():
#     for i in range(1, 10):
#         for x in range(1, i):
#             print(end="             ")
#         for k in range(i, 10):
#             print("{0} * {1} = {2}   ".format(i, k, i * k), end="")
#         print("")


def reverse2():
    start = 9
    ans = []
    for i in range(0, 9):
        ans.append(start)
        start -= 1
        for j in range(ans[i], 0, -1):
            print(str(ans[i]) + '*' + str(j) + '=' + str(ans[i] * j) + ' ', end="")
        print("")


if __name__ == '__main__':
    # reverse_print_multi()
    reverse2()

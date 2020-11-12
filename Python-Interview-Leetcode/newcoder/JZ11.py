def NumberOf1(n):
    # write code here
    cot = 0
    if n < 0:
        ans = bin(2 ** 32 + n).replace('0b', '')
        print(ans)
        for i in ans:
            if i == '1':
                cot += 1
        return cot

    elif n == 1:
        return 1

    else:
        ans = bin(n).replace('0b', '')
        for i in ans:
            if i == '1':
                cot += 1
        return cot


if __name__ == '__main__':
    print(NumberOf1(5))

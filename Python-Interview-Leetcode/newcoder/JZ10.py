# -*- coding:utf-8 -*-


def rectCover(number):
    # write code
    if number == 0:
        return 0
    
    if number == 1:
        return 1
    
    if number == 2:
        return 2
    
    else:
        ans = rectCover(number - 1) + rectCover(number - 2)
    
    return ans


def rectCover1(number):
    # write code
    #     li = [0, 1, 2]
    #
    #     if number == 0:
    #         return li[0]
    #
    #     if number == 1:
    #         return li[1]
    #
    #     if number == 2:
    #         return li[2]
    #
    #     for i in range(3, number + 1):
    #         li[i] = rectCover(number - 1) + rectCover(number - 2)
    #
    #     return li[number]



if __name__ == '__main__':
    print(rectCover(5))
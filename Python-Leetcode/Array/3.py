from itertools import permutations


def solution():
    data = list(map(int, input().split()))
    
    ans = list(permutations(data, 3))
    sorted(ans)
    temp = []
    for i in ans:
        if int(str(i[0]) + str(i[1]) + str(i[2])) < 100:
            ans.remove(i)
        else:
            temp.append(i)
            
    min_v = ''
    max_v = ''
    for x in min(temp):
        min_v += str(x)
    for y in max(temp):
        max_v += str(y)
    
    print(min_v)
    print(max_v)
    # print(ans)
    # print(temp)
    return int(max_v) - int(min_v)


if __name__ == '__main__':
    print(solution())

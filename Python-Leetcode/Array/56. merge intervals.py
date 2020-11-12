#coding=utf-8
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


if __name__ == '__main__':
    ll = [[2, 6], [8, 10], [15, 18], [1, 3]]
    print(merge(ll))


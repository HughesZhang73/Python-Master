
def bit_add(a:int, b:int) -> int:
    res = a
    carry = b
    while carry:
        temp = res
        res = (res ^ carry)
        carry = (temp & carry) << 1
    return res


def convert_to_negative(num: int) -> int:
    return bit_add(~num, 1)
    
    
def bit_minus(a: int, b: int) -> int:
    return bit_add(a, convert_to_negative(b))


if  __name__ == '__main__':
    # print(bit_add(2, 12))
    print(bit_minus(4, 2))
    
# coding=utf-8

import unittest


def ip_covert_to_int(ip: str) -> int:
    temp = ip.split('.')
    str_num = ''
    for i in temp:
        str_num += str(bin(2 ** 8 + int(i)).replace('0b', '')[1:])
    # print(str_num)
    return int(str_num, 2)


def int_convert_to_ip(num: int):
    temp = bin(num).replace('0b', '')
    ll = [temp[i:i + 8] for i in range(0, len(temp), 8)]
    # print(ll)
    ip = []
    for i in ll:
        ip.append(str(int(i, 2)))
    # print(ip)
    return '.'.join(ip)


# class MyTestCase(unittest.TestCase):
#     def test_ip_to_int(self):
#         a = "123.125.0.236"
#         b = "192.168.122.234"
#
#         ans1, ans2 = map(ip_covert_to_int, (a, b))
#         self.assertEqual(2071789804, ans1)
#         self.assertEqual(3232266986, ans2)
#
#     def test_int_to_ip(self):
#         a1 = 2071789804
#
#         ans3 = int_convert_to_ip(a1)
#
#         self.assertEqual("123.125.0.236", ans3)


if __name__ == '__main__':
    # unittest.main()
    print(ip_covert_to_int("123.125.0.236"))
    print(int_convert_to_ip(2071789804))

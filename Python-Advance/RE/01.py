import re

str1 = 'imooc'
pa = re.compile(r'imooc')
print(type(pa))
ma = pa.match(str1)

print(ma.group())
print(ma.span())

print(ma.string)


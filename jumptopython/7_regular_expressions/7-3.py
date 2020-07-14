import re
# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'Life is too short, you need python'))

# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group(0))

# p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-2054-9719")
# print(m.group(0))

# p = re.compile(r'(\b\w+)\s+\1')
# p.search('Paris in the the spring').group()

# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group("name"))

# p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
# print(
# p.search("Paris is the the spring").group()
# )

# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())

# p = re.compile('(blue|white|red)')
# print(
# p.subn('colour','blue socks and red shoes')
# )

# p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

# def hexrepl(match):
#     value = int(match.group())
#     return hex(value)
#
# p = re.compile(r'\d+')
# print(
# p.sub(hexrepl, 'Call 65490 for printing, 49512 for user code')
# )

s = '<html><head><title>Title</title>'
len(s)
print(re.match('<.*?>',s).span())
print(re.match('<.*?>',s).group())

import re

data = """
park 970202-1523412
kim 960321-2534123
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

"""convert MAC format from XXXX:XXXX:XXXX to XXXX.XXXX.XXXX"""

'''def split_this(LONG_STRING, SIGN):
    """Return both strip and split by SIGN methods of LONG_STRING"""
    return LONG_STRING.strip().split(SIGN)
'''
MAC = "AAAA:BBBB:CCCC"

print(MAC.replace(":", "."))
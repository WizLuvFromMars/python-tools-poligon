"""AAAA.BBBB.CCCC mac to AA:AA:BB:BB:CC:CC."""

from netaddr import EUI, mac_unix_expanded

# def main():
# 	pass

SOME_FILE = open(r'C:\Users\ssukhonx\Documents\pyhton_tools\list.txt', 'r')
TEST_MAC = EUI('00aA.BbBB.cCcC', dialect=mac_unix_expanded)
print(TEST_MAC)

# print(SOME_FILE.read())

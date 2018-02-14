"""format OSPF ROUTE output string"""

def split_this(long_string):
    """Return both strip and split methods of string"""
    return long_string.strip().split()

OSPF_ROUTE = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
TITLE_LIST = ["Protocol:",
              "Prefix:",
              "AD/Metric:",
              "Next-Hop:",
              "Last update:",
              "Outbound Interface:"]

FINAL_LIST = split_this(OSPF_ROUTE.replace(',', ''))
FINAL_LIST.remove('via')
FINAL_LIST[2] = FINAL_LIST[2][1:-1]

D = dict(zip(TITLE_LIST, FINAL_LIST))

for key in D:
    print('{:22} {:22}'.format(key, D[key]))

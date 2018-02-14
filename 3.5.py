""" Sort a list of VLANs """

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLAN_SET = list(set(VLANS))
VLAN_SET.sort()
print(VLAN_SET)
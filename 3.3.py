""" Get VLAN list from CONFIG string """

CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
VLAN = CONFIG.split()[-1].split(",")

print(VLAN)
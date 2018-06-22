"""list of common VLANs."""


def int_in_list(a_list):
    """Convert a_list elements to int type."""
    counter = 0
    for elem in a_list:
        a_list[counter] = int(elem)
        counter += 1


COMMAND1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
COMMAND2 = "switchport trunk allowed vlan 1,3,100,200,300"

COMMAND_LIST = [COMMAND1, COMMAND2]
COMMON_VLAN = []

for element in COMMAND_LIST:
    ADDIT = element.split()[-1].split(",")
    int_in_list(ADDIT)
    COMMON_VLAN.append(ADDIT)
    # print(set(COMMON_VLAN))

print(set(COMMON_VLAN[0]).intersection(set(COMMON_VLAN[1])))

"""Substitution."""

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
INJECT = "Gigabit"
print(NAT.replace('Fast', 'Gigabit'))

""" Convert IP from decimal to binary form """
from scriptsuit import int_in_list

IP = '192.168.3.1'
IP_LIST = IP.split('.')

k = 1
inter = ' '
print('{l[0]:10}{inter}{l[1]:10}{inter}{l[2]:10}{inter}{l[3]:10}'.format(l=IP_LIST, inter=inter*k))
int_in_list(IP_LIST)
print('{l[0]:08b}   {l[1]:08b}   {l[2]:08b}   {l[3]:08b}'.format(l=IP_LIST))
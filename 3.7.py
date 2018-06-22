"""Convert IP from decimal to binary form."""
from scriptsuit import int_in_list

IP = '192.168.3.1'
IP_LIST = IP.split('.')

k = 1
inter = ' '
print('{alist[0]:10}{inter}{alist[1]:10}{inter}{alist[2]:10}{inter}{alist[3]:10}'.format(alist=IP_LIST, inter=inter * k))
int_in_list(IP_LIST)
print('{alist[0]:08b}   {alist[1]:08b}   {alist[2]:08b}   {alist[3]:08b}'.format(alist=IP_LIST))

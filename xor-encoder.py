#!/usr/bin/python

# Python XOR encoder by Vivek

shellcode = ()

encoded = ''
encoded2 = ''

print 'Encoded shellcode ...'

for x in bytearray(shellcode):

	# XOR encoding
	y = x^0xAA
	encoded += '\\x'
	encoded += '%02x' % y

	encoded2 += '0x'
	encoded2 += '%02x,' % y

print encoded
print encoded2

print 'Len: %d' % len(bytearray(shellcode))

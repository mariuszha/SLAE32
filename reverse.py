#!/usr/bin/python
import sys


input = str(sys.argv[1])

print 'String length: %s' % len(input)
print ''

if len(input) % 4 != 0:
	print 'Length of the string is not a multiple of 4!'

else:
	stringList = [input[i:i+4] for i in range(0, len(input),4)]
	
	for item in stringList[::-1]:
		print item[::-1] + ': ' + str(item[::-1].encode('hex')) 

print ''
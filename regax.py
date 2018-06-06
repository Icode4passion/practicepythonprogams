import re

def multi_pattern(pattern,phrase):

	for pat in pattern:
		print "Searching for pattern {}".format(pat)
		print re.findall(pat,phrase)
		print "\n"

test_phrase = 'sdsd..sssddd..sdddsdd...dsds...dsssss...sdddd'
test_pattern = ['sd?']

multi_pattern(test_pattern,test_phrase)
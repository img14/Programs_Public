"""
Program to decode a shift cipher with a key
"""

ciphertext = raw_input("Enter cipher text: ")
key = raw_input("Enter key: ")

ln = len(key)
list_of_stuff = []
list_of_decoded = []

def parse_into_strings():
	for i in range(ln):
		string = ""
		x = i
		while x < len(ciphertext):
			string = string + ciphertext[x]
			x = x + ln
		list_of_stuff.append(string)

def decode_strings():
	k = 0
	for s in list_of_stuff:
		shift = ord(key[k]) - 97
		st = shift_decode(s, shift)
		list_of_decoded.append(st)
		k = k + 1

def shift_decode(tx, sh):
	string = ""
	for c in tx:
		v = ord(c) - sh
		if v < 97:
			v = v + 26
		string = string + "%s"%chr(v)
	return string

def put_together():
	final_string = ""
	for xx in range(len(ciphertext)/len(key)):
		for y in list_of_decoded:
			final_string = final_string + y[xx]
	print(final_string)

parse_into_strings()
decode_strings()
put_together()
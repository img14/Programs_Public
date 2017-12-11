"""
Methods to decode and encode a vignere cipher
"""

def caeser_shift(plaintext, char):
	shift = ord(char) - 65
	string = ""
	for c in plaintext:
		t = ord(c) + shift
		if t > 90:
			t = t - 26
		elif t < 65:
			t = t + 26
		string = string + str(chr(t))
	return string

def caeser_unshift(ciphertext, char):
	shift = ord(char) - 65
	string = ""
	for c in ciphertext:
		t = ord(c) - shift
		if t > 90:
			t = t - 26
		elif t < 65:
			t = t + 26
		string = string + str(chr(t))
	return string

def caeser_brute_force(ciphertext):
	caeser_brute_force_list = []
	for i in range(65, 91):
		caeser_brute_force_list.append(caeser_unshift(ciphertext, chr(i)))
	return caeser_brute_force_list

def split_by_keyword(eithertext, keyword):
	list_of_split_strings = []
	for i in range(len(keyword)):
		string = ""
		x = i
		while x < len(eithertext):
			string = string + eithertext[x]
			x = x + len(keyword)
		list_of_split_strings.append(string)
	return list_of_split_strings

def vignere_encode(plaintext, keyword):
	plaintext = plaintext.upper()
	list_of_encoded = []
	strings = split_by_keyword(plaintext, keyword)
	k = 0
	for s in strings:
		st = caeser_shift(s, keyword[k])
		list_of_encoded.append(st)
		k = k + 1
	final_string = ""
	for xx in range(len(plaintext)/len(keyword)):
		for y in list_of_encoded:
			final_string = final_string + y[xx]
	return final_string

def vingnere_decode(ciphertext, keyword):
	ciphertext = ciphertext.upper()
	list_of_decoded = []
	strings = split_by_keyword(ciphertext, keyword)
	k = 0
	for s in strings:
		st = caeser_unshift(s, keyword[k])
		list_of_decoded.append(st)
		k = k + 1
	final_string = ""
	for xx in range(len(ciphertext)/len(keyword)):
		for y in list_of_decoded:
			final_string = final_string + y[xx]
	return final_string

def get_frequencies(ciphertext):
	freq_list = [0]*26
	ciphertext = ciphertext.upper()
	ciphertext = ciphertext.replace(' ', '')
	for c in ciphertext:
		freq_list[ord(c) - 65] = freq_list[ord(c) - 65] + 1 
	return freq_list

def index_of_coincidence(ciphertext):
	freq_list = get_frequencies(ciphertext)
	sm = 0
	total = 0
	for c in ciphertext:
		sm = sm + (freq_list[ord(c) - 65] * (freq_list[ord(c) - 65] - 1))
		total = total + 1
	ind = sm/(t*(t-1))
	return(ind)

def friedman_estimate(ciphertext):
	n = .027*len(ciphertext)
	d = .0655 - index_of_coincidence(ciphertext) + (len(ciphertext)*(index_of_coincidence(ciphertext) - .0385))
	fe = n/d
	return fe











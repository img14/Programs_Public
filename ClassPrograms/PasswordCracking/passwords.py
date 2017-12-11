"""
Knowing that one user used a common password encrypted with a hill cipher, crack the other passwords (encrypted with the same matrix)
"""
from Cryptoalphabet import *
from MatrixCiphers import *

a_string = ""
for i in range(33,94):
	a_string = a_string + chr(i)

alpha = Cryptoalphabet(alphabet = a_string)

passwords = []
people = []
common_passwords = []

infile = open("passwords.txt","r")
for line in infile.readlines():
	  line = line.strip()
	  (w1,w2) = line.split()
	  people.append(str(w1))
	  passwords.append(str(w2))
infile.close()

infile = open("common-passwords.txt","r")
for line in infile.readlines():
	line = line.strip()
	if len(line) >= 6:
		common_passwords.append(line)
infile.close()

#p = passwords[0]


unames = []
for p in passwords:
	print("Checking: %s"%people[passwords.index(p)])
	for c in common_passwords:
		D = get_decryption_matrix(c[:4].upper(), p[:4].upper(), alpha)
		s = decrypt(D, p, alpha)
		if s[:7].upper() == c[:7].upper():
			unames.append(people[passwords.index(p)])
print(unames)



#print(people.index('2018emoar'))
#print(people.index('2018kgatesma'))


#MATCH FOR 2018emoar 2018kgatesma
#130, 228


pswds = []
p = passwords[228]
for c in common_passwords:
	D = get_decryption_matrix(c[:4].upper(), p[:4].upper(), alpha)
	s = decrypt(D, p, alpha)
	if s[:7].upper() == c[:7].upper():
		pprint(D)
		pswds.append(c)
print(pswds)


D = Matrix([[16,38],[56,29]]) #From code above
for p in passwords:
	s = decrypt(D, p, alpha)
	print("%s: %s"%(people[passwords.index(p)], s))





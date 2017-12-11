class Cryptoalphabet:
	def __init__(self, alphabet):
		self.alphabet = alphabet
	def getIndex(self, c):
		c = c.upper()
		return self.alphabet.index(c)
	def charNum(self, i):
		i = i % len(self.alphabet)
		return self.alphabet[i]
	def prepare(self, s):
		v = ""
		for c in s:
			if c.isalpha():
				v = v + c.upper()
		return v
	#def digraphToInt(self, s):
	#def intToDigraph(self, i)
import numpy as np
import random

l1 = np.genfromtxt('adjectives.txt',dtype='string')
l2 = np.genfromtxt('nouns.txt',dtype='string')
l3 = np.genfromtxt('adverbs.txt',dtype='string')
l4 = np.genfromtxt('verbs.txt',dtype='string')

la = np.genfromtxt('list1.txt',dtype='string')
ln = np.genfromtxt('list2.txt',dtype='string')
lav = np.genfromtxt('list3.txt',dtype='string')
lv = np.genfromtxt('list4.txt',dtype='string')
	
def generate_codename_ab(a1,a2):
	codename = a1[random.randint(0, len(a1)-1)]+" "+a2[random.randint(0, len(a2)-1)]
	return codename

def generate_codenameaofa(b1):
	w1 = b1[random.randint(0, len(b1)-1)]
	w2 = w1
	while w1 == w2:
		w2 = b1[random.randint(0, len(b1)-1)]
	codename = w1 + " of " + w2
	return codename
def generate_codenameaofb(c1,c2):
	codename = c1[random.randint(0, len(c1)-1)] + " of " +  c2[random.randint(0, len(c2)-1)]
	return codename
	
def generate_codenametheaofb(c1,c2):
	codename = "The " + c1[random.randint(0, len(c1)-1)] + " of " +  c2[random.randint(0, len(c2)-1)]
	return codename
	
def generate_codename_abc(a1,a2,a3):
	codename = a1[random.randint(0, len(a1)-1)]+" "+a2[random.randint(0, len(a2)-1)] + " " + a3[random.randint(0, len(a3)-1)]
	return codename
	
def more_complex_codename():
	a = random.randint(0,100)
	if a < 10:
		codename = generate_codename_abc(l3,l4,l2)
	elif a < 15:
		codename = generate_codenameaofa(l1)
	elif a < 25:
		codename = generate_codename_ab(l4,l2)
	else:
		codename = generate_codename_ab(l1,l2)
	return codename
	
def more_complex_codename_editable(d1,d2,d3,d4):
	a = random.randint(0,100)
	if a < 10:
		codename = generate_codename_abc(d3,d4,d2)
	elif a < 15:
		codename = generate_codenameaofa(d2)
	elif a < 25:
		codename = generate_codename_ab(d4,d2)
	else:
		codename = generate_codename_ab(d1,d2)
	return codename
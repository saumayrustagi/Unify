# IMPORTS
import ast

#

# FUNCTIONS


## List Functions
def readList(list):
	with open(list) as f:
		data = f.read()
	d = ast.literal_eval(data)
	return d


def writeList(write, list):
	with open(list, 'w') as open_list:
		open_list.write(str(write))


##


## Dictionary Functions
def readDict(dict):
	with open(dict) as f:
		data = f.read()
	d = ast.literal_eval(data)
	return d


def writeDict(write, dict):
	with open(dict, 'w') as open_dict:
		open_dict.write(str(write))


def checkFF(s):
	frm_str = s.lower().strip()
	# frm_char = frm_str[0]

	for short_form in full_form:
		for arr in full_form[short_form]:
			if frm_str in arr:
				return (True, short_form)
	return (False, s)


def addtoFF(shrtfrm, wrd):
	(tr, stf) = checkFF(wrd)
	if not tr:
		wrd = wrd.strip().lower()
		full_form[shrtfrm].append(wrd)


##


## LEVENSHTEIN
def comp_lev(val, arr2):
	arr1 = val.split('_')
	# print(arr1)
	# print(arr2)
	# DO LEVENSHTEIN FOR EACH WORD

	flag = 0  # WHETHER A WORD MATCHES OR NOT

	lev = 0

	dissim = 0

	i = 0
	j = 0
	while (i < len(arr1)):
		while (j < len(arr2)):
			if (arr1[i][0] == arr2[j][0]):
				# COMPUTE
				sim = levnshtn(arr1[i], arr2[j])
				if sim == 1:
					flag = 0
				lev += sim
				# UPDATE
				j = 0
				break
			else:
				flag += 1
			j += 1
		if (flag > 0):
			dissim += 1
			j = 0
			flag = 0
		i += 1

	# DONE
	dissim = dissim / (len(arr1))
	a = lev - dissim
	return a


def ret_lev(inp):
	dt = ((inp.lower()).strip())  # lowercase and strip whitespace
	arr1 = dt.split('_')  # Input the string words into arrays
	(word, lev, bestw, maxlev, shrtfrm, bstshrtfrm) = ("", 0, "", 0, "", "")

	for short_form in full_form:
		for arr in full_form[short_form]:
			# print(arr)
			lev = comp_lev(arr, arr1)
			shrtfrm = short_form
		if (lev > maxlev):
			maxlev = lev
			bstshrtfrm = shrtfrm
	return (inp, maxlev, bstshrtfrm)


def levnshtn(a, b):
	n1 = len(a)
	n2 = len(b)
	dist = max(n1, n2) - min(n1, n2)
	i = 0
	while (i < min(n1, n2)):
		if a[i] != b[i]:
			dist += 1
		i += 1
	dist = dist / (n1 + n2)
	return (1 - dist)


##

## MAIN


def intls(ring):

	def insf(ss):
		ss = ss.upper()
		cnt = 0
		for short_form in full_form:
			cnt = 0
			i = 0
			j = 0
			while i < len(short_form) and j < len(ss):
				if short_form[i] == ss[i]:
					cnt += 1
				i += 1
				j += 1
			if cnt >= len(short_form):
				return (True, short_form)
		return (False, '')

	def stndrd(nn):
		str = nn.strip()
		str = ''.join(str.split('.'))
		str = ''.join(str.split('_'))
		return str

	def cap(sr):
		fm_str = stndrd(sr)
		str = ''
		for a in fm_str:
			if a.isupper():
				str += a
		(tr, wd) = insf(str)
		if tr:
			return wd
		else:
			return spc(sr)

	def spc(sr):
		ss = stndrd(sr)
		arr = ss.split('_')

		str = ''
		for a in arr:
			str += a[0]

		(tr, wd) = insf(str)
		if tr:
			return wd
		else:
			return compl(sr, 1)

	return cap(ring)


def compl(sr, thrshld):
	(tr, crrct) = checkFF(sr)
	if not tr:
		(sr, lev, shrtfrm) = ret_lev(sr)
		print(i, lev)
		if lev >= thrshld:
			addtoFF(shrtfrm, sr)
			return shrtfrm
		else:
			return sr
	else:
		return crrct


##

#

# COMMANDS
full_form = readDict('dictionary.txt')
inp_fl = readList('list.txt')

## CHANGE VALUES

i = 0
while i < len(inp_fl):
	inp_fl[i][0] = intls(inp_fl[i][0])
	i += 1

##

print()

print(inp_fl)

writeList(inp_fl, 'list.txt')

print()

print(full_form)

print("\nWrite data to dictionary [y/n]? ", end='')
comm = input()
if comm == 'y':
	writeDict(full_form, 'dictionary.txt')

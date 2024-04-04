#!/usr/bin/env python3

from bisect import bisect
from struct import unpack
from array import array
import operator

def merge(a, b):
	outDocs = []
	outFreqs = []
	ai = 0
	bi = 0
	while ai < len(a[0]) and bi < len(b[0]):
		if a[0][ai] < b[0][bi]:
			ai += 1
		elif b[0][bi] < a[0][ai]:
			bi += 1
		elif a[0][ai] == b[0][bi]:
			outDocs.append(a[0][ai])
			outFreqs.append(a[1][ai] + b[1][bi])
			ai += 1
			bi += 1

	return (outDocs, outFreqs)

def invert(lst):
	out = []
	for i in range(len(lst[0])):
		out.append((lst[0][i], lst[1][i]))
	return out


docIds = []
with open('docs.dat', 'r') as file:
	docIds = file.readlines()

words = []
with open('words.dat', 'r') as file:
	words = file.readlines()

postingsFile = open('postings.dat', 'rb')
offsetFile = open('offset.dat', 'rb')

query = input('').split()
results = []
for term in query:
	i = bisect(words, term)

	offsetFile.seek(i * 4)
	offset = unpack('i', offsetFile.read(4))[0]

	postingsFile.seek(offset)
	docCount = unpack('i', postingsFile.read(4))[0]
	postingsFile.seek(offset+4)

	docs = array('i')
	docs.frombytes(postingsFile.read(4*docCount))

	postingsFile.seek(offset+4 + docCount * 4)

	freqs = array('i')
	freqs.frombytes(postingsFile.read(4*docCount))

	results.append((docs, freqs))

result = results[0]
for i in range(1, len(results)):
	result = merge(result, results[i])

result = invert(result)
result.sort(key = operator.itemgetter(1), reverse = True)

for r in result:
	print(docIds[r[0]][:-1], r[1])

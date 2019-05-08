#!/usr/bin/env python3

from struct import pack
from array import array

docNo = -1
docIds = []
index = {}
with open('wsj.xml', 'r') as file:
	isDocno = False
	for line in file:
		for word in line.split():
			if word == '<DOCNO>':
				isDocno = True
				continue
			if word[0] == '<' and word[-1] == '>':
				continue
			if isDocno:
				docNo += 1
				isDocno = False
				docIds.append(word)
				continue
			word = word.lower()
			if word in index:
				if index[word][0][-1] == docNo:
					index[word][1][-1] += 1
				else:
					index[word][0].append(docNo)
					index[word][1].append(1)
			else:
				index[word] = (array('i', [docNo]), array('i', [1]))

# Write index

with open('docs.dat', 'w') as file:
	for doc in docIds:
		file.write(doc)
		file.write('\n')

wordsFile = open('words.dat', 'w')
postingsFile = open('postings.dat', 'wb')
offsetFile = open('offset.dat', 'wb')

for word in sorted(index):
	wordsFile.write(word)
	wordsFile.write('\n')

	offsetFile.write(pack('i', postingsFile.tell()))

	docs = index[word][0]
	postingsFile.write(pack('i', len(docs)))
	docs.tofile(postingsFile)

	freqs = index[word][1]
	freqs.tofile(postingsFile)

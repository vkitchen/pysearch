#!/usr/bin/env python3

docNo = -1
docIds = []
index = {}
with open('wsj.xml', 'r') as file:
	isDocno = False
	for line in file:
		for word in line.split():
			word = word.lower()
			if word == '<docno>':
				isDocno = True
				continue
			if word[0] == '<' and word[-1] == '>':
				continue
			if isDocno:
				docNo += 1
				isDocno = False
				docIds.append(word)
				continue
			if word in index:
				lastPosting = index[word][-1]
				if lastPosting[0] == docNo:
					index[word][-1] = (docNo, lastPosting[1] + 1)
				else:
					index[word].append((docNo, 1))
			else:
				index[word] = [(docNo, 1)]

# Write index

with open('docs.dat', 'w') as file:
	for doc in docIds:
		file.write(doc)
		file.write('\n')

with open('words.dat', 'w') as file:
	for word in sorted(index):
		file.write(word)
		file.write('\n')

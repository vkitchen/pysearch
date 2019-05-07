#!/usr/bin/env python3

from bisect import bisect

words = []
with open('words.dat', 'r') as file:
	words = file.readlines()

query = input('').split()
for term in query:
	i = bisect(words, term)
	print(term, i, words[i])

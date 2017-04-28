#!/usr/bin/env python3

import string, json, sys, re, pdb

def DirectMeToTheFile(text, bookID):
	text = open('BOOKSinTXT.Entered/' + bookID).read()
	text = ' '.join(text.lower().split('\n'))
	metaDataChunk = re.compile('\*\*\* start of this.+\*\*\*')
	text = re.split(metaDataChunk, text)[1]
	return text

def WordInstance (text, bookID):
	for c in string.punctuation:
		text = text.replace(c, '')
	text = text.split(' ')
	bigDict = {}
	for e in text:
		bigDict[e] = text.count(e)
		text.remove(e)
	saveCOUNT = open('wordCOUNTS/' + bookID, 'w')
	saveCOUNT.write(json.dumps(bigDict))
	saveCOUNT.close()
	return bigDict

def WordFreq(text, bookID):
	yep = []
	for each in InstanceTuples.keys():
		yep.append([InstanceTuples[each], each])
	pdb.set_trace()


text = ''
text = DirectMeToTheFile(text, sys.argv[1])
InstanceTuples = WordInstance(text, sys.argv[1])
WordFreq(InstanceTuples, sys.argv[1])

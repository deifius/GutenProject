#!/usr/bin/env python3

import sqlite3
import sys
import pdb
import re
import os
import random

def populate(bookid):
	tags = { 'bookID': bookid, 'title': '', 'author': '', 'language': '', 'translator': '', 'illustrator': '', 'release date': '', 'edition': ''}
	print(tags['bookID'] + "\n\n")
	metaDataChunk = re.compile('\n\*\*\* start.+\*\*\*\n')
	Chunk = re.sub('\n+', '\n', re.split(metaDataChunk, open("BOOKSinTXT/" + tags['bookID']).read().lower())[0]).split('\n')
	if Chunk[-1] == '': Chunk.pop() 

	for e in Chunk:
		if re.search(': ',e) != None:
			tags[e.split(': ')[0]] = e.split(': ')[1]
	tags['title'] = re.sub(r'[^0-9|^A-Z|^a-z|^ ]','', tags['title'])
	tags['author'] = re.sub(r'[^0-9|^A-Z|^a-z|^ ]','', tags['author'])
	conn = sqlite3.connect('bookMetaData')
	c = conn.cursor()
	sqliterow = 'INSERT INTO books (bookID, title, author, language, translator,illustrator, releasedate, edition) VALUES ("'
	sqliterow += tags['bookID'] +'", "'+ tags['title'] +'", "'+ tags['author'] +'", "'+ tags['language'] +'", "'+ tags['translator'] +'", "'+ tags['illustrator'] +'", "'+ tags['release date'] +'", "'+ tags['edition'] + '")'

	#pdb.set_trace()
	c.execute(sqliterow)
	conn.commit()
	conn.close()

targets = os.listdir('BOOKSinTXT')
random.shuffle(targets)
for each in targets:
	populate(each)


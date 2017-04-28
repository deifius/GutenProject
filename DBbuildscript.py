#!/usr/bin/env python3

import sqlite3

def initial_eyes():
	conn = sqlite3.connect('bookMetaData')
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS books(\
		bookID TEXT, \
		title  TEXT,\
		author TEXT,\
		language TEXT,\
		translator TEXT,\
		illustrator TEXT,\
		releasedate TEXT,\
		edition TEXT)')

initial_eyes()

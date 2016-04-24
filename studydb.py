# Study Guide CRUD for MongoDB
# 
# 21 April 2016
# Craig Gonzales
# This tool will allow me to create, read, update, and delete data to a MongoDB database 

from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017")
db = client.cyberStudy

def create(collect):
	# Apologies for inelegant if-elif structure. Focusing on CRUD. 
	if collect == "NoSQL":
		coll = db.NoSQL.insert(new_data)
	elif collect == "SQLite3":
		coll = db.SQLite3.insert(new_data)
	elif collect == "Splunk":
		coll = db.Splunk.insert(new_data)
	elif collect == "RegEx":
		coll = db.RegEx.insert(new_data)
	elif collect == "Kafka":
		coll = db.Kafka.insert(new_data)
	return 	

def read(collect):
	if collect == "NoSQL":
		for document in db.NoSQL.find():
			print(document)
	elif collect == "SQLite3":
		for document in db.SQLite3.find():
			print(document)
	elif collect == "Splunk":
		for document in db.Splunk.find():
			print(document)
	elif collect == "RegEx":
		for document in db.RegEx.find():
			print(document)
	elif collect == "Kafka":
		for document in db.Kafka.find():
			print(document)
	return 	
	
def update(id, data):
	if collect == "NoSQL":
		coll = db.NoSQL.update(id, data)
	elif collect == "SQLite3":
		coll = db.SQLite3.update(id, data)
	elif collect == "Splunk":
		coll = db.Splunk.update(id, data)
	elif collect == "RegEx":
		coll = db.RegEx.update(id, data)
	elif collect == "Kafka":
		coll = db.Kafka.update(id, data)
	return 
	
def delete(data):
	if collect == "NoSQL":
		coll = db.NoSQL.remove(data)
	elif collect == "SQLite3":
		coll = db.SQLite3.remove(data)
	elif collect == "Splunk":
		coll = db.Splunk.remove(data)
	elif collect == "RegEx":
		coll = db.RegEx.remove(data)
	elif collect == "Kafka":
		coll = db.Kafka.remove(data)
	return 	

# CRUD Question - I hate that I am using if-then, but I have to create this NoSQL tool quickly
action = raw_input("Create, Read, Update, or Delete? [C, R, U, D]: ")

if action == "C":
	# Work with the correct data. Case sensitive and this isn't a functional application, 
	# so it'll stay case sensitive. In a real solution I wouldn't be using python to collect data
	collect = raw_input("Which Collection? [NoSQL, SQLite3, Splunk, RegEx, Kafka]: ")
	datatype = raw_input("What datatype? [Document, Video]: ")
	name = raw_input("What is the title? ")
	url = raw_input("What is the URL? ")
	rw = raw_input("Have you read/watched it? [Yes, No]")
	comments = raw_input("What comments do you have? ")
	data = '{"%s":{"Name" : "%s", "URL" : "%s", "Read/Watched?" : "%s", "Comments" : "%s"}}' % (datatype, name, url, rw, comments)
	new_data = json.loads(data)
	create(collect)

if action == "R":
	# I will keep this simple, just to prove I can read and print this stuff out. 
	collect = raw_input("Which Collection? [NoSQL, SQLite3, Splunk, RegEx, Kafka]: ")
	read(collect)
	
if action == "U":
	collect = raw_input("Which Collection? [NoSQL, SQLite3, Splunk, RegEx, Kafka]: ")
	read(collect)
	whichId = raw_input("Which Title? ")
	datatype = raw_input("What datatype? [Document, Video]: ")
	name = raw_input("What is the title? ")
	url = raw_input("What is the URL? ")
	rw = raw_input("Have you read/watched it? [Yes, No]")
	comments = raw_input("What comments do you have? ")
	data = '{"%s":{"Name" : "%s", "URL" : "%s", "Read/Watched?" : "%s", "Comments" : "%s"}}' % (datatype, name, url, rw, comments)
	id = '{"Name" : "%s"}' % whichId
	new_id = json.loads(id)
	new_data = json.loads(data)
	update(new_id, new_data)	

if action == "D":
	collect = raw_input("Which Collection? [NoSQL, SQLite3, Splunk, RegEx, Kafka]: ")
	read(collect)
	name = raw_input("Which Title? ")
	datatype = raw_input("What datatype? [Document, Video]: ")
	url = raw_input("What is the URL? ")
	rw = raw_input("Have you read/watched it? [Yes, No]")
	comments = raw_input("What comments do you have? ")
	data = '{"%s":{"Name" : "%s", "URL" : "%s", "Read/Watched?" : "%s", "Comments" : "%s"}}' % (datatype, name, url, rw, comments)
	new_data = json.loads(data)
	delete(new_data)	
	
client.close()
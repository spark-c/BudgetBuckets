# application for budgeting
# organizes moneys into "buckets" according to a given percentage of total income
# Collin Sparks 01/15/2021 (Last Updated: 01/16/2021)
# Python 3.8

import os
import Buckets
import json


def printBuckets():
	print('\n')
	for bucket in Buckets.Bucket.activeBuckets:
		bucket.printout() + '\n'


def check_existing_buckets(): # checks for existing Buckets. If no .\Buckets, creates it.
	cwd = os.getcwd()
	if not os.path.isdir(cwd + '/Buckets'):
		os.mkdir(r'./Buckets')
		return False # No records exist

	if len(os.listdir('./Buckets')) == 0: # Directory exists but no files
		return False

	return True # Records found


def load_buckets(): # loads existing buckets into memory
	if check_existing_buckets():
		for file in os.listdir('./Buckets'):
			try:
				with open('./Buckets/' + file, 'r') as f: # cwd is ..Buckets/bucket.json so we append ./Buckets/
					bucket_json = json.load(f) # dict
				newObj = Buckets.Bucket(bucket_json['name'], bucket_json['allotment'], bucket_json['allotment_type'], bucket_json['balance']) # Bucket __init__ automatically updates dict of active buckets
			except:
				print('Something went wrong while loading file {}'.format(file))
		print('Successfully loaded {} buckets!'.format(len(Buckets.Bucket.activeBuckets)))

	else:
		print('No buckets found.')


def save_buckets(): # saves all existing buckets to the drive
	bucket_objects = Buckets.Bucket.activeBuckets.values() # a list containing only the bucket objects
	for bucket in bucket_objects:
	#try:
		outfile = './Buckets/' + bucket.name + '.json'
		with open(outfile, 'w') as f: # builds the filename from bucket.name
			dump = json.dump(bucket.printout('j'), f, indent = "") # bucket.printout(j) returns dict of obj; indent = "" improves readability in outfile;
		print('Saved file {}'.format(outfile))
	#except:
		#print('Bucket {} failed to save!'.format(bucket.name))



load_buckets()

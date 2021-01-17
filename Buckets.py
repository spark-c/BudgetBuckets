# intro

import Bucket_Input_Validation as biv

class Bucket:

	activeBuckets = {}

	def __init__(self, name, allotment, allotment_type, balance=0):
			self.name = name
			self.allotment = allotment
			self.allotment_type = allotment_type
			self.balance = balance
			Bucket.activeBuckets[self.name] = self # creates a dictionary of loaded buckets accessible by name.


	def printout(self, j=False): # if j, method returns a serialized string for writing to JSON file
		if j == 'j':
			d = {
			'name': self.name,
			'allotment': self.allotment,
			'allotment_type': self.allotment_type,
			'balance': self.balance
			}
			return d

		else:
			print(
				'Bucket: {}\n'.format(self.name) +
				'Allotment: {0}{1}\n'.format(self.allotment, self.allotment_type) +
				'Balance: {}\n'.format(self.balance)
				)


	def rename(self, new_name):
		if biv.rename(new_name):
			return
		self.name = new_name


	def reallot(self, allotment, type): # change allotment for the bucket. Does not allow a bucket to receive over 100% of income.
		if biv.reallot(allotment, type): # returns 1 (True) for INVALID input.
			return

		self.allotment = allotment
		self.allotment_type = type


	def deposit(self, amount):
		self.balance += amount


	def withdraw(self, amount):
		if biv.withdraw(self, amount):
			return
		self.balance -= amount


	def delete(self):
		activeBuckets.remove(self)

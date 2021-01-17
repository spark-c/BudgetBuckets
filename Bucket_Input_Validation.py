# Fuctions for validating user input for Bucket application


def rename(new_name): # we can only accept alphabetic and underscore characters because it's used as object name upon loading.
	temp = new_name.split('_') # split name on underscores and combine. if remainder is only alpha, then we're good.
	if not ''.join(temp).isalpha():
		print('ERROR: Name can only contain alphabetic characters and underscores!')
		return 1 # ERROR
	else:
		return 0


def reallot(allotment, type):
	if type != '%' and type != '$':
		print('ERROR: Allotment type must be % or $')
		return 1 # INVALID input

	if type == '%' and allotment > 100:
		print('ERROR: Allotment is greater than 100% !')
		return 1

	return 0 # Input valid


def withdraw(bucket, amount):
    if bucket.balance < amount:
        print('ERROR: Withdraw exceeds available balance!')
        return 1
    else:
        return 0

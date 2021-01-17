# BudgetBuckets
A tool for budgeting and keeping track of how much money is available for which purposes.

Current features:

-Each "Bucket" object represents a pool of money reserved for a given purpose
	-Name, allotment (dollar amt or percentage of income), allotment_type($ or %), balance (current balance of bucket)
-At runtime, script checks for existing JSON bucket data in ./Buckets; loads and initializes objects from this data.
-Function "save_buckets()" saves bucket data to JSON files in ./Buckets
-Bucket methods in place to allow for editing all attributes of Bucket objects.

TO-DO:
-implement a Breakdown Calculator that will accept a dollar amount (paycheck) and correctly distribute the moneys to buckets.
	-ability to edit allotment before proposed changes/distribution is made
-implement GUI!
-surely more along the way

def display_hash(hashtable):
	for i in range(len(hashtable)):
		print(i, end=" ")
		for j in hashtable[i]:
			print("-->",end=" ")
			print(j , end = " ")

		print()


hashtable = [[] for _ in range(10)]

def hashing(keyValue):
	return keyValue%len(hashtable)

def insert(hashtable,keyValue,value):
	hash_key = hashing(keyValue)
	hashtable[hash_key].append(value)


insert(hashtable, 10, 'Allahabad') 
insert(hashtable, 25, 'Mumbai') 
insert(hashtable, 20, 'Mathura') 
insert(hashtable, 9, 'Delhi') 
insert(hashtable, 21, 'Punjab') 
insert(hashtable, 21, 'Noida') 

display_hash(hashtable)
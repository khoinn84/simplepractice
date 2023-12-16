# original project let people input an email address, then slice it to get the username and the domain
# original project ref https://www.facebook.com/groups/1212071995953351/?multi_permalinks=1687398441754035

# version 1 will try to get the same result
# version 2 will read all the email addresses from a text file and slice them to get the (username,domain) into a list of tuples. This file is Version 2.

handle = open('doc/sample02.txt')

words = []
elist = []

for line in handle:
	words.extend(line.strip().split())

for word in words:
	if word.__contains__('@'):
		elist.append((word.strip('.;"').split('@')[0] , word.strip('.;"').split('@')[1]))

#print(words)
print(elist)
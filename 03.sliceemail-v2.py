# original project let people input an email address, then slice it to get the username and the domain
# original project ref https://www.facebook.com/groups/1212071995953351/?multi_permalinks=1687398441754035

# version 1 will try to get the same result
# version 2 will read all the email addresses from a text file and slice them to get the (username,domain) into a list of tuples. This file is Version 2.
# version 2 is now enhanced to include version 1, so it will prompt user to select either simply enter an email address, or select file

ans = input('Do you want to slice username and domain from the email address that you will enter, or print the list of email username & domain from a text file?\nType 1 to select the former, type 2 to select the latter: ')

if ans == '1':
	email = input('Enter an email address:').strip()

	user = email.split('@')[0]
	domain = email.split('@')[1]

	print('User is ',user,' and domain is ',domain)

elif ans == '2':
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

else:
	print("Sorry, you didn't choose either 1 or 2. Please restart the program if needed.")
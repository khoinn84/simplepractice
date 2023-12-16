# original project let people input an email address, then slice it to get the username and the domain
# original project ref https://www.facebook.com/groups/1212071995953351/?multi_permalinks=1687398441754035

# version 1 will try to get the same result
# version 2 will read all the email addresses from a text file and slice them to get the (username,domain) into a list of tuples

email = input('Enter an email address:').strip()

user = email.split('@')[0]
domain = email.split('@')[1]

print('User is ',user,' and domain is ',domain)
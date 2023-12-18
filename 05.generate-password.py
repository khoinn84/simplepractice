import string
import random

passw = ''


all_printable_chars = list(string.printable)

#print(all_printable_chars)

num = int(input("How many characters do you want for your password? "))
if num <= 0:
	print('Invalid number')
else:
	for i in range(num):
		ran = random.randint(0,93)
		passw += all_printable_chars[ran]
	print('Your password is: ' + passw)
# solution of author: https://github.com/kienonline19/60PythonProjectsWithSourceCode/blob/main/acronyms.py
# create acronyms of input string

str = input("Enter the string you want to create its acronyms:")
tmpList = str.split()
result = ""
for i in tmpList:
	result += i[0].upper()

print("The acronyms are:", result)

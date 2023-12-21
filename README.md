# simplepractice
This repo stores the code for multiple simple problems, mostly for practising.

01.acronym.py
Create acronyms of input string
Practice the methods of string: split(), upper()

02.alarmclock-v1.py
Enter the alarm time, compare the hour and minute with current time, if they are the same then play the alarm sound
Practice the methods of string: split() and string slicing
Practice the usage of datetime module, playsound module, while True loop to wait until the correct condition then break

03.sliceemail-v1.py
03.sliceemail-v2.py
original project let people input an email address, then slice it to get the username and the domain
version 1 will try to get the same result
version 2 will allow user to choose to either enter an email directly, or read all the email addresses from a text file and slice them to get the (username,domain) into a list of tuples.
Practice opening a file and read content
Practice the methods of string: strip(), split(), __contain__()
Practice the methods of list: append(), extend()

04.story-generator.py
generate a random sentence using random module and a preset of lists of words
Practice using random module

05.generate-password.py
Generate random password base on the number of characters input by user
Practice using random module to generate integer number
Practice using string module to get printable ASCII characters by using the string.printable constant

06.rockpaperscissor-game.py
Let user choose Rock/Paper/Scissors and compare with computer random choice then announce the detailed result, and let the use choose to continue playing or stop, and display final score
Practice using random module to randomly select a value in a predefined list
Practice using function to update global variable
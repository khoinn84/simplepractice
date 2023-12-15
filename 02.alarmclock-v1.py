# get the alarm time from input and if current time (hour and minute) is the same then right the sound
# sample solution https://github.com/kienonline19/60PythonProjectsWithSourceCode/blob/main/alarm.py but my code will be slightly different in how we slice the input string and convert to integer to compare
# note: in order to play sound, you need to import sound module, and also install 2 things to your PC, the command lines are:
# pip3 install playsound==1.2.2
# pip3 install -U PyObjC

from datetime import datetime
from playsound import playsound

alarmTime = input("Enter the alarm time in format (HH:MM AM/PM)\nFor example: 11:30 AM\nAlarm time: ")
str = alarmTime.split()
alarmH = int(str[0][0:2])
alarmM = int(str[0][3:])
dayNight = str[1]
if dayNight == 'PM':
	alarmH += 12

while True:
	time = datetime.now()

	if time.hour == alarmH and time.minute == alarmM:
		playsound("sound/SwissBellSound.mp3")
		break

#print(alarmH)
#print(alarmM)
#print(dayNight)
#print(time)
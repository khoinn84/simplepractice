import random
options = ['Rock','Paper','Scissors']

playerScore = 0
compScore = 0
cont = True

def Win(playerC, compC):
	global playerScore
	global compScore
	global cont

	if playerC == compC:
		print('Tie!')
	elif (playerC == 'Rock' and compC == 'Scissors') or (playerC == 'Paper' and compC == 'Rock') or (playerC == 'Scissors' and compC == 'Paper'):
		print(f'Computer goes {compC}, you win!\n')
		playerScore += 1
	elif (playerC == 'Rock' and compC == 'Paper') or (playerC == 'Paper' and compC == 'Scissors') or (playerC == 'Scissors' and compC == 'Rock'):
		print(f'Computer goes {compC}, sorry, you lose.\n')
		compScore += 1
	x = input('Play again? (Y/N):')
	if x == 'Y':
		cont = True
	else:
		cont = False


while cont:
	playerChoice = input('Choose Rock, Paper or Scissors: ')
	computerChoice = random.choice(options)
	Win(playerChoice, computerChoice)

print(f'Final result: your score is {playerScore}, computer score is {compScore}')
if playerScore > compScore:
	print('YOU WIN!')
elif playerScore < compScore:
	print('Sorry, you lost')
else:
	print("It's a TIE")
import random
choice=["s",'w','g']
Human_choice=''
number_of_limit=8
number_of_guss=0
human_score=0
computer_score=0
Name=input("Enter the name:")

# def play(choices):
# 	human_score=0
# 	computer_score=0
print(f"Welcome to our game  {Name}")
while Human_choice!=choice:
	computer_choice=random.choice(choice)
	
	if number_of_guss < number_of_limit:
		Human_choice=input(''' snake,water, gun
                    snake-s
                    water-w
                    gun-g
                Enter the choice : ''')
		number_of_guss+=1
		print(f'you have {number_of_limit-number_of_guss}round')


		print('You gussed',Human_choice)
		print("computer gussed",computer_choice)
		if Human_choice==computer_choice:
		    print("Both are tie 😂")
			
		elif Human_choice== 's':
			if computer_choice == 'g':
				print('you lose, sorry 😢')
				computer_score+=1
			elif computer_choice == 'w':
				print('You win!!!!! congrats 😎')
				human_score+=1
		elif Human_choice == 'w':
			if computer_choice == 'g':
				print('You win!!!!! congrats 😎')
				human_score+=1
			elif computer_choice == 's':
				print('you lose, sorry 😢 ')
				computer_score+=1
		elif Human_choice== 'g':
			if computer_choice == 's':
				print('You win!!!!! congrats 😎')
				human_score+=1
			elif computer_choice == 'w':
				print('you lose, sorry 😢')
				computer_score+=1 
	else:
		break
print(f"your score is {human_score} and computer got {computer_score} ")


if computer_score>human_score:
	print(f"""<--------------------------------------------------------------------------------
	            computer has won the game by  {computer_score}round
	-------------------------------------------------------------------------------------->""")
else:
	print(f"""<--------------------------------------------------------------------------------
	            {Name} has won the game by {human_score}rounds
-------------------------------------------------------------------------------------->""")
	
# play(choice)


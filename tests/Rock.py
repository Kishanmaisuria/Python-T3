import random
Tie = 0
Wins = 0
Loses = 0 
	
while True:
	options = ["Rock", "Paper", "Scissors"]
	user_choice = input("Choose Rock, Paper, or Scissors: ")
	computer_choice = random.choice(options)

	

	print("You chose: ", user_choice)

	print("Computer chose: ", computer_choice)
	

	

	if user_choice == computer_choice:

		print("It's a tie!")
		Tie +=1 

	elif user_choice == "Rock" and computer_choice == "Scissors":

		print("You win!")
		Wins +=1

	elif user_choice == "Paper" and computer_choice == "Rock":

		print("You win!")
		Wins +=1

	elif user_choice == "Scissors" and computer_choice == "Paper":

		print("You win!")
		Wins +=1 

	else:

		print("Computer wins!")
		Loses +=1 

	Score_board = Tie,Wins,Loses
	print ("Tie,Wins,Loses",{Score_board}) 

	
	play_again = input(f"\n want to try again Y(yes) or N(no): ")
	if play_again.lower() != "y":
		break
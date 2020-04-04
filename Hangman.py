#Hangman game project
import time

name = raw_input("Tell me your name.")

print "hello" + name, "Let's play some hangman!!!"

print"
"

time.sleep(1)

print "Make a guess...."
time.sleep(0.5)

word = ""

guesses = ''

turns = 10

while turns > 0:
	
	failed = 0
	
	for char in word 
		
		if char in guesses :
			
			print char, 
		
		else:
			
			print "_"
			
			failed += 1 
	if failed == 0:

		print "You Won!!!!"

		break

	print 

	guess = raw_input("Guess a letter:")
		
		if guess not in word: 
			
			turns -= 1
			
			print "Wrong!!"

			print "you have", + turns, "more guesses"

			if turns == 0:

				print "You lose, play again!!"

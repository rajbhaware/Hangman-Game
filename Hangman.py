def matchChar(guessCh,count):
	ch=raw_input("Guess a  %d character :"%(count+1))
	if ch == guessCh:
		return True
	else:
		return False

import random
play=True
while play:
	choice=False
	count=0
	attemp=3
	lines = open(r"C:\Rajnikant\Python\Hangman\Words.txt").read().splitlines()
	guessWord =random.choice(lines)
	
	if __name__ == '__main__':
		print "guessWord " ,guessWord
	
	print "Start guising...You have %d attemps" %attemp
	guessedWord=['_']*len(guessWord)
	print "Start Guessing...."
	for guessCh in guessWord:
		if attemp!=0:
			print "for guessCh ", guessedWord
			while attemp > 0: 
				#choice=matchChar(guessCh,count)
				ch=raw_input("Guess a  %d character :"%(count+1))
				if ch == guessCh:
					choice = True
				else:
					choice = False
				if choice==True:
					guessedWord[count]=guessCh
					break
				if choice==False:
					attemp=attemp-1
					print "Wrong.. you have %d attemps"%attemp
			count=count+1
			if attemp==0 or count==len(guessWord):
				print "The Word is : " ,guessWord
	ch=raw_input("Do you want to countinue press y/n: ")
	if ch=='n' or ch=='N':
		play=False



	

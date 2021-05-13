def shuffle_list(mylist):
  from random import shuffle
  shuffle(mylist)
  return mylist

def player_guess():
  guess=''
  while guess not in ['0','1','2']:
    guess= input('Pick a number between 0, 1 or 2')
  return int(guess)

def check_guess(mylist, guess):
  if mylist[guess] == 'o':
    print('Correct guess')
  else:
    print('Wrong guess, sorry!')
    print(mylist)
    
#INITIAL LIST
mylist= ['', 'o', '']

#SHUFFLED LIST
mylist_mixed= shuffle_list(mylist)
#USER GUESS
guess= player_guess()
#FINAL CHECK
check_guess(mylist_mixed, guess)

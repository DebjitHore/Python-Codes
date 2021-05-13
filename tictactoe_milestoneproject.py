#!/usr/bin/env python
# coding: utf-8

# In[23]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    pass


# In[24]:


test_board = ['#','X','O','X','O','X','O','A','O','X']
display_board(test_board)


# In[25]:


def player_input():
    marker=''
    while marker!='X' and marker!= 'O':
        marker=input('Player 1 please enter X or O')
    if marker=='X':
        return('X','O')
    else:
        return ('O','X')

    
#OUTPUT IN FORM OF tuple (Player 1 marker, Player 2 marker)


# In[26]:


def place_marker(board, marker, position):
    board[position]= marker


# In[27]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[28]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[29]:


display_board(board)
win_check(board,'X')


# In[30]:


import random

def choose_first():
    x=random.randint(1,10)
    if x%2==0:
        print('Player 1 goes')
    else:
        print('Player 2 goes')


# In[31]:


choose_first()


# In[37]:


def space_check(board, position):
    if board[position].isspace():
        return True
    else:
        return False
     


# In[38]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i) is True:
            return False
            break
    return True #BOARD is full
            


# In[39]:


def player_choice(board):
    choice=0
    while choice not in range(1,10) or space_check(board,choice) is False :
        choice=int(input('Player please enter your position choice from 1-9'))
    return choice      


# In[40]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[42]:


print('Welcome to Tic Tac Toe')

while True:
    
    board= [' ']*10
#display_board(board)
    player1_marker, player2_marker= player_input()
    turn= choose_first()
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn=='Player 1 goes':
            display_board(board)
            position= player_choice(board)
            place_marker(board,player1_marker,position)
            #display_board(board)
            if win_check(board,player1_marker) is True:
                display_board(board)
                print('Player 1 has won')
                game_on=False
            else:
                if full_board_check(board) is True:
                    display_board(board)
                    print('Tie Game!!')
                    game_on=False
                else:
                    print('Player 2 goes')
                    turn= 'Player 2 goes'
                
        else:
            display_board(board)
            position= player_choice(board)
            place_marker(board,player2_marker,position)
            #display_board(board)
            if win_check(board,player2_marker) is True:
                display_board(board)
                print('Player 2 has won')
                game_on=False
            else:
                if full_board_check(board) is True:
                    display_board(board)
                    print('Tie Game!!')
                    game_on=False
                else:
                    print('Player 1 goes')
                    turn= 'Player 1 goes'
    if not replay():
        break
    
    
    
    


# In[ ]:





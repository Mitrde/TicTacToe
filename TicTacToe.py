#first try ti create file
player1=[]
player2=[]
play = True
answer= True
def to_turns(turns1,turns2):
    turns=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for turn in turns1:
        turns[turn]='X'
    for turn in turns2:
        turns[turn]='0'
    return turns
        

def print_field(t):
    print(f'   |   |   \n {t[0]} | {t[1]} | {t[2]} \n   |   |   \n-----------')
    print(f'   |   |   \n {t[3]} | {t[4]} | {t[5]} \n   |   |   \n-----------')
    print(f'   |   |   \n {t[6]} | {t[7]} | {t[8]} \n   |   |   ')

def ask_turn1():
    print(f"Turn of X ")
    x=int(input())
    while not(0<=x<10 and x not in player1 and x not in player2):        
        print('wrong input')
        x=int(input())
    else:
        player1.append(x)
        
def ask_turn2():
    print(f"Turn of O ")
    x=int(input())
    while not(0<=x<10 and x not in player1 and x not in player2):        
        print('wrong input')
        x=int(input())
    else:
        player2.append(x)

def check_win(turns):
    win_list=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    win_condition=0
    for win in win_list:
        for turn in win:
            if turn in turns:
                win_condition+=1
            else:
                break
        if win_condition==3:
            return True
        else:
            win_condition=0
    else:
        return False    

print_field(['0','1','2','3','4','5','6','7','8'])
print('For making a turn insert the number of cell:')    
while answer==True:
    while True:
        print_field(to_turns(player1,player2))
        ask_turn1()
        if check_win(player1):
            print('Congrats Player X')
            break
        if len(player1+player2)==9:
            print("WOW NICE PLAY! IT'S DRAW")
            break
        print_field(to_turns(player1,player2))
        ask_turn2()
        if check_win(player2):
            print('Congrats Player O')
            break
        
    print_field(to_turns(player1,player2))
    print('\nWanna play again?\nInput "yes" or "no" ')
    wanna=input()
    while (wanna!="yes" and wanna!="no"):
        print('wrong input')
        wanna=input()
        
        
    if wanna=='yes':
        player1=[]
        player2=[]
    elif wanna=='no':
        answer=False
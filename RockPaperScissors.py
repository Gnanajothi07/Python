import random

def play():
    user = input("'r' for rock, 'p' for paper , 's' for scissors : ")
    computer = random.choice(['r' , 'p' , 's'])
    
    if user == computer:
        return "Match Tie"
    
    if is_win(user , computer):
        return "Your Win"
    return "You Lost"
    #r<p , p<s , s<r
def is_win(player , oppenent):
    if ( (player == 'p' and oppenent == 'r') or (player == 's' and oppenent == 'p') or (player == 'r' and oppenent == 's') ):
        return True
print(play())        

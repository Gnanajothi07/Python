import random
from words import words

choosen_word = random.choice(words)            
print(choosen_word)
correct_letter = []   
game_over = False
while not game_over:
    guess = input("Enter the letter : ").lower()  

    placeholder = ''
    words_length = len(choosen_word) 
    for i in range(words_length-1):  
        placeholder += '_'   
 
    display = ""   
    for letter in choosen_word:     
        if guess == letter:        
            correct_letter.append(guess)   
            display+=letter                
        elif letter in correct_letter:
            display += letter
        else:
            display+= '_'
    print(display)        
    if '_' not in display:
        game_over = True
        print("You Won")

#Step 5

import random
import hangman_art
#OR WE CAN Use
#from hangman_art import word_list
import hangman_words
#OR WE CAN Use
#from hangman_words import stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"
guesslist=[]
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
      if guess in guesslist:
         print(f"You have already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guesslist+=guess 
    
             

    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"You guessed {guess}, thats not int the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    print(hangman_art.stages[lives])
import random
from hangman_art import stages, logo
# from hangman_art import logo
import hangman_words

print(logo)
lives = 6

curr_ans=""

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#h_word = word_list [random.randint(0,2)]
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#user_guess = (input("Guess a letter (a-z): ")).lower()
#print(user_guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Initialse list
curr_ans = []
i=len(chosen_word)
for _ in range(i):
  #curr_ans.append['_']
  curr_ans += "_"

print(curr_ans)


end_of_game = False
previous_guesses = []

while not end_of_game:
  user_guess = (input("Guess a letter (a-z): ")).lower()
  ltr_in_word = False

  if user_guess in previous_guesses:
    print (f"You have already tried letter - {user_guess}")
    continue
  else:
    previous_guesses += user_guess

  for j in range(i):
  #for letter in chosen_word:
    if user_guess == chosen_word[j]:
      curr_ans [j] = user_guess
      ltr_in_word = True 
  
  #print (lives)
  #print(ltr_in_word)
  if not ltr_in_word:
      lives -=1 

  print(stages[lives])
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(curr_ans)}")
  #print (curr_ans)

  if "_" not in curr_ans:
    end_of_game = True
    print("You win")
  elif lives == 0:
    end_of_game = True
    print("You LOSE")

  






# target_words = 'hotdog'
# user_input = input('Enter your guess:')
# guessed_letters = []
# print(guessed_letters)

# if user_input in target_words:
#     print("getting closer")
#     print(input('Enter your guess:\n'))

# elif user_input != target_words:
#     print("try again")
#     print(input('Enter your guess:\n')

target_word = "special"
wrong_guess_counter = 0

while wrong_guess_counter < 4:
  user_guess = input('Guess a letter:').lower()
  if len(user_guess)>1:
    print("Please enter only one   letter at a time.")
  elif user_guess.isnumeric():
    print("Please enter a letter not a number")
  else:
    if user_guess in target_word:
      print("Getting closer")
    else:
      if wrong_guess_counter < 4:
        print('Please try again')
      else:
        print("Game Over")
      wrong_guess_counter += 1
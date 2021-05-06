import random

ROUNDS = 3

def main():
  '''
    - Welcome user
    - Initialize score to 0
    - Play n rounds indicated by ROUNDS
      - For each round:
        - update the score with the result of that round from results dictionary
        - add most recent user choice to user's choices list
        - add most recent AI choice to AI's choices list
    - After n rounds, print final score.
  '''
  welcome()
  score = 0
  ai_choices = []
  user_choices = []
  for i in range(ROUNDS):
    results = play_round(score, i, ai_choices, user_choices)
    ai_choices.append(results['ai_choice'])
    user_choices.append(results['user_choice'])
    score = results['score']
  print('Your score is %i'%(score))


def welcome():
  print('Welcome to Rock Paper Scissors')
  print('You will play 3 games against the AI')
  print('Rock beats Scissors')
  print('Scissors beats Paper')
  print('Paper beats Rock')
  print('----------------------------------------------')

def play_round(score, round_number, ai_choices, user_choices):
  '''
  - Takes in player's current score, round number, and lists of previous user & ai choices
  - Gets the new choice from both user & AI.
  - Determine the winner / score change
  - Prints winner
  - Updates score
  - Returns a dictionary with updated score, user's choice, and ai's choice
  '''
  ai_choice = get_ai_choice(round_number, ai_choices, user_choices)
  user_choice = get_user_choice()
  print('The AI plays ' + ai_choice)
  score_change = determine_outcome(ai_choice, user_choice)
  print_winner(score_change)
  score += score_change 
  return {'score': score, 'user_choice':user_choice, 'ai_choice':ai_choice}

def get_ai_choice(round_num, ai_choices, user_choices):
  '''
  Takes in round number to determine strategy, and previous choices lists for user & AI
  Strategy:
  - Round 0 (First iteration): Converts a random integer in range(1,3) to a correct game choice
  - After Round 1:
    - If AI lost previous round, choose thing that beats what user played last
    - If AI won, choose thing that would have beat what you AI played last
  '''
  if round_num == 0:
    return select_random()
  else:
    # ai_choices[round_num - 1] = Accesses the rock, paper, scissor selection from AI from previous round's index in list
    return select_by_previous(ai_choices[round_num - 1], user_choices[round_num - 1])


def select_random():
  '''
    Selects a random rock, paper, scissors option and returns string
  '''
  num = random.randint(1,3)
  if num == 1:
    return 'rock'
  elif num == 2:
    return 'paper'
  elif num == 3:
    return 'scissors'

def select_by_previous(ai_choice, user_choice):
  '''
    Takes in user and AI input from previous round
    Returns AI choice for current round as a string
  '''
  result = determine_outcome(ai_choice, user_choice)
  if result == 0: return select_random()
  if result == 1: # User won, choose what would have beat them
    return get_winning_choice(user_choice)
  if result == -1: #AI won, choose what would have beat AI
    return get_winning_choice(ai_choice)

def get_winning_choice(choice):
  '''
  Takes in a rock, paper, scissors choice and returns 
  the choice that beats it
  '''
  if choice == 'rock':
    return 'paper'
  if choice == 'paper':
    return 'scissors'
  if choice == 'scissors':
    return 'rock'

def get_user_choice():
  '''
  - Asks user for selection of rock, paper, or scissors
  - Validates user input by removing any potential whitespace 
    before/after the word and making it uniformly lowercase
  - When a valid input is entered, return that string
  '''
  choice = input('What do you play?\n("rock", "paper", or "scissors")\n')
  while choice.strip().lower() not in ['rock', 'paper', 'scissors']:
    print('')
    print('Invalid Choice')
    choice = input('What do you play?\n')
  return choice.strip().lower()

def determine_outcome(ai_choice, user_choice):
  '''
  - Compare ai & user inputs according to game rules
  - if tie, return 0
  - if user wins, return +1
  - if AI wins, return -1
  '''
  if ai_choice == user_choice:
    return 0
  elif ai_choice == 'rock':
    return 1 if user_choice == 'paper' else -1
  elif ai_choice == 'paper':
    return 1 if user_choice == 'scissors' else -1
  elif ai_choice == 'scissors':
    return 1 if user_choice == 'rock' else -1

def print_winner(score_change):
  '''
    - Accepts score change from this round
    - Prints result message based on score change
  '''
  if score_change > 0:
    print('The winner is: Human')
  elif score_change < 0:
    print('The winner is: AI')
  else:
    print('This round is a tie.')
  print('')

main()
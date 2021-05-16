'''
This program will take in a series of scores from a user
and store them into a list.
'''

EXTRA_CREDIT = 5

def main():
  score_list = get_scores()
  if len(score_list) == 0: 
    print("No Scores Entered")
    return
  print('Scores are:')
  print_list(score_list)
  average = compute_average(score_list)
  print('Average score is:', average)
  print('Adding extra credit:', EXTRA_CREDIT, 'points')
  
  apply_extra_credit(score_list)
  print('Scores are:')
  print_list(score_list)
  new_average = compute_average(score_list)
  print('New average score is:', new_average)

def get_scores():
  '''
  Asks user for scores and returns a list containing the scores
  '''
  score_list = []
  while True:
    score = float(input('Enter a score (0 to stop): '))
    if score == 0: break
    score_list.append(score)
  return score_list

def compute_average(score_list):
  '''
  Takes in a list of scores and returns the average value
  '''
  total = sum(score_list)
  count = len(score_list)
  return total / count

def apply_extra_credit(score_list):
  '''
  Takes in a list of scores and applies a point bonus to each value
  '''
  for i in range(len(score_list)):
    score_list[i] += EXTRA_CREDIT

def print_list(list):
  '''
    Takes in a list and prints each element in the list
  '''
  for el in list:
    print(el)

main()
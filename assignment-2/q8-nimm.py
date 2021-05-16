
'''
Nimm is an ancient game of strategy that is named after the old German word for "take." 
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. 
Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:
- The game starts with a pile of 20 stones between the players.
- The two players alternate turns.
- On a given turn, a player may take either 1 or 2 stone from the center pile.
- The two players continue until the center pile has run out of stones.
'''

NUM_STONES = 20

def main():
  current_player = 1
  current_stones = NUM_STONES

  while current_stones > 0:
    selection = get_valid_selection(current_stones, current_player)
    print('')
    current_stones -= selection
    current_player = 2 if current_player == 1 else 1
  print('Player %i wins!'%(current_player))
  



def get_valid_selection(current_stones, current_player):
  selection = 0
  print('There are ' + str(current_stones) + ' stones left')
    selection = int(input('Player %i would you like to remove 1 or 2 stones? '%(current_player)))
  while not (selection == 1 or selection == 2):
    if selection < 1 or selection > 2:
      selection = int(input('Please enter 1 or 2: '))
  return selection





main()
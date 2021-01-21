# Azaan Dawson and Ryan Dentchev amdg 1-13-21

import random
def start_game(x):
  user_versus_input = input("Do you want to play against the computer?(Y/N)\n")
  if user_versus_input.upper() == "Y":
    player_cards = random.sample(x, 7)
    computer_cards = random.sample(x, 7)
    starting_card = random.choice(x)
    print('The cards have been dealt\n Directions: type the card you want to play (in lowercase) in the terminal. If you don\'t have a card to play input pick up. If you would like to quit the game enter quit. If starting card is wild card or draw 4 restart.')
    print('The starting card is {0}. Go player one!\n'.format(starting_card))
    card_down = starting_card
    card_down_check = starting_card.split(' ', 1)
    quit = 0
    while True:
      if computer_cards == []:
        print('The Computer won!!')
        break 
      while True: 
        player_play= input('Player 1 you have {0} cards in your hand and {1} is the card down. which one will you play? \n'.format(player_cards, card_down))
        player_play_check = player_play.split(' ', 1)

        if player_play == 'pick up':
          print('Player 1 has no cards\n')
          player_cards.append(random.choice(x))
          break

        elif player_play == 'quit':
          quit += 1
          break 
    
        elif player_play == 'wild card':
          card_down = player_play
          new_color = input('Pick the color you want: ')
          card_down_check[0] = new_color
          print('Player 1 changed the color to {0}'.format(new_color))
          player_cards.remove(player_play)
          break

        elif player_play == 'draw 4':
          card_down = player_play
          new_color = input('Pick the color you want: ')
          card_down_check[0] = new_color
          print('Player 1 changed the color to {0}'.format(new_color))
          computer_cards.extend(random.sample(x,4))
          player_cards.remove(player_play)
          print('The computer\'s turn was skipped go again\n')
          continue
        
        elif player_play_check[0] != card_down_check[0] and player_play_check[1] != card_down_check[1]:
          print('{0} can not be played, the number and/or color to not match. pick again\n'.format(player_play))
          continue
      
        elif player_play_check[1] == 'draw 2':
          card_down = player_play
          card_down_check = player_play_check
          computer_cards.extend(random.sample(x,2))
          player_cards.remove(player_play)
          print('The computer\'s turn was skipped go again\n')
          continue

        elif player_play_check[1] == 'skip':
          card_down = player_play
          card_down_check = player_play_check
          player_cards.remove(player_play)
          print('The computer\'s turn was skipped go again\n')
          continue

        elif player_play_check[1] == 'reverse':
          card_down = player_play
          card_down_check = player_play_check
          player_cards.remove(player_play)
          print('The computer\'s turn was skipped go again\n')
          continue 

        elif player_play_check[0] == card_down_check[0]:
          card_down = player_play
          card_down_check = player_play_check
          player_cards.remove(player_play)
          break  

        elif player_play_check[1] == card_down_check[1]:
          card_down = player_play
          card_down_check = player_play_check
          player_cards.remove(player_play)
          break    

        elif player_play == card_down:
          player_cards.remove(player_play)
          break

      if player_cards == []:
        print('Player 1 won!!')
        break
      if quit != 0:
        print('YOU LOSE!!')
        break     
          #split between p and computer
      while True:
        card_match = 0
        for card in computer_cards:
          card_check = card.split(' ', 1)
          if card != card_down:
            if card == 'wild card':
              card_down = card
              new_color = random.choice(['red', 'blue', 'green', 'yellow'])
              card_down_check[0] = new_color
              print('The Computer put down a {1}, and changed the color to {0}'.format(new_color, card))
              computer_cards.remove(card)
              card_match +=1
              break

            if card == 'draw 4':
              card_down = card
              new_color = random.choice(['red', 'blue', 'green', 'yellow'])
              card_down_check[0] = new_color
              print('The computer put down a {1}, and changed the color to {0}'.format(new_color,card))
              player_cards.extend(random.sample(x,4))
              computer_cards.remove(card)
              print('Player 1\'s turn was skipped.\n')
              continue

            elif card_check[0] == card_down_check[0] or card_check[1] == card_down_check[1]:
              if card_check[1] == 'skip':
                card_down = card
                card_down_check = card_check
                computer_cards.remove(card)
                print('The computer put down a {0}'.format(card))
                print('Player\'s turn was skipped go again\n')
                continue

              elif card_check[1] == 'reverse':
                card_down = card
                card_down_check = card_check
                computer_cards.remove(card)
                print('The computer put down a {0}'.format(card))
                print('Player\'s turn was skipped go again\n')
                continue
                
              elif card_check[1] == 'draw 2':
                card_down = card
                card_down_check = card_check
                player_cards.extend(random.sample(x,2))
                computer_cards.remove(card)
                print('The computer put down a {0}'.format(card))
                print('Player\'s turn was skipped go again\n')
                continue
              else:
                card_down = card      
                card_down_check = card_check
                computer_cards.remove(card)
                print('The computer put down a {0}'.format(card))
                card_match +=1
                break

          elif card == card_down:
            print("The computer put down a {0}".format(card))
            computer_cards.remove(card)
            card_match +=1
            break

        if card_match == 0 :
          print('Computer has no cards\n')
          computer_cards.append(random.choice(x))
          break

        elif card_match != 0:
          card_match = 0
          break  

          #split between pvc and 2p
  elif user_versus_input.upper() == "N":
    player1_cards = random.sample(x, 7)
    player2_cards = random.sample(x, 7)
    starting_card = random.choice(x)
    print('The cards have been dealt\n Directions: type the card you want to play (in lowercase) in the terminal. If you don\'t have a card to play input pick up.')
    print('The starting card is {0}. Go player one!\n'.format(starting_card))
    card_down = starting_card
    card_down_check = starting_card.split(' ', 1) 
    quit = 0
    while True:
      if player2_cards == []:
        print('Player 2 won!!')
        break 
      while True: 
        player1_play= input('Player 1 you have {0} cards in your hand and {1} is the card down. which one will you play? \n'.format(player1_cards, card_down))
        player1_play_check = player1_play.split(' ', 1)

        if player1_play == 'pick up':
          print('Player 1 has no cards\n')
          player1_cards.append(random.choice(x))
          break
        elif player1_play == 'quit':
          quit += 1
          break  
    
        elif player1_play == 'wild card':
          card_down = player1_play
          new_color = input('Pick the color you want: ')
          card_down_check[0] = new_color
          print('Player 1 changed the color to {0}'.format(new_color))
          player1_cards.remove(player1_play)
          break

        elif player1_play == 'draw 4':
          card_down = player1_play
          new_color = input('Pick the color you want: ')
          card_down_check[0] = new_color
          print('Player 1 changed the color to {0}'.format(new_color))
          player2_cards.extend(random.sample(x,4))
          player1_cards.remove(player1_play)
          print('Player 2\'s turn was skipped go again\n')
          continue
        
        elif player1_play_check[0] != card_down_check[0] and player1_play_check[1] != card_down_check[1]:
          print('{0} can not be played, the number and/or color to not match. pick again\n'.format(player1_play))
          continue
      
        elif player1_play_check[1] == 'draw 2':
          card_down = player1_play
          card_down_check = player1_play_check
          player2_cards.extend(random.sample(x,2))
          player1_cards.remove(player1_play)
          print('Player 2\'s turn was skipped go again\n')
          continue

        elif player1_play_check[1] == 'skip':
          card_down = player1_play
          card_down_check = player1_play_check
          player1_cards.remove(player1_play)
          print('Player 2\'s turn was skipped go again\n')
          continue

        elif player1_play_check[1] == 'reverse':
          card_down = player1_play
          card_down_check = player1_play_check
          player1_cards.remove(player1_play)
          print('Player 2\'s turn was skipped go again\n')
          continue   

        elif player1_play == card_down:
          player1_cards.remove(player1_play)
          break

        elif player1_play_check[0] == card_down_check[0] or player1_play_check[1] == card_down_check[1]:
          card_down = player1_play
          card_down_check = player1_play_check
          player1_cards.remove(player1_play)
          break

      if player1_cards == []:
        print('Player 1 won!!')
        break
      if quit != 0:
        print('YOU LOSE!')
        break     
          #split between p1 and 2
      while True:  
          player2_play= input('Player 2 you have {0} cards in your hand and {1} is the card down. which one will you play? \n'.format(player2_cards, card_down))
          player2_play_check = player2_play.split(' ', 1)
          
          if player2_play == 'pick up':
            print('Player 2 has no cards\n')
            player2_cards.append(random.choice(x))
            break
          if player2_play == 'quit':
            quit +=1
            break  

          elif player2_play == 'wild card':
            card_down = player2_play
            new_color = input('Pick the color you want: ')
            card_down_check[0] = new_color
            print('Player 2 changed the color to {0}'.format(new_color))
            player2_cards.remove(player2_play)
            break

          elif player2_play == 'draw 4':
            card_down = player2_play
            new_color = input('Pick the color you want: ')
            card_down_check[0] = new_color
            print('Player 2 changed the color to {0}'.format(new_color))
            player1_cards.extend(random.sample(x,4))
            player2_cards.remove(player2_play)
            print('Player 1\'s turn was skipped go again\n')
            continue

          elif player2_play_check[0] != card_down_check[0] and player2_play_check[1] != card_down_check[1]:
            print('{0} can not be played, the number and/or color to not match. pick again\n'.format(player2_play))
            continue

          elif player2_play_check[1] == 'draw 2':
            card_down = player2_play
            card_down_check = player2_play_check
            player1_cards.extend(random.sample(x,2))
            player2_cards.remove(player2_play)
            print('Player 1\'s turn was skipped go again\n')
            continue

          elif player2_play_check[1] == 'skip':
            card_down = player2_play
            card_down_check = player2_play_check
            player2_cards.remove(player2_play)
            print('Player 1\'s turn was skipped go again\n')
            continue

          elif player2_play_check[1] == 'reverse':
            card_down = player2_play
            card_down_check = player2_play_check
            player2_cards.remove(player2_play)
            print('Player 1\'s turn was skipped go again\n')
            continue   

          elif player2_play == card_down:
            player2_cards.remove(player2_play)
            break

          elif player2_play_check[0] == card_down_check[0] or player2_play_check[1] == card_down_check[1]:
            player2_cards.remove(player2_play)
            card_down = player2_play
            card_down_check = player2_play_check
            break
      if quit != 0:
        print('YOU LOSE!')
        break      

uno_deck2 = ['wild card', 'wild card', 'wild card', 'wild card', 'draw 4', 'draw 4', 'draw 4', 'draw 4', 'red 0', 'red 1', 'red 1', 'red 2', 'red 2', 'red 3', 'red 3', 'red 4', 'red 4', 'red 5', 'red 5', 'red 6', 'red 6', 'red 7', 'red 7', 'red 8', 'red 8', 'red 9', 'red 9', 'red skip', 'red skip', 'red reverse', 'red reverse', 'red draw 2', 'red draw 2', 'green 0', 'green 1', 'green 1', 'green 2', 'green 2', 'green 3', 'green 3', 'green 4', 'green 4', 'green 5', 'green 5', 'green 6', 'green 6', 'green 7', 'green 7', 'green 8', 'green 8', 'green 9', 'green 9', 'green skip', 'green skip', 'green reverse', 'green reverse', 'green draw 2', 'green draw 2', 'blue 0', 'blue 1', 'blue 1', 'blue 2', 'blue 2', 'blue 3', 'blue 3', 'blue 4', 'blue 4', 'blue 5', 'blue 5', 'blue 6', 'blue 6', 'blue 7', 'blue 7', 'blue 8', 'blue 8', 'blue 9', 'blue 9', 'blue skip', 'blue skip', 'blue reverse', 'blue reverse', 'blue draw 2', 'blue draw 2', 'yellow 0', 'yellow 1', 'yellow 1', 'yellow 2', 'yellow 2', 'yellow 3', 'yellow 3', 'yellow 4', 'yellow 4', 'yellow 5', 'yellow 5', 'yellow 6', 'yellow 6', 'yellow 7', 'yellow 7', 'yellow 8', 'yellow 8', 'yellow 9', 'yellow 9', 'yellow skip', 'yellow skip', 'yellow reverse', 'yellow reverse', 'yellow draw 2', 'yellow draw 2']

(start_game(uno_deck2))

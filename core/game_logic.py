def calculate_hand_value(hand: list[dict]) -> int:
    calc = 0
    convert = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    for i in hand['hand']:
        if hand['hand']['rank'].isdigit():
            calc+= int(hand['hand']['rank'])
        else:
            if hand['hand']['rank'] in convert:
                calc += convert[hand['hand']['rank']]
    return calc            








def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
        for i in range (2):
            player['hand'] = deck.pop()
            dealer['hand'] = deck.pop()
        print("your hand is:", calculate_hand_value(player))
        print("dealer hand is:", calculate_hand_value(dealer))       

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    if calculate_hand_value(dealer)>= 17 < 21:

        return True
    return "dealer lost", False 

def ask_player_action() -> str:
    choise = ['H','S']
    input1 = input("Choose H or S: ")
    if input1 not in choise:
         ask_player_action()
    return input1

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while  ask_player_action() == 'H':
          player['hand'] = deck.pop()
          if calculate_hand_value(player) > 21:
              print("lost")
    else:
        if dealer_play(deck,dealer) == True:
            if calculate_hand_value(dealer) > calculate_hand_value(player):
                 return 'dealer won'
            elif calculate_hand_value(dealer) < calculate_hand_value(player):
                 return "you won"
            elif calculate_hand_value(dealer) == calculate_hand_value(player):
                return "equal"
        return "win!!"        
    

          
        
          

     
    


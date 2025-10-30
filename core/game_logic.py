import deck
def calculate_hand_value(hand: list[dict]) -> int:
    value= {'rank':'', 'suite': '', 'value': ''}
    convert = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    
    value['rank'] =  hand['rank']
    value['suite'] = hand['suite']
    if hand['rank'].isdigit() :
        value['value'] = int(hand['rank'])
    else:
        value ['value'] =  convert[hand['rank']]  
    return value ['value']



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
        player.update(deck[0])
        player.update(deck[1])
        del deck[0]
        del deck [1]
        dealer.update(deck[0])
        dealer.update(deck[1])
        del deck[0]
        del deck [1]
        print(calculate_hand_value(player))
        print((calculate_hand_value(dealer)))
        
print(deal_two_each(deck.build_standard_deck(),{},{}))        

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    if calculate_hand_value(dealer)>=17 < 21:
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
     while ask_player_action() == 'H':
          deck.update(deck[0])
          del deck[0]
          if calculate_hand_value(player)>21:
            return 'lost', run_full_game
          continue
     else:
        if dealer_play(deck,dealer) == True:
            if calculate_hand_value(dealer) > calculate_hand_value(player):
                 print('dealer won')
            elif calculate_hand_value(dealer) < calculate_hand_value(player):
                 print("you won")
            else:
                 print("equal")    
        print("win!!")    
          
          

          
        
          

     
    


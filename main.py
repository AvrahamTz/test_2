import core.deck
import core.game_logic
if __name__ == "__main__":
    deck = core.deck.shuffle_by_suit(core.deck.build_standard_deck())
    player = {'hand': [ ] }
    dealer = {'hand': [ ] }



core.game_logic.run_full_game(core.deck.shuffle_by_suit(core.deck.build_standard_deck()),{'hand': [ ] },{'hand': [ ] })           
          
          
    




















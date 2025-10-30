import random
def build_standard_deck() -> list[dict]:

    cards_list=[]
    
    def  create_card(rank, suite):
        deck = {}
        deck['rank'] = rank
        deck ['suite'] =suite
        return deck

    
    rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K',]
    
    suite = ['H','C','D', 'S']

    for ranks in rank:
        for suites in suite:
            cards_list.append(create_card(ranks,suites))
    return cards_list



def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(swaps):
        index_i = random.randint(0,len(deck)-1)
        index_j = random.randint(0,len(deck)-1)
        if index_i == index_j or (deck[index_j]['suite'] == 'H'and index_j % 5 != 0) or (deck[index_j]['suite'] == 'C'and index_j % 3 != 0) or  (deck[index_j]['suite'] == 'D'and index_j % 2 != 0) or (deck[index_j]['suite'] == 'S'and index_j % 7!= 0):
            continue
        deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
    return deck


        




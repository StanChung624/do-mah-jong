from Deck import Deck
from typing import Dict, List, Tuple

def comb_remove_pair(holding:List[str])->List[List[str]]:
    """
        move pair to last and returns combinations from given holdings.
        ex: given [A,A,B,B,B,C,D,E]
        return: [[B,B,B,C,D,E,A,A], 
                 [A,A,B,C,D,E,B,B] ]

    """
    ret = list()
    tmp_map = dict()
    for card in holding:
        tmp_map[card] = 0
    for card in holding:
        tmp_map[card] += 1

    def remove_pair(target:str)->List[str]:
        ret = list()
        for card, count in tmp_map.items():
            if target == card:
                ret += [card]*(count-2)
            else:
                ret += [card]*count
        ret += [target, target]
        return ret


    for card, count in tmp_map.items():
        # for text pair only
        if count == 2 and card in Deck().t_list:
            return [remove_pair(card)]

    for card, count in tmp_map.items():
        if count >= 2:
            ret.append(remove_pair(card))
            

    return ret

def get_neighbor(card:str)->List[str]:
    """
        given card in format from deck, given -2 to +2.
        ex: given "o3"
        return: ["o1","o2","o3","o4","o5"]
    """    
    ret = list()
    # check is numeric card
    if card in Deck().m_list or \
    card in Deck().l_list or \
    card in Deck().o_list:        
        neighbor = [int(card[1]) - 2, int(card[1]) - 1, int(card[1]), int(card[1]) +1, int(card[1]) + 2]
        for nei in neighbor:
            if nei >= 1 and nei <= 9:
                ret.append(card[0]+str(nei))
        return ret
    else:
        return None


def check_txt(no_pair:List[str])->Tuple[List[str], Dict[str,int]]:
    """
        check for text card in holdings (pair removed already)
        and return with only numeric cards, and map of text
        ex: given o1, o2, o3, o4, o4, o4, N, N, N, S, S
        return: [o1, o2. o3, o4, o4, o4] and {N:3, S:2}
    """
    txt_map = dict(E=0, S=0, W=0, N=0, Ch=0, Fa=0, By=0)
    ret = list()
    for card in no_pair:
        if card in txt_map.keys():
            txt_map[card] += 1
        else:
            ret.append(card)
    
    for card, count in txt_map.items():
        if count < 3:
            return ret, None
    return ret, txt_map
        
def check_id(no_pair_n_txt:list, target:str, tri_count:int = 0):

    def get_pure_num(no_pair_n_txt:list, target:str):
        ret = list()
        for card in no_pair_n_txt:
            if target in card:
                ret.append(card.replace(target, ''))
        return ret
    
    def remove_smallest_pon(pure_num, tri_count=0):        
        if pure_num[0] == pure_num[1] and pure_num[1] == pure_num[2]:
            tri_count+=1
            return pure_num[3:], tri_count
        else:
            return pure_num, tri_count
        
    def remove_smallest_stt(pure_num):
        if len(pure_num)==0:
            return pure_num
        if int(pure_num[1]) == int(pure_num[0])+1 and int(pure_num[2]) == int(pure_num[0])+2:
            return pure_num[3:]
        else:
            return pure_num
    
    pure_num = get_pure_num(no_pair_n_txt, target)
    if len(pure_num) % 3 != 0:
        return False, tri_count
    
    pure_num.sort()

    while len(pure_num) != 0:
        origin = len(pure_num)
        pure_num, tri_count = remove_smallest_pon(pure_num, tri_count)
        pure_num = remove_smallest_stt(pure_num)
        if origin == len(pure_num):
            return False, tri_count
        
    return True, tri_count

def is_win(holding):
        combinations = comb_remove_pair(holding)

        if (len(combinations)==0):
            # no pair
            return False
        
        for comb in combinations:
            tri_count = 0
            no_pair_n_txt, no_use = check_txt(comb[:-2])
            if not no_use:
                continue

            result, tri_count = check_id(no_pair_n_txt, "o", tri_count)
            if not result:
                continue
            
            result, tri_count = check_id(no_pair_n_txt, "l", tri_count)
            if not result:
                continue

            result, tri_count = check_id(no_pair_n_txt, "m", tri_count)
            if not result:
                continue
            
            return True
        
        return False

if __name__ == "__main__":        

    test = ['o2', 'o3', 'l3', 'l3', 'l3', 'm5', 'm7', 'm6', 'Fa', 'Fa', 'S', 'S', 'S', 'W', 'W', 'W', 'o1']

    print(is_win(test))

    no_pair = comb_remove_pair(test)
    for comb in no_pair:
        print(comb)
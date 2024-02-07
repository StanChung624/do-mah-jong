def comb_remove_pair(holding:list):
    tmp_map = dict()
    ret = list()
    for card in holding:
        tmp_map[card] = 0
    for card in holding:
        tmp_map[card] += 1

    for card, value in tmp_map.items():
        if value >= 2:
            out = list()
            cnt = 0
            for c in holding:
                if c == card and cnt < 2:
                    cnt+=1
                    pass
                else:
                    out.append(c)
            out.extend([card,card])
            ret.append(out)
    return ret

def check_txt(no_pair:list):
    txt_map = dict(E=0, S=0, W=0, N=0, Ch=0, Fa=0, By=0)
    ret = list()
    for card in no_pair:
        if card in txt_map.keys():
            txt_map[card] += 1
        else:
            ret.append(card)
    
    for k, v in txt_map.items():
        if v == 1 or v == 2:
            return False, None
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
            if not no_pair_n_txt:
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
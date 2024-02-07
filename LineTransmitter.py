from Player import Player

def line_transmitter(in_string):
    try:
        tiles = list()
        in_string = in_string.replace(" ","")
        in_string = in_string.replace("\n","")
        map = {"筒":"o","條":"l","萬":"m","中":"Ch","發":"Fa","白":"By","東":"E","南":"S","西":"W","北":"N","None":""}
        def translate(tile:str):
            for k, v in map.items():
                if len(tile) == 1:
                    if v == tile:
                        return k
                elif not tile[1].isnumeric():
                    if v == tile:
                        return k
                else:
                    if v == tile[0]:
                        return tile[1] + k
        
        current = "萬"
        print(in_string)
        for chr in in_string:
            if not chr.isnumeric() or chr == "萬":
                current = map[chr]
                continue
            else:
                if current in ["Ch","Fa","By","E","S","W","N"]:
                    tiles.extend([current]*int(chr))
                else:
                    tiles.append(current+chr)
        
        print(tiles)
        listen_tiles = get_listen_tiles(tiles)
        print(listen_tiles)

        ret = ""
        for tile in listen_tiles:
            ret += translate(tile) + ", "

        return ret
    except:
        return "請用下面範例的格式告訴我你的牌唷！\n 筒、條、萬：直接輸入數字\n 中、發、白、風：輸入張數 \n範例1:\n筒1112345678999 條 萬 中3 發 白 東 南 西 北 \n範例2:\n筒5551234"
            

def get_listen_tiles(holdings):
    player = Player()
    player.holding = holdings
    return player.listen()

if __name__ == "__main__":
    test = "筒1112345678999條 萬 中3發白東南西北"
    print(line_transmitter(test))
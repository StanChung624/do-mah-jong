from Player import Player
from test.TestLineTransmitter import *

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
        
        current = "m"
        
        for chr in in_string:
            if not chr.isnumeric() or chr == "萬":
                current = map[chr]
                continue
            else:
                if current in ["Ch","Fa","By","E","S","W","N"]:
                    tiles.extend([current]*int(chr))
                else:
                    tiles.append(current+chr)
        
        ret = ""

        # 聽牌 mode
        if (len(tiles) - 2) % 3 != 0 :
            listen_tiles = get_listen_tiles(tiles)    
            if len(listen_tiles) > 0:
                ret += "等： "
                
                for tile in listen_tiles:
                    ret += translate(tile) + ", "
            else:
                ret = "好像沒有等耶!"

            
        # 胡牌 mode
        else:
            player = Player(holding=tiles)
            if player.is_win():
                return "胡啦!!"
            analysis = player.analyze()            
            for ditch_card, waits in analysis.items():
                ret += "丟 <" + translate(ditch_card) + "> 等：\n"
                for pairs in waits:
                    for k,v in pairs.items():
                        ret += "  " + translate(k) + "有 " + str(v) + "張\n"
                ret += "\n"

        return ret

    except:
        return "請用下面範例的格式告訴我你的牌唷！\n"\
        "筒、條、萬：直接輸入數字\n"\
        "中、發、白、風：輸入張數\n"\
        "記得包含雀唷!\n\n"\
        "範例1:\n"\
        "筒1112345678999 條 萬 中3 發 白 東 南 西 北\n\n"\
        "範例2:\n"\
        "筒5551234發3\n\n"\
        "也可以直接告訴我數字牌的數字\n"\
        "範例3:\n4567888"
            

def get_listen_tiles(holdings):
    player = Player()
    player.holding = holdings 
    return player.listen()

if __name__ == "__main__":
    print("TestDitchCardMode result = ", TestDitchCardMode(line_transmitter))
    print("TestListenCardMode result = ", TestListenCardMode(line_transmitter))
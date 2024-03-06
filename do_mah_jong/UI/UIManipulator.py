from typing import List
from .BaseStructure import BaseStructure, QtGui, QtCore, QtWidgets

from ..Basic.Deck import translate, translate_list
from ..UI.UIPlayer import UIPlayer, Player
from ..UI.Status import Status
from time import sleep

def get_icon_name(card:str):
    ret = "./do_mah_jong/icon/"
    if card[0] == "X":
        ret += "x" + card[1] + "_.jpg"
    else:
        ret += card + ".jpg"
    return ret

class UIManipulator(BaseStructure):

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        Dialog.setWindowTitle("do-mah-jong")
        Dialog.setWindowIcon(QtGui.QIcon(get_icon_name("o1")))
        # sea messages control
        self.sea_cards = list()
        self.current_sea_index = 0
    
    def set_button_tiles(self):
        self.seas = self.__set_sea_button()
        self.__set_tiles_button()        
        for tile in self.tiles:
            tile.setText("")
        for flw in self.flws:
            flw.setText("")
        return

    def to_sea(self, card:str):
        self.sea_cards.append(card)        
        
    def flush_sea(self):
        for i in range(self.current_sea_index, len(self.sea_cards)):
            card = self.sea_cards[i]
            qpixmap = QtGui.QPixmap()
            qpixmap = qpixmap.fromImage(QtGui.QImage(get_icon_name(card)))
            qpixmap = qpixmap.scaled(30,40)
            self.seas[i].setPixmap(qpixmap)
        self.current_sea_index = len(self.sea_cards)
        self.ui_com_discard_card_clear()

    def reset_sea(self):
        self.sea_cards = list()
        for sea in self.seas:
            sea.setPixmap(QtGui.QPixmap())
        return
    
    def tiles_off(self):
        for tile in self.tiles:
            tile.setEnabled(False)

    def tiles_on(action):
        def wrapper(self, ui_player:UIPlayer):
            if self.status == Status.to_ditch:
                for tile in self.tiles:
                    tile.setEnabled(True)            
            action(self ,ui_player)
        return wrapper
    
    def ui_com_discard_card(self, player:Player, card):
        if player.index == 1:
            label = self.p1_discard
        elif player.index == 2:
            label = self.p2_discard
        elif player.index == 3:
            label = self.p3_discard
        
        qpixmap = QtGui.QPixmap()
        qpixmap = qpixmap.fromImage(QtGui.QImage(get_icon_name(card)))
        qpixmap = qpixmap.scaled(30,40)
        label.setPixmap(qpixmap)
        QtCore.QCoreApplication.processEvents()
        if player.index == 3:
            sleep(1.5)
            QtCore.QCoreApplication.processEvents()
        else:
            sleep(0.5)

    def ui_com_discard_card_clear(self):
        self.p1_discard.setPixmap(QtGui.QPixmap())
        self.p2_discard.setPixmap(QtGui.QPixmap())
        self.p3_discard.setPixmap(QtGui.QPixmap())
        

    @tiles_on
    def show_tiles(self, ui_player:UIPlayer):
        if self.status == Status.to_ditch:
            self.copilot_msg.setText(
                "o_o:\n我是會丟 " + translate(ui_player.copilot()) + " 啦"
            )
        else:
            self.copilot_msg.setText(
                "o_o"
            )

        Nholding = len(ui_player.holding)
        Nflower = len(ui_player.flower)
        for i in range(len(self.tiles)):
            if i < Nholding:          
                card = ui_player.holding[i]
                #self.tiles[i].setText(translate(card))
                self.tiles[i].setIcon(QtGui.QIcon(get_icon_name(card)))
                self.tiles[i].setIconSize(QtCore.QSize(40,40))
            else:
                self.tiles[i].setIcon(QtGui.QIcon())
                self.tiles[i].setEnabled(False)
        for i in range(len(self.flws)):
            if i < Nflower:
                card = ui_player.flower[i]
                self.flws[i].setIcon(QtGui.QIcon(get_icon_name(card)))
                self.flws[i].setIconSize(QtCore.QSize(40,40))
                self.flws[i].setEnabled(True)
            else:
                self.flws[i].setIcon(QtGui.QIcon())
                self.flws[i].setEnabled(False)

    def __set_sea_button(self)->List[QtWidgets.QPushButton]:
        ret = list()
        for i in range(60):
            eval("ret.append(self.sea_" + str(i) + ")")
        return ret

    def __set_tiles_button(self)->None:
        self.tiles = list()
        self.tiles.append(self.tile_0)
        self.tiles.append(self.tile_1)
        self.tiles.append(self.tile_2)
        self.tiles.append(self.tile_3)
        self.tiles.append(self.tile_4)
        self.tiles.append(self.tile_5)
        self.tiles.append(self.tile_6)
        self.tiles.append(self.tile_7)
        self.tiles.append(self.tile_8)
        self.tiles.append(self.tile_9)
        self.tiles.append(self.tile_10)
        self.tiles.append(self.tile_11)
        self.tiles.append(self.tile_12)
        self.tiles.append(self.tile_13)
        self.tiles.append(self.tile_14)
        self.tiles.append(self.tile_15)
        self.tiles.append(self.tile_16)

        self.flws = list()
        self.flws.append(self.flw_0)
        self.flws.append(self.flw_1)
        self.flws.append(self.flw_2)
        self.flws.append(self.flw_3)
        self.flws.append(self.flw_4)

        self.flws.append(self.flw_5)
        self.flws.append(self.flw_6)
        self.flws.append(self.flw_7)
        self.flws.append(self.flw_8)
        self.flws.append(self.flw_9)

        self.flws.append(self.flw_10)
        self.flws.append(self.flw_11)
        self.flws.append(self.flw_12)
        self.flws.append(self.flw_13)
        self.flws.append(self.flw_14)

        self.flws.append(self.flw_15)      

        def ditch_card_action(self):
            self.tiles_off()
            self.status = Status.ditched
            self.reset_act_button()
            self.players.reset(self.ui_player)
            self.user_ditch_card=self.ui_player.holding[self.user_ditch_card_id]
            self.ui_player.discard_card(self.user_ditch_card)
            self.log("打: " + translate(self.user_ditch_card))
            self.show_tiles(self.ui_player)
            self.check_others_action() 
    
        def fn_0():
            self.user_ditch_card_id = 0
            ditch_card_action(self)
            return
        def fn_1():
            self.user_ditch_card_id = 1
            ditch_card_action(self)
            return
        def fn_2():
            self.user_ditch_card_id = 2
            ditch_card_action(self)
            return
        def fn_3():
            self.user_ditch_card_id = 3
            ditch_card_action(self)
            return
        def fn_4():
            self.user_ditch_card_id = 4
            ditch_card_action(self)            
            return
        def fn_5():
            self.user_ditch_card_id = 5
            ditch_card_action(self)
            return
        def fn_6():
            self.user_ditch_card_id = 6
            ditch_card_action(self)
            return
        def fn_7():
            self.user_ditch_card_id = 7
            ditch_card_action(self)
            return
        def fn_8():
            self.user_ditch_card_id = 8
            ditch_card_action(self)
            return
        def fn_9():
            self.user_ditch_card_id = 9
            ditch_card_action(self)
            return
        def fn_10():
            self.user_ditch_card_id = 10
            ditch_card_action(self)
            return
        def fn_11():
            self.user_ditch_card_id = 11
            ditch_card_action(self)
            return        
        def fn_12():
            self.user_ditch_card_id = 12
            ditch_card_action(self)
            return        
        def fn_13():
            self.user_ditch_card_id = 13
            ditch_card_action(self)
            return        
        def fn_14():
            self.user_ditch_card_id = 14
            ditch_card_action(self)
            return
        def fn_15():
            self.user_ditch_card_id = 15
            ditch_card_action(self)
            return        
        def fn_16():
            self.user_ditch_card_id = 16
            ditch_card_action(self)
            return
        
        self.tile_0.clicked.connect(fn_0)
        self.tile_1.clicked.connect(fn_1)
        self.tile_2.clicked.connect(fn_2)
        self.tile_3.clicked.connect(fn_3)
        self.tile_4.clicked.connect(fn_4)

        self.tile_5.clicked.connect(fn_5)
        self.tile_6.clicked.connect(fn_6)
        self.tile_7.clicked.connect(fn_7)
        self.tile_8.clicked.connect(fn_8)
        self.tile_9.clicked.connect(fn_9)

        self.tile_10.clicked.connect(fn_10)
        self.tile_11.clicked.connect(fn_11)
        self.tile_12.clicked.connect(fn_12)
        self.tile_13.clicked.connect(fn_13)
        self.tile_14.clicked.connect(fn_14)
        self.tile_15.clicked.connect(fn_15)
        self.tile_16.clicked.connect(fn_16)

        

    def set_button_eat(self, ui_player:UIPlayer):
            eat_combinations = ui_player.eat_combinations

            def show_eat_combination():
                if len(eat_combinations) >= 1:
                    def ui_eat_0():                        
                        ui_player.eat(formation=eat_combinations[0])
                        self.status = Status.to_ditch
                        self.show_tiles(ui_player)
                        self.reset_act_button()
                        return
                    self.button_eat.setText(str(translate_list(eat_combinations[0])))
                    self.button_eat.setEnabled(True)
                    self.button_pon.setEnabled(False)
                    self.button_gan.setEnabled(False)
                    self.button_win.setEnabled(False)
                    self.button_eat.clicked.connect(ui_eat_0)
                if len(eat_combinations) >= 2:
                    def ui_eat_1():
                        ui_player.eat(formation=eat_combinations[1])
                        self.status = Status.to_ditch
                        self.show_tiles(ui_player)
                        self.reset_act_button()                        
                        return
                    self.button_pon.setText(str(translate_list(eat_combinations[1])))
                    self.button_pon.setEnabled(True)
                    self.button_pon.clicked.connect(ui_eat_1)
                if len(eat_combinations) >= 3:
                    def ui_eat_2():
                        ui_player.eat(formation=eat_combinations[2])
                        self.status = Status.to_ditch
                        self.show_tiles(ui_player)
                        self.reset_act_button()                        
                        return
                    self.button_gan.setText(str(translate_list(eat_combinations[2])))
                    self.button_gan.setEnabled(True)
                    self.button_gan.clicked.connect(ui_eat_2)

            self.button_eat.setEnabled(True)
            self.button_eat.clicked.connect(show_eat_combination)

    def set_button_pon(self, ui_player:UIPlayer):
        def ui_pon():
                ui_player.pon()
                self.button_pon.setEnabled(False)
                self.status = Status.to_ditch
                self.show_tiles(ui_player)
                self.reset_act_button()
                return

        self.button_pon.setEnabled(True)
        self.button_pon.clicked.connect(ui_pon)

    def set_button_gan(self, ui_player:UIPlayer):
        def ui_gan():
                ui_player.gan()
                self.log("補進了 " + translate(ui_player.last_draw))
                self.button_gan.setEnabled(False)               
                self.reset_act_button()
                self.status = Status.to_ditch
                self.show_tiles(ui_player)
                return

        self.button_gan.setEnabled(True)
        self.button_gan.clicked.connect(ui_gan)

    def set_button_self_gan(self, ui_player:UIPlayer):
        def ui_self_gan():
                ui_player.self_gan()
                self.log("補進了 " + translate(ui_player.last_draw))
                self.button_gan.setEnabled(False)               
                self.reset_act_button()
                self.status = Status.to_ditch
                self.show_tiles(ui_player)
                return

        self.button_gan.setEnabled(True)
        self.button_gan.clicked.connect(ui_self_gan)

    def set_button_win(self, ui_player:UIPlayer):
        def action():
            if self.players.current().index == ui_player.index:
                self.log("player " + str(ui_player.index) + " 胡啦! (自摸)")            
            ui_player.win()
            self._environment_update()
            self.show_tiles(ui_player)
            self.status = Status.start_game
            self.set_regame_button(self.setup_game)
            return 
        self.button_win.setEnabled(True)
        self.button_win.clicked.connect(action)

    def set_button_no_act(self, ui_player:UIPlayer, action):        
        if not ui_player.can_win:
            self.button_win.setText("過")
            self.button_win.setEnabled(True)
            self.button_win.clicked.connect(action)
        elif not ui_player.can_gan:
            self.button_gan.setText("過")
            self.button_gan.setEnabled(True)
            self.button_gan.clicked.connect(action)
        elif not ui_player.can_pon:
            self.button_pon.setText("過")
            self.button_pon.setEnabled(True)
            self.button_pon.clicked.connect(action)
        elif not ui_player.can_eat:
            self.button_eat.setText("過")
            self.button_eat.setEnabled(True)
            self.button_eat.clicked.connect(action)

    def reset_act_button(self):
        self.button_eat.setText("吃")        
        self.button_pon.setText("碰")        
        self.button_gan.setText("槓")
        self.button_win.setText("胡")
        self.button_eat.setEnabled(False)
        self.button_pon.setEnabled(False)
        self.button_gan.setEnabled(False)
        self.button_win.setEnabled(False)        
        try:
            self.button_eat.clicked.disconnect()
        except:
            pass
        try:
            self.button_pon.clicked.disconnect()
        except:
            pass
        try:
            self.button_gan.clicked.disconnect()
        except:
            pass
        try:
            self.button_win.clicked.disconnect()
        except:
            pass

    def set_regame_button(self, action):
        self.reset_act_button()
        self.button_eat.setEnabled(True)
        self.button_pon.setEnabled(False)
        self.button_gan.setEnabled(False)
        self.button_win.setEnabled(False)
        self.button_eat.setText("繼續?")

        self.button_eat.clicked.connect(action)
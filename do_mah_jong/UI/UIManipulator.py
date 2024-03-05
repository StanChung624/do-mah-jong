from typing import List
from .BaseStructure import BaseStructure
from ..Basic.Deck import translate, translate_list
from ..UI.UIPlayer import UIPlayer
from ..UI.Status import Status


class UIManipulator(BaseStructure):
    def __init__(self) -> None:
        super().__init__()
        
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        return self.__set_tiles_button()
    
    def tiles_off(self):
        for tile in self.tiles:
            tile.setEnabled(False)

    def tiles_on(action):
        def wrapper(self, ui_player:UIPlayer):
            for tile in self.tiles:
                tile.setEnabled(True)
            action(self ,ui_player)
        return wrapper

    @tiles_on
    def show_tiles(self, ui_player:UIPlayer):
        Nholding = len(ui_player.holding)
        ui_player.holding.sort()
        Nflower = len(ui_player.flower)
        for i in range(len(self.tiles)):
            if i < Nholding:          
                card = ui_player.holding[i]
                self.tiles[i].setText(translate(card))
            else:
                self.tiles[i].setText("")
                self.tiles[i].setEnabled(False)
        for i in range(len(self.flws)):
            if i < Nflower:
                card = ui_player.flower[i]
                self.flws[i].setText(translate(card))
            else:
                self.flws[i].setText("")        

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
    
        def fn_0():
            self.ditched_card_id = 0
            self.ui_ditch_card()
            return
        def fn_1():
            self.ditched_card_id = 1
            self.ui_ditch_card()
            return
        def fn_2():
            self.ditched_card_id = 2
            self.ui_ditch_card()
            return
        def fn_3():
            self.ditched_card_id = 3
            self.ui_ditch_card()
            return
        def fn_4():
            self.ditched_card_id = 4
            self.ui_ditch_card()            
            return
        def fn_5():
            self.ditched_card_id = 5
            self.ui_ditch_card()
            return
        def fn_6():
            self.ditched_card_id = 6
            self.ui_ditch_card()
            return
        def fn_7():
            self.ditched_card_id = 7
            self.ui_ditch_card()
            return
        def fn_8():
            self.ditched_card_id = 8
            self.ui_ditch_card()
            return
        def fn_9():
            self.ditched_card_id = 9
            self.ui_ditch_card()
            return
        def fn_10():
            self.ditched_card_id = 10
            self.ui_ditch_card()
            return
        def fn_11():
            self.ditched_card_id = 11
            self.ui_ditch_card()
            return        
        def fn_12():
            self.ditched_card_id = 12
            self.ui_ditch_card()
            return        
        def fn_13():
            self.ditched_card_id = 13
            self.ui_ditch_card()
            return        
        def fn_14():
            self.ditched_card_id = 14
            self.ui_ditch_card()
            return
        def fn_15():
            self.ditched_card_id = 15
            self.ui_ditch_card()
            return        
        def fn_16():
            self.ditched_card_id = 16
            self.ui_ditch_card()
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
                        self.show_tiles(ui_player)
                        self.reset_act_button()                        
                        return
                    self.button_pon.setText(str(translate_list(eat_combinations[1])))
                    self.button_pon.setEnabled(True)
                    self.button_pon.clicked.connect(ui_eat_1)
                if len(eat_combinations) >= 3:
                    def ui_eat_2():
                        ui_player.eat(formation=eat_combinations[2])
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
                self.show_tiles(ui_player)
                self.button_pon.setEnabled(False)               
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
                self.show_tiles(ui_player)
                return

        self.button_gan.setEnabled(True)
        self.button_gan.clicked.connect(ui_self_gan)

    def set_button_win(self, ui_player:UIPlayer):
        def action():
            if self.players.current().index == ui_player.index:
                self.log("player " + str(ui_player.index) + " 胡啦! (自摸)")
            else:
                self.log("player " + str(ui_player.index) + " 胡啦! ( player "+ str(self.players.index) +" 放槍)")

            ui_player.win()
            self._environment_update()
            self.show_tiles(ui_player)
            self.status = Status.start_game
            self.set_regame_button(self.setup_game)
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
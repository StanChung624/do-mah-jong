from do_mah_jong.Basic.GameController import GameControl, Players, Player, Deck
from do_mah_jong.Basic.Deck import CustomDeck, translate, translate_list
from do_mah_jong.UI.UIPlayer import UIPlayer


class status():
    start_game = "start_game"
    to_ditch = "to_ditch"
    ditched = "ditched"
    to_act = "to_act"
    acted = "acted"

class UIGameConroller(GameControl, ):
    def __init__(self, ui, debug: bool = False) -> None:
        self.ui = ui        
        
        self.set_tiles_button()
        self.sea = ""
        self.sea_count = 0
        self.ditched_card_id = -1
        self.ditched_card = ""
        self.ui_no_act = False

        self.on_screen = ""

        self.status = status.start_game

        for tile in self.tiles:
            tile.setText("")
        for flw in self.flws:
            flw.setText("")

        super().__init__(debug)

    def to_sea(self, card:str):
        self.sea_count += 1
        self.sea += translate(card) + ", "
        if self.sea_count % 20 == 0:
            self.sea += "\n"
        self.ui.sea.setText(self.sea)


    def show_tiles(self):
        Nholding = len(self.ui_player.holding)
        self.ui_player.holding.sort()
        Nflower = len(self.ui_player.flower)
        for i in range(len(self.tiles)):
            if i < Nholding:          
                card = self.ui_player.holding[i]
                self.tiles[i].setText(translate(card))
            else:
                self.tiles[i].setText("")
        for i in range(len(self.flws)):
            if i < Nflower:
                card = self.ui_player.flower[i]
                self.flws[i].setText(translate(card))
            else:
                self.flws[i].setText("")        
    
    def log(self, message: str, player: Player = None, end: str = "\n", announce: bool = True):
        super().log(message, player, end, announce)
        msg = ""
        if len(self._log) < 15:
            for log_ in self._log:
                msg += log_
        else:
            for log_ in self._log[-15:]:
                msg += log_
        self.ui.message.setText(msg)

    def output_env(self):
        env = "wind: " + self.winds.current() + " " + str(self.players.current_id()) + "\n"
        env += "streak: " + str(self.players.current().is_owner())
        self.ui.text_env.setText(env)
        self.sea = ""
        self.to_sea("")

    def setup_game(self):
        self.reset_act_button()
        self._log = list()
        self.ui.message.setText("")
        
        if self.status == status.start_game:
            self.deck = Deck()
            for player in self.players_list:
                player.reset()        
                player.deck = self.deck
                if type(player) is UIPlayer:
                    self.ui_player = player

            count = 0
            self.log("game start:", announce=True)
            
            self.players = Players(self.players_list, start_index=self.crrnt_id.current_id())

            self.output_env()

            dice_point = self.deck.roll_dice()
            self.log("roll dice: " + str(dice_point), announce=True)

            #deal cards
            for grab_i in range(4):
                for player in self.players:
                    for card_i in range(4):
                        player.draw_card()                 

            #amend flowers
            for player in self.players:
                player.amend_flower()
            
            self.players_draw_card()

    def check_others_action(self):
        card = self.ditched_card
        others = self.players.others()
        others.reverse()

        for player in others:
            player.see(card, self.players.current())
            can_act = player.can_eat or player.can_gan or\
                    player.can_pon or player.can_win
            if not can_act:
                continue
            elif self.ui_no_act:
                continue
            elif type(player) is UIPlayer and can_act:
                self.status = status.to_act
                self.set_act_button()
                return
            
            action = player.action()
            if action:
                if player.is_win():
                    self.log("player " + str(player.index) + " 胡啦!" +
                              "player " + str(self.players.current().index) + " 放槍)", player = player)
                    self._environment_update()
                    self.status = status.start_game
                    self.set_regame_button()
                    return
                self.ditched_card = player.ditch()
                self.log("player " + str(player.index) + " " + action + ", 打: " + translate(self.ditched_card))
                self.players.reset(player)
                return self.check_others_action()
    
        self.to_sea(card)
        self.players.next()
        self.players_draw_card()
        return    

    def _environment_update(self):
        return super()._environment_update()

    def players_draw_card(self):
        player = self.players.current()
        if self.players.current_id() == self.crrnt_id:
            self.count += 1

        card = player.draw_card()
        if card is None:
            self.log("流局")
            self._environment_update()
            self.status = status.start_game
            self.set_regame_button()
            return

        player.amend_flower()
        card = player.last_draw

        if player.is_win():
            self.log("player " + str(player.index) + " 胡啦! (自摸)", player = player)
            self._environment_update()
            self.status = status.start_game
            self.set_regame_button()
            return
        if type(player) is UIPlayer:
            self.status = status.to_ditch
            self.show_tiles()
            self.tiles_on()
            self.log("你摸進了 " + translate(card))
        else:            
            card = player.ditch()
            self.ditched_card = card
            self.log("player " + str(player.index) + ", 打: " + translate(self.ditched_card))
            self.check_others_action()

    def reset_act_button(self):
        self.ui.button_eat.setText("吃")        
        self.ui.button_pon.setText("碰")        
        self.ui.button_gan.setText("槓")
        self.ui.button_win.setText("胡")
        self.ui.button_eat.setEnabled(False)
        self.ui.button_pon.setEnabled(False)
        self.ui.button_gan.setEnabled(False)
        self.ui.button_win.setEnabled(False)        
        try:
            self.ui.button_eat.clicked.disconnect()
        except:
            pass
        try:
            self.ui.button_pon.clicked.disconnect()
        except:
            pass
        try:
            self.ui.button_gan.clicked.disconnect()
        except:
            pass
        try:
            self.ui.button_win.clicked.disconnect()
        except:
            pass

    def set_regame_button(self):
        self.reset_act_button()
        self.ui.button_eat.setEnabled(True)
        self.ui.button_pon.setEnabled(False)
        self.ui.button_gan.setEnabled(False)
        self.ui.button_win.setEnabled(False)
        self.ui.button_eat.setText("繼續?")

        self.ui.button_eat.clicked.connect(self.setup_game)

    
    def set_act_button(self):
        self.show_tiles()
        self.ui.button_eat.setEnabled(self.ui_player.can_eat)
        self.ui.button_pon.setEnabled(self.ui_player.can_pon)
        self.ui.button_gan.setEnabled(self.ui_player.can_gan)
        self.ui.button_win.setEnabled(True)
        if self.ui_player.can_eat:
            combs = self.ui_player.eat_combinations            
            def show_eat_combination():
                if len(combs) >= 1:
                    def ui_eat_0():
                        self.ui_player.eat(formation=combs[0])
                        self.show_tiles()
                        self.reset_act_button()
                        self.tiles_on()
                        return
                    self.ui.button_eat.setText(str(translate_list(combs[0])))
                    self.ui.button_eat.setEnabled(True)
                    self.ui.button_pon.setEnabled(False)
                    self.ui.button_gan.setEnabled(False)
                    self.ui.button_win.setEnabled(False)
                    self.ui.button_eat.clicked.connect(ui_eat_0)
                if len(combs) >= 2:
                    def ui_eat_1():
                        self.ui_player.eat(formation=combs[1])
                        self.show_tiles()
                        self.reset_act_button()
                        self.tiles_on()
                        return
                    self.ui.button_pon.setText(str(translate_list(combs[1])))
                    self.ui.button_pon.setEnabled(True)
                    self.ui.button_pon.clicked.connect(ui_eat_1)
                if len(combs) >= 3:
                    def ui_eat_2():
                        self.ui_player.eat(formation=combs[2])
                        self.show_tiles()
                        self.reset_act_button()
                        self.tiles_on()
                        return
                    self.ui.button_gan.setText(str(translate_list(combs[2])))
                    self.ui.button_gan.setEnabled(True)
                    self.ui.button_gan.clicked.connect(ui_eat_2)

            self.ui.button_eat.clicked.connect(show_eat_combination)

        if self.ui_player.can_pon:
            def ui_pon():
                self.ui_player.pon()
                self.show_tiles()
                self.ui.button_pon.setEnabled(False)               
                self.reset_act_button()
                self.tiles_on()
                return

            self.ui.button_pon.clicked.connect(ui_pon)
                
        if self.ui_player.can_gan:
            def ui_gan():
                self.ui_player.gan()
                self.show_tiles()
                self.ui.button_gan.setEnabled(False)               
                self.reset_act_button()
                self.tiles_on()
                return

            self.ui.button_gan.clicked.connect(ui_gan)

        if self.ui_player.can_win:
            def ui_win():
                self.log("player " + str(self.ui_player.index) + " 胡啦! ( player "+ str(self.players.index) +" 放槍)")
                self.ui_player.win()
                self._environment_update()
                self.show_tiles()
                self.status = status.start_game
                self.set_regame_button()

            self.ui.button_win.clicked.connect(ui_win)            
        

        def no_act():
            self.ui_no_act = True
            self.check_others_action()
            self.ui_no_act = False
            self.reset_act_button()
            return
        
        if not self.ui_player.can_win:
            self.ui.button_win.setText("過")
            self.ui.button_win.setEnabled(True)
            self.ui.button_win.clicked.connect(no_act)
        elif not self.ui_player.can_gan:
            self.ui.button_gan.setText("過")
            self.ui.button_gan.setEnabled(True)
            self.ui.button_gan.clicked.connect(no_act)
        elif not self.ui_player.can_pon:
            self.ui.button_pon.setText("過")
            self.ui.button_pon.setEnabled(True)
            self.ui.button_pon.clicked.connect(no_act)
        elif not self.ui_player.can_eat:
            self.ui.button_eat.setText("過")
            self.ui.button_eat.setEnabled(True)
            self.ui.button_eat.clicked.connect(no_act)
                
    

    def ui_ditch_card(self):
        self.tiles_off()
        self.players.reset(self.ui_player)
        self.ditched_card=self.ui_player.holding[self.ditched_card_id]
        self.ui_player.discard_card(self.ditched_card)
        self.log("打: " + translate(self.ditched_card))
        self.show_tiles()
        self.check_others_action()

    def tiles_off(self):
        for tile in self.tiles:
            tile.setEnabled(False)

    def tiles_on(self):
        for tile in self.tiles:
            tile.setEnabled(True)

    def set_tiles_button(self):
        self.tiles = list()
        self.tiles.append(self.ui.tile_0)
        self.tiles.append(self.ui.tile_1)
        self.tiles.append(self.ui.tile_2)
        self.tiles.append(self.ui.tile_3)
        self.tiles.append(self.ui.tile_4)

        self.tiles.append(self.ui.tile_5)
        self.tiles.append(self.ui.tile_6)
        self.tiles.append(self.ui.tile_7)
        self.tiles.append(self.ui.tile_8)
        self.tiles.append(self.ui.tile_9)

        self.tiles.append(self.ui.tile_10)
        self.tiles.append(self.ui.tile_11)
        self.tiles.append(self.ui.tile_12)
        self.tiles.append(self.ui.tile_13)
        self.tiles.append(self.ui.tile_14)

        self.tiles.append(self.ui.tile_15)
        self.tiles.append(self.ui.tile_16)

        self.flws = list()
        self.flws.append(self.ui.flw_0)
        self.flws.append(self.ui.flw_1)
        self.flws.append(self.ui.flw_2)
        self.flws.append(self.ui.flw_3)
        self.flws.append(self.ui.flw_4)

        self.flws.append(self.ui.flw_5)
        self.flws.append(self.ui.flw_6)
        self.flws.append(self.ui.flw_7)
        self.flws.append(self.ui.flw_8)
        self.flws.append(self.ui.flw_9)

        self.flws.append(self.ui.flw_10)
        self.flws.append(self.ui.flw_11)
        self.flws.append(self.ui.flw_12)
        self.flws.append(self.ui.flw_13)
        self.flws.append(self.ui.flw_14)

        self.flws.append(self.ui.flw_15)       
    
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

        self.ui.tile_0.clicked.connect(fn_0)
        self.ui.tile_1.clicked.connect(fn_1)
        self.ui.tile_2.clicked.connect(fn_2)
        self.ui.tile_3.clicked.connect(fn_3)
        self.ui.tile_4.clicked.connect(fn_4)

        self.ui.tile_5.clicked.connect(fn_5)
        self.ui.tile_6.clicked.connect(fn_6)
        self.ui.tile_7.clicked.connect(fn_7)
        self.ui.tile_8.clicked.connect(fn_8)
        self.ui.tile_9.clicked.connect(fn_9)

        self.ui.tile_10.clicked.connect(fn_10)
        self.ui.tile_11.clicked.connect(fn_11)
        self.ui.tile_12.clicked.connect(fn_12)
        self.ui.tile_13.clicked.connect(fn_13)
        self.ui.tile_14.clicked.connect(fn_14)
        self.ui.tile_15.clicked.connect(fn_15)
        self.ui.tile_16.clicked.connect(fn_16)


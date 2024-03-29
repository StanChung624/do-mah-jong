from do_mah_jong.Basic.GameController import GameControl, Players, Player, Deck
from do_mah_jong.Basic.Deck import CustomDeck, translate, translate_list
from do_mah_jong.UI.UIPlayer import UIPlayer
from do_mah_jong.UI.UIManipulator import UIManipulator
from do_mah_jong.UI.Status import Status

class UIGameConroller(GameControl, UIManipulator):
    def __init__(self, dialog, debug: bool = False) -> None:

        self.setupUi(dialog)
        self.set_button_tiles()
        
        self.user_ditch_card_id = -1
        self.user_ditch_card = ""
        self.flag_user_no_act = False

        self.status = Status.start_game
        super().__init__(debug)       
    
    def log(self, message: str, player: Player = None, end: str = "\n", announce: bool = True):
        super().log(message, player, end, announce)
        with open("log.txt", "w") as f:
            for lg in self._log:
                f.write(lg)

    def output_env(self):
        env = "風: " + translate(self.winds.current()) + " " + str(self.players.current_id()) + "\n"
        env += "連莊: " + str(self.players.current().is_owner())
        self.text_env.setText(env)
        self.reset_sea()

    def setup_game(self):
        self.reset_act_button()
        self.reset_com_tiles()
        self._log = list()

        if self.status == Status.start_game:
            self.deck = Deck()
            for player in self.players_list:
                player.reset()        
                player.deck = self.deck
                if type(player) is UIPlayer:
                    self.ui_player = player

            self.log("deck: \n"+str(self.deck.seq), announce=False)
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
                self.show_flowers(player)
                self.log("initial", player, announce=False)
            
            self.show_tiles(self.ui_player)
            self.player_draw_card()

    def com_action(self, player:Player, card:str):
        action = player.action()
        if action:
            self.show_action(action, player)
            if player.is_win():
                self.log("player " + str(player.index) + " 胡啦!" +
                            " (player " + str(self.players.current().index) + " 放槍)", player = player)
                self.show_action("lose", self.players.current())
                self.show_tiles(player)
                self._environment_update()
                self.status = Status.start_game
                self.set_regame_button(self.setup_game)
                return
            self.show_flowers(player)
            self.user_ditch_card = player.ditch()
            self.ui_com_discard_card_clear()
            self.ui_com_discard_card(player, self.user_ditch_card)
            self.log("player " + str(player.index) + " " + action + ", 打: " + translate(self.user_ditch_card))
            self.players.reset(player)
            # let other see the output flower
            for other in self.players.others():
                other.see(card_list=player.flower[-3:])
            return self.check_others_action()
        else:
            # if there is not action
            self.to_sea(card)
            self.flush_sea()
            self.players.next()
            self.player_draw_card()

    def check_others_action(self):
        card = self.user_ditch_card
        others = self.players.others()
        others.reverse()

        # check someone can win
        for player in others:
            player.see(card, self.players.current())
            can_act = player.can_win
            if not can_act:
                continue
            elif self.flag_user_no_act:
                continue
            elif type(player) is UIPlayer and can_act:
                self.status = Status.to_act                
                self.show_tiles(self.ui_player)
                self.set_act_button()
                return
            else:
                return self.com_action(player, card)
        
        # check someone can pon/gan
        for player in others:
            can_act = player.can_pon or player.can_gan
            if not can_act:
                continue
            elif self.flag_user_no_act:
                continue
            elif type(player) is UIPlayer and can_act:
                self.status = Status.to_act                
                self.show_tiles(self.ui_player)
                self.set_act_button()
                return
            else:
                return self.com_action(player, card)
        
        # check someone can eat
        for player in others:
            can_act = player.can_eat
            if not can_act:
                continue
            elif self.flag_user_no_act:
                continue
            elif type(player) is UIPlayer and can_act:
                self.status = Status.to_act                
                self.show_tiles(self.ui_player)
                self.set_act_button()
                return
            else:
                return self.com_action(player, card)
        
        # if there is not action
        self.to_sea(card)
        self.flush_sea()
        self.players.next()
        self.player_draw_card()
        return    

    def _environment_update(self):
        return super()._environment_update()
    
    def ui_player_check_action(self)->bool:
    # for gan or self draw scenario
        self.ui_player.holding.remove(self.ui_player.last_draw)
        self.ui_player.see(card=self.ui_player.last_draw, player=self.ui_player)
        self.ui_player.holding.append(self.ui_player.last_draw)
        if self.ui_player.can_gan or self.ui_player.can_win:               
            self.set_self_act_button()
            return True

    def player_draw_card(self):
        self.reset_action()
        player = self.players.current()
        if self.players.current_id() == self.crrnt_id:
            self.count += 1

        card = player.draw_card()

        if card is None:
            self.log("流局")
            self.show_action("no_win", player)
            self._environment_update()
            self.status = Status.start_game
            self.set_regame_button(self.setup_game)
            return

        player.amend_flower()
        card = player.last_draw        
        
        if type(player) is UIPlayer:
            self.flush_sea()
            self.status = Status.to_ditch
            self.show_tiles(self.ui_player)
            self.tiles_on()
            self.log("你摸進了 " + translate(card))

            # for gan or self draw scenario
            if self.ui_player_check_action():
                return

        else:
            if player.is_win():
                self.log("player " + str(player.index) + " 胡啦! (自摸)", player = player)
                self.show_tiles(player)
                self.show_action("self_win", player)
                self._environment_update()
                self.status = Status.start_game
                self.set_regame_button(self.setup_game)
                return
            
            card = player.ditch()
            self.user_ditch_card = card
            self.ui_com_discard_card(player, self.user_ditch_card)
            self.log("player " + str(player.index) + ", 打: " + translate(self.user_ditch_card))
            self.check_others_action()
            return
    
    def set_act_button(self):        
        if self.ui_player.can_eat:
            self.set_button_eat(self.ui_player)
        if self.ui_player.can_pon:
            self.set_button_pon(self.ui_player)                
        if self.ui_player.can_gan:
            self.set_button_gan(self.ui_player)
        if self.ui_player.can_win:
            
            self.set_button_win(self.ui_player)
            
        def no_act():
            self.flag_user_no_act = True
            self.check_others_action()
            self.flag_user_no_act = False
            self.reset_act_button()
            return
        
        self.set_button_no_act(self.ui_player, no_act)

    def set_self_act_button(self):        
        if self.ui_player.can_gan:
            self.set_button_self_gan(self.ui_player)
        if self.ui_player.can_win:
            self.set_button_self_win(self.ui_player)


    


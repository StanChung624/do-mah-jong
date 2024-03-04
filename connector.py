from dmj_draft_ui import Ui_Dialog, QtWidgets
from do_mah_jong.Basic import *
from do_mah_jong.Basic.UIGameController import UIGameConroller

class DoMahJongUI(Ui_Dialog):

    def setupUi(self, Dialog):
        super().setupUi(Dialog)        
        self.button_eat.setText("start")
        self.button_eat.clicked.connect(self.set_up_game)        
        
    
    def set_up_game(self):        
        self.game = UIGameConroller(ui=self)
        self.game.register_a_player(UIPlayer(is_owner=0, index=0, ui=self))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=1))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=2))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=3))
        self.game.register_deck(Deck())
        self.game.setup_game()
        self.button_eat.setText("吃")
        self.button_eat.clicked.disconnect(self.set_up_game)
        self.button_eat.setEnabled(False)
        self.button_pon.setEnabled(False)
        self.button_gan.setEnabled(False)
        self.button_win.setEnabled(False)
        self.game.players_draw_card()
        
        

    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DoMahJongUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

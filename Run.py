from PyQt6 import QtWidgets
from do_mah_jong.Basic import *
from do_mah_jong.UI import *
from do_mah_jong.COMStyle.COMStyle import *

class DoMahJongLauncher():

    def setupUi(self, Dialog):
        self.game = UIGameConroller(Dialog)        
        self.game.button_eat.setText("start")
        self.game.button_eat.clicked.connect(self.set_up_game)
    
    def set_up_game(self):        
        self.game.register_a_player(UIPlayer(is_owner=0, index=0, ui=self, strategy=Normal))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=1))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=2))
        self.game.register_a_player(COMPlayer(is_owner=-1, index=3))
        self.game.setup_game()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DoMahJongLauncher()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

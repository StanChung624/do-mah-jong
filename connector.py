from dmj_draft_ui import Ui_Dialog, QtWidgets
from do_mah_jong.Basic import *
from do_mah_jong.UI import *
from do_mah_jong.COMStyle.PoPo import PoPo

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
        self.game.register_a_player(COMPlayer(is_owner=-1, index=3, strategy=PoPo))
        self.game.setup_game()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DoMahJongUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

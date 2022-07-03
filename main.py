# udělal RxiPland (https://github.com/RxiPland)
# 2022
# Phonebook - desktop

from tabulka_data_grafika import Ui_MainWindow_tabulka_data_grafika
from najit_domenu_grafika import Ui_MainWindow_najit_domenu_grafika
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog

class AktualniOkno:

    # uchovává hodnotu, které reprezentuje dané okno

    # okno 0 => okno s tabulkou
    # okno 1 => okno s vyhledáváním

    def __init__(self):
        self.okno = 0

class tabulka_data_grafika0(QMainWindow, Ui_MainWindow_tabulka_data_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def tlacitko_nova_domena(self):

        najit_domenu_grafika1.center_funkce()
        najit_domenu_grafika1.show()
        tabulka_data_grafika1.close()
        aktualni_okno1.okno = 1

    def about_to_quit_funkce(self):

        # class AktualniOkno slouží pro uchovávání čísla, které reprezentuje okno, které je otevřeno naposled

        if aktualni_okno1.okno == 0:
            # pokud uživatel zavře okno s tabulkou, program se ukončí

            sys.exit(app.exec_())
        
        elif aktualni_okno1.okno == 1:
            # pokud uživatel zavře okno najít doménu, funkce otevře okno s tabulkou

            tabulka_data_grafika1.center_funkce()
            tabulka_data_grafika1.show()
            najit_domenu_grafika1.close()
            aktualni_okno1.okno = 0



class najit_domenu_grafika0(QMainWindow, Ui_MainWindow_najit_domenu_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def vyhledat(self):
        # funkce která komunikuje s webovou stránkou

        pass



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    tabulka_data_grafika1 = tabulka_data_grafika0()
    najit_domenu_grafika1 = najit_domenu_grafika0()
    aktualni_okno1 = AktualniOkno()

    tabulka_data_grafika1.show()

    tabulka_data_grafika1.pushButton.clicked.connect(tabulka_data_grafika1.tlacitko_nova_domena)  # najít novou doménu
    #tabulka_data_grafika1.pushButton_2.clicked.connect() # uložit data do souboru
    #tabulka_data_grafika1.pushButton_3.clicked.connect() # kopírovat všechna data do schránky
    #tabulka_data_grafika1.pushButton_4.clicked.connect() # kopírovat řádek do schránky

    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(tabulka_data_grafika1.about_to_quit_funkce)

    sys.exit(app.exec_())
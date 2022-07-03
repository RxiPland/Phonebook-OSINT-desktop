# udělal RxiPland (https://github.com/RxiPland)
# 2022
# Phonebook - desktop

from tabulka_data_grafika import Ui_MainWindow_tabulka_data_grafika
from najit_domenu_grafika import Ui_MainWindow_najit_domenu_grafika
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog


class tabulka_data_grafika0(QMainWindow, Ui_MainWindow_tabulka_data_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


class najit_domenu_grafika0(QMainWindow, Ui_MainWindow_najit_domenu_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    tabulka_data_grafika1 = tabulka_data_grafika0()
    najit_domenu_grafika1 = najit_domenu_grafika0()

    tabulka_data_grafika1.show()

    #tabulka_data_grafika1.pushButton.clicked.connect()  # najít novou doménu
    #tabulka_data_grafika1.pushButton_2.clicked.connect() # uložit data do souboru
    #tabulka_data_grafika1.pushButton_3.clicked.connect() # kopírovat všechna data do schránky
    #tabulka_data_grafika1.pushButton_4.clicked.connect() # kopírovat řádek do schránky

    sys.exit(app.exec_())
# toto je python soubor, který obsahuje grafiku (pro spuštění slouží main.py)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QAbstractItemView

class Ui_MainWindow_tabulka_data_grafika(object):

    def center_funkce(self):

        # funkce, která přesune okno programu do prostřed obrazovky

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def setupUi(self, MainWindow):

        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 542)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 421, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0,410)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setCurrentCell(-1, -1)
        self.tableWidget.setHidden(False)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 50, 141, 44))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 280, 145, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setHidden(True)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 220, 145, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setHidden(True)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 140, 145, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setHidden(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 410, 201, 31))
        self.label.setObjectName("label")
        self.label.setHidden(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 301, 101))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(518, 360, 141, 21))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 440, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setHidden(True)
        self.lineEdit.setReadOnly(True)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 470, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setHidden(True)
        self.lineEdit_2.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuOdkazy = QtWidgets.QMenu(self.menuBar)
        self.menuOdkazy.setObjectName("menuOdkazy")
        MainWindow.setMenuBar(self.menuBar)
        self.actionPhonebook_cz = QtWidgets.QAction(MainWindow)
        self.actionPhonebook_cz.setObjectName("actionPhonebook_cz")
        self.actionHaveibeenpwned_com = QtWidgets.QAction(MainWindow)
        self.actionHaveibeenpwned_com.setObjectName("actionHaveibeenpwned_com")
        self.actionEmail_checker_net = QtWidgets.QAction(MainWindow)
        self.actionEmail_checker_net.setObjectName("ActionEmail-checker_net")
        self.menuOdkazy.addAction(self.actionPhonebook_cz)
        self.menuOdkazy.addAction(self.actionHaveibeenpwned_com)
        self.menuOdkazy.addAction(self.actionEmail_checker_net)
        self.menuBar.addAction(self.menuOdkazy.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phonebook OSINT desktop"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nalezená data"))
        self.pushButton.setText(_translate("MainWindow", "Vyhledat novou\ndoménu"))
        self.pushButton_2.setText(_translate("MainWindow", "Uložit data\ndo souboru"))
        self.pushButton_3.setText(_translate("MainWindow", "Kopírovat všechna\ndata do schránky"))
        self.pushButton_4.setText(_translate("MainWindow", "Kopírovat řádek\ndo schránky"))
        self.label.setText(_translate("MainWindow", "Celkem nalezeno:"))
        self.label_2.setText(_translate("MainWindow", "Zatím nebyla prohledána žádná doména;\nzmáčkněte tlačítko pro vyhledávání"))
        self.label_3.setText(_translate("MainWindow", "<a href='https://phonebook.cz/'>Používaný web</a>"))
        self.lineEdit.setText(_translate("MainWindow", "X emailů/ subdomén/ adresářů"))
        self.lineEdit_2.setText(_translate("MainWindow", "[Doména]"))
        self.menuOdkazy.setTitle(_translate("MainWindow", "Odkazy"))
        self.actionPhonebook_cz.setText(_translate("MainWindow", "Phonebook.cz"))
        self.actionHaveibeenpwned_com.setText(_translate("MainWindow", "Haveibeenpwned.com"))
        self.actionEmail_checker_net.setText(_translate("MainWindow", "Email-checker.net"))
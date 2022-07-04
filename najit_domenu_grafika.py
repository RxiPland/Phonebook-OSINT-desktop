# toto je python soubor, který obsahuje grafiku (pro spuštění slouží main.py)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

class Ui_MainWindow_najit_domenu_grafika(object):

    def center_funkce(self):

        # funkce, která přesune okno programu do prostřed obrazovky

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def setupUi(self, MainWindow):

        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 190)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 20))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 125, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 125, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 181, 20))
        self.label_2.setObjectName("label_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 135, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setHidden(True)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 321, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setHidden(True)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 42, 311, 27))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Najít data podle domény"))
        self.label.setText(_translate("MainWindow", "Zadejte doménu:"))
        self.pushButton.setText(_translate("MainWindow", "Vyhledat"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Vyberte"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Subdomény"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Emailové adresy"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Adresáře"))
        self.label_2.setText(_translate("MainWindow", "Hledat:"))
        self.pushButton_2.setText(_translate("MainWindow", "Načíst data do tabulky"))
        self.label_3.setText(_translate("MainWindow", "Doba vyhledávání:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "facebook.com, email.seznam.cz"))
# udělal RxiPland (https://github.com/RxiPland)
# 2022
# Phonebook - desktop

from tabulka_data_grafika import Ui_MainWindow_tabulka_data_grafika
from najit_domenu_grafika import Ui_MainWindow_najit_domenu_grafika
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog
from requests import Session, get
import time
from threading import Thread
from json import loads
from pyperclip import copy

class Hodnoty_K_pouziti0:

    # uchovává hodnoty

    # okno 0 => okno s tabulkou
    # okno 1 => okno s vyhledáváním

    def __init__(self):
        self.okno = 0               # int
        self.predchozi_id = ""      # str
        self.hotove_hledani = []    # list

class tabulka_data_grafika0(QMainWindow, Ui_MainWindow_tabulka_data_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def tlacitko_nova_domena(self):

        najit_domenu_grafika1.center_funkce()
        najit_domenu_grafika1.show()
        tabulka_data_grafika1.close()
        hodnoty_K_pouziti1.okno = 1

    def about_to_quit_funkce(self):

        # class hodnoty_K_pouziti slouží pro uchovávání čísla, které reprezentuje okno, které je otevřeno naposled

        if hodnoty_K_pouziti1.okno == 0:
            # pokud uživatel zavře okno s tabulkou, program se ukončí

            app.quit()
        
        elif hodnoty_K_pouziti1.okno == 1:
            # pokud uživatel zavře okno najít doménu, funkce otevře okno s tabulkou

            tabulka_data_grafika1.center_funkce()
            tabulka_data_grafika1.show()
            najit_domenu_grafika1.close()
            hodnoty_K_pouziti1.okno = 0


    def ulozit_do_souboru(self):
        # uloží data z tabulky do souboru

        nactena_data = hodnoty_K_pouziti1.hotove_hledani[0]

        f = open("ulozena_data.txt", "w")
        f.writelines(nactena_data)
        f.close()


    def kopirovat_do_schranky(self):
        # zkopíruje všechna data z tabulky do schránky

        nactena_data = hodnoty_K_pouziti1.hotove_hledani[0]
        finalni_string = ""

        for item in nactena_data:
            finalni_string += item + "\n" 

        copy(finalni_string)

class najit_domenu_grafika0(QMainWindow, Ui_MainWindow_najit_domenu_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def reset_hodnot(self):

        # vyresetuje hodnoty v polích v okně najit_domenu.py

        najit_domenu_grafika1.label.setHidden(False)
        najit_domenu_grafika1.label_2.setHidden(True)
        najit_domenu_grafika1.label_3.setHidden(True)

        najit_domenu_grafika1.lineEdit.clear()
        najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: ")
        najit_domenu_grafika1.lineEdit.setClearButtonEnabled(True)

        najit_domenu_grafika1.pushButton.setHidden(False)
        najit_domenu_grafika1.pushButton_2.setHidden(True)

        najit_domenu_grafika1.comboBox.setHidden(False)

    def nacteni_dat_do_tabulky(self):

        list_ziskanych_dat = hodnoty_K_pouziti1.hotove_hledani

        ziskane_informace = list_ziskanych_dat[0]   # emaily/subdomény/adresáře...
        domena_text = list_ziskanych_dat[1]
        typ_hledani = list_ziskanych_dat[2]

        moznosti = {1: "subdomén", 2: "emailových adres", 3: "adresářů"}

        # vložení dat do tabulky

        if len(ziskane_informace) > 0:

            tabulka_data_grafika1.label_2.setHidden(True)

            aktualni_radek = 0

            for row in ziskane_informace:

                self.tableWidget.setRowCount(aktualni_radek+1)
                self.tableWidget.setItem(aktualni_radek, 0, QtWidgets.QTableWidgetItem(row))
                aktualni_radek += 1
        
        else:
            
            tabulka_data_grafika1.label_2.setText("Nebyla nalezena žádná data")
            tabulka_data_grafika1.label_2.setHidden(False)


        tabulka_data_grafika1.lineEdit.setText(len(ziskane_informace), moznosti[typ_hledani])
        tabulka_data_grafika1.lineEdit.setHidden(False)
        tabulka_data_grafika1.lineEdit_2.setText(domena_text)
        tabulka_data_grafika1.lineEdit_2.setHidden(False)
        tabulka_data_grafika1.label.setHidden(False)
        tabulka_data_grafika1.pushButton_2.setHidden(False)
        tabulka_data_grafika1.pushButton_3.setHidden(False)
        tabulka_data_grafika1.pushButton_4.setHidden(False)

        tabulka_data_grafika1.tableWidget.setCurrentCell(-1, -1)

        tabulka_data_grafika1.center_funkce()
        tabulka_data_grafika1.show()
        najit_domenu_grafika1.close()
        hodnoty_K_pouziti1.okno = 0


    def vyhledat(self):
        # funkce která komunikuje s webovou stránkou

        start = time.time()

        headers= {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"}
        moznosti = {"Subdomény": 1, "Emailové adresy": 2, "Adresáře": 3}

        API_KEY = "077424c6-7a26-410e-9269-c9ac546886a4"    # defaultní

        if hodnoty_K_pouziti1.predchozi_id == "":

            phonebook_html = get("https://phonebook.cz", headers=headers).text

            for row in phonebook_html:

                if "var API_KEY" in row:

                    row.replace(" ", "")
                    row = row.split("=")

                    API_KEY = row[1]

                    break

        url = "https://public.intelx.io/phonebook/search?k=" + API_KEY


        vybrane_hledani = najit_domenu_grafika1.comboBox.currentText()
        vybrane_hledani = moznosti[vybrane_hledani]

        domena_text = str(najit_domenu_grafika1.lineEdit.text()).strip()
        domena_text = domena_text.replace("https", "", 1)
        domena_text = domena_text.replace("http", "", 1)
        domena_text = domena_text.replace("://", "", 1)
        domena_text = domena_text.split("/")[0]

        session1 = Session()

        if hodnoty_K_pouziti1.predchozi_id == "":

            # pokud se hledá poprvé od spuštění programu, id bude prázdné (dosadí se null)

            data1 = {"term": domena_text,"maxresults":10000,"media":0,"target":vybrane_hledani,"terminate":[None],"timeout":20}
            response = session1.post(url=url, headers=headers, json=data1)


            if response.status_code == 402:
                
                najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: red")
                najit_domenu_grafika1.lineEdit.setText("Byl přesáhnut denní limit požadavků!")
                najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)
                najit_domenu_grafika1.label.setHidden(True)
                najit_domenu_grafika1.label_2.setHidden(True)

                end = time.time()
                najit_domenu_grafika1.label_3.setHidden(False)
                doba = "Doba trvání: " + str(round(end-start,5)) + " vteřin"
                najit_domenu_grafika1.label_3.setText(doba)

                return "chyba"

            elif response.status_code == 403:
                
                najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: red")
                najit_domenu_grafika1.lineEdit.setText("IP adresa je na black listu (zkuste vypnout VPN)")
                najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)
                najit_domenu_grafika1.label.setHidden(True)
                najit_domenu_grafika1.label_2.setHidden(True)

                end = time.time()
                najit_domenu_grafika1.label_3.setHidden(False)
                doba = "Doba trvání: " + str(round(end-start,5)) + " vteřin"
                najit_domenu_grafika1.label_3.setText(doba)

                return "chyba"

            elif response.status_code == 200:

                hodnoty_K_pouziti1.predchozi_id = loads(response.text)["id"]
           

        else:

            # "terminate" bude hodnota posledního id

            data1 = {"term": domena_text,"maxresults":10000,"media":0,"target":vybrane_hledani,"terminate":[hodnoty_K_pouziti1.predchozi_id],"timeout":20}
            response = session1.post(url=url, headers=headers, json=data1)
            response = loads(response.text)

            hodnoty_K_pouziti1.predchozi_id = response["id"]


        url_get = "https://public.intelx.io/phonebook/search/result?k=" + API_KEY + "&id=" + hodnoty_K_pouziti1.predchozi_id  +"&limit=10000"
        list_ziskanych_dat = []        

        while True:

            # data=data2 není potřeba, protože jsou parametry v URL
            response2 = loads(session1.get(url=url_get, headers=headers).text)

            # příklad response: {"selectors":[{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"info@cichnovabrno.cz","selectorvalueh":"info@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"domov@cichnovabrno.cz","selectorvalueh":"domov@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"elena.kneslova@cichnovabrno.cz","selectorvalueh":"elena.kneslova@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"jaroslav.masek@cichnovabrno.cz","selectorvalueh":"jaroslav.masek@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"helena.kvasnickova@cichnovabrno.cz","selectorvalueh":"helena.kvasnickova@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"vladimir.simicek@cichnovabrno.cz","selectorvalueh":"vladimir.simicek@cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023803@student.cichnovabrno.cz","selectorvalueh":"st023803@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023567@student.cichnovabrno.cz","selectorvalueh":"st023567@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st022987@student.cichnovabrno.cz","selectorvalueh":"st022987@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023320@student.cichnovabrno.cz","selectorvalueh":"st023320@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st022704@student.cichnovabrno.cz","selectorvalueh":"st022704@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023977@student.cichnovabrno.cz","selectorvalueh":"st023977@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023828@student.cichnovabrno.cz","selectorvalueh":"st023828@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023257@student.cichnovabrno.cz","selectorvalueh":"st023257@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024235@student.cichnovabrno.cz","selectorvalueh":"st024235@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"4d7f5e2a-0843-49ea-87bf-3f93aee91f8d@student.cichnovabrno.cz","selectorvalueh":"4d7f5e2a-0843-49ea-87bf-3f93aee91f8d@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st022921@student.cichnovabrno.cz","selectorvalueh":"st022921@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024849@student.cichnovabrno.cz","selectorvalueh":"st024849@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024189@student.cichnovabrno.cz","selectorvalueh":"st024189@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023345@student.cichnovabrno.cz","selectorvalueh":"st023345@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024720@student.cichnovabrno.cz","selectorvalueh":"st024720@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st025054@student.cichnovabrno.cz","selectorvalueh":"st025054@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024326@student.cichnovabrno.cz","selectorvalueh":"st024326@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st023103@student.cichnovabrno.cz","selectorvalueh":"st023103@student.cichnovabrno.cz"},{"selectortype":1,"selectortypeh":"Email Address","selectorvalue":"st024502@student.cichnovabrno.cz","selectorvalueh":"st024502@student.cichnovabrno.cz"}],"status":1}

            if response2["status"] == 0:

                # příchozí data
                list_adres = response2["selectors"]

                for item in list_adres:
                    list_ziskanych_dat.append(item["selectorvalue"])

            elif response2["status"] == 1:

                # konec
                list_adres = response2["selectors"]

                for item in list_adres:
                    list_ziskanych_dat.append(item["selectorvalue"])

                break

            elif response2["status"] == 2:

                # moc stejných requestů
                pass

            elif response2["status"] == 3:

                # prázdné
                pass

            time.sleep(1)

        end = time.time()

        najit_domenu_grafika1.pushButton_2.setHidden(False)
        najit_domenu_grafika1.pushButton.setHidden(True)
        najit_domenu_grafika1.comboBox.setHidden(True)
        najit_domenu_grafika1.label.setHidden(True)
        najit_domenu_grafika1.label_2.setHidden(True)

        #najit_domenu_grafika1.lineEdit.setReadOnly(True)   # NEPOUŽÍVAT - DĚLÁ PROBLÉM (kvůli Threadu)

        najit_domenu_grafika1.lineEdit.setText("Hledání bylo dokončeno.")
        najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)
        najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: green")
        najit_domenu_grafika1.label_3.setHidden(False)
        doba = "Doba vyhledávání: " + str(round(end-start,5)) + " vteřin"
        najit_domenu_grafika1.label_3.setText(doba)
        
    
        hodnoty_K_pouziti1.hotove_hledani = [list_ziskanych_dat, domena_text, vybrane_hledani]  # uložení dat do classy

    def kontrola(self):

        # zkontroluje zda nejsou pole prázdná, doména je platná a je vybrán typ hledání

        domena_text = str(najit_domenu_grafika1.lineEdit.text()).strip()

        if domena_text == "":

            # pole nemůže být prázdné
            
            return 1

        elif "." not in domena_text:

            # doména není úplná
            
            return 2

        elif najit_domenu_grafika1.comboBox.currentText() == "Vyberte":

            # není vybrán typ hledání

            return 3

        else:
            
            # v pořádku

            return 4


    def main(self):
        # hlavní funkce která se spustí ostatní
        # kontroluje správnost

        odpoved = self.kontrola()

        if odpoved == 1:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Vyplňte pole s doménou")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        elif odpoved == 2:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Doména není platná!\n\nNapř. google.com, facebook.com, seznam.cz")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        elif odpoved == 3:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Vyberte co chcete hledat")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            return

        elif odpoved == 4:
            # všechno v pořádku

            najit_domenu_grafika1.pushButton.setEnabled(False)
            najit_domenu_grafika1.comboBox.setEnabled(False)

            hodnoty_K_pouziti1.hotove_hledani = []

            t = Thread(target=najit_domenu_grafika1.vyhledat)
            t.start()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    tabulka_data_grafika1 = tabulka_data_grafika0()
    najit_domenu_grafika1 = najit_domenu_grafika0()
    hodnoty_K_pouziti1 = Hodnoty_K_pouziti0()

    tabulka_data_grafika1.show()

    tabulka_data_grafika1.pushButton.clicked.connect(tabulka_data_grafika1.tlacitko_nova_domena)  # najít novou doménu
    tabulka_data_grafika1.pushButton_2.clicked.connect(tabulka_data_grafika1.ulozit_do_souboru) # uložit data do souboru
    tabulka_data_grafika1.pushButton_3.clicked.connect(tabulka_data_grafika1.kopirovat_do_schranky) # kopírovat všechna data do schránky
    #tabulka_data_grafika1.pushButton_4.clicked.connect(tabulka_data_grafika1.) # kopírovat řádek do schránky

    najit_domenu_grafika1.pushButton.clicked.connect(najit_domenu_grafika1.main)
    najit_domenu_grafika1.pushButton_2.clicked.connect(najit_domenu_grafika1.nacteni_dat_do_tabulky)

    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(tabulka_data_grafika1.about_to_quit_funkce)

    sys.exit(app.exec_())
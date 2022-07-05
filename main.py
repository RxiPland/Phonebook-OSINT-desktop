# udělal RxiPland (https://github.com/RxiPland)
# 2022
# Python 3.9.12


# Phonebook - desktop

from tabulka_data_grafika import Ui_MainWindow_tabulka_data_grafika
from najit_domenu_grafika import Ui_MainWindow_najit_domenu_grafika
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog
from requests import Session, get
import time
from threading import Thread
from json import loads
from pyperclip import copy


class file_dialog0(QDialog):


    def vyberLokace_save(self):
        # otevře průzkumník souborů a nechá uživatele vybrat cestu, kam chce uložit soubor

        try:
            dlg = QFileDialog.getSaveFileName(self, 'Uložte hotový soubor', '','Textový soubor (*.txt);;JSON soubor (*.json);;Všechny soubory (*.*)')
            return dlg

        except:
            return "exited"

class Hodnoty_K_pouziti0:

    # pouze uchovává hodnoty

    def __init__(self):
        self.okno = 0               # int   (aktuální okno)         okno 0 => okno s tabulkou; okno 1 => okno s vyhledáváním
        self.predchozi_id = ""      # str   (předchozí id hledání)
        self.hotove_hledani = []    # list  (nalezená data)


        self.cekani_mezi_requestama = 1 # int MOŽNOST NASTAVIT SVOJI HODNOTU

class tabulka_data_grafika0(QMainWindow, Ui_MainWindow_tabulka_data_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def tlacitko_nova_domena(self):

        najit_domenu_grafika1.reset_hodnot()

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

        moznosti = {1: "Subdoména", 2: "Emailová adresa", 3: "Adresář"}

        vybrana_lokace = file_dialog1.vyberLokace_save()

        cesta_soubor = vybrana_lokace[0]    # cesta k souboru
        typ_souboru = vybrana_lokace[1]     # .txt / .json


        content = hodnoty_K_pouziti1.hotove_hledani[0]

        if ".json" in typ_souboru:

            # uživatel vybral json

            dohromady = []

            domena = hodnoty_K_pouziti1.hotove_hledani[1]
            typ_hledani = moznosti[hodnoty_K_pouziti1.hotove_hledani[2]]

            for item in content:

                sablona = {"Content": item, "Domena": domena, "Typ": typ_hledani}
                dohromady.append(sablona)
            
            finalni_json = {"Data": dohromady}

            with open(cesta_soubor, "w") as f:

                # uložení dat do souboru

                f.write(str(finalni_json))


            with open(cesta_soubor, "r") as f:

                # znovu načtení souboru

                obsah = str(f.read())

            
            with open(cesta_soubor, "w") as f:

                # přepsání ' uvozovek na " kvůli jsonu

                obsah = obsah.replace("\'", "\"")

                f.write(obsah)

        else:

            # uživatel vybral txt

            with open(cesta_soubor, "w") as f:

                for i, item in enumerate(content):

                    if i == 0:
                        f.writelines(item)
                    else:
                        f.writelines("\n" + item)


    def kopirovat_do_schranky(self):
        # zkopíruje všechna data z tabulky do schránky

        nactena_data = hodnoty_K_pouziti1.hotove_hledani[0]
        finalni_string = ""

        for i, item in enumerate(nactena_data):
            finalni_string += item + "\n"

            if i == 0:
                finalni_string += item

            else:
                finalni_string += "\n" + item


        copy(finalni_string)

    
    def kopirovat_konkretni_radek(self):

        # kopírovat pouze vybraný řádek

        vybrany_radek = tabulka_data_grafika1.tableWidget.currentRow()

        if vybrany_radek == -1:
            pass
        else:
            content = hodnoty_K_pouziti1.hotove_hledani[0][vybrany_radek]

            tabulka_data_grafika1.tableWidget.setCurrentCell(-1, -1)

            copy(content)

class najit_domenu_grafika0(QMainWindow, Ui_MainWindow_najit_domenu_grafika):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def reset_hodnot(self):

        # vyresetuje hodnoty do původního stavu v polích v okně najit_domenu.py

        najit_domenu_grafika1.label.setHidden(False)
        najit_domenu_grafika1.label_2.setHidden(True)
        najit_domenu_grafika1.label_3.setHidden(True)

        najit_domenu_grafika1.lineEdit.clear()
        najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: ")
        najit_domenu_grafika1.lineEdit.setClearButtonEnabled(True)
        najit_domenu_grafika1.lineEdit.setReadOnly(False)

        najit_domenu_grafika1.pushButton.setHidden(False)
        najit_domenu_grafika1.pushButton_2.setHidden(True)

        najit_domenu_grafika1.pushButton.setEnabled(True)
        najit_domenu_grafika1.pushButton_2.setEnabled(True)

        najit_domenu_grafika1.comboBox.setHidden(False)
        najit_domenu_grafika1.comboBox.setEnabled(True)
        najit_domenu_grafika1.comboBox.setCurrentIndex(0)

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

                tabulka_data_grafika1.tableWidget.setRowCount(aktualni_radek+1)
                tabulka_data_grafika1.tableWidget.setItem(aktualni_radek, 0, QtWidgets.QTableWidgetItem(row))
                aktualni_radek += 1
        
        else:

            tabulka_data_grafika1.tableWidget.setRowCount(0)

            tabulka_data_grafika1.label_2.setGeometry(QtCore.QRect(150, 190, 301, 101))
            
            tabulka_data_grafika1.label_2.setText("Nebyla nalezena žádná data")
            tabulka_data_grafika1.label_2.setHidden(False)

        informace_text = str(len(ziskane_informace)) + " " + moznosti[typ_hledani]

        tabulka_data_grafika1.lineEdit.setText(informace_text)
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

    
    def nalezeni_API_klice(self, headers):

        # funkce která z html získa api klíč stránky
        # pro nastavení vlastího API klíče smazat celý kód v TÉTO funkci a jako return dát string svého api klíče

        API_KEY = "077424c6-7a26-410e-9269-c9ac546886a4"    # defaultní

        if hodnoty_K_pouziti1.predchozi_id == "":

            phonebook_html = get("https://phonebook.cz", headers=headers).text

            for row in phonebook_html:

                if "var API_KEY" in row:

                    row.replace(" ", "")
                    row = row.split("=")

                    API_KEY = row[1]

                    break

        return API_KEY


    def vyhledat(self):
        # funkce která komunikuje s webovou stránkou

        # 1. vyšle search (1x)
        # 2. while loop, který posílá result requesty, pouze dokud nebude ve vráceném jsonu "status" číslo 1, který tuto smyčku ukončí

        start = time.time()

        headers= {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"}
        moznosti = {"Subdomény": 1, "Emailové adresy": 2, "Adresáře": 3}


        API_KEY = self.nalezeni_API_klice(headers=headers)


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
            # kód v této if podmínce se tedy spouští pouze jednou za celý běh programu, pak se spouští jenom else (v kterém není "terminate" null)

            data1 = {"term": domena_text,"maxresults":10000,"media":0,"target":vybrane_hledani,"terminate":[None],"timeout":20}

        else:

            # "terminate" bude hodnota posledního id

            data1 = {"term": domena_text,"maxresults":10000,"media":0,"target":vybrane_hledani,"terminate":[hodnoty_K_pouziti1.predchozi_id],"timeout":20}
        
        response = session1.post(url=url, headers=headers, json=data1) # search request


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


        url_get = "https://public.intelx.io/phonebook/search/result?k=" + API_KEY + "&id=" + hodnoty_K_pouziti1.predchozi_id  +"&limit=10000"
        list_ziskanych_dat = []

        time.sleep(hodnoty_K_pouziti1.cekani_mezi_requestama)        

        while True:

            # data= v requestu není potřeba, protože jsou parametry už v URL

            response2 = loads(session1.get(url=url_get, headers=headers).text)

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
                break

            elif response2["status"] == 3:

                # prázdné
                pass

            time.sleep(hodnoty_K_pouziti1.cekani_mezi_requestama)   # defaultně 1s

        end = time.time()

        najit_domenu_grafika1.pushButton_2.setHidden(False)
        najit_domenu_grafika1.pushButton.setHidden(True)
        najit_domenu_grafika1.comboBox.setHidden(True)
        najit_domenu_grafika1.label.setHidden(True)
        najit_domenu_grafika1.label_2.setHidden(True)


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
        # hlavní funkce která spustí ostatní
        # na začátku kontroluje správnost
        # requesty probíhají v Threadu

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
            # všechno v pořádku -> spuštění Threadu

            najit_domenu_grafika1.pushButton.setEnabled(False)
            najit_domenu_grafika1.comboBox.setEnabled(False)

            hodnoty_K_pouziti1.hotove_hledani = []

            najit_domenu_grafika1.lineEdit.setReadOnly(True)
            najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)


            t = Thread(target=najit_domenu_grafika1.vyhledat)
            t.start()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    tabulka_data_grafika1 = tabulka_data_grafika0()
    najit_domenu_grafika1 = najit_domenu_grafika0()
    hodnoty_K_pouziti1 = Hodnoty_K_pouziti0()
    file_dialog1 = file_dialog0()

    tabulka_data_grafika1.show()


    tabulka_data_grafika1.pushButton.clicked.connect(tabulka_data_grafika1.tlacitko_nova_domena)  # najít novou doménu
    tabulka_data_grafika1.pushButton_2.clicked.connect(tabulka_data_grafika1.ulozit_do_souboru) # uložit data do souboru
    tabulka_data_grafika1.pushButton_3.clicked.connect(tabulka_data_grafika1.kopirovat_do_schranky) # kopírovat všechna data do schránky
    tabulka_data_grafika1.pushButton_4.clicked.connect(tabulka_data_grafika1.kopirovat_konkretni_radek) # kopírovat řádek do schránky

    najit_domenu_grafika1.pushButton.clicked.connect(najit_domenu_grafika1.main)    # vyhledat doménu
    najit_domenu_grafika1.pushButton_2.clicked.connect(najit_domenu_grafika1.nacteni_dat_do_tabulky)    # načíst data do tabulky

    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(tabulka_data_grafika1.about_to_quit_funkce)

    sys.exit(app.exec_())
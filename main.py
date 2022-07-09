# udělal RxiPland (https://github.com/RxiPland)
# 2022
# Python 3.9.12


# Phonebook - desktop (využívaná stránka: https://phonebook.cz/)

from tabulka_data_grafika import Ui_MainWindow_tabulka_data_grafika
from najit_domenu_grafika import Ui_MainWindow_najit_domenu_grafika
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog
from requests import Session, get
import datetime
import time
from threading import Thread
from os.path import exists
from json import loads
from pyperclip import copy
import webbrowser


class file_dialog0(QDialog):


    def vyberLokace_save(self):
        # otevře průzkumník souborů a nechá uživatele vybrat cestu, kam chce uložit soubor

        try:
            dlg = QFileDialog.getSaveFileName(self, 'Uložte hotový soubor', '','Textový soubor (*.txt);;JSON soubor (*.json);;Zkrášlený JSON (*.json);;CSV (*.csv);;Sešit Excelu (*.xlsx);;Všechny soubory (*.*)')
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

    def start_aplikace(self):

        # spuštění aplikace

        den = datetime.datetime.now().day

        if exists("zbyva_pokusu.json"):

            with open("zbyva_pokusu.json", "r") as f:

                nactena_data = loads(f.read())
                pocet_pokusu = nactena_data["Zbyva_pokusu"]
                posledni_hledani = int(nactena_data["Posledni_hledani"])

                if posledni_hledani != den:  # vyresetovány pokusy (webová stránka)

                    with open("zbyva_pokusu.json", "w") as f:

                        pocet_pokusu_str = '{\"Zbyva_pokusu\": 24, \"Posledni_hledani\": ' + str(den) + '}'   # 24 pokusů / den
                        f.write(pocet_pokusu_str)

                        tabulka_data_grafika1.actionZbyva.setText("Zbývá: 24")

                else:

                    tabulka_data_grafika1.actionZbyva.setText("Zbývá: " + str(pocet_pokusu))

        else:

            with open("zbyva_pokusu.json", "w") as f:

                pocet_pokusu_str = '{\"Zbyva_pokusu\": 24, \"Posledni_hledani\": ' + str(den) + '}'   # 24 pokusů / den

                f.write(pocet_pokusu_str)

                tabulka_data_grafika1.actionZbyva.setText("Zbývá: 24")


        t = Thread(target=tabulka_data_grafika1.aktualizovat_cas)
        t.start()

        tabulka_data_grafika1.show()


    def aktualizovat_cas(self):
        # funkce, která se spustí v Threadu a bude aktualizovat čas do obnovení pokusů

        cas_obnovy = datetime.timedelta(hours=24)

        while ukoncit != True:

            now = datetime.datetime.now()

            hodiny = now.hour
            minuty = now.minute
            sekundy = now.second

            cas_ted = datetime.timedelta(hours=hodiny, minutes=minuty, seconds=sekundy)
            rozdil = str(cas_obnovy - cas_ted)

            tabulka_data_grafika1.actionReset_pokusy.setText("Další pokusy za: " + rozdil)

            time.sleep(1)


    def otevrit_odkaz(self):

        webbrowser.open_new_tab("https://phonebook.cz/")

    def otevrit_odkaz2(self):

        webbrowser.open_new_tab("https://haveibeenpwned.com/")

    def otevrit_odkaz3(self):

        webbrowser.open_new_tab("https://email-checker.net/")

    def napoveda_pocet_pokusu(self):

        # nápověda, která vysvětluje zaznamenávání počtu pokusů

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda")
        msgBox.setText("Počet zbývajících pokusů NEMUSÍ být přesný.\n\nProgram odečítá pouze ty pokusy, které udělá sám, takže pokud uživatel vyhledá přímo z původní stránky (nebo smaže soubor se záznamem), program tento odečtený pokus nezaznamená a zapíše nula pokusů až tehdy, kdy ho stránka nepustí dál.\nTakže se může stát, že uživateli budou zbývat pokusy, ale najednou se z nich stane nula, protože některé z nich BYLY použity mimo program.\n\nPokusy by se měly obnovit každý den v 0:00:00\nOdhadovaný počet pokusů: 24/den")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def otevrit_odkaz_tabulka(self):

        row = tabulka_data_grafika1.tableWidget.currentRow()

        content = str(tabulka_data_grafika1.tableWidget.item(row, 0).text())

        if not "@" in content:  # otevře pouze odkazy

            tabulka_data_grafika1.tableWidget.setCurrentCell(-1, -1)

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Oznámení")
            msgBox.setText("Opravdu chcete otevřít odkaz:\n\n" + content )
            msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            buttonY = msgBox.button(QMessageBox.Yes)
            buttonY.setText("Ano")
            buttonN = msgBox.button(QMessageBox.No)
            buttonN.setText("Zrušit")

            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Yes:

                if not "http" in content or "https" in content:

                    content = "https://" + content

                webbrowser.open_new_tab(content)

            else:

                return


    def tlacitko_nova_domena(self):

        najit_domenu_grafika1.reset_hodnot()

        den = datetime.datetime.now().day

        if exists("zbyva_pokusu.json"):

            with open("zbyva_pokusu.json", "r") as f:

                nactena_data = loads(f.read())
                pocet_pokusu = nactena_data["Zbyva_pokusu"]
                posledni_hledani = int(nactena_data["Posledni_hledani"])

                if posledni_hledani != den:  # vyresetovány pokusy (webová stránka)

                    with open("zbyva_pokusu.json", "w") as f:

                        pocet_pokusu = '{\"Zbyva_pokusu\": 24, \"Posledni_hledani\": ' + str(den) + '}'   # 24 pokusů / den
                        f.write(pocet_pokusu)

                        najit_domenu_grafika1.label_4.setText("zbývá 24 hledání")

                else:

                    najit_domenu_grafika1.label_4.setText("zbývá " + str(pocet_pokusu) + " hledání")

        else:

            with open("zbyva_pokusu.json", "w") as f:

                pocet_pokusu = '{\"Zbyva_pokusu\": 24, \"Posledni_hledani\": ' + str(den) + '}'   # 24 pokusů / den

                f.write(pocet_pokusu)

                najit_domenu_grafika1.label_4.setText("zbývá 24 hledání")

        najit_domenu_grafika1.center_funkce()
        najit_domenu_grafika1.show()
        tabulka_data_grafika1.close()
        hodnoty_K_pouziti1.okno = 1

    def about_to_quit_funkce(self):

        # class hodnoty_K_pouziti slouží pro uchovávání čísla, které reprezentuje okno, které je otevřeno naposled

        if hodnoty_K_pouziti1.okno == 0:
            # pokud uživatel zavře okno s tabulkou, program se ukončí
            global ukoncit, ukoncit2

            ukoncit = True # slouží pro zastavení Threadu ve funkci aktualizovat_cas()
            ukoncit2 = True # slouží pro zastavení Threadu ve funkci doba_trvani_requestu() - mělo by být už dávno vypnuto
            app.quit()
        
        elif hodnoty_K_pouziti1.okno == 1:
            # pokud uživatel zavře okno najít doménu, funkce otevře okno s tabulkou

            ukoncit = False
            ukoncit2 = True

            with open("zbyva_pokusu.json", "r") as f:

                nactena_data = loads(f.read())
                pocet_pokusu = str(nactena_data["Zbyva_pokusu"])

            tabulka_data_grafika1.actionZbyva.setText("Zbývá: " + pocet_pokusu)

            t = Thread(target=tabulka_data_grafika1.aktualizovat_cas)
            t.start()

            tabulka_data_grafika1.center_funkce()
            tabulka_data_grafika1.show()
            najit_domenu_grafika1.close()
            hodnoty_K_pouziti1.okno = 0


    def vymazat_mezery(self, obsah_raw):

        # funkce pro uložení jak zkrášlený json
        # preventivně vymaže všechny mezery (kromě mezer v uvozovkách)

        final = ""
        uvozovky_lock = False   # false == mimo uvozovky;  true == v uvozovkách

        for znak in obsah_raw:
            if znak in ["\"", "\'"]:

                if uvozovky_lock:

                    uvozovky_lock = False
                else:
                    uvozovky_lock = True

                final += znak

            elif znak in [" ", "\n", "\t"] and not uvozovky_lock:
                pass

            else:
                final += znak

        return final


    def ulozit_do_souboru(self, vybrana_lokace):
        # uloží data z tabulky do souboru
        # funkce je spuštěna v Threadu

        cesta_soubor = vybrana_lokace[0]    # cesta k souboru

        if cesta_soubor != "" and vybrana_lokace != "exited":

            typ_souboru: str = vybrana_lokace[1]     # .txt / .json / .xlsx
            content = hodnoty_K_pouziti1.hotove_hledani[0]  # nalezená data

            if ".json" in typ_souboru:

                # uživatel vybral json

                moznosti = {1: "Subdomain", 2: "EmailAddress", 3: "Directory"}

                dohromady = []

                domena = hodnoty_K_pouziti1.hotove_hledani[1]
                typ_hledani = moznosti[hodnoty_K_pouziti1.hotove_hledani[2]]

                for item in content:

                    if "\'" in item:

                        item = str(item).replace("\'", "#&;UVOZOVKA;&#")

                    dohromady.append(item)
                
                finalni_json = str({"Data": dohromady, "Domena": domena, "Typ": typ_hledani})

                if "zkrášlený" in typ_souboru.lower():

                    # zkrášlený json
                    # https://github.com/RxiPland/Json-beautifier

                    finalni_json = tabulka_data_grafika1.vymazat_mezery(finalni_json)
                    
                    final = ""              # pomocná proměnná do které for zapisuje postupně znak po znaku
                    i = 0                   # počet /t (tab) odsazení -> bude se postupně vnořovat
                    uvozovky_lock = False   # false == mimo uvozovky;  true == v uvozovkách

                    for x, character in enumerate(finalni_json):

                        if character in ["\'", "\""]:
                            if uvozovky_lock == False:
                                uvozovky_lock = True
                            else:
                                uvozovky_lock = False

                            final += character
                        
                        elif character == ":" and uvozovky_lock == False:
                            if finalni_json[x] == " ":
                                pass
                            else:
                                character += ' '

                            final += character

                        elif character == "{" and uvozovky_lock == False:
                            final += "{\n" + "\t"*(i+1)
                            i += 1

                        elif character == "}" and uvozovky_lock == False:
                            i -= 1
                            final += "\n" + "\t"*i + "}"

                        elif character == "," and uvozovky_lock == False:
                            final += "," + "\n" + "\t"*i

                        elif character == "[" and uvozovky_lock == False:
                            if finalni_json[x+1] == "]":
                                final += character
                            else:
                                i += 1
                                final += "[" + "\n" + "\t"*i

                        elif character == "]" and uvozovky_lock == False:
                            if finalni_json[x-1] == "[":
                                final += character
                            else:
                                i -= 1
                                final += "\n" + "\t"*i + "]"

                        else:
                            final += character

                    finalni_json = final


                with open(cesta_soubor, "w") as f:

                    # uložení dat do souboru

                    string_json = finalni_json.replace("\'", "\"").replace("#&;UVOZOVKA;&#", "\'")

                    f.write(string_json)

            elif ".csv" in typ_souboru:
            
                # uživatel vybral csv

                import pandas

                pandas_dataframe = pandas.DataFrame({"Data": hodnoty_K_pouziti1.hotove_hledani[0]})
                pandas_dataframe.to_csv(cesta_soubor, index=False)    # uložení hodnot do csv


            elif ".xlsx" in typ_souboru:

                # uživatel vybral excel

                import pandas

                pandas_dataframe = pandas.DataFrame({"Data": hodnoty_K_pouziti1.hotove_hledani[0]})
                pandas_dataframe.to_excel(cesta_soubor, index=False, sheet_name="Sheet1")    # uložení hodnot do excelu


            else:

                # uživatel vybral txt

                with open(cesta_soubor, "w") as f:

                    for i, item in enumerate(content):

                        if i == 0:
                            f.writelines(item)
                        else:
                            f.writelines("\n" + item)

    def ulozit_main(self):

        # funkce která spustí Thread

        vybrana_lokace = file_dialog1.vyberLokace_save()

        t = Thread(target=tabulka_data_grafika1.ulozit_do_souboru, args=[vybrana_lokace])
        t.start()


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

    def doba_trvani_requestu(self):

        global ukoncit2

        # while loop pro vypisování času, který uběhl od začátku poslání requestu
        # spuští se v Threadu

        start = time.time()
        ukoncit2 = False

        while ukoncit2 != True:

            end = time.time()

            doba = "Doba trvání: " + str(round(end-start,2)) + " vteřin"
            najit_domenu_grafika1.label_3.setText(doba)

            time.sleep(0.05)

    def reset_hodnot(self):

        # vyresetuje hodnoty do původního stavu v polích v okně najit_domenu.py

        global ukoncit

        ukoncit = True

        najit_domenu_grafika1.label.setHidden(False)
        najit_domenu_grafika1.label_2.setHidden(False)
        najit_domenu_grafika1.label_3.setHidden(True)
        najit_domenu_grafika1.label_4.setHidden(False)

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

            try:

                phonebook_html = get("https://phonebook.cz", headers=headers).text

            except:

                return "nefunguje_internet"

            for row in phonebook_html:

                if "var API_KEY" in row:

                    row.replace(" ", "")
                    row = row.split("=")

                    API_KEY = row[1]

                    break

        return API_KEY

    def zobrazit_error(self, message: str):

        # funkce, která dosadí do line editu text s chybou, označí ho červeně a ukáže dobu trvání

        najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: red")
        najit_domenu_grafika1.lineEdit.setText(message)
        najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)
        najit_domenu_grafika1.label.setHidden(True)
        najit_domenu_grafika1.label_2.setHidden(True)
        najit_domenu_grafika1.label_4.setHidden(True)

        global ukoncit2
        ukoncit2 = True



    def vyhledat(self):
        # funkce která komunikuje s webovou stránkou

        # 1. vyšle search (1x)
        # 2. while loop, který posílá result requesty, pouze dokud nebude ve vráceném jsonu "status" číslo 1, který tuto smyčku ukončí

        headers= {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"}
        moznosti = {"Subdomény": 1, "Emailové adresy": 2, "Adresáře": 3}


        API_KEY = self.nalezeni_API_klice(headers=headers)

        if API_KEY == "nefunguje_internet":

            try:

                get("https://google.com")

                najit_domenu_grafika1.zobrazit_error("Stránka https://phonebook.cz není dostupná! (výpadek / údržba)")

                return "chyba_phonebook.cz"

            except:

                najit_domenu_grafika1.zobrazit_error("Nelze se připojit k internetu!")

                return "chyba_internet"

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
        
        try:

            response = session1.post(url=url, headers=headers, json=data1) # search request

        except:

            try:

                # zkusí se jestli funguje uživatelův internet -> udělá se request na google

                get("https://google.com")

                najit_domenu_grafika1.zobrazit_error("Stránka https://public.intelx.io není dostupná! (výpadek / údržba)")

                return "chyba_public.intelx.io"

            except:

                najit_domenu_grafika1.zobrazit_error("Nelze se připojit k internetu!")

                return "chyba_internet"


        if response.status_code == 402:
            
            najit_domenu_grafika1.zobrazit_error("Byl přesáhnut denní limit požadavků!")

            with open("zbyva_pokusu.json", "w") as f:

                den = datetime.datetime.now().day

                pocet_pokusu = '{\"Zbyva_pokusu\": 0, \"Posledni_hledani\": ' + str(den) + '}'

                f.write(pocet_pokusu)

                najit_domenu_grafika1.label_4.setText("zbývá 0 hledání")


            return "chyba402"

        elif response.status_code == 403:
            
            najit_domenu_grafika1.zobrazit_error("IP adresa je na black listu (zkuste vypnout VPN)")

            return "chyba403"

        elif response.status_code == 200:

            hodnoty_K_pouziti1.predchozi_id = loads(response.text)["id"]

            url_get = "https://public.intelx.io/phonebook/search/result?k=" + API_KEY + "&id=" + hodnoty_K_pouziti1.predchozi_id  +"&limit=10000"
            list_ziskanych_dat = []

            time.sleep(hodnoty_K_pouziti1.cekani_mezi_requestama)

            global ukoncit2

            while ukoncit2 != True:

                # data= v requestu není potřeba, protože jsou parametry už v URL

                try:

                    response2 = session1.get(url=url_get, headers=headers)

                except:

                    najit_domenu_grafika1.zobrazit_error("Neznámá chyba (pravděpodobně na straně webu)")

                    return

                response2 = loads(response2.text)

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


            ukoncit2 = True  # zastavení časovače

            najit_domenu_grafika1.pushButton_2.setHidden(False)
            najit_domenu_grafika1.pushButton.setHidden(True)
            najit_domenu_grafika1.comboBox.setHidden(True)
            najit_domenu_grafika1.label.setHidden(True)
            najit_domenu_grafika1.label_4.setHidden(True)


            najit_domenu_grafika1.lineEdit.setText("Hledání bylo dokončeno.")
            najit_domenu_grafika1.lineEdit.setClearButtonEnabled(False)
            najit_domenu_grafika1.lineEdit.setStyleSheet("background-color: green")

            den = datetime.datetime.now().day

            if exists("zbyva_pokusu.json"):

                with open("zbyva_pokusu.json", "r") as f:

                    pocet_pokusu = loads(f.read())["Zbyva_pokusu"]  # dictionary


                with open("zbyva_pokusu.json", "w") as f:

                    pocet_pokusu = '{\"Zbyva_pokusu\":' + str(pocet_pokusu-1) + ', \"Posledni_hledani\": ' + str(den) + '}'

                    f.write(pocet_pokusu)

            else:

                with open("zbyva_pokusu.json", "w") as f:

                    pocet_pokusu = '{\"Zbyva_pokusu\": 23, \"Posledni_hledani\": ' + str(den) + '}'   # 24 pokusů / den;  jeden request už proběhl, tudíž 23

                    f.write(pocet_pokusu)

        
            hodnoty_K_pouziti1.hotove_hledani = [list_ziskanych_dat, domena_text, vybrane_hledani]  # uložení dat do classy

        else:

            najit_domenu_grafika1.zobrazit_error("Neznámá chyba (pravděpodobně na straně webu)")

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
            
            najit_domenu_grafika1.label_2.setHidden(True)

            # funkce hledání informací
            t = Thread(target=najit_domenu_grafika1.vyhledat)
            t.start()

            najit_domenu_grafika1.label_3.setHidden(False)

            # funkce pro ukazování času doby trvání
            t = Thread(target=najit_domenu_grafika1.doba_trvani_requestu)
            t.start()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    tabulka_data_grafika1 = tabulka_data_grafika0()
    najit_domenu_grafika1 = najit_domenu_grafika0()
    hodnoty_K_pouziti1 = Hodnoty_K_pouziti0()
    file_dialog1 = file_dialog0()

    global ukoncit, ukoncit2
    ukoncit = False
    ukoncit2 = False

    tabulka_data_grafika1.start_aplikace()

    tabulka_data_grafika1.label_3.linkActivated.connect(tabulka_data_grafika1.otevrit_odkaz)    # otevře odkaz na phonebook.cz

    tabulka_data_grafika1.pushButton.clicked.connect(tabulka_data_grafika1.tlacitko_nova_domena)  # najít novou doménu
    tabulka_data_grafika1.pushButton_2.clicked.connect(tabulka_data_grafika1.ulozit_main) # uložit data do souboru
    tabulka_data_grafika1.pushButton_3.clicked.connect(tabulka_data_grafika1.kopirovat_do_schranky) # kopírovat všechna data do schránky
    tabulka_data_grafika1.pushButton_4.clicked.connect(tabulka_data_grafika1.kopirovat_konkretni_radek) # kopírovat řádek do schránky

    najit_domenu_grafika1.lineEdit.returnPressed.connect(najit_domenu_grafika1.main) # vyhledat doménu (zmáčknutý enter)
    najit_domenu_grafika1.pushButton.clicked.connect(najit_domenu_grafika1.main)    # vyhledat doménu
    najit_domenu_grafika1.pushButton_2.clicked.connect(najit_domenu_grafika1.nacteni_dat_do_tabulky)    # načíst data do tabulky

    tabulka_data_grafika1.actionPhonebook_cz.triggered.connect(tabulka_data_grafika1.otevrit_odkaz)     # otevře odkaz phonebook.cz
    tabulka_data_grafika1.actionHaveibeenpwned_com.triggered.connect(tabulka_data_grafika1.otevrit_odkaz2) # otevře odkaz haveibeenpwned.com
    tabulka_data_grafika1.actionEmail_checker_net.triggered.connect(tabulka_data_grafika1.otevrit_odkaz3) # otevře odkaz email-checker.net

    tabulka_data_grafika1.actionZbyva.triggered.connect(tabulka_data_grafika1.napoveda_pocet_pokusu) # otevře nápovědu

    tabulka_data_grafika1.tableWidget.cellDoubleClicked.connect(tabulka_data_grafika1.otevrit_odkaz_tabulka) # otevře odkaz, pokud uživatel klikl dvakrát na pole v tabulce

    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(tabulka_data_grafika1.about_to_quit_funkce)

    sys.exit(app.exec_())
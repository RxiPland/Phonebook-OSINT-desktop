# Phonebook [OSINT](https://cs.wikipedia.org/wiki/Zpravodajstv%C3%AD_z_otev%C5%99en%C3%BDch_zdroj%C5%AF) desktop

- Program využívá stránku https://phonebook.cz/
- Nejsem vlastníkem této stránky
- Na žádost program odstraním
- Program byl vytvořen pro vzdělávací účely
#
- Program uses website https://phonebook.cz/
- I'm not the owner of this website
- I will remove the program upon request
- The program was made for educational purposes

# Použití

- Program slouží pro získání emailových adres, subdomén nebo adresářů na základě domény (např. github.com)
- Je zde možnost si výsledky zkopírovat do schránky, nebo uložit do souboru jako textový dokument, excelovou tabulku, JSON nebo jako zkrášlený JSON - [Zkrášlovač jsonu](https://github.com/RxiPland/Json-beautifier)
- Stránka má omezený počet vyhledávání/den, tudíž program přestane fungovat, jakmile přesáhnete tento denní limit (na základě IP adresy)
- Program také nebude fungovat, pokud bude aktivní vpn (stránka ji blokuje)
<br/>

# Náhled
![1 1](https://user-images.githubusercontent.com/82058894/177490636-09f99ba3-eef6-4ad1-8b31-9d0c1cbb9ab0.png)

**Možnosti uložení:**<br/>
![2](https://user-images.githubusercontent.com/82058894/177725961-ea62555f-2c23-4929-8662-5021a3f01cdc.png)

# Použité knihovny
```
pip install PyQt5
pip install Requests
pip install Pyperclip
pip install openpyxl
pip install Pandas

```

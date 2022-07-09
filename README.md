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
![1](https://user-images.githubusercontent.com/82058894/177979089-c181c11a-3f28-469f-9082-c16ac4cc17c8.png)

# Možnosti uložení
![2](https://user-images.githubusercontent.com/82058894/178111718-809c00e8-8ff8-4520-85c3-1262401dce8a.png)

# Ukázka uložení jako zkrášlený json
![3](https://user-images.githubusercontent.com/82058894/177979490-e86724bd-722e-4f77-ba76-6948adf817fc.png)

# Použité knihovny
```
pip install PyQt5
pip install Requests
pip install Pyperclip
pip install openpyxl
pip install Pandas

```

from src.io.import_csv import charger_portefeuille_csv

obligations = charger_portefeuille_csv("data/portefeuille.csv")

for o in obligations:
    print(o)

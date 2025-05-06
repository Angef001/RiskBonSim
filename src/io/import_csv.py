import csv
from src.instruments.obligation import Obligation


def charger_portefeuille_csv(chemin_fichier):
    obligations = []

    with open(chemin_fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            oblig = Obligation(
                nom=row["nom"],
                maturite=int(row["maturite"]),
                coupon=float(row["coupon"]),
                frequence=int(row["frequence"]),
                prix=float(row["prix"]),
                nominal=float(row.get("nominal", 1000))
            )
            oblig.poids = float(row.get("poids", 0))  # 👈 AJOUT ICI
            obligations.append(oblig)

    return obligations

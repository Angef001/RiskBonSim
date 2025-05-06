import sys
import os
sys.path.append(os.path.abspath("src"))

from src.io.import_csv import charger_portefeuille_csv
from risk.var import calculer_var_parametrique  # ajoute ce import en haut du fichier

def test_extraire_donnees_var():
    obligations = charger_portefeuille_csv("data/portefeuille.csv")

    valeurs = [o.prix for o in obligations]
    poids = [o.poids / 100 for o in obligations]

    print("✅ Valeurs :", valeurs)
    print("✅ Poids (fraction) :", poids)

    assert len(valeurs) == len(poids), "Longueurs incohérentes"
    assert abs(sum(poids) - 1.0) < 1e-6, "Les poids ne totalisent pas 100%"

    # 🔢 Étape 2 – Ajout des volatilités et corrélation
    volatilites = [0.05, 0.06, 0.04]  # en décimal
    correlation = [
        [1.0, 0.3, 0.2],
        [0.3, 1.0, 0.25],
        [0.2, 0.25, 1.0]
    ]

    print("✅ Volatilités :", volatilites)
    print("✅ Corrélation :")
    for row in correlation:
        print(row)

    # Calcul de la VaR
    var = calculer_var_parametrique(valeurs, poids, volatilites, correlation, niveau_confiance=0.95)
    print(f"📉 VaR estimée (95%) : {var:,.2f} €")



if __name__ == "__main__":
    test_extraire_donnees_var()

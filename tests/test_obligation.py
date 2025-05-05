from scr.instruments.obligation import Obligation

# Création d'une obligation fictive
oblig = Obligation("TestOblig", 5, 5.0, 1, 100)

# Taux de 4%
prix_oblig = oblig.calculer_prix_bond(0.04)

# Afficher le prix
print(f"Le prix de l'obligation est {prix_oblig:.2f}")

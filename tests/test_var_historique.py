from src.risk.historique import simuler_rendements, calculer_pnl_hist

def test_simulation_pnl():
    rendements = simuler_rendements(nb_jours=100, nb_actifs=3)
    poids = [0.3, 0.4, 0.3]
    valeur_totale = 1000000
    pnl = calculer_pnl_hist(rendements, poids, valeur_totale)
    print("✅ P&L simulés :", pnl[:5])

if __name__ == "__main__":
    test_simulation_pnl()

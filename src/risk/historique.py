import numpy as np
import pandas as pd

def simuler_rendements(nb_jours=250, nb_actifs=3, seed=42):
    np.random.seed(seed)
    return np.random.normal(loc=0.0001, scale=0.01, size=(nb_jours, nb_actifs))

def calculer_pnl_hist(rendements, poids, valeur_totale):
    poids = np.array(poids)
    pnl = rendements @ poids * valeur_totale
    return pnl

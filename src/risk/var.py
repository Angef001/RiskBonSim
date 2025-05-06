import numpy as np
from scipy.stats import norm

def calculer_var_parametrique(valeurs_portefeuille, poids, volatilites, correlation, niveau_confiance=0.95):
    """
    Calcule la VaR paramétrique (méthode variance-covariance) d’un portefeuille obligataire.

    :param valeurs_portefeuille: Liste des valeurs de marché des obligations
    :param poids: Liste des pondérations (en fractions, pas en %)
    :param volatilites: Liste des volatilités individuelles (en décimal)
    :param correlation: Matrice de corrélation (carrée, diagonale = 1)
    :param niveau_confiance: Niveau de confiance (ex: 0.95 pour 95%)
    :return: VaR absolue du portefeuille (en €)
    """
    w = np.array(poids)
    sigma = np.diag(volatilites)
    corr = np.array(correlation)
    covariance_matrix = sigma @ corr @ sigma
    z = norm.ppf(niveau_confiance)
    var_portefeuille = w.T @ covariance_matrix @ w
    valeur_totale = sum(valeurs_portefeuille)
    var_abs = z * np.sqrt(var_portefeuille) * valeur_totale
    return var_abs

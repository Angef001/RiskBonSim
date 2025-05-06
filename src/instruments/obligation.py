class Obligation:
    def __init__(self, nom, maturite, coupon, frequence, prix, nominal=1000):
        self.nom = nom
        self.maturite = maturite
        self.coupon = coupon
        self.frequence = frequence
        self.prix = prix
        self.nominal = nominal

    def __repr__(self):
        return f"<Obligation {self.nom} - {self.coupon}% - {self.maturite} ans>"

    def calculer_prix(self, taux):
        n = self.frequence
        T = self.maturite
        N = self.nominal
        y = taux / n
        CF = (self.coupon / 100) * N / n
        prix = 0

        for i in range(1, n * T + 1):
            prix += CF / (1 + y) ** i

        prix += N / (1 + y) ** (n * T)
        return prix


    def obtenir_flux(self):
        """
        Retourne la liste des flux de paiement futurs (coupons + nominal)
        """
        n = self.frequence
        T = self.maturite
        CF = (self.coupon / 100) * self.nominal / n

        flux = [CF] * (n * T)
        flux[-1] += self.nominal  # Ajouter le remboursement du nominal à la dernière période

        return flux

    def calculer_ytm(self, tolérance=1e-6):
        n = self.frequence
        T = self.maturite
        N = self.nominal
        C = (self.coupon / 100) * N / n
        prix_marche = self.prix

        bas = 0.0001
        haut = 1.0
        ytm = (bas + haut) / 2

        while haut - bas > tolérance:
            prix_estime = 0
            for t in range(1, n * T + 1):
                prix_estime += C / (1 + ytm / n) ** t
            prix_estime += N / (1 + ytm / n) ** (n * T)

            if prix_estime > prix_marche:
                bas = ytm
            else:
                haut = ytm
            ytm = (bas + haut) / 2

        return ytm
    
    def calculer_duration_modifiee(self, taux):
        n = self.frequence
        T = self.maturite
        N = self.nominal
        y = taux / n
        CF = (self.coupon / 100) * N / n

        duration = 0
        prix = self.calculer_prix(taux)

        for i in range(1, n * T + 1):
            t = i
            duration += t * CF / (1 + y) ** t

        duration += (n * T) * N / (1 + y) ** (n * T)
        duration /= (prix * n)

        return duration

    def calculer_convexite(self, taux):
        n = self.frequence
        T = self.maturite
        N = self.nominal
        y = taux / n
        CF = (self.coupon / 100) * N / n

        convexite = 0
        prix = self.calculer_prix(taux)

        for i in range(1, n * T + 1):
            t = i
            convexite += t * (t + 1) * CF / (1 + y) ** (t + 2)

        convexite += (n * T) * (n * T + 1) * N / (1 + y) ** (n * T + 2)
        convexite /= (prix * n ** 2)

        return convexite

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdynta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti  # kwh
        super().__init__(rekisteritunnus, huippunopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko  # litraa
        super().__init__(rekisteritunnus, huippunopeus)

sahkoauto = Sahkoauto('ABC-15', 180, 52.5)
polttomoottoriauto = Polttomoottoriauto('ACD-123', 165, 32.3)

sahkoauto.nopeus = 45
polttomoottoriauto.nopeus = 80

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f'{sahkoauto.kuljettu_matka} km')
print(f'{polttomoottoriauto.kuljettu_matka} km')

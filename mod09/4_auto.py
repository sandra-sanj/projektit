import random
from tabulate import tabulate


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


# luo 10 autoa eri rekisteritunnuksilla ja satunnaisella huippunopeudella
autot = [Auto(f'ABC-{index}', random.randint(100, 200)) for index in range(1, 11)]

max_km_kuljettu = False
while not max_km_kuljettu:
    for auto in autot:
        auto.kiihdynta(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            max_km_kuljettu = True

auto_taulukko_formaatti = [
    [auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka] for auto in autot
]

headers = ['Rekisteritunnus', 'Huippunopeus (km/h)', 'Nopeus (km/h)', 'Kuljettu matka (km)']
print(tabulate(auto_taulukko_formaatti, headers=headers, tablefmt='pretty'))

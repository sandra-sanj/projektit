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


class Kilpailu:
    def __init__(self, nimi, pituus_km, osallistuvat_autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            auto.kiihdynta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        auto_taulukko_formaatti = [
            [auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka] for auto in autot
        ]

        headers = ['Rekisteritunnus', 'Huippunopeus (km/h)', 'Nopeus (km/h)', 'Kuljettu matka (km)']
        print(tabulate(auto_taulukko_formaatti, headers=headers, tablefmt='pretty'))

    def kilpailu_ohi(self):
        return any([auto.kuljettu_matka >= self.pituus_km for auto in self.osallistuvat_autot])


# luo 10 autoa eri rekisteritunnuksilla ja satunnaisella huippunopeudella
autot = [Auto(f'ABC-{index}', random.randint(100, 200)) for index in range(1, 11)]
kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

kilpailu_ohi = False
kilpailutunti = 0
while not kilpailu_ohi:
    kilpailu.tunti_kuluu()
    kilpailutunti += 1
    if kilpailutunti % 10 == 0:
        print(f'\nTilanne kilpailutunnilla {kilpailutunti}:')
        kilpailu.tulosta_tilanne()
    kilpailu_ohi = kilpailu.kilpailu_ohi()

print(f'\nKilpailu on ohi! Kilpailu kesti {kilpailutunti} tuntia')
kilpailu.tulosta_tilanne()

import random


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

print('Rekisteritunnus, huippunopeus, nopeus, kuljettu matka')
for auto in autot:
    print(f'{auto.rekisteritunnus} : {auto.huippunopeus} km/h : {auto.nopeus} km/h : {auto.kuljettu_matka} km')

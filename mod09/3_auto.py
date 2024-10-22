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


auto = Auto('ABC-123', 142)

print(f'Aloitusarvot:\n'
      f'Rekisteritunnus {auto.rekisteritunnus}\n'
      f'Huippunopeus {auto.huippunopeus} km/h\n'
      f'Nopeus {auto.nopeus} km/h\n'
      f'Kuljettu matka {auto.kuljettu_matka} km\n')

auto.kiihdynta(60)
print(f'Nopeus: {auto.nopeus} km/h')

auto.kuljettu_matka = 2000
print(f'Auto on kulkenut {auto.kuljettu_matka} km')

auto.kulje(1.5)
print(f'Auto on kulkenut {auto.kuljettu_matka} km')

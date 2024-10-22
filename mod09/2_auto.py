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


auto = Auto('ABC-123', 142)

print(f'Aloitusarvot:\n'
      f'Rekisteritunnus {auto.rekisteritunnus}\n'
      f'Huippunopeus {auto.huippunopeus} km/h\n'
      f'Nopeus {auto.nopeus} km/h\n'
      f'Kuljettu matka {auto.kuljettu_matka} km\n')

auto.kiihdynta(30)
auto.kiihdynta(70)
auto.kiihdynta(50)
print(f'Nopeus: {auto.nopeus} km/h')

auto.kiihdynta(-200)
print(f'Nopeus: {auto.nopeus} km/h')



class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0


auto = Auto('ABC-123', 142)

print(f'{auto.rekisteritunnus}\n{auto.huippunopeus}\n{auto.nopeus}\n{auto.kuljettu_matka}')

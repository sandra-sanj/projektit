class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = self.alin_kerros

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if kerros > self.kerros:
                self.kerros_ylos()
            elif kerros < self.kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1
        print(f'Hissi on kerroksessa {self.kerros}')

    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi on kerroksessa {self.kerros}')

hissi = Hissi(0, 8)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(hissi.alin_kerros)

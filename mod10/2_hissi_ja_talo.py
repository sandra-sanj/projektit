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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(self.alin_kerros, self.ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_nro, kerros):
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kerros)


talo = Talo(0, 8, 3)

talo.aja_hissia(1, 5)

talo.aja_hissia(2, 5)
talo.aja_hissia(2, 3)

talo.aja_hissia(3, 8)

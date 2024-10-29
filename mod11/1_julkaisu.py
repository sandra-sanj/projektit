class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}\n')


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja: {self.paatoimittaja}\n')


lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

import time


class Vozilo:

    def __init__(self, barva, teza, dolzina):
        self.barva = barva
        self.teza = teza
        self.dolzina = dolzina

    def potrobi(self):

        return 'Bip, bip!'

    def pelji(self, koncna_hitrost):

        print 'Pospesujem ...'

        for i in range(koncna_hitrost):
            print 'Trenutna hitrost: {0}'.format(i)
            time.sleep(0.5)

        return 'Peljem na hitrosti: {0}'.format(koncna_hitrost)


class Avto(Vozilo):

    def __init__(self, barva, teza, dolzina, tlak_v_gumah):
        Vozilo.__init__(self, barva, teza, dolzina)
        self.tlak_v_gumah = tlak_v_gumah

    def pelji_nazaj(self, metrov):

        for i in range(metrov):
            if self.tlak_v_gumah > 0:
                self.tlak_v_gumah = self.tlak_v_gumah - 0.1
            print 'Od zacetne tocke sem se premaknil: {0}'.format(i)
            time.sleep(0.05)

        return 'Na tocki: {0}'.format(metrov)

    def napolni_gume(self, tlak):

        if tlak > 3:
            raise ValueError('Previsok tlak, guma je pocila!')
        else:
            self.tlak_v_gumah = tlak


class Coln(Vozilo):

    def __init__(self, barva, teza, dolzina, ugrez):
        Vozilo.__init__(self, barva, teza, dolzina)
        self.ugrez = ugrez

    def sidraj(self, globina, ime_zaliva):

        if globina < self.ugrez:
            raise EnvironmentError('Nasedl si, preplitka voda!')
        else:
            return 'Zasidran v zalivu: {0}'.format(ime_zaliva)


if __name__ == '__main__':

    avto = Avto('rdeca', 1000, 3, 1.5)
    avto.napolni_gume(2)
    avto.pelji_nazaj(10)
    print avto.tlak_v_gumah
    avto.napolni_gume(2)
    print avto.tlak_v_gumah
    print avto.pelji(10)
    print avto.potrobi()
    print avto.barva

    coln = Coln('moder', 1000, 3, 1)
    print coln.pelji(10)
    print coln.potrobi()
    print coln.sidraj(5, 'Modra laguna')
    print coln.pelji(15)
    print coln.sidraj(0.5, 'Mali uvali')


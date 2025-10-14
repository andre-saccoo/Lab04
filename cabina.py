class Cabina:
    def __init__(self,codiceCabina, numeriPosti, ponteNave, prezzo):
        self._codiceCabina=codiceCabina
        self._numeroPosti=numeriPosti
        self._ponteNave=ponteNave
        self._prezzo=prezzo
        self._disponibile=True

    @property
    def disponibile(self):
        return self._disponibile
    @disponibile.setter
    def disponibile(self,disponibile):
        self._disponibile=disponibile

    def __str__(self):
        return f"Codice cabina: {self._codiceCabina}\n" \
               f"numero posti: {self._numeroPosti}\n"\ 
               f"Ponte nave: {self._ponteNave}"\
               f"prezzo: {self._prezzo}"

class Cabina_deluxe(Cabina):
    def __init__(self, codiceCabina, numeriPosti, ponteNave, prezzo, tipologia):
        super().__init__(codiceCabina, numeriPosti, ponteNave, prezzo)
        self._tipologia=tipologia

    def sovrapprezzo (self):
        return self._prezzo * 1.2

class Cabina_animale(Cabina):
    def __init__(self, codiceCabina, numeriPosti, ponteNave, prezzo, numeroAnimal):
        super().__init__(codiceCabina, numeriPosti, ponteNave, prezzo)
        self.numeroAnimali=numeroAnimal

    def sovrapprezzo (self):
        return self._prezzo * (1+0.1*self.numeroAnimali)
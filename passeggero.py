class Passeggero():
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = None
    #def __str__(self):
    #    return f"codice: {self.codice}\n nome: {self.nome}\n cognome: {self.cognome}\n"

    def __str__(self):
        cabinaInfo = f" Cabina: {self.cabina._codiceCabina}" if self.cabina else ""
        return f"codice passeggero: {self.codice}\n nome passeggero: {self.nome}\n cognome passeggero: {self.cognome}\n  {cabinaInfo}"


    def __eq__(self, other):
        return self.codice == other.codice
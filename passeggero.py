class Passeggero():
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = None
    def __str__(self):
        return f"codice: {self.codice}\n nome: {self.nome}\n cognome: {self.cognome}\n"

    def __eq__(self, other):
        return self.codice == other.codice
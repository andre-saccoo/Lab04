class Passeggero():
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return f"codice: {self.codice}\n nome: {self.nome}\n cognome: {self.cognome}"

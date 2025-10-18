import  csv

class Crociera:
    def __init__(self, nome):
        self.nome=nome

        @property
        def nome(self):
            return self._nome
        @nome.setter
        def nome(self, nome):
            self._nome = nome


    def carica_file_dati(self, file_path):
        try:
            with open(file_path) as csv_file:
                for row in csv_file:
                    row = csv.Reader(csv_file)
                    print(row)
        except FileNotFoundError:
            print("File not found")






        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO


import  csv
from passeggero import Passeggero
from cabina import Cabina

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
            infile=open(file_path)
            reader = csv.reader(infile)
            for row in reader:
                print(row)
                id= row[0].upper()
                if len(row)==3 and id.startswith("P"):
                    id, nome, cognome= Passeggero
                    print(f"questa è un passeggero {row}")
                if len(row)==4:
                    print(f"questa è una cabina semplice {row}")
                if len(row)==5:
                    try:
                        int(row[4])
                        print(f"questa è una cabina per animali{row}")
                    except ValueError:
                        print(f"questa è una cabina deluxe {row}")
            infile.close()
        except FileNotFoundError:
            print("File not found")



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO


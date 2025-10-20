import  csv
from passeggero import Passeggero
from cabina import Cabina, Cabina_deluxe, Cabina_animale

#definisco la classe cabina che gestisce anche le classi cabina (di vario tipo) e la classe passeggero
class Crociera:
    def __init__ (self, nome):
        self._nome=nome

        # per i passeggeri e per le cabine creo sia una lista che un dizionario,
        #le liste sono più veloci nell'ordinamento, i dizionari nella ricerca
        self.listaPasseggeri=[]
        self.dizionarioPasseggeri=dict()
        self.listaCabine=[]
        self.dizionarioCabina=dict()

    #definisco il metodo setter e getter per poter leggere i dati della nave
    @property
    def nome (self):
        return self._nome
    @nome.setter
    def nome (self, nome):
        self._nome = nome

    #DUCK TYPING
    # funzione che prova ad aprire il file, per ogni riga controlla la lunghezza
    def carica_file_dati (self, file_path):
        try:
            infile=open (file_path)
            reader = csv.reader (infile)
            for row in reader:
                print (row)
                id= row[0].upper()

                # se la lunghezza della riga è 3 sto leggendo un passeggero, controllo anche chi il codice passeggero inizi con P, controllo non sia
                #già presente nel dizionario dei passeggeri, se non è presente lo aggiungo sia alla lista che al dizionario dei passeggeri
                if len(row)==3 and id.startswith("P"):
                    id, nome, cognome= row[0], row[1], row[2]
                    if id in self.dizionarioPasseggeri:
                        raise ValueError(f" passeggero {id} già presente ")
                    passeggero = Passeggero (id, nome, cognome)
                    self.listaPasseggeri.append(passeggero)
                    self.dizionarioPasseggeri[id] = passeggero

                # se la lunghezza della riga è 4 sto leggendo una cabina standard, controllo che il codice cominci con CAB, controllo non sia già presente
                # nel dizionario dedicato, se non è presente la aggiungo sia alla lista che al dizionario delle cabine
                if len(row)==4 and id.startswith("CAB"):
                    id, numLetti, numPonte, PrezzoBase= row[0], row[1], row[2], row[3]
                    if id in self.dizionarioCabina:
                        raise ValueError(f" cabina {id} già presente nel sistema")
                    cabina= Cabina(id, numLetti, numPonte, PrezzoBase)
                    self.listaCabine.append(cabina)
                    self.dizionarioCabina[id] = cabina

                # se la lunghezza della riga è 5 e il codice cabina comincia con CAB, provo a convertire il quinto elemento in intero,
                # se riesco è una cabina per animali e la aggiungo alla lista e al dizionario delle cabine se non è già presente, se non riesco a
                # convertire attraverso le eccezioni capisco il tipo e aggiungo la cabina di tipo deluxe alla lista e al dizionario delle cabine

                if len(row)==5 and id.startswith("CAB"):
                    try:
                        int(row[4])
                        if id in self.dizionarioCabina:
                            raise ValueError(f" cabina {id} già presente nel sistema")
                        id, numLetti, numPonte, prezzoBase, numAnimali= row[0], row[1], row[2], row[3], row[4]
                        cabinaAnimali=Cabina_animale(id, numLetti, numPonte, prezzoBase, numAnimali)
                        self.listaCabine.append(cabinaAnimali)
                        self.dizionarioCabina[id] = cabinaAnimali
                    except ValueError:
                        if id in self.dizionarioCabina:
                            raise ValueError(f" cabina {id} già presente nel sistema")
                        id, numLetti, numPonte, prezzoBase, tipologia = row[0], row[1], row[2], row[3], row[4]
                        cabinaDeluxe=Cabina_deluxe (id, numLetti, numPonte, prezzoBase, tipologia)
                        self.listaCabine.append(cabinaDeluxe)
                        self.dizionarioCabina[id] = cabinaDeluxe
            infile.close()
        # gestisco l'eccezione nel caso il file non venga trovato
        except FileNotFoundError:
            print (" File not found ")

        #stampo i dizionari contenti i dati di cabine e passeggeri come verifica
        for id, passeggero in self.dizionarioPasseggeri.items():
            print ( passeggero )

        for id, cabina in self.dizionarioCabina.items():
            print ( cabina )

    # al metodo vengono passati il codice cabina e il codice passeggero, controllo che esistano nel sistema, se la cabina è disponibile
    # se supera i controlli rendo la cabina non disponibile, salvo i dati di passeggero e cabina nel sistema
    def assegna_passeggero_a_cabina (self, codice_cabina, codice_passeggero):
        if codice_cabina not in self.dizionarioCabina:
            raise ValueError ( " la cabina richiesta non esiste nel sistema" )
        if codice_passeggero not in self.dizionarioPasseggeri:
            raise ValueError ( " il passeggero non esiste nel sistema" )

        cabina=self.dizionarioCabina [codice_cabina]
        passeggero=self.dizionarioPasseggeri [codice_passeggero]

        if cabina.disponibile == False:
            print ( " la cabina richiesta non è disponibile ")
        else:
            cabina.passeggero=passeggero
            passeggero.cabina=cabina
            cabina.disponibile=False

    #controllo che i dati siano già stati caricati nel sistema, se la lista è piena la ordino in base al prezzo
    def cabine_ordinate_per_prezzo(self):
            if len(self.listaCabine)>0:
                cabineOrdinate = sorted(self.listaCabine, key=lambda c: c.prezzoFinale())
                for c in cabineOrdinate:
                    print(c)
            else :
                print(" Non sono cabine nel sistema")

#la stampo normalmente se presente la cabina aggiornata viene aggiunta dall'if nel __str__
    def elenca_passeggeri(self):
        if len(self.listaPasseggeri)==0:
            print('non ci sono passeggeri a bordo')
        else:
            for p in self.listaPasseggeri:
                print(p)


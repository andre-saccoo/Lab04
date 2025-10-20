#importo la classe crociere che gestisce tutto il sistema
from crociera import Crociera

#stampo il menù con le opzioni che l'utente può scegliere
def menu ():
    print( f'\n--- MENU CROCIERA ---' )
    print( "1. Modifica nome della crociera" )
    print( "2. Carica dati da file" )
    print( "3. Assegna cabina a passeggero" )
    print( "4. Visualizza cabine ordinate per prezzo" )
    print( "5. Visualizza elenco passeggeri" )
    print( "6. Esci" )
    return input( "Scegli un'opzione: " )

def main():
    #definisco il nome della crociera da codice che l'utente può poi modificare scegliendo l'opzione 1
    crociera = Crociera( "MSC Futura" )

    #fino a che l'utente non sceglie di uscire con il comando 6 il programma non si ferma
    while True:
        scelta = menu ()

        #cambio nome alla nave
        if scelta == "1":
            nuovo_nome = input ( "Inserisci il nuovo nome della crociera: " )
            crociera.nome = nuovo_nome
            print ( f"il nuovo nome della crociera è: {crociera.nome}" )

        # carico i dati dal file path dando conferma all'utente o segnalando errore, la funzione carica_file_dati è definita in crociera.py
        elif scelta == "2":
            file_path = "dati_crociera.csv"
            try:
                crociera.carica_file_dati (file_path)
                print ( "Dati caricati correttamente." )
            except FileNotFoundError:
                print ( "File non trovato." )

        # chiedo all'utente di inserire un codice cabina e un codice passeggero, li rendo maiuscoli con il metodo .upper() e li passo alla funzione
        elif scelta == "3":
            codice_cabina = input ( "Codice cabina: ")
            codiceCabina = codice_cabina.upper()
            codice_passeggero = input ( "Codice passeggero: ")
            codicePasseggero = codice_passeggero.upper()
            try:
                crociera.assegna_passeggero_a_cabina(codiceCabina, codicePasseggero)
                print ( "Cabina assegnata con successo." )
            except Exception as e:
                print ( f"Errore: {e}" )

        # stampo la lista delle cabine ordinate per prezzo finale
        elif scelta == "4":
            crociera.cabine_ordinate_per_prezzo()
            print ( "\n--- Cabine ordinate per prezzo ---" )


        elif scelta == "5":
            print ( "\n--- Elenco passeggeri ---" )
            crociera.elenca_passeggeri()

        elif scelta == "6":
            print ( "Uscita dal programma." )
            break

        else:
            print ( "Scelta non valida." )

if __name__ == "__main__":
    main()
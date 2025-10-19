from crociera import Crociera

def menu():
    print(f'\n--- MENU CROCIERA ---')
    print("1. Modifica nome della crociera")
    print("2. Carica dati da file")
    print("3. Assegna cabina a passeggero")
    print("4. Visualizza cabine ordinate per prezzo")
    print("5. Visualizza elenco passeggeri")
    print("6. Esci")

    return input("Scegli un'opzione >> ")

def main():
    crociera = Crociera("MSC Futura")

    while True:
        scelta = menu()
        # controllare
        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome della crociera: ")
            crociera.nome= nuovo_nome
            print(f"il nuovo nome della crociera è: {crociera.nome}")

        elif scelta == "2":
            file_path = "dati_crociera.csv"
            try:
                crociera.carica_file_dati(file_path)
                print("Dati caricati correttamente.")
            except FileNotFoundError:
                print("File non trovato.")

        elif scelta == "3":
            codice_cabina = input("Codice cabina: ")
            codiceCabina=codice_cabina.upper()
            codice_passeggero = input("Codice passeggero: ")
            codicePasseggero = codice_passeggero.upper()
            try:
                crociera.assegna_passeggero_a_cabina(codiceCabina, codicePasseggero)
                print("Cabina assegnata con successo.")
            except Exception as e:
                print(f"Errore: {e}")

        elif scelta == "4":
            crociera.cabine_ordinate_per_prezzo()
            print("\n--- Cabine ordinate per prezzo ---")


        elif scelta == "5":
            print("\n--- Elenco passeggeri ---")
            crociera.elenca_passeggeri()

        elif scelta == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
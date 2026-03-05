import translator as tr

t = tr.Translator()


while True:

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input("\nInserisci il numero dell'opzione: ")

    # Add input control here!
    if not txtIn.isdigit():
        print("Input non valido. Inserisci un numero.")
        continue
    if int(txtIn) > 5:
        print("Numero non valido. Inserisci un numero valido.")
        continue

    if int(txtIn) == 1:
        entry = input("Ok, quale parola devo aggiungere?\n")
        t.handleAdd(entry)
    if int(txtIn) == 2:
        query = input("Ok, quale parola devo cercare?\n")
        t.handleTranslate(query)
    if int(txtIn) == 3:
        query = input("Ok, quale parola devo cercare con wildcard?\n")
        t.handleWildCard(query)
    if int(txtIn) == 4:
        print("\nContenuto del Dizionario:")
        t.dict.printAll()
    if int(txtIn) == 5:
        print("Uscita in corso...")
        break
from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dict = Dictionary()

    def printMenu(self):
        print("\n-----------------------------")
        print("Translator Alien-Italian")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("-----------------------------")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        try:
            with open(dict, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        alien_word = parts[0].lower()
                        translations = [p.lower() for p in parts[1:]]
                        self.dict.addWord(alien_word, translations)
        except FileNotFoundError:
            print(f"File {dict} non trovato.")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        # <parola aliena> <traduzione1 traduzione2 ...>
        parts = entry.strip().split()
        if len(parts) < 2:
            print("Errore: devi inserire la parola aliena e almeno una traduzione divise da spazio.")
            return

        # Controllo errori input: solo caratteri ammessi
        for part in parts:
            if not part.isalpha():
                print("Errore: sono ammessi solo caratteri alfabetici [a-zA-Z].")
                return

        alien_word = parts[0].lower()
        translations = [p.lower() for p in parts[1:]]
        self.dict.addWord(alien_word, translations)
        print("Aggiunta!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.strip().lower()
        if not query.isalpha():
            print("Errore: la parola deve contenere solo caratteri alfabetici [a-zA-Z].")
            return

        translations = self.dict.translate(query)
        if translations:
            for t in translations:
                print(t)
        else:
            print("Nessuna traduzione trovata.")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.strip().lower()

        # Ammesso un solo "?" e controllo che il resto siano lettere
        if query.count('?') != 1 or not query.replace('?', '').isalpha():
            print("Errore: inserire solo caratteri alfabetici e esattamente un carattere jolly '?'.")
            return

        matches = self.dict.translateWordWildCard(query)
        if matches:
            for alien_word, translations in matches.items():
                print(f"Trovata parola {alien_word}: {translations}")
        else:
            print("Nessuna corrispondenza trovata.")
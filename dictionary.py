class Dictionary:
    def __init__(self):
        # Inizializza il dizionario: chiave = parola aliena, valore = lista di traduzioni
        self._dict = {}

    def addWord(self, alien_word, translations):
        #Aggiunge una parola e le sue traduzioni al dizionario.
        if alien_word not in self._dict:
            self._dict[alien_word] = []

        # Aggiunge le traduzioni evitando duplicati
        for t in translations:
            if t not in self._dict[alien_word]:
                self._dict[alien_word].append(t)

    def translate(self, alien_word):
        #Ritorna la lista di traduzioni per la parola aliena.
        return self._dict.get(alien_word, [])

    def translateWordWildCard(self, pattern):
        #Cerca parole aliene corrispondenti al pattern con la wildcard '?' senza usare regex."""
        matches = {}

        # Dividiamo la parola da cercare in due parti usando il '?'
        # Esempio: se pattern è "ali?no", parti diventerà ["ali", "no"]
        parti = pattern.split("?")

        # Se non c'è il '?' per qualche motivo (o ce n'è più di uno), split
        # restituirà una lista con una lunghezza diversa da 2.
        # Il controllo rigoroso lo fai già in translator.py, ma qui assegniamo le variabili:
        if len(parti) == 2:
            prefisso = parti[0]
            suffisso = parti[1]
        else:
            return matches  # Ritorna dizionario vuoto se il pattern è malformato

        # Iteriamo su tutte le parole del nostro dizionario
        for alien_word, translations in self._dict.items():
            # 1° Controllo: La lunghezza deve essere esattamente la stessa
            if len(alien_word) == len(pattern):
                # 2° e 3° Controllo: Inizia con il prefisso e finisce con il suffisso?
                if alien_word.startswith(prefisso) and alien_word.endswith(suffisso):
                    # Se passa tutti i controlli, l'abbiamo trovata!
                    matches[alien_word] = translations

        return matches

    def printAll(self):
        #Stampa l'intero dizionario (utile per l'opzione 4)
        for alien_word, translations in self._dict.items():
            print(f"{alien_word}: {translations}")
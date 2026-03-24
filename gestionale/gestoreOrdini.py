"""""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini
1.1) quando arriva un nuovo ordine, lo aggiungo alla coda assicurandomi che sia eseguito solo dopo altri
2) avere delle funzionalità per avere statistiche sugli ordine
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente
"""
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine


class GestoreOrdini:
    # costruttore
    def __init__(self):
        self._ordini_da_processare = deque() # qui viene creata la coda di ordini
        self._ordini_processati = [] # lista per archiviare ordini processati
        self._statistiche_prodotti = Counter() # dizionario speciale per contare quanti prodotti sono stati venduti
        self._ordini_per_categoria = defaultdict() # dizionario che crea automaticamente un valore di default
        # serve per raggruppare gli ordini per categoria cliente

    def add_ordine(self, ordine: Ordine):
        # aggiunge un nuovo ordine agli elementi da gestire
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    # Prende i sei campi crea tutti gli oggetti e li impacchetta in un ordine e lo restituisce
    def crea_ordine(self, nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP,prezzoP), quantitaP)],
                      ClienteRecord(nomeC, mailC, categoriaC))

    def processa_prossimo_ordine(self):
        # legge il prossimo ordine in coda e lo gestisce

        # assicuriamoci che l'ordine da processare esista
        if not self._ordini_da_processare:
            print("Non vi sono ordini da processare")
            return False #interrompo il metodo

        # se esiste, gestiamo il primo in coda
        ordine = self._ordini_da_processare.popleft() #logica FIFO, processo il primo ordine

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        # mi serve per aggiornare le statistiche sui prodotti venduti
        # es. Laptop - 10 + 2
        # Mouse - 5 + 1
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        # raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        # archivio l'ordine nella lista creata
        self._ordini_processati.append(ordine)

        print("Ordine correttamante processato")


    def processa_tutti_ordini(self):
        # processa tutti gli ordini attualmente presenti in coda
        print(f"Processando {len(self._ordini_da_processare)} ordini")

        # finchè la coda non è vuota processa ordini chiamando il metodo precedente
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self, top_n: int=5):
        # restituisce info sui prodotti più venduti
        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append(prodotto, quantita)
        return valori #restituisco la lista di tuple

    def get_distribuzione_categorie(self):
        # legge tutte le chiavi del dizionario, cicla sulle chiavi e su ognuna va a recuperare la lista
        # degli ordini effettuati, poi mi da delle statistiche come il totale fatturato e lo aggiuge a una lista

        # restituisce info su totale fatturato per ogni categoria presente
        valori = []
        for cat in self._ordini_per_categoria.keys(): # scorre tutte le categorie
            ordini = self._ordini_per_categoria[cat] # prendo la lista di ordini per la categoria
            # sommo il totale lordo degli ordini
            totale_Fatturato = sum( [o.ordini.totale_lordo(0.22) for o in ordini] )
            valori.append(cat, totale_Fatturato)
        return valori

    def stampa_riepilogo(self):
        # vado a stampare lo stato del sistema
        print("Stato attuale del business: ")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}") # numero ordini processati
        print(f"Ordini in coda: {len(self._ordini_da_processare)}") # numero ordini in coda

        print("Prodotti più venduti: ") # stampo i prodotti più venduti
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print(f"Fatturato per categoria: ") # stampa il fatturato per categoria
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat}: {fatturato}")

# serve per testare il sistema e vedere se tutti i metodi creati funzionano in una lista di ordini
def test_modulo():
    sistema = GestoreOrdini() # creo il sistema

    # creo la lista di ordini
    ordini = [
        Ordine([Rigaordine(ProdottoRecord("Laptop",1200.0),1),
                Rigaordine(ProdottoRecord("Mouse", 10.0), 3)
                ], ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),

        Ordine([Rigaordine(ProdottoRecord("Laptop",1200.0),1),
                Rigaordine(ProdottoRecord("Mouse", 10.0), 3),
                Rigaordine(ProdottoRecord("Tablet", 100.0), 1),
                Rigaordine(ProdottoRecord("Cuffie", 140.0), 3)
                ], ClienteRecord("Fulvio Bianchi", "fulvio@mail.it", "Gold")),

        Ordine([
            Rigaordine(ProdottoRecord("Laptop", 1200.0), 1),
            Rigaordine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("Giuseppe Averta", "giuseppe@mail.it", "Silver")),

        Ordine([Rigaordine(ProdottoRecord("Laptop",1200.0),1),
                Rigaordine(ProdottoRecord("Mouse", 10.0), 3),
                Rigaordine(ProdottoRecord("Cuffie", 10.0), 3)
                ], ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),

        Ordine([Rigaordine(ProdottoRecord("Mouse", 10.0), 3)
                ], ClienteRecord("Federica Blu", "federica@mail.it", "Gold"))
    ]

    # aggiungo ordini
    for o in ordini:
        sistema.add_ordine(o)

    # processo tutti gli ordini
    sistema.processa_tutti_ordini()

    # stampo le statistiche
    sistema.stampa_riepilogo()

# main
if __name__ == "__main__":
    test_modulo()



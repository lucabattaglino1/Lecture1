import copy

from gestionale.core.prodotti import ProdottoRecord
#creo singoli prodotti e li aggiungo a una lista
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello =[p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

#stampo i prodotti nome e prezzo
print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#aggiungo a una lista un nuovo prodotto
carrello.append(ProdottoRecord("Monitor", 150.0))

#ordino la listaper prezzo decrescente
carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)

#stampo i prodotti nome e prezzo
print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#faccio la somma di tutti i prodotti nella lista e li vado a stampare
tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

# AGGIUNGERE
#aggiungo un nuovo prodotto
carrello.append(ProdottoRecord("Propdo", 100.0))
#qui con extend posso aggiungere più prodotti
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
#qui ho due elementi (indice, prodotto), perciò inserisco un prodotto in una posizione precisa
carrello.insert(2, ProdottoRecord("ccc", 100.0))

# RIMUOVERE
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) #elimino la prima occorrenza di p1
carrello.clear() #svuoto la lista

# ORDINARE
carrello.sort() #ordina seguendo ordinamento naturale -- questo non funziona se gli oggetti contenuti non definisco un metodo __lt__
carrello.sort(reverse=True) #ordina al contrario
carrello.sort(key = function) #ordina secondo una chiave
carrello_ordinato = sorted(carrello) #prende il carrello lo ordina e cambia il nome, cosi ho due liste una ordinata e una no

# COPIE
carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # crea una copia della lista (se modifico la prima, modifico anche questa)
carrello_copia2 = copy.deepcopy(carrello) # copio anche il contenuto qui (se modifico la prima, non modifico anche questa)

# TUPLE (immutabili)
sede_principale = (45, 8) #lat e long della sede di torino
sede_milano = (45, 9) #lat e long della sede di milano
#stampo queste tuple
print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

#insieme di tuple (tupla di tuple)
AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

#ciclo su una tupla di tuple
for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi)) #restituisco in una tupla

tot, media, max, min = calcola_statistiche_carrello(carrello)

tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie) #stampa solo i primi 3 perchè diversi
print(len(categorie)) #calcola la dimensione (3)
categorie2 = {"Platinum", "Elite", "Gold"}
categorie_all = categorie.union(categorie2) #unisco
categorie_all = categorie | categorie2 # stessa cosa
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 #solo gli elementi presenti in uno dei due set
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2 # differenza simmetrica
print(categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200),
                     ProdottoRecord("Mouse", 20),
                     ProdottoRecord("Tablet", 700)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200),
                     ProdottoRecord("Mouse2", 20),
                     ProdottoRecord("Tablet", 700)}

#Metodi utili per i set
s = set()
s1 = set()

# AGGIUNGERE
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiungo più elementi

# RIMUOVERE
s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear()

# OPERAZIONI INSIEMISTICHE
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

#Dictionary

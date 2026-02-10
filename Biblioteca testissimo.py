biblioteca = [
    {"titolo": "Il Nome della Rosa", "autore": "Umberto Eco", "anno": 1980},
    {"titolo": "Baudolino", "autore": "Umberto Eco", "anno": 2000},
    {"titolo": "Il Barone Rampante", "autore": "Italo Calvino", "anno": 1957},
    {"titolo": "Se una notte d'inverno un viaggiatore", "autore": "Italo Calvino", "anno": 1979},
    {"titolo": "Fontamara", "autore": "Ignazio Silone", "anno": 1933}
]

#COMPITI:
#1. RAGGRUPPAMENTO PER AUTORE (come film per regista)
#Crea dizionario: {"Umberto Eco": ["Il Nome della Rosa", "Baudolino"], ...}
#2. AUTORE CON PIÙ LIBRI (come regista con più film)
#Trova l'autore con più opere in biblioteca
#3. LIBRI DOPO IL 1950 (nuovo!)
#Crea lista di libri pubblicati dopo il 1950
#4. ORDINAMENTO PER ANNO (per autore)
#Per ogni autore, lista libri in ordine cronologico
#CONCETTI DA APPLICARE:
#Raggruppamento dizionario (chiave=autore, valore=lista titoli)
#Trova massimo (autore con più libri)
#Filtro per condizione (anno > 1950)
#Ordinamento interno alle liste

autore_prolifico= {}
aggiungi_titolo = []

for libro in biblioteca:
    scrittore = libro["autore"]
    titolo_libro = libro["titolo"]
    if  scrittore not in autore_prolifico:
        autore_prolifico[scrittore] = []

    autore_prolifico[scrittore].append(titolo_libro)

for autore, titoli in autore_prolifico.items(): #Unisce i titoli agli autori
    # titoli = ["Il Nome della Rosa", "Baudolino"] (lista)
    titoli_stringa = ", ".join(titoli)  # Unisci agli autori i titoli
    print(f"Autore: {autore}, Titoli: {titoli_stringa}")

print("="*50)

autore_max = []
max_libri = 0

for autore, lista_titoli in autore_prolifico.items():
    if len(lista_titoli) > max_libri:
        max_libri = len(lista_titoli)
        autore_max = [autore]

    elif len(lista_titoli) == max_libri:

        autore_max.append(autore)  # Aggiungi altro autore con stesso numero

print(f"{autore_max }   {max_libri}")

print("="*50)

più_vecchio = ""

for libri in biblioteca:
    if libri["anno"] < 1950:
        print(f"Libri antecedenti 1950: Titolo:  {libri["titolo"]}   Autore:    {libro["autore"]}")


libri_dopo_1950 = []  # LISTA vuota (fuori ciclo)

for libro in biblioteca:
    if libro["anno"] > 1950:
        libri_dopo_1950.append(libro["titolo"])  # Aggiungi ALLA LISTA

print(f"Libri dopo il 1950: {libri_dopo_1950}")

autore_libri_completi = {}  # {"Eco": [{"titolo": "...", "anno": 1980}, ...]}

for libro in biblioteca:
    autore = libro["autore"]
    if autore not in autore_libri_completi:
        autore_libri_completi[autore] = []
    autore_libri_completi[autore].append({"titolo": libro["titolo"], "anno": libro["anno"]})

    for autore, libri in autore_libri_completi.items():
        libri_ordinati = sorted(libri, key=lambda x: x["anno"])  # Per anno
        print(f"\n{autore}:")
        for libro in libri_ordinati:
            print(f"  {libro['anno']}: {libro['titolo']}")

# 1. Ordina per autore e anno
biblioteca_ordinata = sorted(biblioteca, key=lambda x: (x["autore"], x["anno"]))

# 2. Stampa con separazione "visiva" tra autori
autore_corrente = ""
for libro in biblioteca_ordinata:
    if libro["autore"] != autore_corrente:
        print(f"\n=== {libro['autore']} ===")
        autore_corrente = libro["autore"]
    print(f"  {libro['anno']}: {libro['titolo']}")
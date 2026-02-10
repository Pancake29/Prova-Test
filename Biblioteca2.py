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

autore_max = []
max_libri = 0

for autore, lista_titoli in autore_prolifico.items():
    if len(lista_titoli) > max_libri:
        max_libri = len(lista_titoli)
        autore_max = [autore]

    elif len(lista_titoli) == max_libri:

        autore_max.append(autore)  # Aggiungi altro autore con stesso numero

        print(autore_prolifico)

print(f"Autore con più libri: {autore_max} ({max_libri} libri: {autore_max}")

autori_ordinati_per_libro = sorted(autore_prolifico.items(),
                        key=lambda x: len(x[1]),  # x[1] = lista titoli
                        reverse=True)
print(f"Lista autori_ordinati_per_libro {autori_ordinati_per_libro}")

for autore, libri in autori_ordinati_per_libro:
    print(f"\nAutore: {autore} ({len(libri)} libri)")
    for titolo in libri:
        print(f"  - {titolo}")
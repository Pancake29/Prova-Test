

libri = [
    {"titolo": "Il nome della rosa", "autore": "Eco", "genere": "giallo", "pagine": 512, "anno": 1949},
    {"titolo": "1984", "autore": "Orwell", "genere": "distopico", "pagine": 328, "anno": 1949},
    {"titolo": "La tregua", "autore": "Levi", "genere": "memoriale", "pagine": 256, "anno": 1963},
    {"titolo": "Se questo è un uomo", "autore": "Levi", "genere": "memoriale", "pagine": 208, "anno": 1947},
    {"titolo": "Il pianeta delle scimmie", "autore": "Boulle", "genere": "fantascienza", "pagine": 224, "anno": 1963},
    {"titolo": "Fahrenheit 451", "autore": "Bradbury", "genere": "distopico", "pagine": 256, "anno": 1953},
    {"titolo": "L'amica geniale", "autore": "Ferrante", "genere": "romanzo", "pagine": 416, "anno": 2011},
    {"titolo": "Io, Robot", "autore": "Asimov", "genere": "fantascienza", "pagine": 288, "anno": 1950}
]
#Raggruppa i titoli per genere (dizionario con liste)

libri_per_genere = {}

for libro in libri:
    generi = libro["genere"]
    titoli = libro["titolo"]
    pagine = libro["pagine"]
    autore = libro["autore"]
    if generi not in libri_per_genere:
        libri_per_genere[generi] = []
    libri_per_genere[generi].append((titoli, pagine))
#print(libri_per_genere)



#Stampare verticale sotto, devo fare ciclo

for genere, lista_autori in libri_per_genere.items():
    print(f"\nGenere {genere}:")
    for titolo in lista_autori:
        print(f"{titolo} ")

#Media pagine per autore (dizionario autore → media pagine)
totale_pagine_complessive_per_autore = 0
media_pagine_complessiva_per_autore = 0


print("="*75)

libri_autori = {}

for libro in libri:
    autori = libro["autore"]
    titolo = libro["titolo"]
    pagina = libro["pagine"]
    if autori not in libri_autori:
        libri_autori[autori] = []
    libri_autori[autori].append(pagina)

for autore, lista_autori in libri_autori.items():
    print(f"\nAutore {autore}:")
    for titolo in lista_autori:
        print(f"Pagine {titolo} ")

print("="*75)

for autori, media_pag_autore in libri_autori.items():
    somma = sum(media_pag_autore)
    conteggio = len(media_pag_autore)
    media = somma / conteggio
    print(f"Media Pagine per Autori: {autori:<10} Media pagine:  {media:>10}")

print("="*75)

#Libri pubblicati prima del 1960 (lista di titoli)

libri_per_anno = {}


for libro in libri:
    titolo = libro["titolo"]
    anno = libro["anno"]
    autore = libro["autore"]
    if anno < 1960:
        if anno not in libri_per_anno:
            libri_per_anno[anno] = []
        libri_per_anno[anno].append(autore)
        libri_per_anno[anno].append(titolo)

print(f"Libri antecedenti 1960 {libri_per_anno}")



print("="*75)


#Autore con più libri (nome e conteggio)

autore_max = {}
libri_max = 0

autore_più_titoli = {}
aggiungi_titolo = []

for autore in libri:
    autori = autore["autore"]
    titolo = autore["titolo"]
    if autori not in autore_più_titoli:

        autore_più_titoli[autori]= []

    autore_più_titoli[autori].append(titolo)


for autore, lista_titolo in autore_più_titoli.items():
    if len(lista_titolo) > libri_max:
        libri_max = len(lista_titolo)
        autore_max = (autore)

print(f"Autore con piu' libri: {autore_max} ({libri_max} libri)")
print(f"Titoli: {autore_più_titoli[autore_max]}")

print("="*75)

#Genere con media pagine più alta (nome genere e media)

pagine_per_genere = {}


for libro in libri:
    generi = libro["genere"]
    titoli = libro["titolo"]
    pagine = libro["pagine"]
    autore = libro["autore"]
    if generi not in pagine_per_genere:
        pagine_per_genere[generi] = []
    pagine_per_genere[generi].append( pagine)



for generi, media_pag_genere in pagine_per_genere.items():
    somma = sum(media_pag_genere)
    conteggio = len(media_pag_genere)
    media = somma / conteggio
    print(f"Media Pagine per Genere: {generi:<15} Media pagine:  {media:>15}")

print("="*75)

media_per_genere = {}
media_max = 0

for genere, lista_pagine in pagine_per_genere.items():
    media = sum(lista_pagine) / len(lista_pagine)
    media_per_genere[genere] = media

    if media > media_max:
        media_max = media
        genere_max = genere
print(f"Media max. pagine/genere   {genere_max}   {media_max}")







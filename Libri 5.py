biblioteca = [
    {"titolo": "Il nome della rosa", "autore": "Eco", "anno": 1980, "copie": 5, "genere": "giallo"},
    {"titolo": "1984", "autore": "Orwell", "anno": 1949, "copie": 8, "genere": "distopico"},
    {"titolo": "La tregua", "autore": "Levi", "anno": 1963, "copie": 3, "genere": "memoriale"},
    {"titolo": "Se questo è un uomo", "autore": "Levi", "anno": 1947, "copie": 4, "genere": "memoriale"},
    {"titolo": "Fahrenheit 451", "autore": "Bradbury", "anno": 1953, "copie": 6, "genere": "distopico"},
    {"titolo": "L'amica geniale", "autore": "Ferrante", "anno": 2011, "copie": 7, "genere": "romanzo"},
    {"titolo": "Io, Robot", "autore": "Asimov", "anno": 1950, "copie": 5, "genere": "fantascienza"},
    {"titolo": "Cose che nessuno sa", "autore": "Gamberale", "anno": 2021, "copie": 2, "genere": "romanzo"},
    {"titolo": "Il problema dei tre corpi", "autore": "Liu", "anno": 2008, "copie": 4, "genere": "fantascienza"},
    {"titolo": "Niente di vero", "autore": "Verdi", "anno": 2023, "copie": 1, "genere": "narrativa"}
]

#Raggruppa i titoli per genere (dizionario genere → lista titoli)
libri_genere = {}
print('Raggruppa i titoli per genere (dizionario genere → lista titoli)')
for libro in biblioteca:
    gene = libro["genere"]
    tito = libro["titolo"]
    unità = libro["copie"]
    if gene not in libri_genere:
        libri_genere[gene] = []
    libri_genere[gene].append((tito, unità))
for genere, titolo in libri_genere.items():
    print(f"Genere: {genere:<15}  Titolo: {titolo}")

print("="*75)

copie_autore = {}

print('Numero totale di copie per autore (dizionario autore → somma copie)')
for libro in biblioteca:
    numero_copie = libro["copie"]
    scrittore  = libro["autore"]
    if scrittore not in copie_autore:
        copie_autore[scrittore] = []
    copie_autore[scrittore].append(numero_copie)
for scrittori, copie in copie_autore.items():
    somma = sum(copie)
    print(f"Autore: {scrittori:<15} NUmero copie: {somma}")

print("="*75)
print('Libro più vecchio e più nuovo (due dizionari separati: min/max anno) — gestisci eventuali ex-aequo')

libro_più_vecchio = []
libro_più_nuovo = []
anno_min = 3000
anno_max =  0

for libro in biblioteca:
    data = libro["anno"]
    tito = libro["titolo"]
    if data < anno_min:
        anno_min = data
        libro_più_vecchio = [(tito, data)]

    elif data == anno_min:
        libro_più_vecchio.append((tito, data))

print(libro_più_vecchio)

for libro in biblioteca:
    data = libro["anno"]
    tito = libro["titolo"]
    if data > anno_max:
        anno_max = data
        libro_più_nuovo = [(tito, data)]

    elif data == anno_max:
        libro_più_nuovo.append((tito, data))

print(libro_più_nuovo)

print("="*75)



print('Ordina i libri per copie (decrescente) (lista con solo titolo e copie)')
lista_libro_copie = sorted(biblioteca,key=lambda x:x["copie"],reverse=True)
lista_semplice_copie = [(a["titolo"], a["copie"])for a in lista_libro_copie]

for titoli, copia in lista_semplice_copie:
    print(f"Titolo: {titoli:<25}   Copie N. {copia}")

print("="*75)
print('Filtra i libri con copie >= 4 (lista di titoli')
titoli_sup_4 = []

for tito, cop in lista_semplice_copie:
    if cop >= 4:
        titoli_sup_4 = [(tito, cop)]
        print(f"Titolo: {tito:<25} Numero copie: {cop}")

print("="*75)




print('Media copie per genere (dizionario genere → media copie')

for tipo, lista_tuple in libri_genere.items():
    copia = []
    for titolo, cop in lista_tuple:
        copia.append(cop)
    media = sum(copia)/ len(copia)
    print(f"Genere: {tipo:<12} Voto Medio: {media}")

print("="*75)

print('Libri per Autore in biblioteca (nome e conteggio titoli)')
libri_per_autore = {}
scrittore_prolifico = []
max_libri = 0

for libri in biblioteca:
    scrittore = libri["autore"]
    titoli = libri["titolo"]
    if  scrittore not in libri_per_autore:
        libri_per_autore[scrittore] = []
    libri_per_autore[scrittore].append(titoli)

for autore, titolo in libri_per_autore.items():
    print(f"Autore {autore:<18} Titolo {titolo}")

print("="*75)

print('Autore prolifico in biblioteca (nome e conteggio titoli)')

for scrittori, lista_titoli in libri_per_autore.items():
    if len(lista_titoli) > max_libri:
        max_libri = len(lista_titoli)
        scrittore_prolifico = [scrittori]
    elif len(lista_titoli) == max_libri:
        scrittore_prolifico.append(scrittori)

print(f"Scrittore con più libri {scrittore_prolifico }   {max_libri}")
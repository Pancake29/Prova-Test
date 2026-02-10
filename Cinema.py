cineteca = [
    {"titolo": "Inception", "regista": "Nolan", "voto": 8.8, "anno": 2010},
    {"titolo": "Il Padrino", "regista": "Coppola", "voto": 9.2, "anno": 1972},
    {"titolo": "Interstellar", "regista": "Nolan", "voto": 8.6, "anno": 2014},
    {"titolo": "Pulp Fiction", "regista": "Tarantino", "voto": 8.9, "anno": 1994}
]

#1. ORDINAMENTO MULTIPLO
#Ordina i film per:
#Prima voto (decrescente), poi anno (crescente)
#Prima regista (alfabetico), poi titolo (alfabetico)
#2. RICERCA FILM MIGLIORE/ PEGGIORE
#Film con voto più alto
#Film più vecchio (anno minimo)
#Regista con più film in cineteca
#3. STATISTICHE
#Media voti
#Conteggio film per regista
#Film dopo il 2000
#4. AGGIUNTA INTERATTIVA (opzionale avanzato)
#Menu che permette di aggiungere nuovi film
#Validazione input (voto 0-10, anno realistico)

ordine_voto = sorted(cineteca, key=lambda x: (x["voto"]), reverse=True)
ordine_anno = sorted(cineteca, key=lambda x: (x["anno"]), reverse=False)

for film in ordine_voto:
    print("Film per voto decrescente titolo: " + film["titolo"])
    print("Regista: " + str(film["regista"]))
    print("Voto: " + str(film["voto"]))
    print("Anno: " + str(film["anno"]))
    print("")

print("="*50)

for film in ordine_anno:
    print("Film per anno crescente titolo: " + film["titolo"])
    print("Regista: " + str(film["regista"]))
    print("Voto: " + str(film["voto"]))
    print("Anno: " + str(film["anno"]))
    print("")

print("="*50)

voto_più_alto = 0
più_vecchio = 2000
regista_più_film = {}


for movie in cineteca:
    merito = movie["voto"]
    if merito > voto_più_alto:
        voto_più_alto = merito
        nome = movie["titolo"]
print(f"Film con voto piu' alto: {nome}    {voto_più_alto}")


for movie in cineteca:
    data = movie["anno"]

    if data < più_vecchio:
        più_vecchio = data
        nome = movie["titolo"]
print(f"Film più vecchio:  {nome}  {più_vecchio}")

regista_più_film = {}
aggiungi_titolo = []

for regia in cineteca:
    regista = regia["regista"]
    titolo = regia["titolo"]
    if regista not in regista_più_film:

        regista_più_film[regista]= []

    regista_più_film[regista].append(titolo)

regista_max = ""
max_film = 0

for regista, lista_titoli in regista_più_film.items():
    if len(lista_titoli) > max_film:
        max_film = len(lista_titoli)
        regista_max = regista

print(f"Regista con più film: {regista_max} ({max_film} film)")
print(f"Titoli: {regista_più_film[regista_max]}")









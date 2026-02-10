film = [
    {"titolo": "Inception", "regista": "Nolan", "voto": 8.8, "anno": 2010},
    {"titolo": "Il Padrino", "regista": "Coppola", "voto": 9.2, "anno": 1972},
    {"titolo": "Interstellar", "regista": "Nolan", "voto": 8.6, "anno": 2014},
    {"titolo": "Pulp Fiction", "regista": "Tarantino", "voto": 8.9, "anno": 1994},
    {"titolo": "Il Cavaliere Oscuro", "regista": "Nolan", "voto": 9.0, "anno": 2008}
]
#COMPITI:
#1. RAGGRUPPAMENTO PER REGISTA
#Crea dizionario: {"Nolan": ["Inception", "Interstellar", ...], ...}
#2. REGISTA CON PIÙ FILM
#Trova il/i regista/i con più film (gestisci pareggi!)
#3. FILM DOPO IL 2000
#Lista di titoli di film usciti dopo il 2000
#4. ORDINAMENTO PER VOTO (per regista)
#Per ogni regista, lista film in ordine di voto (dal più alto)

film_per_regista = {}
film_per_genere = {}
regista_prolifico= {}
aggiungi_titolo = []

print("="*80)

for movie in film:
    regista = movie["regista"]
    titolo = movie["titolo"]

    if regista not in film_per_regista:
        film_per_regista[regista] = []
    film_per_regista[regista].append(titolo)

print(f"Film per regista   Titolo {film_per_regista}")

print("="*80)


regista_max = []
max_film = 0

for regista, lista_titoli in film_per_regista.items():
    if len(lista_titoli) > max_film:
        max_film = len(lista_titoli)
        regista_max = [regista]

    elif len(lista_titoli) == max_film:

        regista_max.append(regista)

print(f"Regista con piu' film {regista_max }   {max_film}")

print("="*80)

for films in film:
    regista = films["regista"]
    titolo_film = films["titolo"]
    if  regista not in regista_prolifico:
        regista_prolifico[regista] = []

    regista_prolifico[regista].append(titolo_film)

for regista, titoli in regista_prolifico.items():

    titoli_stringa = ", ".join(titoli)
    print(f"Lista Regista con piu' films: {regista}, Titoli: {titoli_stringa}")

print("=" * 80)

for films in film:
    if films["anno"] > 2000:
        print(f"Film dopo 2000: Titolo: Regista: {films["regista"]}  Film: {films["titolo"]} Voto:  {films["voto"]}")

print("=" * 80)

film_ordinati = sorted(film, key=lambda x: (x["regista"], x["voto"]), reverse=True)



regista_corrente = ""

for films in film_ordinati:
    if films["regista"] != regista_corrente:
        print(f"\n{films['regista']} ")
        regista_corrente = films["regista"]

    print(f"In ordine di voto {films['voto']}: {films['titolo']}")
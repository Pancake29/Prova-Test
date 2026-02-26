film = [
    {"titolo": "Inception", "regista": "Nolan", "anno": 2010, "voto": 8.8, "genere": "fantascienza", "durata": 148},
    {"titolo": "Il Cavaliere Oscuro", "regista": "Nolan", "anno": 2008, "voto": 9.0, "genere": "azione", "durata": 152},
    {"titolo": "Pulp Fiction", "regista": "Tarantino", "anno": 1994, "voto": 8.9, "genere": "crime", "durata": 154},
    {"titolo": "Kill Bill", "regista": "Tarantino", "anno": 2003, "voto": 8.2, "genere": "azione", "durata": 111},
    {"titolo": "Interstellar", "regista": "Nolan", "anno": 2014, "voto": 8.6, "genere": "fantascienza", "durata": 169},
    {"titolo": "La vita è bella", "regista": "Benigni", "anno": 1997, "voto": 8.6, "genere": "dramma", "durata": 116},
    {"titolo": "Nuovo Cinema Paradiso", "regista": "Tornatore", "anno": 1988, "voto": 8.5, "genere": "dramma", "durata": 155},
    {"titolo": "Django Unchained", "regista": "Tarantino", "anno": 2012, "voto": 8.4, "genere": "western", "durata": 165},
    {"titolo": "Memento", "regista": "Nolan", "anno": 2000, "voto": 8.4, "genere": "thriller", "durata": 113},
    {"titolo": "C'era una volta in America", "regista": "Leone", "anno": 1984, "voto": 8.4, "genere": "gangster", "durata": 229}
]

#Raggruppa i titoli per regista (dizionario regista → lista titoli)
#Voto medio per regista (dizionario regista → voto medio)
#Film con voto massimo (titolo e voto) — gestisci eventuali ex-aequo
#Ordina i film per durata (decrescente) (lista con solo titolo e durata)
#Filtra i film con voto >= 8.5 (lista di titoli)
#Durata media per genere (dizionario genere → durata media)

print('Titoli per regista (dizionario regista → lista titoli)')
film_per_regista = {}

for regista in film:
    registi = regista["regista"]
    titoli = regista["titolo"]
    votazione = regista["voto"]
    if registi not in film_per_regista:
        film_per_regista[registi] = []
    film_per_regista[registi].append((titoli, votazione))
for regia, titol in film_per_regista.items():
    print(f"Regista: {regia:<12} Titolo: {titol} ")

print("="*75)
print('Voto medio per regista (dizionario regista → voto medio)')

for regie, lista_tuple in film_per_regista.items():
    votaz= []
    for titolo, voti in lista_tuple:
        votaz.append(voti)
    media = sum(votaz)/ len(votaz)
    print(f"Regista: {regie:<12} Voto Medio: {media}")

print("="*75)

print('Lista film per voto')


ordina_voto = sorted(film, key=lambda x:x["voto"], reverse=False)
ordina_voto_semplice  = [(a["titolo"], a["voto"]) for a in ordina_voto]

for tit, voti in ordina_voto_semplice:
    print(f"Titolo: {tit:<28} Voto {voti}")
print("="*75)
print('\nFilm voto massimo')
voto_max = 0

dizionario_titoli = {titolo: voto for titolo, voto in ordina_voto_semplice}
voto_max = max(dizionario_titoli.values())
titolo_max = [titolo for titolo, voto in dizionario_titoli.items() if voto == voto_max]
print(f"Voto {voto_max:<10} Modelli: {titolo_max}")
print("="*75)

print('Ordina i film per durata (decrescente) (lista con solo titolo e durata)')

ordina_durata = sorted(film, key=lambda x:x["durata"], reverse=False)
ordina_durata_semplice  = [(a["titolo"], a["durata"]) for a in ordina_durata]

for t, tempo in  ordina_durata_semplice:
    print(f"Titolo: {t:<28} Durata: {tempo}")

print("="*75)
print('Filtra i film con voto >= 8.5 (lista di titoli))')

voto_sup_uguale = []

for tito, voto in ordina_voto_semplice:
    if voto >= 8.5:
        voto_sup_uguale.append(tito)

print(f"Titoli: {voto_sup_uguale}")
print("="*75)
print('Filtra i film per genere(Dizionario genere )')

film_genere = {}

for genere in film:
    generi = genere["genere"]
    tempi = genere["durata"]

    if generi not in film_genere:
        film_genere[generi] = []
    film_genere[generi].append(tempi)

    print(f"Genere: {generi:<12} Durata: {tempi} ")

print("="*75)
print('Durata media per genere (dizionario genere → durata media)')

for genere, lista_durate in film_genere.items():

    media = sum(lista_durate) / len(lista_durate)
    print(f"Genere: {genere:<12} Durata media: {media:.1f} min")

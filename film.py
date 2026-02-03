film = [
    {"titolo": "Inception", "regista": "Christopher Nolan", "anno": 2010, "genere": ["thriller", "fantascienza"], "voto": 8.8},
    {"titolo": "La La Land", "regista": "Damien Chazelle", "anno": 2016, "genere": ["musical", "drammatico"], "voto": 8.0},
    {"titolo": "Il Padrino", "regista": "Francis Ford Coppola", "anno": 1972, "genere": ["drammatico", "crime"], "voto": 9.2},
    {"titolo": "Interstellar", "regista": "Christopher Nolan", "anno": 2014, "genere": ["fantascienza", "drammatico"], "voto": 8.6},
    {"titolo": "Parasite", "regista": "Bong Joon-ho", "anno": 2019, "genere": ["thriller", "commedia", "drammatico"], "voto": 8.6}
]

#STEP 1: ANALISI SEMPLICE
#Conta quanti film hanno voto > 8.5

#Trova l'anno del film più recente
movie = len(film)
print(movie)
contatore_film = 0


for i in film:
    if i['voto'] > 8.5:
        contatore_film +=1

print(f"Film voto sopra 8.5 n.:  {contatore_film} {film}")


#STEP 2: RAGGRUPPAMENTO
#Raggruppa film per regista (dizionario: regista → lista di titoli)

#Raggruppa film per genere (attenzione: ogni film può avere più generi!)

film_per_regista = {}
film_per_genere = {}

for a in film:
    regista = a["regista"]
    titolo = a["titolo"]

    if regista not in film_per_regista:
        film_per_regista[regista] = []
    film_per_regista[regista].append(titolo)
    #print("Titolo:" +   titolo +       "Regista"   + regista)
    print(f"Titolo: {titolo} - Regista: {regista}")


    lista_generi = a["genere"] # creo lista generi avendo il singolo film piu' di un genere
    for genere_nome in lista_generi:
        if genere_nome not in film_per_genere:
            film_per_genere[genere_nome] = []
        film_per_genere[genere_nome].append(titolo)

        print("titolo: " + titolo + " - genere: " + genere_nome)



    print("_"*50)

print(f" Lista  {film}")
print(F" Film per regista: {film_per_regista}")
        #print( "Titolo:"       + titolo +         "Regista" +             regista)

conta = 0
for indice, elemento in enumerate(film, start=1):
    conta = indice  # L'ultimo indice è il numero totale!

print(f"Numero totale film: {conta}")  # Funziona!


for i, movie in enumerate(film, start=1):
    print(f"{i}.")

    print(f"  Titolo: {movie['titolo']}")
    print(f"  Regista: {movie['regista']}")
    print(f"  Anno: {movie['anno']}")
    print(f"  Generi: {', '.join(movie['genere'])}")
    print(f"  Voto: {movie['voto']}")
    print()  # linea vuota

    casa = [1, 2, 3]
    for elemento in casa:  # Nome diverso!
        print(elemento)
        print(casa)
casa = [1, 2, 3]          # 1. casa è una LISTA
print(casa)               # Output: [1, 2, 3]

for casa in casa:         # 2. casa diventa PRIMA 1, POI 2, POI 3
    print("Dentro:", casa) # Stampa: 1, 2, 3

    print("Dopo:", casa)      # 3. Ora casa = 3 (numero), NON la lista!
# casa è 3, non [1,2,3]!
# Se provi: casa.append(4) → ERRORE! (3 è numero, non lista)
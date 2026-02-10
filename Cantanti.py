cantanti = [
    {"nome": "Vasco Rossi", "genere": "Rock", "ascolti_milioni": 120, "album": 30},
    {"nome": "Laura Pausini", "genere": "Pop", "ascolti_milioni": 100, "album": 15},
    {"nome": "Eros Ramazzotti", "genere": "Pop", "ascolti_milioni": 90, "album": 20},
    {"nome": "Lucio Dalla", "genere": "Canzone d'autore", "ascolti_milioni": 80, "album": 25},
    {"nome": "Michele Zarrillo", "genere": "Rock", "ascolti_milioni": 98, "album": 10}
]
#COMPITI (scegline 1-2):
#Raggruppa per genere → {"Rock": ["Vasco Rossi", "Michele Zarrillo"], ...}
#Cantante con più ascolti (gestisci pareggi!)
#Media album per genere (es: Rock: (30+10)/2 = 20)
#Cantanti con > 50 milioni ascolti

print("="*80)

ascolti_Max = 0

for cantante in cantanti:
    ascolti = cantante["ascolti_milioni"]
    nomi = cantante["nome"]
    if ascolti > 50:
        print(f"Cantanti con ascolti >50mil    Nome: {nomi:<15}         Milioni di ascolti: {ascolti:>15}")


print("="*80)

for cantante in cantanti:
    ascolti = cantante["ascolti_milioni"]

    if ascolti > ascolti_Max:
        ascolti_Max = ascolti
        nomi = cantante["nome"]
print(f"Cantante con piu' ascolti      Nome: {nomi:<15}         Milioni di ascolti: {ascolti:>15} ")

print("="*80)

cantante_per_genere = {}


for cantante in cantanti:
    nomi = cantante["nome"]
    generi = cantante["genere"]
    if generi not in cantante_per_genere:
        cantante_per_genere[generi] = []
    cantante_per_genere[generi].append(nomi)

print(f"Cantanti per genere {cantante_per_genere}")


print("="*80)

album_per_genere = {}


for dischi in cantanti:
    numero = dischi["album"]
    genere = dischi["genere"]
    if genere not in album_per_genere:
        album_per_genere[genere] = []
    album_per_genere[genere].append(numero)

print(f"Album per genere {album_per_genere}")

print("="*80)

for genere, lista_album in album_per_genere.items():

    somma = sum(album_per_genere[genere])
    conteggio = len(album_per_genere[genere])
    media_album = somma / conteggio


    print(f" Genere: {genere:<18} Somma:{somma:>8}   Media album{media_album:>10}")
print("="*80)
ristoranti = [
    {"nome": "Da Gigi", "cucina": "Italiana", "stelle": 1, "prezzo_medio": 45, "città": "Roma"},
    {"nome": "Sakura", "cucina": "Giapponese", "stelle": 2, "prezzo_medio": 80, "città": "Milano"},
    {"nome": "El Fogon", "cucina": "Messicana", "stelle": 0, "prezzo_medio": 30, "città": "Roma"},
    {"nome": "Le Jardin", "cucina": "Francese", "stelle": 3, "prezzo_medio": 120, "città": "Firenze"},
    {"nome": "Curry House", "cucina": "Indiana", "stelle": 1, "prezzo_medio": 25, "città": "Milano"},
    {"nome": "Osteria Vecchia", "cucina": "Italiana", "stelle": 1, "prezzo_medio": 38, "città": "Bologna"},
    {"nome": "La Torre", "cucina": "Italiana", "stelle": 2, "prezzo_medio": 65, "città": "Firenze"},
    {"nome": "Sushi Time", "cucina": "Giapponese", "stelle": 0, "prezzo_medio": 22, "città": "Napoli"}
]

#Compiti:
#Raggruppa i nomi dei ristoranti per città (dizionario città → lista nomi)

ristoranti_per_città = {}

for ristorante in ristoranti:
    località = ristorante["città"]
    nomi = ristorante["nome"]
    if località not in ristoranti_per_città:
        ristoranti_per_città[località] = []
    ristoranti_per_città[località].append(nomi)
#print(f" Località ristorante {ristoranti_per_città} Nome Ristorante {nomi}")

for luogo, brand in ristoranti_per_città.items():
    print(f" Località: {luogo:<12} Brands : {brand}")
#Prezzo medio per tipo di cucina (dizionario cucina → prezzo medio)

print("="*75)
tipi_di_cucina = {}

for ristorante in ristoranti:
    gusto= ristorante["cucina"]
    prezzi_medi = ristorante["prezzo_medio"]
    if gusto not in tipi_di_cucina:
        tipi_di_cucina[gusto] = []
    tipi_di_cucina[gusto].append(prezzi_medi)
#print(f" Località ristorante {ristoranti_per_città} Nome Ristorante {nomi}")

for gusto, px_medi in tipi_di_cucina.items():
    print(f"Località : {gusto:<12} Brands € : {px_medi}")

print("="*75)

for taste, lista_prezzi in tipi_di_cucina.items():
    media = sum(lista_prezzi) / len(lista_prezzi)
    print(f"Tipo cucina: {taste:<20}  Prezzo medio €: {media:.1f} ")


print("="*75)
#Ristorante con più stelle (nome e numero stelle)


ristor_stelle = {}
max_stelle = 0
ristor_max_stelle = ""

for ristorante in ristoranti:
    stelline = ristorante["stelle"]
    nomi = ristorante["nome"]
    if stelline not in ristor_stelle:
        ristor_stelle[stelline] = []
    ristor_stelle[stelline].append(nomi)
#print(f" Nome Ristorante {nomi}Numero Stelle {ristor_stelle}")
print("="*75)

for nom, stell in ristor_stelle.items():
    print(f"Nome Ristorante : {nom:<18} Numero Stelle : {stell}")

print("="*75)

for stars, no in ristor_stelle.items():
    if stars > max_stelle:
        max_stelle = stars
        ristor_max_stelle = no
print(f"Nome Ristorante max stars : {ristor_max_stelle} Numero Stelle : {max_stelle}")

print("="*75)


#Ordina i ristoranti per prezzo (crescente) (lista con solo nome e prezzo)
#Filtra i ristoranti con prezzo medio < 50 (lista di nomi)
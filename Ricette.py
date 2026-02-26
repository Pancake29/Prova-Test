ricette = [
    {"nome": "Spaghetti alla carbonara", "difficolta": "media", "tempo_min": 30, "calorie": 550, "regione": "Lazio"},
    {"nome": "Pizza margherita", "difficolta": "facile", "tempo_min": 20, "calorie": 800, "regione": "Campania"},
    {"nome": "Risotto alla milanese", "difficolta": "media", "tempo_min": 40, "calorie": 600, "regione": "Lombardia"},
    {"nome": "Tiramisù", "difficolta": "facile", "tempo_min": 45, "calorie": 450, "regione": "Veneto"},
    {"nome": "Lasagna alla bolognese", "difficolta": "difficile", "tempo_min": 90, "calorie": 700, "regione": "Emilia-Romagna"},
    {"nome": "Ossobuco", "difficolta": "difficile", "tempo_min": 120, "calorie": 650, "regione": "Lombardia"},
    {"nome": "Gelato artigianale", "difficolta": "media", "tempo_min": 60, "calorie": 300, "regione": "Sicilia"},
    {"nome": "Focaccia", "difficolta": "facile", "tempo_min": 40, "calorie": 400, "regione": "Liguria"}
]

#Raggruppa i nomi delle ricette per regione (dizionario regione → lista ricette)

ricette_regione = {}

for ricetta in ricette:
    località = ricetta["regione"]
    ingredienti = ricetta["nome"]
    if località not in ricette_regione:
        ricette_regione[località] = []
    ricette_regione[località].append(ingredienti)
print(ricette_regione)

for regione, ricetta in ricette_regione.items():

    print(f" Regione {regione} {ricetta}")

print("="*100)



#Tempo medio di preparazione per difficoltà (facile, media, difficile)

difficolta_ricetta = {}

for ricetta in ricette:
    impegno = ricetta["difficolta"]
    tempi = ricetta["tempo_min"]
    if impegno not in difficolta_ricetta:
        difficolta_ricetta[impegno] = []
    difficolta_ricetta[impegno].append(tempi)
print(difficolta_ricetta)

for difficolta, tempi in difficolta_ricetta.items():
    print(f"Difficoltà: {difficolta:<10}         Tempi: {tempi}")

print("="*100)

media_tempi = {}

for difficolta, tempo_medio in difficolta_ricetta.items():
    media = sum(tempo_medio) / len(tempo_medio)
    media_tempi[difficolta] = media
print(f"Tempo medio per diff. in minuti: {media_tempi}")

for diff, tempo_md in media_tempi.items():
    print(f"Difficoltà: {diff:<10}      Tempo medio: {tempo_md}")

print("="*100)

#Ordina per calorie e trova Ricetta con più calorie (nome e calorie)

ricetta_calorica= {}

for ricetta in ricette:
    caloria = ricetta["calorie"]
    nomi = ricetta["nome"]
    if caloria not in ricetta_calorica:
        ricetta_calorica[caloria] = []
    ricetta_calorica[caloria].append(nomi)


lista_ordinata = sorted(ricette, key=lambda x:x["calorie"],reverse=True)

lista_semplice = [(a["nome"], a["calorie"])for a in lista_ordinata]
print(f"Lista ricette per calorie:{lista_semplice}")
print("="*100)
max_calorie = 0
ricetta_max_calorie = ""

for nome, calorie  in lista_semplice:
    if calorie > max_calorie:
        max_calorie = calorie
        ricetta_max_calorie = nome
print(f"Ricetta max calorie: {ricetta_max_calorie} Calorie: {max_calorie}")

print("="*100)

#Ordina le ricette per tempo di preparazione (crescente) (lista con solo nome e tempo)
lista_preparazione = sorted(ricette, key=lambda x:x["tempo_min"], reverse=True)
lista_minimal = [(b["nome"], b["tempo_min"])for b in lista_preparazione]
print(lista_minimal)
for ricetta, tempo in lista_minimal:
    print(f"Ricetta: {ricetta:<30} Tempo: {tempo}")

print("="*100)

#Filtra le ricette con calorie < 500 (lista di nomi)

ricette_calor_down500 = []

for nomi, caloria in lista_semplice:
    if caloria < 500:

        ricette_calor_down500.append(nomi)
        print(f"Ricetta meno 500 cal.: {nomi:<20}  Calorie: {caloria}")










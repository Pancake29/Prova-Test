calciatori = [
    {"nome": "Messi", "nazionalita": "Argentina", "goal": 672, "assist": 268, "club": "PSG"},
    {"nome": "Ronaldo", "nazionalita": "Portogallo", "goal": 701, "assist": 220, "club": "Al-Nassr"},
    {"nome": "Neymar", "nazionalita": "Brasile", "goal": 136, "assist": 120, "club": "PSG"},
    {"nome": "Mbappé", "nazionalita": "Francia", "goal": 180, "assist": 95, "club": "PSG"},
    {"nome": "Haaland", "nazionalita": "Norvegia", "goal": 150, "assist": 40, "club": "Manchester City"},
    {"nome": "Lewandowski", "nazionalita": "Polonia", "goal": 512, "assist": 120, "club": "Barcellona"},
    {"nome": "De Bruyne", "nazionalita": "Belgio", "goal": 90, "assist": 180, "club": "Manchester City"},
    {"nome": "Salah", "nazionalita": "Egitto", "goal": 200, "assist": 110, "club": "Liverpool"}
]

#Raggruppa i nomi per club (dizionario club → lista calciatori)

club_calciatori = {}

for calciatore in calciatori:
    appartenenza = calciatore["club"]
    nomi = calciatore["nome"]
    segnature = calciatore["goal"]
    if appartenenza not in club_calciatori:
        club_calciatori[appartenenza] = []
    club_calciatori[appartenenza].append((nomi, segnature))


for club, giocatore in club_calciatori.items():
    print(f"Calciatori per Club: {club:<22} Giocatore: {giocatore} ")

print("="*100)

#Goal per nazionalita'

nazionalità_giocatori = {}

for calciatore in calciatori:
    nazione = calciatore["nazionalita"]
    nomi = calciatore["nome"]
    segnature = calciatore["goal"]
    if nazione not in nazionalità_giocatori:
        nazionalità_giocatori[nazione] =[]
    nazionalità_giocatori[nazione].append(segnature)

for nazio, segn in nazionalità_giocatori.items():
    print(f" Lista goal per Nazionalità: {nazio:<20} Goal: {segn}")
print("="*100)
lista_ordinata = sorted(calciatori, key=lambda x:x["goal"], reverse=True)

lista_semplice = [(a["nazionalita"], a["goal"]) for a in lista_ordinata]

for nazio, segn in lista_semplice:
    print(f"Lista ordinata Goal per nazionalità: {nazio:<15} Goal: {segn}")
media_goal= {}

#for naz, media in lista_semplice:



print("="*100)


#Calciatore con più assist (nome e assist)
assist_per_calciatore = {}
asset_max = 0
calciatore_asset_max = ""

for calciatore in calciatori:
    passaggi = calciatore["assist"]
    nomi = calciatore["nome"]
    if passaggi not in assist_per_calciatore:
        assist_per_calciatore[passaggi] = []
    assist_per_calciatore[passaggi].append(nomi)


for calciatore, assist in assist_per_calciatore.items():
    print(f"Assist per Calciatore: {calciatore} {assist}")
print("="*100)
for passaggi, nome in assist_per_calciatore.items():
    if passaggi > asset_max:
         asset_max = passaggi
         calciatore_asset_max = nome
print(f"Calciatore piu' assist: {calciatore_asset_max} Assist: {asset_max}")


#Calcola media goal per club

#Ordina i calciatori per goal (decrescente) (lista con solo nome e goal)
print("="*80)
Goal_calciatore = {}
for calciatore in calciatori:
    nomi = calciatore["nome"]
    segnature = calciatore["goal"]
    #print(f"Nome Calciatore  {nomi:<15}  Goal:{segnature}")

lista_goal_ord = sorted(calciatori, key=lambda x:x["goal"], reverse=True)
lista_semplificata = [(a["nome"], a["goal"]) for a in lista_goal_ord]
#print(lista_semplificata)

for nome, goal in lista_semplificata:
    print(f"Lista Goals Ord x Calciatore: {nome:<20} Goals: {goal}")

print("="*80)

#Filtra i calciatori con goal > 200 (lista di nomi)

calciatore_sopra_duecento_goal = {}

for calciatore in calciatori:
    nom = calciatore["nome"]
    segno = calciatore["goal"]
    if segno > 200:
        calciatore_sopra_duecento_goal[segno]= []
        calciatore_sopra_duecento_goal[segno].append(nom)
print(calciatore_sopra_duecento_goal)
print("="*80)
#media goals per club

lista_club_goal = [(c["club"], c["goal"]) for c in calciatori]
# 1. Raggruppa goal per club (dal punto 1)
goal_per_club = {}

for calciatore in calciatori:
    club = calciatore["club"]
    goal = calciatore["goal"]

    if club not in goal_per_club:
        goal_per_club[club] = []
    goal_per_club[club].append(goal)

# 2. Calcola e stampa le medie
print("Media goal per club:")
for club, lista_goal in goal_per_club.items():
    media = sum(lista_goal) / len(lista_goal)
    print(f"{club:<20} {media:.1f} goal")
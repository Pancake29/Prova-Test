giocatori = [
    {"nome": "Messi", "ruolo": "attaccante", "goal": 672, "assist": 268, "partite": 700},
    {"nome": "Ronaldo", "ruolo": "attaccante", "goal": 701, "assist": 220, "partite": 800},
    {"nome": "Neymar", "ruolo": "attaccante", "goal": 136, "assist": 120, "partite": 400},
    {"nome": "Mbappé", "ruolo": "attaccante", "goal": 180, "assist": 95, "partite": 300},
    {"nome": "Haaland", "ruolo": "attaccante", "goal": 150, "assist": 40, "partite": 250},
    {"nome": "Lewandowski", "ruolo": "attaccante", "goal": 512, "assist": 120, "partite": 600},
    {"nome": "De Bruyne", "ruolo": "centrocampista", "goal": 90, "assist": 180, "partite": 500},
    {"nome": "Salah", "ruolo": "attaccante", "goal": 200, "assist": 110, "partite": 400},
    {"nome": "Modric", "ruolo": "centrocampista", "goal": 70, "assist": 130, "partite": 600},
    {"nome": "Kanté", "ruolo": "centrocampista", "goal": 30, "assist": 50, "partite": 450},
    {"nome": "Van Dijk", "ruolo": "difensore", "goal": 20, "assist": 15, "partite": 350},
    {"nome": "Chiellini", "ruolo": "difensore", "goal": 25, "assist": 10, "partite": 500},
]
print('-------------------------------------------')
print('Raggruppa i nomi dei giocatori per ruolo(ruolo_giocatore={})')
print('-------------------------------------------')
ruolo_giocatore = {}

for giocatore in giocatori:
    impiego = giocatore["ruolo"]
    nomi = giocatore["nome"]
    segnatura = giocatore["goal"]
    if impiego not in ruolo_giocatore:
        ruolo_giocatore[impiego] = []
    ruolo_giocatore[impiego].append(nomi)
    ruolo_giocatore[impiego].append(segnatura)

for ruoli, nomi in ruolo_giocatore.items():
    print(f"Ruolo: {ruoli:<15} Nome Giocatore: {nomi} ")
print('--------------------------------------------------------------')
print('Calcola media da ruolo_giocatore')
print('--------------------------------------------------------------')
for ruolo, lista_mista in ruolo_giocatore.items():
    goals = lista_mista[1::2]          # estrae solo i goal
    media = sum(goals) / len(goals)
    print(f"Ruolo giocatore: {ruolo}: Media goals per ruolo: {media:.2f}")

print("="*75)

print('Calcola la media goal per ruolo con nuovo ciclo')
print('-------------------------------------------------------------')
goal_ruolo = {}

for player in giocatori:
    ruoli = player["ruolo"]
    goals = player["goal"]
    if ruoli  not in goal_ruolo:
        goal_ruolo[ruoli]= []
    goal_ruolo[ruoli].append(goals)


media_per_ruolo = {}

for ruolo, lista_goal in goal_ruolo.items():
    media_per_ruolo[ruolo] = sum(lista_goal) / len(lista_goal)

media_arrotondata = {ruolo: round(media, 2) for ruolo, media in media_per_ruolo.items()}
print(media_arrotondata)


print("="*75)
print('Trova il giocatore con più goal Se c’è ex aequo, devono essere restituiti tutti')


lista_goal = sorted(giocatori, key=lambda x:x["goal"], reverse=True)
lista_goal_semplificata = [(a["nome"], a["goal"])for a in lista_goal]

print( lista_goal_semplificata)

max_goal_giocatore = []
goal_max = 0


for nome, goal in lista_goal_semplificata:
    if goal > goal_max:
            goal_max = goal
            max_goal_giocatore = [nome]
    elif goal == goal_max:
        max_goal_giocatore.append(nome)

print(f"Giocatori con max goal ({goal_max}): {max_goal_giocatore}")


print("="*75)
print('Trova il giocatore con meno goal Se c’è ex aequo, devono essere restituiti tutti')
min_goal_giocatore = []
goal_min = 1000


for nome, goal in lista_goal_semplificata:
    if goal < goal_min:
            goal_min = goal
            min_goal_giocatore = [nome]
    elif goal == goal_min:
        min_goal_giocatore.append(nome)

print(f"Giocatori con min goal ({goal_min}): {min_goal_giocatore}")

print("="*75)
print('Filtra i giocatori con goal più 150')

più_150_goal = []

for nome, goal in lista_goal_semplificata:
    if goal > 150:
        più_150_goal = [(nome, goal)]
        print(f"Nome: {nome:<25} Numero goal: {goal}")

print("="*75)
print('Ordina i giocatori per goal decrescente Output: lista di tuple (nome, goal)')

lista_goal_semplificata = [(a["nome"], a["goal"])for a in lista_goal]

#print( lista_goal_semplificata)

for nome, goal in lista_goal_semplificata:
    print(f"Nome giocatore: {nome:<20} Numero goal: {goal}")


print("="*75)
print('Trova i ruoli con più giocatori Output: [ruolo1, ruolo2, ...] (tutti quelli col massimo')

print('PRIMO METODO')
max_giocatore = 0
ruoli_max = []

for ruoli, lista in ruolo_giocatore.items():
    numero_giocatori = len(lista) // 2
    if numero_giocatori > max_giocatore:
        max_giocatore = numero_giocatori
        ruoli_max = [ruoli]
    elif numero_giocatori == max_giocatore:
        ruoli_max.append(ruoli)

print(f"{ruoli_max} {max_giocatore}")

print('SECONDO METODO')#SECONDO METODO

lista_gio_ruolo = [(a["ruolo"], a["nome"])for a in lista_goal]

ruolo_gio = []
giocatore_per_ruolo = {}

for ruolo, nome in lista_gio_ruolo:
    if ruolo not in giocatore_per_ruolo:
        giocatore_per_ruolo[ruolo] = []
    giocatore_per_ruolo[ruolo].append(nome)
print(f"{giocatore_per_ruolo}")

max_giocatore = 0
ruoli_max = []

for ruoli, lista_giocat in giocatore_per_ruolo.items():
    if len(lista_giocat) > max_giocatore:
        max_giocatore = len(lista_giocat)
        ruoli_max = [ruoli]
    elif len(lista_giocat) == max_giocatore:
        ruoli_max.append(ruoli)
print(f"{ruoli_max} {max_giocatore} ")



print("="*75)
print('GOAL PER PARTITA (media) Aggiungi un campo goal_partita = goal / partite (arrotondato)')



lista_goal_partita = [(a["nome"], a["goal"], a["partite"])for a in lista_goal]
for nome, gol, partite in lista_goal_partita:

    media = gol / partite
    print(f" Goal per partita: {nome:<12} {media:.2f}")


print("="*75)
print('Trova il giocatore con miglior media goal/partita Ex aequo? Devono essere restituiti tutti')
max_media_goal_par = 0
migliori_media = []

lista_media_semplificata = [(a["nome"], a["goal"], a["partite"])for a in lista_goal]
for nome, goal, partite in lista_media_semplificata:
    media = goal / partite

    if media > max_media_goal_par:
        max_media_goal_par = media
        migliori_media = nome
    elif media == max_media_goal_par:
        migliori_media.append(nome)
print(f"Migliore giocatore media partita: {migliori_media} media: {max_media_goal_par:.2f}")

print("="*75)
print('Trova il giocatore con più assist Ex aequo? Devono essere restituiti tutti')


lista_assist_semplificata = [(a["nome"], a["assist"])for a in lista_goal]
max_assist = 0
migliore_assist = []

for nome, assist in lista_assist_semplificata:
    if assist > max_assist:
        max_assist = assist
        migliore_assist = nome
    elif assist == max_assist:
        migliore_assist.append(nome)
print(f"Giocatore max assist: {migliore_assist} Numero assist: {max_assist}")






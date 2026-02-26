recensioni = [
    {"nome": "Da Gigi", "cucina": "Italiana", "città": "Roma", "stelle": 4, "prezzo_medio": 45, "recensioni": 1200},
    {"nome": "Sakura", "cucina": "Giapponese", "città": "Milano", "stelle": 5, "prezzo_medio": 80, "recensioni": 800},
    {"nome": "El Fogon", "cucina": "Messicana", "città": "Roma", "stelle": 3, "prezzo_medio": 30, "recensioni": 450},
    {"nome": "Le Jardin", "cucina": "Francese", "città": "Firenze", "stelle": 5, "prezzo_medio": 120, "recensioni": 600},
    {"nome": "Curry House", "cucina": "Indiana", "città": "Milano", "stelle": 4, "prezzo_medio": 25, "recensioni": 300},
    {"nome": "Osteria Vecchia", "cucina": "Italiana", "città": "Bologna", "stelle": 4, "prezzo_medio": 38, "recensioni": 950},
    {"nome": "La Torre", "cucina": "Italiana", "città": "Firenze", "stelle": 4, "prezzo_medio": 65, "recensioni": 720},
    {"nome": "Sushi Time", "cucina": "Giapponese", "città": "Napoli", "stelle": 3, "prezzo_medio": 22, "recensioni": 500},
    {"nome": "Trattoria Roma", "cucina": "Italiana", "città": "Roma", "stelle": 4, "prezzo_medio": 35, "recensioni": 1100},
    {"nome": "Burger House", "cucina": "Fast Food", "città": "Milano", "stelle": 3, "prezzo_medio": 15, "recensioni": 2000}
]

print('--------------------------------------------------------')
print('Raggruppa i nomi dei ristoranti per città ')
print('--------------------------------------------------------')
città_ristorante = {}
for recensione  in recensioni:
    luogo = recensione ["città"]
    nomi = recensione["nome"]
    if luogo not in città_ristorante:
        città_ristorante[luogo] = []
    città_ristorante[luogo].append(nomi)
print(f"Ristorante per città: {città_ristorante}")

print('==========================================================')
print('Calcola la media delle stelle per ogni tipo di cucina ')
print('----------------------------------------------------------')

recensioni_cucina = {}

for cucina in recensioni:
    cucine = cucina["cucina"]
    stars = cucina["stelle"]
    if cucine not in recensioni_cucina:
        recensioni_cucina[cucine] = []
    recensioni_cucina[cucine].append(stars)


media_stelle_per_cucine = {}

for cucine, lista_stella in recensioni_cucina.items():
    media_stelle_per_cucine[cucine] = sum(lista_stella) / len(lista_stella)

media_arrotondata = {cucine: round(media, 2) for cucine, media in media_stelle_per_cucine.items()}
print(media_arrotondata)




print('======================================================')
print('Trova il ristorante con più recensioni (gestisci ex-aequo) Output: lista di tuple /'
      '[(nome, recensioni)')
print('-------------------------------------------')
lista_ord_recensioni = sorted(recensioni, key=lambda x:x["recensioni"], reverse=True)
lista_ord_recen_semplice = [(a["nome"], a["recensioni"])for a in lista_ord_recensioni]
recens_max = 0
ristorante_max = []

for nome, recens in lista_ord_recen_semplice:
    if recens > recens_max:
        recens_max = recens
        ristorante_max = [nome]
    elif recens == recens_max:
        ristorante_max.append(nome)
print(f"Ristorante recensione max: {ristorante_max} {recens_max}")



print('========================================================')
print('Ordina i ristoranti per prezzo medio dal più caro al più economico Output: lista di tuple '
      '(nome, prezzo')
print('-------------------------------------------')

lista_ord_prezzo_semplice = [(a["nome"], a["prezzo_medio"])for a in lista_ord_recensioni]
ordinata = sorted(lista_ord_prezzo_semplice, key= lambda x:x[1], reverse= True)
print(f"Prezzo medio ristorante : {ordinata}")






print('========================================================')
print('Filtra i ristoranti con stelle ≥ 4 Output: lista di nomi')
print('-------------------------------------------')

lista_ord_stelle = sorted(recensioni, key=lambda x:x["stelle"], reverse=True)
lista_stelle_semplice = [(a["nome"], a["stelle"])for a in lista_ord_stelle]
# I METODO (non salva la lista in quanto ad ogni ciclo soprappone l'ultimo stampandolo nel ciclo/
# riporta tutto, fuori ciclo darebbe solo l'ultimo
rist_stelle_supeuguali4 = []

for nome, stella in lista_stelle_semplice:
    if stella >= 4:
        rist_stelle_supeuguali4 = [(nome, stella)]
        print(f"Ristorante: {nome:<19} Numero Stelle {stella}")
print('-----------------------------------------------------------')
#II METODO (salva la lista che posso riusare
rist_stelle_supeugua4 = []
for nome, stella in lista_stelle_semplice:
    if stella >= 4:
        rist_stelle_supeugua4.append((nome, stella))

print("Lista completa:", rist_stelle_supeugua4)
print("Lista completa:", len(rist_stelle_supeugua4)) #Len lo posso mettere nel print e mi da il numero/
                                                     #assoluto dei ristoranti con >=4 stelle
nomi_solo = [nome for nome, stella in rist_stelle_supeugua4] #Stampa solo i nomi senza stelle


print('========================================================')
print('Calcola il prezzo medio per ogni città Output: {"Roma": 38.3, "Milano": 40.0, ...}')
print('-------------------------------------------')


lista_ord_città = sorted(recensioni, key=lambda x:x["città"], reverse=True)
lista_città_prezzi = [(a["città"], a["prezzo_medio"]) for a in lista_ord_città]
#print(lista_città_prezzi)

dizionario_città_prezzo = {}

for città, prezzi in lista_città_prezzi:
    if città not in dizionario_città_prezzo:
        dizionario_città_prezzo[città] = []
    dizionario_città_prezzo[città].append(prezzi)
#print(dizionario_città)

for città, lista_prezzi in dizionario_città_prezzo.items():
    prezzo_medio = sum(lista_prezzi) / len(lista_prezzi)

    print(f"Città: { città:<15} Prezzo Medio €: {prezzo_medio:.2f}")






print('========================================================')
print('Trova la/e città con il maggior numero di ristoranti Output: lista di città')
print('-------------------------------------------')

città_max_rist = []
max_rist = 0

for città, lista_rist in città_ristorante.items():
    if len(lista_rist) > max_rist:
        max_rist = len(lista_rist)
        città_max_rist = [città]
    elif len(lista_rist) == max_rist:
        città_max_rist.append(città)

print(f" Città {città_max_rist} Numero ristoranti: {max_rist}")

print('========================================================')
print('Per ogni ristorante, calcola il rapporto stelle / prezzo_medio Trova il/i ristoranti con il /'
      'rapporto più alto Output: lista di tuple (nome, rapporto)')
print('-------------------------------------------')
max_rapporto = 0
migliori_ristoranti = []

dati_ristoranti = [(r["nome"], r["stelle"], r["prezzo_medio"]) for r in recensioni]
for r in recensioni:
    rapporto = r["stelle"] / r["prezzo_medio"]
    if rapporto > max_rapporto:
        max_rapporto = rapporto
        migliori_ristoranti = [nome]
    elif rapporto == max_rapporto:
        migliori_ristoranti.append(nome)
print(f"Nome Risorante: {migliori_ristoranti} Rapporto N. {rapporto}")


print('========================================================')
print('Calcola la media delle recensioni generale Trova i ristoranti con recensioni > media /'
      ' Output: lista di nomi')
print('-------------------------------------------')





print('-------------------------------------------')
print('Trova la cucina con il prezzo medio più alto Gestisci eventuali ex-aequo / '
       'Output: {"cucina": prezzo} (o lista di tuple)')
print('-------------------------------------------')
px_max = 0
rist_px_max = []
lista_ord_prezzo_semplice = [(a["cucina"], a["prezzo_medio"])for a in lista_ord_recensioni]
lista_ordinata_px = sorted(lista_ord_prezzo_semplice, key= lambda x:x[1], reverse= True)

for nome,  prezzo in lista_ordinata_px:
    if prezzo > px_max:
        px_max = prezzo
        rist_px_max = [nome]
    elif prezzo == px_max:
        rist_px_max.append(nome)
print(f"Nome Cucina {rist_px_max} Prezzo {px_max}")


prezzi_cucina = {}

for cucina in recensioni:
    cucine = cucina["cucina"]
    prezzo = cucina["prezzo_medio"]
    if cucine not in prezzi_cucina:
        prezzi_cucina[cucine] = []
    prezzi_cucina[cucine].append(prezzo)
print(prezzi_cucina)
px_medio = 0
cucine_px_medio = []

prezzo_max = 0
cucine_px_max = []
for nome,  lista_prezzo in prezzi_cucina.items():
    prezzo_medio = sum(lista_prezzo) / len(lista_prezzo)
    if prezzo_medio > prezzo_max:
       prezzo_max = prezzo_medio
       cucine_px_max = [nome]
    elif prezzo_medio == prezzo_max:
        cucine_px_max.append(nome)
print(f"Nome Cucina {cucine_px_max} Prezzo {prezzo_max}")


automobili = [
    {"marca": "Fiat", "modello": "Panda", "anno": 2020, "prezzo": 15000, "alimentazione": "benzina"},
    {"marca": "Fiat", "modello": "500", "anno": 2021, "prezzo": 18000, "alimentazione": "ibrida"},
    {"marca": "Ford", "modello": "Fiesta", "anno": 2020, "prezzo": 17000, "alimentazione": "benzina"},
    {"marca": "Ford", "modello": "Focus", "anno": 2022, "prezzo": 22000, "alimentazione": "diesel"},
    {"marca": "Toyota", "modello": "Yaris", "anno": 2021, "prezzo": 20000, "alimentazione": "ibrida"},
    {"marca": "Toyota", "modello": "Corolla", "anno": 2022, "prezzo": 30000, "alimentazione": "ibrida"},
    {"marca": "Volkswagen", "modello": "Golf", "anno": 2021, "prezzo": 23000, "alimentazione": "diesel"},
    {"marca": "Volkswagen", "modello": "Polo", "anno": 2020, "prezzo": 19000, "alimentazione": "benzina"},
    {"marca": "Fiat", "modello": "Panda", "anno": 2022, "prezzo": 16000, "alimentazione": "benzina"},
    {"marca": "Ford", "modello": "Kuga", "anno": 2023, "prezzo": 30000, "alimentazione": "ibrida"}
]



#Raggruppa i modelli per marca (dizionario marca → lista modelli)
marca_auto = {}

for automobile in automobili:
    brand = automobile["marca"]
    tipi = automobile["modello"]
    costo = automobile["prezzo"]
    if brand not in marca_auto:
        marca_auto[brand] = []
    marca_auto[brand].append((tipi, costo))

print(f"\nRaggruppa i modelli per marca (dizionario marca → lista modelli)")
for bran, lista_tuple in marca_auto.items():

    print(f"Marca Auto:{bran:<15} Modello: {lista_tuple}")

print("="*75)

#Prezzo medio per marca (dizionario marca → prezzo medio)
print(f"\nPrezzo medio per marca (dizionario marca → prezzo medio))")
for bran, lista_tuple in marca_auto.items():
    prezzi = []
    for marchi, costi in lista_tuple:
        prezzi.append(costi)
    media = sum(prezzi) / len(prezzi)
    print(f"Brand: {bran:<15}: prezzo medio {media:.1f}€")

print("="*75)



lista_per_prezzo = sorted(automobili, key = lambda x:x["prezzo"], reverse=True)
lista_px_mod = [(a["prezzo"], a["modello"]) for a in lista_per_prezzo]

for costo, mod in lista_px_mod:
    print(f"Prezzo Auto: {costo:<13} Modello auto: {mod}")

print("=" * 75)
print(f"\nAuto per prezzo  (modello e prezzo) — gestisci eventuali ex-aequo))")
dizionario_modelli = {modello: prezzo for prezzo, modello in lista_px_mod}
for pre, mode in dizionario_modelli.items():
    print(f"Modello: {pre:<12} Prezzo: {mode}")

print("="*75)
print(f"\nAuto con prezzo massimo (modello e prezzo) — gestisci eventuali ex-aequo))")
prezzo_max = 0

prezzo_max = max(dizionario_modelli.values())
modelli_max = [modello for modello, prezzo in dizionario_modelli.items() if prezzo == prezzo_max]
print(f"Prezzo {prezzo_max:<10} Modelli: {modelli_max}")
print("="*75)

#Ordina le auto per anno (crescente) (lista con solo modello e anno)

anno_auto = {}
print(f"\nOrdina le auto per anno (crescente) (lista con solo modello e anno)))")
for auto in automobili:
    anni = auto["anno"]
    tipo = auto["modello"]
    if anni not in anno_auto:
        anno_auto[anni] = []
    anno_auto[anni].append(tipo)


for anno, mod in anno_auto.items():
    print(f"Anno: {anno} Modello {mod}")

print("="*75)

#Filtra le auto con alimentazione "ibrida" (lista di modelli)

aliment = {}
print(f"\nLista le auto per alimentazione  (lista di modelli)")

for mezzi in automobili:
    alimento = mezzi["alimentazione"]
    modelli = mezzi["modello"]
    if alimento not in aliment:
        aliment[alimento] = []
    aliment[alimento].append(modelli)



for carb, modello in aliment.items():
    print(f"Alimentazione: {carb:<12}  {modello}")

print("="*75)

print(f"\nFiltra le auto con alimentazione ibrida (lista di modelli)")
print(f"Auto ibride: {aliment['ibrida']}")



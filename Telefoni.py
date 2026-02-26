telefoni = [
    {"marca": "Samsung", "modello": "Galaxy S23", "ram_gb": 8, "prezzo": 899, "anno": 2023},
    {"marca": "Apple", "modello": "iPhone 14", "ram_gb": 6, "prezzo": 999, "anno": 2022},
    {"marca": "Xiaomi", "modello": "Redmi Note 12", "ram_gb": 6, "prezzo": 299, "anno": 2022},
    {"marca": "Samsung", "modello": "Galaxy A54", "ram_gb": 6, "prezzo": 399, "anno": 2023},
    {"marca": "Apple", "modello": "iPhone 13", "ram_gb": 4, "prezzo": 699, "anno": 2021},
    {"marca": "OnePlus", "modello": "Nord 3", "ram_gb": 8, "prezzo": 449, "anno": 2023},
    {"marca": "Google", "modello": "Pixel 7", "ram_gb": 8, "prezzo": 649, "anno": 2022},
    {"marca": "Samsung", "modello": "Galaxy Z Flip", "ram_gb": 8, "prezzo": 1099, "anno": 2023}
]
#Compiti:
#Raggruppa i modelli per marca (dizionario marca → lista modelli)

telef_per_marca = {}

for telefono in telefoni:
    brand = telefono["marca"]
    mod = telefono["modello"]
    costo = telefono["prezzo"]
    if brand not in telef_per_marca:
        telef_per_marca[brand] = []
    telef_per_marca[brand].append((mod, costo))



for marca, lista_tuple in telef_per_marca.items():
    print(f"{marca}: {lista_tuple}")

print("="*75)

#Prezzo medio per marca (dizionario marca → prezzo medio)
# Per ogni marca, estrai i prezzi dalle tuple
for marca, lista_tuple in telef_per_marca.items():
    # lista_tuple = [('Galaxy S23', 899), ('Galaxy A54', 399), ...]

    #prezzi = [prezzo for modello, prezzo in lista_tuple]  # list comprehension
    # oppure
    prezzi = []
    for modello, prezzi in lista_tuple:
        prezzi.append(prezzi)

    media = sum(prezzi) / len(prezzi)
print(f"Brand: {marca:<15}: prezzo medio {media:.1f}€")

print("="*75)

#Telefono con RAM maggiore (nome modello e quantità RAM)

ram_phone = {}
ram_phone_max = []
max_ram = 0

for telefono in telefoni:
    ram = telefono["ram_gb"]
    mod = telefono["modello"]
    if ram not in ram_phone:
        ram_phone[ram] = []
    ram_phone[ram].append(mod)


for ramgb, lista_mod in ram_phone.items():
    print(f"Ram GB: {ramgb} {lista_mod}")

print("="*75)

max_ram = max(ram_phone.keys())
modelli_max = ram_phone[max_ram]
print(f"Ram GB {max_ram:<10} Modelli: {modelli_max}")

print("="*75)


#Ordina i telefoni per prezzo (crescente) (lista con solo modello e prezzo)


ordina_lista = sorted(telefoni,key=lambda x: x["prezzo"],reverse=False)


lista_semplice = [(a["modello"], a["prezzo"]) for a in ordina_lista]

for mod, px in lista_semplice:
    print(f"Modello: {mod:<15}  Prezzo: {px} ")


print("="*75)
#Filtra i telefoni con prezzo < 500 (lista di modelli)
mod_inf_500 = []

for modello, pz in lista_semplice:
    if pz < 500:
        mod_inf_500.append(modello)
        print(f"Modelli inferiori 500 €:{modello:<15} Prezzo €: {pz} ")



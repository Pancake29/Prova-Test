# Dizionario con liste
dati = {
    "frutta": ["mela", "pera", "banana"],
    "verdura": ["carota", "sedano"],
    "bevande": ["acqua", "vino", "birra", "succo"]
}

# Voglio trovare la categoria con più elementi
categoria_max = []      # parto con stringa vuota
lunghezza_max = 0

for categoria, lista in dati.items():
    if len(lista) > lunghezza_max:
        lunghezza_max = len(lista)
        categoria_max = categoria   # qui assegno una stringa

print(f"La categoria con più elementi è {categoria_max} con {lunghezza_max} elementi")
# Output: La categoria con più elementi è bevande con 4 elementi

dati = {
    "frutta": ["mela", "pera", "banana", "ananas"],
    "verdura": ["carota", "sedano"],
    "bevande": ["acqua", "vino", "birra", "succo"]
}

fruttivendolo_max = []    # lista vuota
lunghezza_max = 0

for categoria, lista in dati.items():
    if len(lista) > lunghezza_max:
        lunghezza_max = len(lista)
        fruttivendolo_max = [categoria]      # nuova lista con questa categoria
    elif len(lista) == lunghezza_max:
        fruttivendolo_max.append(categoria)  # aggiungi alla lista esistente

# Se frutta e bevande hanno entrambe 4, avrai ["frutta", "bevande"]
print(f"La categoria con più elementi è {fruttivendolo_max} con {lunghezza_max} elementi")

dati = {
    "frutta": ["mela", "pera", "banana", "ananas"],
    "verdura": ["carota", "sedano"],
    "bevande": ["acqua", "vino", "birra", "succo"]
}

#categoria_max = []    # lista vuota
lunghezza_max = 0

for categoria, lista in dati.items():
    if len(lista) > lunghezza_max:
        lunghezza_max = len(lista)
        categoria_max = [categoria]      # nuova lista con questa categoria
    elif len(lista) == lunghezza_max:
        categoria_max.append(categoria)  # aggiungi alla lista esistente

# Se frutta e bevande hanno entrambe 4, avrai ["frutta", "bevande"]
print(f"La categoria con più elementi è {categoria_max} con {lunghezza_max} elementi")
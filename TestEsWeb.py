# Dizionario con liste
dati = {
    "chiave1": [1, 2, 3],
    "chiave2": [4, 5],
    "chiave3": [6, 7, 8, 9],
    "chiave4": [6, 7, 8, 9]
}


# 1. Ottenere la lunghezza di una specifica chiave
lunghezza_chiavi = len(dati)
print(f"Lunghezza chiavi: {lunghezza_chiavi}") # Output: 3

# 2. Ottenere il conteggio di tutti i valori (dict comprehension)
conteggio_valori = {chiave: len(v) for chiave, v in dati.items()}
print(conteggio_valori) # Output: {'chiave1': 3, 'chiave2': 2, 'chiave3': 4}

for chiave, valori in dati.items():
    print(f" {chiave} {valori}")

print("="*70)

lista_uno = [1, 2, 3]
lista_due = [3, 1, 4]

mix = []

for x in lista_uno:
    for y in lista_due:
        if x != y:
            mix.append((x, y))

print(mix)
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

mix = [(x, y) for x in lista_uno for y in lista_due if x != y]

print(mix)
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
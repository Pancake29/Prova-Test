registro = {
    "Classe A": [80, 90, 75],
    "Classe B": [60, 70, 85]
}

# Tuple Unpacking: itera su chiave (k) e lista valori (v)
for classe, voti in registro.items():
    print(f"Analisi {classe}:")
    # Qui stiamo unpackando la lista 'voti'
    for voto in voti:
        print(f" - Voto: {voto}")

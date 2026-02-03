casa = [1, 2, 3]
for elemento in casa:  # Nome diverso!
        print(elemento)
        print(casa)
casa = [1, 2, 3]          # 1. casa è una LISTA
print(casa)               # Output: [1, 2, 3]

for casa in casa:         # 2. casa diventa PRIMA 1, POI 2, POI 3
    print("Dentro:", casa) # Stampa: 1, 2, 3

    print("Dopo:", casa)      # 3. Ora casa = 3 (numero), NON la lista!
# casa è 3, non [1,2,3]!
# Se provi: casa.append(4) → ERRORE! (3 è numero, non lista)
casa = [1,2,3]
pietra = 4*2
casa = pietra
print(casa)
a = [1, 2, 3]  # Fotocopia 1
c = a          # NON è una fotocopia! È dire: "c punta alla FOTOCOPIA 1"

print(f"a is c? {a is c}")           # True (stesso oggetto)
print(f"id(a) == id(c)? {id(a) == id(c)}")  # True (stesso indirizzo)

a.append(4)    # Scrivi su fotocopia 1
print(c)       # [1, 2, 3, 4] ← Anche c è cambiato!


# ESEMPIO 1: LEN (BUILT-IN) vs APPEND (METODO)
mia_lista = [1, 2, 3]

# BUILT-IN: len() - Funziona su MOLTI tipi (liste, stringhe, ecc.)
print(len(mia_lista))      # Built-in: 3
print(len("ciao"))         # Built-in: 4 (funziona anche sulle stringhe!)

# METODO: .append() - Funziona SOLO sulle liste
mia_lista.append(4)        # Metodo SPECIFICO delle liste
print(mia_lista)           # [1, 2, 3, 4]

# "ciao".append("!")       # ERRORE! Le stringhe non hanno .append()


# 1. METODO che CREA nuovo oggetto (non modifica)
lista = [1, 2, 3]
nuova_lista = lista.copy()      # METODO .copy() → CREA nuovo oggetto
print(id(lista) == id(nuova_lista))  # False → Sono OGGETTI DIVERSI

# 2. BUILT-IN che MODIFICA? (In realtà no, restituisce nuovo)
stringa = "ciao"
maiuscola = str.upper(stringa)  # Equivalente a stringa.upper()
print(stringa)                  # "ciao" ← ORIGINALE INTATTA
print(maiuscola)                # "CIAO" ← NUOVO oggetto
libri = [
    {"titolo": "Il Nome della Rosa", "autore": "Umberto Eco", "anno": 1980, "genere": "giallo storico", "prestito": True},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "genere": "distopico", "prestito": False},
    {"titolo": "Il Piccolo Principe", "autore": "Antoine de Saint-Exupéry", "anno": 1943, "genere": "favola", "prestito": True},
    {"titolo": "Se questo è un uomo", "autore": "Primo Levi", "anno": 1947, "genere": "memorialistica", "prestito": False},
    {"titolo": "La Coscienza di Zeno", "autore": "Italo Svevo", "anno": 1923, "genere": "romanzo psicologico", "prestito": True}
]
#STEP 1: CONTATORI BASE
#Quanti libri sono attualmente in prestito (prestito: True)?

#Quanti libri sono stati pubblicati prima del 1950?
libri_in_prestito = 0

for i in libri:
    if i["prestito"] == True:
        libri_in_prestito += 1
        print(i ["titolo"])

print(f"Totale libri in prestito: {libri_in_prestito}")

anno_pubblicazione = 0

for libro in libri:
    if libro["anno"] < 1950:
        anno_pubblicazione += 1
        print(f" {libro["titolo"]} {libro ["anno"]}")

libri_per_genere = {}  # Dizionario vuoto

for libro in libri:
    genere = libro["genere"]  # "giallo storico"
    titolo = libro["titolo"]  # "Il Nome della Rosa"

    if genere not in libri_per_genere:  # Se genere NON c'è
        libri_per_genere[genere] = []  # Crea LISTA VUOTA

    # SEMPRE (con o senza if):
    libri_per_genere[genere].append(titolo)  # Aggiungi titolo alla lista

print(libri_per_genere)


for genere, titoli in libri_per_genere.items():
    print(genere + ":")
    for titolo in titoli:
        print("  • " + titolo)
    print()  # linea vuota



# Trova l'indice MANUALMENTE per debug
indice_1984 = None
for i, libro in enumerate(libri):
    if libro["titolo"] == "1984":
        indice_1984 = i
        break

print(f"Indice di '1984': {indice_1984}")

for i in range(len(libri)):
    if libri[i]["titolo"] == "1984":
        libri[i]["prestito"] = not libri[i]["prestito"]  # ✅ CORRETTO
        print(libri)
# COPIA E INCOLLA QUESTO ESATTO CODICE:

# Modifica DIRETTA
if indice_1984 is not None:
    print(f"Prima: {libri[indice_1984]['prestito']}")
    libri[indice_1984]["prestito"] = False  # Forza a False
    print(f"Dopo: {libri[indice_1984]['prestito']}")
print(libri)

# 1. PRIMA tutto il tuo codice esistente...

# 2. POI, DOPO i cicli ma PRIMA di STEP 5:
nuovo_libro = {
    "titolo": "Il barone rampante",
    "autore": "Italo Calvino",
    "anno": 1957,
    "genere": "romanzo",
    "prestito": False
}

libri.append(nuovo_libro)  # UNA volta sola
print(f"Aggiunto: {nuovo_libro['titolo']}")
print(f"Totale libri: {len(libri)}")  # Dovrebbe essere 6

anno_piu_antico = libri[0]["anno"]  # Prendi il primo come riferimento

for libro in libri:
    if libro["anno"] < anno_piu_antico:
        anno_piu_antico = libro["anno"]

print(f"Anno di pubblicazione più antico: {anno_piu_antico}")


for libro in libri:
    print( "titolo: " + libro["titolo"])
    print( "autore: " + libro["autore"])
    print( "anno: " + str(libro["anno"]))    # anno è numero, converti in stringa
    print("genere: " + libro["genere"])
    print( "prestito: " + str(libro["prestito"]))  # prestito è booleano
    print( "" ) # linea vuota
    #print(libri)
print(f"Verifica: lista ora ha {len(libri)} libri")



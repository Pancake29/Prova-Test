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

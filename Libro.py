libri = [
    {"titolo": "Il Nome della Rosa", "autore": "Umberto Eco", "anno": 1980, "genere": "giallo storico", "prestito": True},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1955, "genere": "distopico", "prestito": False},
    {"titolo": "Il Piccolo Principe", "autore": "Antoine de Saint-Exupéry", "anno": 1943, "genere": "favola", "prestito": True},
    {"titolo": "Se questo è un uomo", "autore": "Primo Levi", "anno": 1947, "genere": "memorialistica", "prestito": False},
    {"titolo": "La Coscienza di Zeno", "autore": "Italo Svevo", "anno": 1923, "genere": "romanzo psicologico", "prestito": True}
]
genere = []



for libro in libri:
    if libro["anno"] < 1950:  # Condizione su un campo del dizionario
        print(libro["titolo"])


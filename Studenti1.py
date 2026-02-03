studenti = [
    {
        "nome": "Mario",
        "cognome": "Rossi",
        "voti": [
            {"materia": "Matematica", "voto": 28, "crediti": 6},
            {"materia": "Fisica", "voto": 25, "crediti": 8},
            {"materia": "Informatica", "voto": 27, "crediti": 10}
        ]
    },
    {
        "nome": "Luisa",
        "cognome": "Verdi",
        "voti": [
            {"materia": "Matematica", "voto": 30, "crediti": 6},
            {"materia": "Informatica", "voto": 29, "crediti": 10},
            {"materia": "Statistica", "voto": 26, "crediti": 6}
        ]
    },
    {
        "nome": "Anna",
        "cognome": "Bianchi",
        "voti": [
            {"materia": "Fisica", "voto": 24, "crediti": 8},
            {"materia": "Informatica", "voto": 28, "crediti": 10},
            {"materia": "Matematica", "voto": 26, "crediti": 6}
        ]
    }
]

#1. Calcola la media reale (invece di usare quella già presente)
#Per ogni studente: sum(voti) / len(voti)

#2. Voto più alto per studente
#Per ogni studente, trova il massimo in voti
#3. Materia con voto più alto (più complesso)
#Associa ogni voto alla materia corrispondente (stessa posizione)

somma_voti = 0
somma_per_materia = 0





for studente in studenti:
    somma_voti = 0
    conta_voti = 0


    for esame in studente["voti"]:
        nome_completo = studente["nome"] + " " + studente["cognome"]
        somma_voti += esame["voto"]
        conta_voti += 1
        media_calcolata = somma_voti / conta_voti

    print(F" {nome_completo:<15}  Media Voti {media_calcolata:,.2f}")

print("\n" + "=" * 70)

for studente in studenti:
    voto_massimo = 0
    studente_migliore = studente["nome"] + " " + studente["cognome"]

    for esame in studente["voti"]:
        voto = esame["voto"]

        if voto > voto_massimo:
            voto_massimo = voto


    print(f" Studente voto massimo:  {studente_migliore:>15} {voto_massimo:>10}")

print("\n" + "=" * 70)

studente_record = ""
materia_voto_max = ""
voto_max_globale = 0


for studente in studenti:
    nome_studente = studente["nome"] + " " + studente["cognome"]
    for esame in studente["voti"]:
        if esame["voto"] > voto_max_globale:
            voto_max_globale = esame["voto"]
            materia_voto_max = esame["materia"]
            studente_record = nome_studente
print(f"Materia con voto piu alto {studente_record},  {materia_voto_max}, {voto_max_globale}")

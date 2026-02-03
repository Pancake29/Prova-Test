studenti = [
    {"nome": "Mario", "cognome": "Rossi", "esami": ["Matematica", "Fisica", "Informatica"], "media": 25.5},
    {"nome": "Luisa", "cognome": "Verdi", "esami": ["Letteratura", "Storia"], "media": 28.0},
    {"nome": "Anna", "cognome": "Bianchi", "esami": ["Informatica", "Matematica", "Statistica"], "media": 26.8},
    {"nome": "Luca", "cognome": "Neri", "esami": ["Fisica", "Chimica"], "media": 24.2},
    {"nome": "Mario", "cognome": "Rossi", "esami": ["Economia", "Diritto"], "media": 27.3}
]

#COMPITI:
#STEP 1: ANALISI
#Conta quanti studenti hanno media > 26

#Trova lo studente con la media più alta



for indice, studente in enumerate(studenti):
    media = studente["media"]

media_massima = 0
studente_migliore = None
medie_superiori = 0

for studente in studenti:
    media = studente["media"]

    if media > media_massima:
        media_massima = media

        studente_migliore = studente["nome"] + " " + studente["cognome"]
print(f" Studente media migliore {studente_migliore} {media_massima}")

for studente in studenti:
    voti = studente["media"]
    if voti > 26:
        medie_superiori = voti
        medie_superiori = studente["nome"] + "  " + studente["cognome"]
        print(f" Medie oltre 26 {medie_superiori}  {voti}")

cognomi = {}

for cogn in studenti:
    nome = cogn["nome"]
    cognome = cogn["cognome"]
    if cognome not in cognomi:
        cognomi[cognome] = []
    cognomi[cognome].append(nome)
print(cognomi)

for cognome, lista_nomi in cognomi.items():  # Ciclo ESTERNO
    print(f"Cognome: {cognome}")

    for nome in lista_nomi:  # Ciclo INTERNO
        print(f"Nome  - {nome}")

    print()

esami_per_studenti = {}
studenti_per_esame = {}

print(f" Esami per Studente   Nome e Cognome             Materia       ")

for studente in studenti:
    nome = studente["nome"]
    cognome = studente["cognome"]
    nome_completo = nome + " " + cognome
    lista_esami = studente["esami"]
    if nome_completo not in esami_per_studenti:
        esami_per_studenti[nome_completo] = lista_esami
    print(f"                      {nome_completo}                {lista_esami}")

print('_'*100)
print(f" Materia Esame                  Nome e Cognome                    ")
for studente in studenti:  # CICLO SU TUTTI GLI STUDENTI
    nome_completo = studente["nome"] + " " + studente["cognome"]
    for esame in studente["esami"]:
        if esame not in studenti_per_esame:
            studenti_per_esame[esame] = []
        studenti_per_esame[esame].append(nome_completo)
print("\n" + "="*50)
print("ESAME               STUDENTI")
print("="*50)

for esame, lista_studenti in studenti_per_esame.items():
    print(f"\n{esame}:")
    for studente in lista_studenti:
        print(f"  - {studente}")






#print(f" Studente per esame   Nome esame             Nome e Cognome ")




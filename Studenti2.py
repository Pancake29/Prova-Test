studenti = [
    {"nome": "Marco", "classe": "3A", "voti": [6, 7, 8, 5]},
    {"nome": "Anna", "classe": "3B", "voti": [9, 8, 7, 9]},
    {"nome": "Luca", "classe": "3A", "voti": [5, 6, 7, 6]},
    {"nome": "Sofia", "classe": "3B", "voti": [8, 8, 9, 8]}
]

#1. RAGGRUPPA PER CLASSE
#{"3A": ["Marco", "Luca"], "3B": ["Anna", "Sofia"]}
#2. MEDIA VOTI PER STUDENTE
#Per ogni studente, calcola media voti (somma/len)
#3. STUDENTE CON MEDIA PIÙ ALTA
#Trova lo studente con media voti più alta (gestisci pareggi!)
#4. ORDINA STUDENTI PER MEDIA (decrescente)
#Lista studenti ordinata per media (dal voto più alto)
#5. MEDIA PER CLASSE
#Media di tutte le medie degli studenti di ogni classe

print("="*100)

Studenti_per_classi = {}

for studente in studenti:
    classe = studente["classe"]
    nome = studente["nome"]
    if classe not in Studenti_per_classi:
        Studenti_per_classi[classe] = []
    Studenti_per_classi[classe].append(nome)
print(f"Raggruppamento per Classe: {Studenti_per_classi} ")

print("="*100)

for Studente in studenti:
    voto = Studente["voti"]
    nome = Studente["nome"]


    print(f"{nome} {voto}")

print("="*100)

media_per_studente = {}

for studente in studenti:
    nome = studente["nome"]
    voti = studente["voti"]

    media = sum(voti) / len(voti)
    media_per_studente[nome] = media

print(f"Media per studente {media_per_studente}")

print("="*100)

studente_migliore = []
mediamax = 0

for nome, media in media_per_studente.items():

    if media > mediamax:
        mediamax = media
        studente_migliore = [nome]

    elif media == mediamax:
        studente_migliore.append(nome)

print(f"Studenti con media migliore {studente_migliore} {media}")

print("="*100)

studenti_ordinati = sorted(media_per_studente.items(), key=lambda x:x[1],  reverse=True)

print(f"Studenti ordinati per media: {studenti_ordinati}")
print("="*100)

media_generale_medie = 0
tutte_medie = []

for nome, media in media_per_studente.items():
    tutte_medie.append(media)

    media_generale = sum(tutte_medie) / len(tutte_medie)
print(f"Media Generale {media_generale}")

print("="*100)
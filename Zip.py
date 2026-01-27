from itertools import zip_longest

nomi = ["Alice", "Bob", "Carla", "Davide"]
eta = [25, 32, 28, 41]
citta = ["Roma", "Milano", "Napoli", "Torino"]

#Alice ha 25 anni e vive a Roma
#Bob ha 32 anni e vive a Milano
#Carla ha 28 anni e vive a Napoli
#Davide ha 41 anni e vive a Torino

for nome, anni, indirizzo in zip(nomi, eta, citta):
    print(f"{nome} ha {anni} anni e vive a {indirizzo}")

print("-" * 100)

studenti = ["Marco", "Laura", "Giovanni", "Sofia"]
esami = ["Matematica", "Fisica", "Informatica"]
voti = [28, 30, 25, 27, 29]
date = ["15/05", "18/05"]

for universitari, materia, risultato, temporale in zip_longest(studenti, esami, voti, date, fillvalue="N/D"):
    print(f"{universitari} ha dato esame in {materia} ed ha preso {risultato} in data {temporale}")

print('_' * 100)

registro = [
    {"studente": "Marco", "esame": "Matematica", "voto": 28, "data": "15/05"},
    {"studente": "Laura", "esame": "Fisica", "voto": 30, "data": "18/05"},
    {"studente": "Giovanni", "esame": "Informatica", "voto": 25, "data": "22/05"},
    {"studente": "Sofia", "esame": "Matematica", "voto": 27, "data": "15/05"},
    {"studente": "Sofia", "esame": "Fisica", "voto": 29, "data": "18/05"}
]
for record in registro:
    print(f"{record['studente']} ha preso {record['voto']} in {record['esame']} il {record['data']}")

conteggio_sofia = 0
for record in registro:
    if record["studente"] == "Sofia":
        conteggio_sofia += 1
print(conteggio_sofia)

somma_matematica = 0
conteggio_matematica = 0

for record in registro:
    if record["esame"] == "Matematica":
        somma_matematica += record["voto"]
        conteggio_matematica += 1
print(conteggio_matematica)

media_matematica = somma_matematica / conteggio_matematica
print(media_matematica)

somma_matematica = 0
conteggio_matematica = 0
conteggio_sofia = 0


for record in registro:
    if record["studente"] == "Sofia":
        conteggio_sofia += 1

    if record["esame"] == "Matematica":
        somma_matematica += record["voto"]

        conteggio_matematica += 1

print(conteggio_sofia)
print(conteggio_matematica)
print(media_matematica)
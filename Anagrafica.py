persone = [
    {"nome": "Anna", "citta": "Roma", "eta": 25},
    {"nome": "Marco", "citta": "Milano", "eta": 30},
    {"nome": "Laura", "citta": "Roma", "eta": 22},
    {"nome": "Luca", "citta": "Napoli", "eta": 35},
    {"nome": "Sofia", "citta": "Milano", "eta": 28}
]

#Compiti:

#Raggruppa i nomi per città (dizionario con liste)
#Calcola l'età media per città
#Trova la persona più giovane
#Ordina le persone per età (crescente)
#Filtra le persone che hanno più di 25 anni

nomi_per_citta = {}

for persona in persone:
    nomi = persona["nome"]
    residenza = persona["citta"]
    anni = persona["eta"]
    if residenza not in nomi_per_citta:
        nomi_per_citta[residenza] = []
    nomi_per_citta[residenza].append((nomi, anni))
print(nomi_per_citta)

print("="*75)

#Calcola l'età media per città


for citta, lista_tuple in nomi_per_citta.items():
    solo_eta = [tupla[1] for tupla in lista_tuple]
    media = sum(solo_eta) / len(solo_eta)
    print(f"Città:  {citta:<10} Media età: {media:>10}")
    print(solo_eta)

print("="*75)

#Trova la persona più giovane

persone_ordinate = sorted(persone, key=lambda x:x["eta"], reverse=False)

for i in persone_ordinate:
    print(f"Nome: {i['nome']:<10} Anni:{i['eta']:>10} ")


print("="*75)

anni_min = 1000
persona_min = ""

for a in persone_ordinate:
    nomi = a["nome"]
    anni = a["eta"]
    if anni < anni_min:
        anni_min = anni
        persona_min = nomi

print(f"Persona età minima: {persona_min} Eta: {anni_min}")

print("="*75)

#Filtra le persone che hanno più di 25 anni



for b in persone_ordinate:
    nomi = b["nome"]
    anni = b["eta"]
    if anni > 25:
        nominativo = b["nome"]



        print(f" Eta oltre 25 {nominativo} Anni {anni}")
nomi_persona = []
for persona in persone:
    nomi_persona.append(persona["nome"])
    # a ogni giro AGGIUNGI alla lista

print(nomi_persona)
# ['Anna', 'Marco', 'Laura', 'Luca', 'Sofia']  ← TUTTI i nomi
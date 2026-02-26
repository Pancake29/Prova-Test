animali = [
    {"nome": "Balena", "specie": "Mammifero", "peso_kg": 50000, "velocita_kmh": 30, "habitat": "oceano"},
    {"nome": "Ghepardo", "specie": "Mammifero", "peso_kg": 60, "velocita_kmh": 120, "habitat": "savana"},
    {"nome": "Aquila", "specie": "Uccello", "peso_kg": 5, "velocita_kmh": 160, "habitat": "montagna"},
    {"nome": "Elefante", "specie": "Mammifero", "peso_kg": 5000, "velocita_kmh": 40, "habitat": "savana"},
    {"nome": "Falco", "specie": "Uccello", "peso_kg": 1.5, "velocita_kmh": 180, "habitat": "montagna"},
    {"nome": "Squalo bianco", "specie": "Pesce", "peso_kg": 1100, "velocita_kmh": 56, "habitat": "oceano"},
    {"nome": "Leone", "specie": "Mammifero", "peso_kg": 190, "velocita_kmh": 80, "habitat": "savana"},
    {"nome": "Pinguino", "specie": "Uccello", "peso_kg": 25, "velocita_kmh": 8, "habitat": "antartide"}
]

#Compiti:
#Raggruppa i nomi per habitat (dizionario habitat → lista nomi)


abitanti_habitat = {}


for animale in animali:
    ambiente = animale["habitat"]
    nomi = animale["nome"]
    if ambiente not in abitanti_habitat:
        abitanti_habitat[ambiente]= []
    abitanti_habitat[ambiente].append(nomi)
print(abitanti_habitat)

#Peso medio per specie (dizionario specie → peso medio)

abitanti_specie = {}

for animale in animali:
    speci = animale["specie"]
    peso = animale["peso_kg"]
    if speci not in abitanti_specie:
        abitanti_specie[speci]= []
    abitanti_specie[speci].append( peso)
print(abitanti_specie)

lista_ordinata = sorted(abitanti_specie.items(), key=lambda x:x[0] )
print(lista_ordinata)

print("="*75)

media_pesi = {}

for specie, lista_pesi in abitanti_specie.items():
        media = sum(lista_pesi) / len(lista_pesi)
        media_pesi[specie] = media

print(f"Peso medio per specie: {media_pesi}")

print("="*75)

#Animale più veloce (nome e velocità)

velocità_max = 0
animale_più_veloce = ""

for animale in animali:
    velocità = animale["velocita_kmh"]
    nomi = animale["nome"]
    if velocità > velocità_max:
        velocità_max = velocità
        animale_più_veloce = nomi
print(f"Animale piu' veloce: {animale_più_veloce}     Velocita: {velocità_max}")


#Ordina gli animali per peso (decrescente) (lista ordinata)

lista_ordinata = sorted(animali, key=lambda x:x["peso_kg"] , reverse=True)
print(lista_ordinata)

lista_semplice = [(a["nome"], a["peso_kg"]) for a in lista_ordinata]
print(lista_semplice)

for nome, peso in lista_semplice:
    print(f"{nome} {peso}")

#Filtra gli animali che vivono in "savana" (lista di nomi)

animali_savana = []
for animale in animali:

    if animale["habitat"] == "savana":
        animali_savana.append(animale ["nome"])

print(animali_savana)
studenti = [
    {"nome": "Anna", "voti": [8, 7, 9, 6]},
    {"nome": "Marco", "voti": [6, 5, 7, 6]},
    {"nome": "Laura", "voti": [9, 8, 9, 8]},
    {"nome": "Luca", "voti": [5, 4, 6, 5]},
    {"nome": "Sofia", "voti": [7, 8, 7, 8]}
]

#Calcola la media voti per ogni studente
#(dizionario nome → media)

media_voti = {}
for studente in studenti:
    voto = studente["voti"]
    nomi = studente["nome"]
    somma= sum(voto)
    conteggio = len(voto)
    media_voti[nomi] = somma / conteggio
print(f"Media voti: {media_voti}")

for nome, media in media_voti.items():
    print(f"Nome studente: {nome:<10} Media voti: {media:>7}")

print("="*75)

#Trova lo studente con la media più alta
#(nome e media)
media_max = 0
for nome, media in media_voti.items():
    if media > media_max:
        media_max = media
        studente_max = nome

print(f"Studente media piu' alta: {studente_max}    Media: {media_max}")

print("="*75)

#Ordinagli studenti per media(decrescente) Che funzione useresti? Elambda cosa deve
#restituire?

lista_ordinata = sorted(media_voti.items(), key=lambda x:x[1], reverse=True)
print(lista_ordinata)

for nome, media in lista_ordinata:

    print(f"Nome studente : {nome:<8}  {media:>8}")

print("="*75)

#Filtra gli studenti per media  >= 7

lista_media_uguale_superiore7 = {}

for nome, media in media_voti.items():

    if media >= 7:
        lista_media_uguale_superiore7[nome]= media # aggiungi il nome

print(f"{lista_media_uguale_superiore7} ")

for nome, media in lista_media_uguale_superiore7.items():
    print(f"{nome} {media}")


print("="*75)

#Crea una lista di tuple (nome,media) solo per chi ha la media uguale maggiore di 7. Che struttura useresti,
# come la ottieni

lista_ugsup7 = sorted(lista_media_uguale_superiore7.items(), key=lambda x:x[1], reverse=True)
print(lista_ugsup7)



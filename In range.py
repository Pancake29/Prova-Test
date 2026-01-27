for number in range (10, -1, -1):
    print(number)
    if number == 0:
        print('Decollo!')

print("-" * 100)


La_mia_playlist =[
'Imagine',
'Bohemian Rhapsody',
'Billie Jean',
'Smells Like Teen Spirit',
'Hallelujah'
]
print("Lista originale:")
for song in (La_mia_playlist):
    print(song)


print("-" * 100)


La_mia_playlist.append('Shape of You')
La_mia_playlist[2] = 'Like a Rolling Stone'
for song1 in (La_mia_playlist):
    print(song1)



print("-" * 100)

# 1. Lista iniziale
playlist = ['Imagine', 'Bohemian Rhapsody', 'Billie Jean', 'Smells Like Teen Spirit', 'Hallelujah']

# 2. Funzione per stampare
def stampa(playlist, titolo):
    print(f"\n{titolo}:")
    for brano in playlist:  # ← NO list() qui!
        print(brano)

# 3. Operazioni
stampa(playlist, "Playlist originale")
playlist.append('Shape of You')  # ← Direttamente
stampa(playlist, "Dopo aggiunta")
playlist[2] = 'Like a Rolling Stone'
stampa(playlist, "Dopo modifica")
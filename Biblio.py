biblioteca = [
    {"titolo": "Il Signore degli Anelli", "pagine": 423, "prestiti": 15},
    {"titolo": "1984", "pagine": 328, "prestiti": 22},
    {"titolo": "Harry Potter", "pagine": 309, "prestiti": 18}
]

#Libro più spesso prestato (massimo prestiti)
#Libro più lungo (massimo pagine)
#Media pagine di tutti i libri
#Totale prestiti della biblioteca

prestiti_massimi = 0
libro_più_fogli = 0
totale_pagine_complessive = 0
media_pagine_complessiva = 0
giorni_prestiti_totali = 0
nome_libro_più_pagine = ""
nome_libro_più_prestiti = ""
pagina = 0
Totale_libri = 0
Numero_libri = len(biblioteca)
libro_prestiti_fogli_massimo = 0
lista = biblioteca

for libro in biblioteca:
    prestito = libro["prestiti"]
    fogli = libro["pagine"]
    titoli = libro["titolo"]
    nome_libro = titoli
    totale_pagine_complessive +=fogli
    media_pagine_complessiva = totale_pagine_complessive / Numero_libri
    lista = biblioteca
    if prestito > prestiti_massimi:
        prestiti_massimi = prestito
        nome_libro_più_prestiti = titoli


    if fogli > libro_più_fogli:
        libro_più_fogli = fogli
        nome_libro_più_pagine = titoli






print(libro_prestiti_fogli_massimo)


print(f"Prestito maggiore: {nome_libro_più_prestiti}  Giorni: {prestiti_massimi}")
print(f"Libro piu' pagine: {nome_libro_più_pagine}  - Pagine: {libro_più_fogli}")
print(f"Pagine complessive:  {totale_pagine_complessive}")
print(f"Media pagine complessiva:  {media_pagine_complessiva:,.2f}")

print("="*50)

nuovo_libro = {"titolo": "Il Piccolo Principe", "pagine": 325, "prestiti": 28}
biblioteca.append(nuovo_libro)
for libro in biblioteca:
    print( "titolo: " + libro["titolo"])
    print("Pagine: " + str(libro["pagine"]))
    print( "prestito: " + str(libro["prestiti"]))
    print( "" )

prestiti_massimi = 0
libro_più_fogli = 0
totale_pagine_complessive = 0
media_pagine_complessiva = 0
giorni_prestiti_totali = 0
nome_libro_più_pagine = ""
nome_libro_più_prestiti = ""
pagina = 0
Totale_libri = 0
Numero_libri = len(biblioteca)
prestiti_pagine_massimo = 0

for libro in biblioteca:
    prestito = libro["prestiti"]
    fogli = libro["pagine"]
    titoli = libro["titolo"]
    nome_libro = titoli
    totale_pagine_complessive +=fogli
    media_pagine_complessiva = totale_pagine_complessive / Numero_libri

    if prestito > prestiti_massimi:
        prestiti_massimi = prestito
        nome_libro_più_prestiti = titoli


    if fogli > libro_più_fogli:
        libro_più_fogli = fogli
        nome_libro_più_pagine = titoli




print(f"Prestito maggiore: {nome_libro_più_prestiti}  Giorni: {prestiti_massimi}")
print(f"Libro piu' pagine: {nome_libro_più_pagine}  - Pagine: {libro_più_fogli}")
print(f"Pagine complessive:  {totale_pagine_complessive}")
print(f"Media pagine complessiva:  {media_pagine_complessiva:,.2f}")

print("="*50)

ordinati_combinati = sorted(biblioteca, #SORTED NON ENTRA MAI IN UN CICLO, LAVORA SULLA LISTA INTERA
                           key=lambda x: (x["prestiti"], x["pagine"]), #LAMBDA CONSENTE DI LAVORARE SU UNA LISTA DI DIZIONARI
                           reverse=True)
#Se non so confrontare gli OGGETTI, uso lambda per confrontare i loro PEZZI"

#Ogni volta che vedi lambda x: x["chiave"], pensa: "trasforma -> estrai -> confronta".


for libro in ordinati_combinati:
    print("Ordinati combinati titolo: " + libro["titolo"])
    print("Pagine: " + str(libro["pagine"]))
    print("prestito: " + str(libro["prestiti"]))
    print("")
print("="*50)
ordinati_combinati = sorted(biblioteca,
                           key=lambda x: (x["pagine"], x["prestiti"]),
                           reverse=True)
for libro in ordinati_combinati:
    print("Ordinati combinati titolo: " + libro["titolo"])
    print("Pagine: " + str(libro["pagine"]))
    print("prestito: " + str(libro["prestiti"]))
    print("")
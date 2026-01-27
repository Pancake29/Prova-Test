numeri = [5, -3, 12, -8,  7, -1, 15, -4, 9]

positivi = 0
negativi = 0
zeri = 0
lista_positivi = [] # per creare una lista sulla quale posso operare con ulteriori calcoli sui numeri
lista_negativi = []

for numero in numeri:

    if numero > 0:
        positivi +=1
        lista_positivi.append(numero)
    elif numero <0:
        negativi +=1
        lista_negativi.append(numero)
    else:
        zeri +=0


print(f"{'Numeri positivi':<10}  {'Numeri negativi':>10}  {'Zeri':>10}")
print(f"      {positivi:<10}   {negativi:>6}        {zeri:>10}")

somma_positivi = sum(lista_positivi)
somma_negativi = sum(lista_negativi)

conteggio_positivi =len(lista_positivi)
conteggio_negativi = len(lista_negativi)

media_positivi = somma_positivi / conteggio_positivi
media_negativi = somma_negativi / conteggio_negativi

print(f"Totale Positivi    {somma_positivi}")
print(f"Totale Negativi   {somma_negativi}")
print(f"Media Positivi      {media_positivi}")
print(f"Media Negativi     {media_negativi}")

max = max(lista_positivi)
min = min(lista_negativi)
print(f"Massimo lista positivi  {max}")
print(f"Minimo  lista negativi  {min}")

for numero in lista_positivi:
    if numero > media_positivi:
        print(f"Num. maggiori media positivi {numero}")

risultati = []  # lista di stringhe per calcolare i numeri che superano la media
conteggio = 0

for numero in lista_positivi:
    if numero > media_positivi:
        risultati.append(str(numero))  # converti in stringa
        conteggio += 1

# Unisci tutti i numeri con virgola
numeri_str = ", ".join(risultati)
print(f"Numeri > media positivi ({media_positivi}): {numeri_str}")
print(f"Totale: {conteggio} numeri")
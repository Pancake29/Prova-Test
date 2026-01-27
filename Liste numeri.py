numeri = [7, 12, 25, 18, 33, 42, 51, 64, 79, 88]
#Compito:
#Contare quanti numeri sono:
#Pari (% 2 == 0)
#Dispari
#Maggiori di 10
#Trovare:
#Il numero più grande
#Il numero più piccolo
#La somma totale
#La media

Numeri = [15, 7, 22, 4, 18, 9, 31, 5, 12]

pari = 0
dispari =0
maggiori_di_10= 0
QtàNum = len(Numeri)

sum(Numeri)
max(Numeri)
min(Numeri)

media_Numeri = sum(Numeri)/len(Numeri)

print(f"  {'Quantità Num':>13} | {'Numero Max':>13} | {'Numero Min':>13} | {'Totale Numeri':>10} | {'Media Numeri':>10}")
print(f"  {QtàNum:>14}|  {max(Numeri):>13}| {min(Numeri):>13} |    {sum(Numeri):>10} |   {media_Numeri:>10,.2f}")

for numeri in Numeri:
        if numeri % 2 == 0:
            pari += 1
        else:
            dispari += 1

        if numeri > 10:
            maggiori_di_10 += 1

print("-" * 100)

print(f"{'Numeri Pari':<15} {'Numeri Dispari':>15} | {'Mag di 10':>15}")
print(f"{pari:<15} |{dispari:>15}| {maggiori_di_10:>15}")

etichette = ['Quantità', 'Max', 'Min', 'Somma', 'Media', 'Pari', 'Dispari', 'Maggiore di 10']
valori = [
    len(Numeri),
    max(Numeri),
    min(Numeri),
    sum(Numeri),
    f"{sum(Numeri)/len(Numeri):.2f}",
    pari,
    dispari,
    maggiori_di_10
]

for etichetta, valore in zip(etichette, valori):
        print(f"│ {etichetta:<15} │ {valore:>14}│")
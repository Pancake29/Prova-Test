lista_numeri = [7, 12, 25, 18, 33, 42, 51, 64, 79, 88]

pari = 0
dispari =0



for numeri in lista_numeri:
        if numeri % 2 == 0:
            pari += 1
        else:
            dispari += 1

print(f"{'Numeri Pari':<15}       {'Numeri Dispari':>15} ")
print(f"{pari:>11}     {dispari:>21}")

print(''*50)

numeri = [7, 12, 25, 18, 33, 42, 51, 64, 79, 88]

pari = []
dispari= []

for i in numeri:
    if i % 2 == 0:

        pari.append(i)
    else:
        dispari.append(i)



print(f"Numeri Pari {pari}")
print(f"Numeri Dispari {dispari}")

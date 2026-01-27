#Esercizio termostato con temperatura = 20

Temperatura = int(input(f'Inserisci temperatura: '))
if Temperatura < 18:
    print('Accendi Riscaldamento')

elif Temperatura <= 24:
    print('Temperatura perfetta')

else:
    print('Accendi il condizionatore')


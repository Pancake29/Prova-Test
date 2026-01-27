#Calcolo sconto per età

#Input: età = int(input("Inserisci età: "))


#Under 18 → Sconto 50%

#18-65 → Sconto 0% (nessuno)
#Over 65 → Sconto 30%
#Compito:
#Usa solo if/elif/else per determinare la percentuale di sconto e stampare:
#"Hai diritto al X% di sconto"



Età = int(input(f'Inserisci la tua eta:'))

if Età < 18:
    print('Hai diritto ad uno sconto del 50%')
elif Età <= 65:
    print('Non hai diritto a sconti')

elif Età <= 80:
    print('Hai diritto ad uno sconto del 30%')

else:
    print('Hai diritto ad uno sconto del 40%')
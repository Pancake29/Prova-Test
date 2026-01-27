#Devi classificare ogni temperatura in:

#"Fredda" se < 20°
#"Normale" se tra 20 e 25 (inclusi)
#"Calda" se > 25
#Scrivi un ciclo che stampi per ogni temperatura:
#"Giorno X: Y gradi → Z" dove X è il numero del giorno (partendo da 1), Y è la temperatura, Z è la classificazione.
##Poi calcola e stampa:
#La temperatura media della settimana
#Quanti giorni sono stati "Caldi"
temperature = [22.5, 19.0, 25.5, 30.2, 17.8, 23.0, 28.4]
print(temperature)
giorni = len(temperature)
media_temp = sum(temperature)/ giorni

contatore_giorni = 0
contatore_caldi = 0
somma_temperature = 0
giorni_caldi = []

print('_'*80)

for gradi in temperature:
    contatore_giorni += 1
    if gradi  < 20:
        percezione = 'Fredda'
    elif gradi <=25:
        percezione = 'Normale'
    else:
        contatore_caldi += 1
        giorni_caldi.append(contatore_giorni)
        percezione = 'Calda'

    X = contatore_giorni
    Y = gradi
    Z = percezione

    print(f"{X}: {Y} {percezione}")

#Fuori ciclo
print(f"Giorni caldi{giorni_caldi}")
print(f'Giorni misurati: {giorni}')
print(f'Temperatura media: {media_temp:,.2f}')





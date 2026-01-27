temperature = [2, -1, 5, 0, -3, 4, 1]  # °C per 7 giorni
condizioni = ["pioggia", "neve", "sole", "nebbia", "neve", "pioggia", "nuvoloso"]
gg = [1, 2, 3, 4, 5, 6, 7, 8]
#1. ANALISI TEMPERATURE (cicli + condizioni)
#Conta quanti giorni hanno temperatura sotto zero
#Conta quanti giorni hanno temperatura sopra zero
#Trova la temperatura massima e minima della settimana
sotto_zero = 0
sopra_zero = 0
zero = 0

giorni_sopra_zero = 0
giorni_sotto_zero = 0

giorni = len(temperature)
tmp_media = sum(temperature) / giorni
max(temperature)
min(temperature)

pioggia = 0
neve = 0
sole = 0
nuvoloso = 0
nebbia = 0


for gradi, tempo, temporalita in zip (temperature, condizioni,gg):
        if gradi < 0:
            sotto_zero +=1


        elif gradi > 0:
            sopra_zero +=1

        else:
            gradi == 0
            zero +=1


print(f"Giorni sotto 0:     {sotto_zero}")
print(f"Giorni sotto 0:     {sopra_zero}")
print(f"Giorni a 0:         {zero}")
print(f"Temperature media:  {tmp_media:,.2f}")
print(f"Temperature max:    {max(temperature)}")
print(f"Temperature min:   {min(temperature)}")


#2. ANALISI CONDIZIONI (dizionario + contatori)
#Crea un dizionario che conti quante volte appare ogni condizione meteo
#Esempio risultato: {"pioggia": 2, "neve": 1, ...}
stesse_condizioni = {}

for cond in condizioni:  # 1 ciclo, 7 iterazioni

    if cond in stesse_condizioni:          # Se già esiste
        stesse_condizioni[cond] += 1
    else:                          # Se è nuova
        stesse_condizioni[cond] = 1        # Crea nuova chiave

print(f"Frequenza Condizioni {stesse_condizioni}")


giorni_sottozero_neve = []

for i in range(len(temperature)):
    if temperature[i] < 0 and condizioni[i] == "neve":
        giorni_sottozero_neve.append(i)

print(f"Giorni sotto zero con neve {giorni_sottozero_neve}")

temperature_solo_pioggia = []
for i in range(len(temperature)):
    if condizioni[i] == "pioggia":  # SOLO questa condizione!
        temperature_solo_pioggia.append(temperature[i])  # Aggiungi la TEMPERATURA, non l'indice!

print(f"Temperature Giorni pioggia {temperature_solo_pioggia}")
somma_temperature = 0
conteggio_giorni = 0
for i in range(len(temperature)):
    if condizioni[i] != "neve":
        somma_temperature += temperature[i]
        conteggio_giorni +=1

med_tem_senza_neve = somma_temperature / conteggio_giorni
print(f"Media temp. giorni senza neve {med_tem_senza_neve:,.2f}")


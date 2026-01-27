clienti = ["Rossi", "Bianchi", "Verdi", "Neri"]
persone = [4, 2, 6, 3]           # Numero di persone
orari = ["20:00", "19:30", "21:00", "20:30"]
confermate = [True, False, True, True]  # Prenotazione confermata?

for nome, num_per, time, conferma in  zip (clienti, persone, orari, confermate):
    if conferma == True:
        if num_per > 4:
            tavolo = 'Grande'

        if num_per == 4:
            tavolo = 'Medio'

        if num_per < 4:
            tavolo = 'Piccolo'

        print(f"{nome} ha prenotato per {num_per} persone per le ore {time} un tavolo {tavolo}")

print('' * 100)

clienti = ["Rossi", "Bianchi", "Verdi", "Neri"]
persone = [2, 4, 3, 6]           # Numero di persone
orari = ["20:00", "19:30", "21:00", "20:30"]
confermate = [True, False, True, True]  # Prenotazione confermata?

for nome, num_per, time, conferma in  zip (clienti, persone, orari, confermate):
    if conferma == True:
        if num_per > 4:
            tavolo = 'Grande'

        if num_per == 4:
            tavolo = 'Medio'

        if num_per < 4:
            tavolo = 'Piccolo'

        print(f"{nome} ha prenotato per {num_per} persone per le ore {time} un tavolo {tavolo}")




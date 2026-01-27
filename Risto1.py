clienti = ["Rossi", "Bianchi", "Verdi", "Neri"]
persone = [4, 2, 6, 3]           # Numero di persone
orari = ["20:00", "19:30", "21:00", "20:30"]
confermate = [True, False, True, True]  # Prenotazione confermata?



for nome, num_per, time, conferma in zip(clienti, persone, orari, confermate):
    if conferma == True:  # UNICA volta!
        if num_per > 4:
            tavolo = "Grande"
        elif num_per == 4:
            tavolo = "Medio"
        else:  # <4
            tavolo = "Piccolo"

        print(f"{nome} ha prenotato per {num_per} per le ore {time} un Tavolo {tavolo}")
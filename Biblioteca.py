#OBIETTIVI di ANALISI FINANZIARIA:
#1. PER OGNI LIBRO (analisi per titolo): Ricavo totale da multe per quel libro
#Numero di utenti in ritardo per quel: libro Multa media per infrazione (solo chi ha pagato)
#2. PER OGNI UTENTE (analisi per cliente): Ricavo totale da ogni utente (somma multe di TUTTI i libri)
#Identifica utenti più "problematici" (più multe)
#Identifica utenti "puntuali" (nessuna multa)
#3. TOTALE BIBLIOTECA: Ricavo totale annuale da multe
#Numero totale di infrazioni
#Multa media per infrazione (globale)
#Libro più redditizio (più ricavo multe)
#4. METRICHE STRATEGICHE:
#"Tasso di infrazione" = % prestiti in ritardo
#"Redditività per libro" = ricavo multe / numero prestiti
#"Giorni ritardo medi" per chi è in ritardo

# I 3 BESTSELLER
libri = ["Harry Potter", "Guerra e Pace", "Il Signore degli Anelli"]

# 8 UTENTI per ogni libro (24 prestiti totali)
utenti = ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8"]

# Giorni di ritardo per OGNI prestito (0 = restituito in tempo)
ritardi_hp = [0, 5, 0, 10, 0, 15, 3, 0]      # 8 utenti per Harry Potter
ritardi_gp = [20, 0, 8, 0, 12, 0, 0, 6]      # 8 utenti per Guerra e Pace
ritardi_sda = [0, 0, 4, 0, 0, 7, 0, 2]       # 8 utenti per Il Signore degli Anelli

# Tariffe multe DIVERSE per libro (€/giorno)
tariffa_hp = 0.15   # Harry Potter: 0.15€/giorno
tariffa_gp = 0.20   # Guerra e Pace: 0.20€/giorno
tariffa_sda = 0.10  # Il Signore degli Anelli: 0.10€/giorno
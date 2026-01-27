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


#I 3 BESTSELLER
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

libri_ripetuti = ["Harry Potter"]*8 + ["Guerra e Pace"]*8 + ["Il Signore degli Anelli"]*8
tariffe_ripetute = [0.15]*8 + [0.20]*8 + [0.10]*8
ritardi_tutti = ritardi_hp + ritardi_gp + ritardi_sda
utenti_ripetuti = utenti * 3
somma_giorni_ritardo = 0
prestiti_totali = 24

#CONTATORI PER LIBRO

ricavi_per_libro = {
    "Harry Potter": 0.0,          # float: somma multe di TUTTI gli utenti per HP
    "Guerra e Pace": 0.0,         # float: somma multe per GP
    "Il Signore degli Anelli": 0.0  # float: somma multe per SDA
}

infrazioni_per_libro = {
    "Harry Potter": 0,           # int: conta QUANTI utenti in ritardo per HP
    "Guerra e Pace": 0,          # int: conta per GP
    "Il Signore degli Anelli": 0   # int: conta per SDA
}

#2. CONTATORI per UTENTE (lista di 8 elementi)

# ========= CONTATORI PER UTENTE =========
# Lista di 8 float: indice 0=U1, 1=U2, ..., 7=U8
ricavi_per_utente = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# [U1_totale, U2_totale, U3_totale, ..., U8_totale]

infrazioni_per_utente = [0, 0, 0, 0, 0, 0, 0, 0]
# [U1_conteggio, U2_conteggio, ..., U8_conteggio]
#3. CONTATORI GLOBALI (singole variabili)
# ========= CONTATORI GLOBALI =========
ricavo_totale = 0.0                # float: somma di TUTTE le multe
infrazioni_totali = 0  # int: conta TUTTE le infrazioni
multe = 0

# Per il "RECORD" (libro più redditizio)
libro_piu_redditizio = ""          # str: nome del libro
max_ricavo = 0.0                   # float: valore del massimo ricavo

for i in range(24):  # 24 prestiti totali
    libro = libri_ripetuti[i]  # str: "Harry Potter"
    utente_idx = i % 8  # int: 0=U1, 1=U2, ..., 7=U8
    ritardo = ritardi_tutti[i]  # int: giorni di ritardo
    tariffa = tariffe_ripetute[i]  # float: €/giorno
    multa = 0.0
    somma_giorni_ritardo += ritardo  # ✅ Aggiungi i GIORNI effettivi!
    if ritardo > 0:  # SE C'È RITARDO
        # 1. Calcola multa per QUESTO prestito
        multa = ritardo * tariffa  # float

        # 2. Aggiorna CONTATORI PER LIBRO (dizionario)
        ricavi_per_libro[libro] += multa  # somma soldi
        infrazioni_per_libro[libro] += 1  # +1 infrazione

        # 3. Aggiorna CONTATORI PER UTENTE (lista)
        ricavi_per_utente[utente_idx] += multa  # somma soldi utente
        infrazioni_per_utente[utente_idx] += 1  # +1 infrazione utente

        # 4. Aggiorna CONTATORI GLOBALI
        ricavo_totale += multa  # somma a totale generale
        infrazioni_totali += 1  # +1 a infrazioni totali



        # 5. Controlla RECORD (libro più redditizio)
        if ricavi_per_libro[libro] > max_ricavo:
            max_ricavo = ricavi_per_libro[libro]
            libro_piu_redditizio = libro

    # ==================== DOPO IL CICLO ====================

print("\n" + "=" * 70)
print("RIEPILOGO FINALE BIBLIOTECA")
print("=" * 70)

    # 1. PER LIBRO
print("\n1. MULTE PER LIBRO:")
print("-" * 50)
print(f"{'LIBRO':<25} | {'TOTALE MULTE':>12} | {'INFAZIONI':>10}")
print("-" * 50)


for libro in ["Harry Potter", "Guerra e Pace", "Il Signore degli Anelli"]:
        totale = ricavi_per_libro[libro]
        conteggio = infrazioni_per_libro[libro]
        print(f"{libro:<25} | €{totale:>11,.2f} | {conteggio:>10}")

    # 2. PER UTENTE
print("\n\n2. MULTE PER UTENTE:")
print("-" * 50)
print(f"{'UTENTE':<10} | {'TOTALE MULTE':>12} | {'INFAZIONI':>10}")
print("-" * 50)

for i in range(8):  # U1 a U8
        utente = f"U{i + 1}"
        totale = ricavi_per_utente[i]
        conteggio = infrazioni_per_utente[i]
        print(f"{utente:<10} | €{totale:>11,.2f} | {conteggio:>10}")

    # 3. TOTALE GLOBALE
print("\n\n3. TOTALE BIBLIOTECA:")
print("-" * 50)
print(f"RICAVO TOTALE: €{ricavo_totale:,.2f}")
print(f"TOTALE INFAZIONI: {infrazioni_totali}")
print(f"MULTA MEDIA PER INFAZIONE: €{ricavo_totale / infrazioni_totali:,.2f}")
print(f"LIBRO PIÙ REDDITIZIO: {libro_piu_redditizio} (€{max_ricavo:,.2f})")

# 4. METRICHE STRATEGICHE
print("\n\n4. METRICHE STRATEGICHE:")
print("-" * 50)

# A) Tasso di infrazione
tasso_infrazione = (infrazioni_totali / 24) * 100
print(f"Tasso di infrazione: {tasso_infrazione:.1f}%")

# B) Redditività per libro
print("\nRedditività per libro (per prestito):")
for libro in libri:
    redditivita = ricavi_per_libro[libro] / 8  # 8 prestiti per libro
    print(f"  {libro:<25}: €{redditivita:.2f} per prestito")

if infrazioni_totali > 0:

    giorni_medi = somma_giorni_ritardo / infrazioni_totali  # ✅ QUI

    print(f"Giorni di ritardo medi: {giorni_medi:.1f} giorni")  # ✅ QUI



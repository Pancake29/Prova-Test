dipendenti = [
    {"nome": "Anna", "reparto": "Vendite", "stipendio": 3400, "anni_esperienza": 3},
    {"nome": "Marco", "reparto": "IT", "stipendio": 3000, "anni_esperienza": 5},
    {"nome": "Laura", "reparto": "Vendite", "stipendio": 2800, "anni_esperienza": 7},
    {"nome": "Luca", "reparto": "IT", "stipendio": 3200, "anni_esperienza": 2},
    {"nome": "Sofia", "reparto": "HR", "stipendio": 2200, "anni_esperienza": 4}
]


#COMPITI (applica specchietto):
#1. RAGGRUPPA per REPARTO (STRINGHE)
#{"Vendite": ["Anna", "Laura"], "IT": ["Marco", "Luca"], "HR": ["Sofia"]}

print("="*80)

reparto = {}

for dipendente in dipendenti:
    reparti = dipendente["reparto"]
    nome = dipendente["nome"]
    retribuzione = dipendente["stipendio"]
    if reparti not in reparto:
        reparto[reparti] = []
    reparto[reparti].append(nome)
print(f"Reparti {reparto} ")

print("="*80)

#2. MEDIA STIPENDIO per REPARTO (NUMERI)
#{"Vendite": 2650, "IT": 3100, "HR": 2200}

stipendi_reparto = {}

for stipendi in dipendenti:
    retribuzione =stipendi["stipendio"]
    reparti = stipendi["reparto"]
    if reparti not in stipendi_reparto:
        stipendi_reparto[reparti] = []
    stipendi_reparto[reparti].append(retribuzione)
print(f"Stipendi per reparto {stipendi_reparto}")

print("="*80)

medie_reparti = {}  # NUOVO dizionario per salvare le medie

for reparti, media_retr_reparto in stipendi_reparto.items():
    somma = sum(media_retr_reparto)
    conteggio = len(media_retr_reparto)
    media = somma / conteggio

    # SALVA la media nel NUOVO dizionario
    medie_reparti[reparti] = media  # {"Vendite": 2650, "IT": 3100, "HR": 2200}

    print(f"Stipendio medio per reparto {media} Reparto {reparti}")

print("=" * 80)

#3. DIPENDENTE con PIÙ ESPERIENZA (NUMERI)
#Nome e anni del più esperto

esperienza_max = 0
for dipendente in dipendenti:
    esperienza = dipendente["anni_esperienza"]

    if esperienza > esperienza_max:
        nomi = dipendente["nome"]
        esperienza_max = esperienza
print(f"Dipendente con piu' esperienza: {nomi} Anni Esperienza {esperienza_max}")

print("="*80)
#4. ORDINA per STIPENDIO (decrescente)
#Lista ordinata dal più pagato

dipendenti_ordinati = sorted(dipendenti, key=lambda x: x["stipendio"], reverse=True)

for i in dipendenti_ordinati:
    print(f"Nome: {i['nome']}")
    print(f"Retribuzione: {i['stipendio']}")

    #print()
print("=" * 80)

#5. REPARTO con STIPENDIO MEDIO PIÙ ALTO combinazione

reparto_migliore = []  # LISTA vuota
media_max = 0

for reparti, media in medie_reparti.items():
    if media > media_max:
        media_max = media
        reparto_migliore = [reparti]     # Ricomincia LISTA
    elif media == media_max:
        reparto_migliore.append(reparti) # Aggiungi a LISTA

# Stampa intelligente
if len(reparto_migliore) == 1:
    print(f"Reparto con media più alta: {reparto_migliore[0]} ({media_max})")
else:
    print(f"Reparti a pari merito ({media_max}): {', '.join(reparto_migliore)}")
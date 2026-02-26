from Dipendenti import dipendenti

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
print("=" * 80)

#Bonus esperienza: Calcolare stipendio + bonus (100€ per anno esperienza) per ogni dipendente.


for dipendente in dipendenti:
    stipendio_base = dipendente["stipendio"]
    nomi = dipendente["nome"]
    esperienza = dipendente["anni_esperienza"]
    if esperienza > 0:
        nuovo_stipendio = stipendio_base + (esperienza* 100)
    print(f"Nome Dipendente:{nomi:>10}    Nuovo Stipendio:{nuovo_stipendio:> 10}")

print("=" * 80)

#Soglia stipendio: Trovare tutti i dipendenti che guadagnano sopra 3000€.
stipendio_sopra_3000 = []
dipendenti_sopra_3000 = []

for dipendente in dipendenti:
    stipendi = dipendente["stipendio"]
    nomi = dipendente["nome"]
    reparti = dipendente ["reparto"]
    if stipendi > 3000:
        stipendio_sopra_3000.append(nomi)
        dipendenti_sopra_3000.append(dipendente)
        print(f"Dipendenti Stipendi sopra 3000: {nomi}  Importo {stipendi}€ {reparti}")


#Contatori avanzati: Numero dipendenti per reparto (usando len() sulle liste esistenti).


conteggio_valori = {k: len(v) for k, v in reparto.items()}

print(f" {conteggio_valori}")

for rep, num in conteggio_valori.items():
    print(f"Reparto {rep}: {num} dipendenti")


conteggio = {}
for d in dipendenti:
    r = d["reparto"]
    nomi = d["nome"]
    if r not in conteggio:
        conteggio[r] = 0
    conteggio[r] += 1

print(f" {conteggio}")

for chiave in reparto:
    lista_nomi = reparto[chiave]
    numero = len(lista_nomi)


for chiave, lista_nomi in reparto.items():
    print(chiave, len(lista_nomi))


#Filtro multiplo: Dipendenti IT con più di 3 anni esperienza.

repit_esp_sopra_3nni= []

for dipendente in dipendenti:
    a_esperienza = dipendente["anni_esperienza"]
    reparti = dipendente["reparto"]
    nomi = dipendente["nome"]
    if reparti == "IT" and a_esperienza > 3:
        repit_esp_sopra_3nni.append(nomi)

print(f"Nome {repit_esp_sopra_3nni}")

for i in repit_esp_sopra_3nni:
    print(f"Nome dipendente per repart IT con più di 3 anni di esperienza: {i}")

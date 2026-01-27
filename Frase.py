from collections import Counter
import re
testo = "python è fantastico e python è potente"

testo.count(testo)

print(f"Python appare {testo.count('python')} volte")

print(f"Numero parole {len(testo.split())}")

print(testo.split())

parole = testo.split()
parola = len(parole)

parola_lunga = max(parole, key=len)
print(f"La parola piu lunga é: {parola_lunga}")

parola_corta = min(parole, key=len)
print(f"La parola piu corta é: {parola_corta}")

ordina = sorted(parole, key=len)
print(f"L'ordine per lunghezza é: {ordina}")



parole = re.findall(r'\b\w+\b', testo.lower())
conteggio = Counter(parole)

print(conteggio)

conteggi = {}
for p in parole:
    conteggi[p] = conteggi.get(p, 0) + 1
print(conteggi)
























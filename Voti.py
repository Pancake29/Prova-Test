voti = [18, 25, 22, 30, 28, 15, 20, 24, 29, 17]
sufficienti = 0
insufficienti = 0
eccellenti = 0

for voto in voti:
    if voto >= 28:
        eccellenti += 1
    if 18 <= voto <= 27:
        sufficienti += 1
    if voto < 18:
        insufficienti += 1

print(f"Sufficienti: {sufficienti}")
print(f"Insufficienti: {insufficienti}")
print(f"Eccellenti: {eccellenti}")
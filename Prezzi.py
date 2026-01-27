prezzi = [15.99, 8.50, 22.30, 5.99, 45.00, 12.49, 33.75, 9.99, 28.60, 6.50]
#Conta quanti prodotti costano meno di 10€ (economici)
#Conta quanti prodotti costano più di 30€ (premium)
#Calcola il prezzo medio di tutti i prodotti
#Calcola il totale valore dell'inventario (somma tutti i prezzi)
#(Bonus) Trova il prodotto più economico e più costoso
economici = 0
premium = 0

for prezzo in prezzi:
    if prezzo > 30:
        premium += 1
    elif prezzo <= 10:
        economici +=1
    else:
        print()

print(f"Prodotti Premium {premium}")
print(f"Prodotti Economici {economici}")

sum(prezzi)
max(prezzi)
min(prezzi)
prezzo_medio = sum(prezzi) / len(prezzi)
totale_prezzi = sum(prezzi)
piu_costoso = max(prezzi)
meno_costoso = min(prezzi)

print(f"Prezzo Medio:  €  {prezzo_medio:,.2f} ")
print(f"Totale prezzi: € {totale_prezzi:,.2f} ")
print(f"Piu costoso:   €  {piu_costoso:,.2f} ")
print(f"Meno Costoso:  €   {meno_costoso:,.2f} ")







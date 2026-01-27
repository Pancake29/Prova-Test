# Crea un f-string che:
#
# Inserisca due variabili: product = "Laptop" e price = 899.99
#
# Calcoli l'IVA al 22% (price * 1.22)
#
# Mostri il prezzo finale formattato con 2 decimali e il simbolo €
#
# Esempio di output atteso: "Il Laptop costa 1097.99 € (IVA inclusa)"

Product = "laptop"
Price = 899.99
IVA = Price * 0.22
Costo = Price + IVA


print(f"Il laptop costa {Costo:.2f} € (Iva inclusa)")
print(f"Il {Product} costa {Price * 1.22:.2f} \u20AC (IVA inclusa)") # \u20AC euro


# Prova tutti e tre i metodi
prezzo = 1097.99

print("Metodo 1 (copia €):", f"{prezzo:.2f} €")
print("Metodo 2 (unicode):", f"{prezzo:.2f} \u20AC")
print("Metodo 3 (parola):", f"{prezzo:.2f} euro")

# Se vedi 3 righe con l'euro, funziona tutto!


numero = 1234.56789
print(f"{numero:.1f}")
print(f"{numero:,.2f}")

prezzi = [1234.567, 9876.543, 150.999]

for p in prezzi:
    print(f"{p:10,.2f} €")  # :10 = larghezza 10 caratteri, .2f = 2 decimali

# Output allineato:
#  1234.57 €
#  9876.54 €
#   151.00 €  (arrotondato da 150.999!)

#Crea una tabella di prodotti con:

#Nome prodotto (allineato a sinistra, larghezza 15)

#Prezzo (allineato a destra, larghezza 10, 2 decimali, separatore migliaia)

#Quantità (allineato a destra, larghezza 5, 0 decimali)

#Totale (prezzo × quantità, formattato come prezzo)

Pr1 = "Monitor"
Pr2 = "Mouse"
PxPr1 = 1015.99
PxPr2 = 89.90
QPr1 = 10
QPr2 = 10
TPr1 = PxPr1 * QPr1
TPr2 = PxPr2 * QPr2
print(f"{'Prodotto':<12} | {'Prezzo':>10} | {'Q.tà':>5} | {'Totale':>12}")
print("-" * 50)
print(f"{Pr1:<12} | {PxPr1:>7,.2f} € | {QPr1:>5} | {TPr1:>12,.2f} €")
print(f"{Pr2:<12} | {PxPr2:>8,.2f} € | {QPr2:>5} | {TPr2:>12,.2f} €")


prodotti = ["Monitor", "Mouse", "Tower"]
prezzi = [1015.99, 89.90, 3200.00]
quantita = [10, 10, 1]

print(f"{'Prodotto':<12} | {'Prezzo':>10} | {'Q.tà':>5} | {'Totale':>12}")
print("-" * 50)

for i in range(len(prodotti)):
    nome = prodotti[i]
    prezzo = prezzi[i]
    qta = quantita[i]
    totale = prezzo * qta

print(f"{nome:<12} | {prezzo:>10,.2f} € | {qta:>5} | {totale:>12,.2f} €")



#print(f"{'Pr1':<7} | {'Pr2':<7} | {'PxPr1':>7} | {'PxPr2':>7} | {'QPr1':>5} | {'QPr2':>5} | {'TPr1' :>6} | {'TPr2' :>6}")

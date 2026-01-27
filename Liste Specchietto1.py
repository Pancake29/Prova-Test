prodotti = ["Monitor", "Mouse", "Tower"]
prezzi = [1015.99, 89.90, 3200.00]
quantita = [10, 10, 1]
totale_generale = 0
totali = []


print(f"{'Prodotto':<12} | {'Prezzo':>10} | {'Q.tà':>5} | {'Totale':>12}")
print("-" * 50)

#for i in range(len(prodotti)):
    #nome = prodotti[i]
    #prezzo = prezzi[i]
    #qta = quantita[i]
    #totale = prezzo * qta

for nome, prezzo, qta in zip(prodotti, prezzi, quantita):

    totale = prezzo * qta
    #totale_generale += totale

    print(f"{nome:<12} | {prezzo:>10,.2f} € | {qta:>5} | {totale:>12,.2f} €")
    #print(f"'Totale Generale' {totale:>12,.2f} €")
    totali = [10159.90, 899.00, 3200.00]


Totale_generale=sum(totali)
Media_prezzi = sum(prezzi) / len(prezzi)
PrezzoMax = max(prezzi)
PrezzoMin = min(prezzi)
print(f"{'Totale Generale':<12} | voti = [8, 7, 9, 6, 10]


print(f"{'Prezzo medio':<15} | {'':>10} | {'':>5} | {Media_prezzi:>11,.2f} €")
print(f"{'Prezzo Max':<15} | {'':>10} | {'':>5} | {PrezzoMax:>11,.2f} €")
print(f"{'Prezzo Min':<15} | {'':>10} | {'':>5} | {PrezzoMin:>11,.2f} €")
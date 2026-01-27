prodotti = ["Monitor", "Mouse", "Tower"]
prezzi = [1015.99, 89.90, 3200.00]
quantita = [10, 10, 1]

#print(f"{'Prodotto':<12} | {'Prezzo':>10} | {'Q.tà':>5} | {'Totale':>12}")
print("-" * 50)

#for i in range(len(prodotti)):
    #nome = prodotti[i]
    #prezzo = prezzi[i]
    #qta = quantita[i]
    #totale = prezzo * qta

for nome, prezzo, qta in zip(prodotti, prezzi, quantita):

    totale = prezzo * qta

    print(f"{nome:<12} | {prezzo:>10,.2f} € | {qta:>5} | {totale:>12,.2f} €")
    print(f"{'TOTALE GENERALE':<12} | {'':>10} | {'':>5} | {sum(prezzo * qta for prezzo, qta in zip(prezzi, quantita)):>12,.2f} €")
    print(f"{'PREZZO MEDIO':<12} | {sum(prezzi) / len(prezzi):>10,.2f} € | {'':>5} | {'':>12}")
    print(f"{'MAX PREZZO':<12} | {max(prezzi):>10,.2f} € | {'':>5} | {'':>12}")
#Un programma che:

#Registra spese (descrizione, importo, categoria) \
#Calcola statistiche (totale, media, max/min spesa)
#Mostra report formattato come tabella
#Filtra per categoria (es. "Supermercato", "Trasporti")
#📝 Struttura Concettuale:
#text
#1. LISTA spese = [
    #["Pane", 2.50, "Supermercato"],
    #["Benzina", 45.00, "Trasporti"],
    #["Cinema", 12.00, "Svago"]


#2. FUNZIONI:
   #- totale_spese(spese)
   #- media_spese(spese)
   #- spesa_massima(spese)
   #- spesa_minima(spese)
   #- spese_per_categoria(spese, "Supermercato")

#3. OUTPUT:
   #TABELLA con tutte le spese + STATISTICHE

Categorie = ['Alimentari', 'Trasporti', 'Svago']
Prodotti = ['Pane','Benzina','Cinema']
PxPr = [2.50, 45.00, 12.00]
PxPane = 2.50
PxBenzina = 45.00
PxCinema = 12.00
print(f"{'':<15} | {'Alimentari':>15} | {'Trasporti':>15} | {'Svago':>15}")


for i in range(len(Prodotti)):
    nome = Prodotti[i]


    print(f"{nome:<15} | {PxPane:>14,.2f} € | {PxBenzina:>14,.2f} € | {PxCinema:>14,.2f}")
    #print(f"{nome:<15} | {'':>14,.2f} | {PxBenzina:>14,.2f} €")
   # print(f"{nome:<15} | {'':>14,.2f} | {'':>14,.2f} | {PxSvago:>14,.2f} €")


print("-" * 50)

sum(PxPr)
max(PxPr)
min(PxPr)

media_Spesa = sum(PxPr) / len(PxPr)


print(f"{'Totale Spesa':>13} | {'Spesa Media':>13} | {'Spesa Max':>10} | {'Spesa Min':>10}")
print(f"{sum(PxPr):>12} | {media_Spesa:>10,.2f} | {max(PxPr):>13} | {min(PxPr):>10}")







#for i in range Categorie, prodotti, qta in zip(prodotti, prezzi, quantita)
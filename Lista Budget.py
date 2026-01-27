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
LARGHEZZA_COLONNA = 15
LARGHEZZA_COLONNA1 = 13
#PxPane = 2.50
#PxBenzina = 45.00
#PxCinema = 12.00
print(f"{'':<{LARGHEZZA_COLONNA}} |    {'Alimentari':>{LARGHEZZA_COLONNA}} | {'Trasporti':>{LARGHEZZA_COLONNA}} | {'Svago':>{LARGHEZZA_COLONNA}}")
tot_cat = [0, 0, 0]
tot_alimentari = 0
tot_trasporti = 0
tot_svago = 0

for i in range(len(Prodotti)):
    nome = Prodotti[i]  # "Pane"
    categoria = Categorie[i]  # "Alimentari"
    prezzo = PxPr[i]  # 2.50

    celle = ['', '', '', '']
    celle[0] = nome



    # DECIDI:
    if categoria == "Alimentari":
        celle[1] = f"  {prezzo:>15.2f}€"
        tot_cat[0] += prezzo
        #print(f" {nome:<15} | {prezzo:>15} | {'':15} | {'':15}")
    elif categoria == "Trasporti":
        celle[2] = f"  {prezzo:>15.2f}€"
        tot_cat[1] += prezzo
        #print(f" {nome:<15} | {'':>15} | {prezzo:>15} | {'':>15}")
    elif categoria == "Svago":
        celle[3] = f"  {prezzo:>14.2f}€ "
        tot_cat[2] += prezzo
        #print(f"{nome:<15}  {'':>15} | {'':>15} | {:>15}")
    print(f"{nome:<{LARGHEZZA_COLONNA}}   {celle[1]:>{LARGHEZZA_COLONNA}}   {celle[2]:>{LARGHEZZA_COLONNA}}    {celle[3]:>{LARGHEZZA_COLONNA}}")

print("-" * 100)
print(f"{'TOTALI':<{LARGHEZZA_COLONNA}}     {tot_cat[0]:>{LARGHEZZA_COLONNA}.2f}€  {tot_cat[1]:>{LARGHEZZA_COLONNA}.2f}€  {tot_cat[2]:>{LARGHEZZA_COLONNA}.2f}€")


print("-" * 100)

sum(PxPr)
max(PxPr)
min(PxPr)

media_Spesa = sum(PxPr) / len(PxPr)

print("-" * 100)

print(f"{'Totale Spesa':>13} | {'Spesa Media':>13} | {'Spesa Max':>10} | {'Spesa Min':>10}")
print(f"{sum(PxPr):>13} | {media_Spesa:>13,.2f} | {max(PxPr):>10,.2f} | {min(PxPr):>10}")





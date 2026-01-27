#Usa zip() per scorrere le 3 liste insieme
#Per ogni cliente stampa:
"[Nome] ha fatto [X] acquisti spendendo €[Y]"
#Conta quanti clienti hanno fatto più di 3 acquisti
#Calcola la spesa media per cliente
#Trova il nome del cliente che ha speso di più
#Bonus:
#6. Crea una lista clienti_fedeli con i nomi di chi ha speso oltre 50€

nomi = ["Anna", "Luca", "Marco", "Sofia", "Elena"]
acquisti = [3, 5, 1, 4, 2]           # numero di acquisti nel mese
spese = [45.50, 120.30, 15.99, 85.20, 60.00]  # totale speso in €

contatore_acquisti_alti = 0
somma_spese = 0
spesa_max = 0
nome_spesa_max = ""
clienti_fedeli = []

for nome, acquisto, spesa in zip(nomi, acquisti,spese):

    print(f"{nome} ha fatto {acquisto} per un importo di {spesa}")

    if spesa > 50:
        clienti_fedeli.append(nome)

    if spesa > spesa_max:
        spesa_max = spesa
        nome_spesa_max = nome



print(f"I clienti fedeli sono {clienti_fedeli}")


print(f"Cliente che ha speso di più: {nome_spesa_max} con {spesa_max}€")






for spesa in acquisti:
    if spesa > 3:
        contatore_acquisti_alti +=1

print(f"\nClienti con più di 3 acquisti: {contatore_acquisti_alti}  ")
sum(spese)
max(spese)
sp_media = sum(spese) / len(nomi)
print(f"La spesa media e {sp_media}")
print(f"La spesa max e {max(spese)}")

for importo in spese:
    if importo > spesa_max:
        spesa_max = importo
        nome_spesa_max = clienti_fedeli








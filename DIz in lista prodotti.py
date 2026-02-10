prodotti = [{"nome": "Pane", "prezzo": 2.5}, {"nome": "Latte", "prezzo": 1.8}]


#Devi:

#Prendere ogni prodotto

#Calcolare prezzo con IVA (22%)

#Stampare "Prodotto X costa Y"
costo_totale = 0
totale_iva = 0
costo_complessivo = 0
for prodotto in prodotti:
    print(prodotto["nome"])

print("="*45)

for beni in prodotti:
    prezzo = beni["prezzo"]
    nome = beni["nome"]
    iva = prezzo * 0.22
    totale_iva +=iva
    totale = prezzo + iva
    costo_totale +=prezzo
    costo_complessivo = costo_totale + totale_iva



    print(f"Prodotto {prodotto["nome"]}  costa  {str(totale)}")

print("="*45)
print(f"Costo prodotti {costo_complessivo:,.2f}")

print("="*45)

prezzo_massimo = 0
prezzo_minimo = 1000

for bene in prodotti:
    prezzi = bene["prezzo"]
    if prezzi > prezzo_massimo:
        prezzo_massimo = prezzi

print(f"Prezzo massimo {prezzo_massimo}")

for articolo in prodotti:
    price = articolo["prezzo"]
    if price < prezzo_minimo:
        prezzo_minimo = price

print(f"Prezzo minimo {prezzo_minimo}")
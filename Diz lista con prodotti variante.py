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
nome_caro = " "
nome_economico = ""
for bene in prodotti:
    prezzi = bene["prezzo"]
    nome = bene["nome"]


    if prezzi > prezzo_massimo:
        prezzo_massimo = prezzi
        nome_caro = nome

    if prezzi < prezzo_minimo:
        prezzo_minimo = prezzi
        nome_economico = nome


print(f"Prezzo massimo {nome_caro}  {prezzo_massimo}")

print(f"Prezzo minimo {nome_economico} {prezzo_minimo}")
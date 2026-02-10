negozio = [
    {"prodotto": "Maglia", "quantità": 10, "prezzo": 20},
    {"prodotto": "Pantalone", "quantità": 5, "prezzo": 35},
    {"prodotto": "Cappello", "quantità": 15, "prezzo": 12}
]
#MISSIONI (scegline una):
#Valore totale inventario = somma di (quantità × prezzo) per ogni prodotto

#Prodotto con più unità in magazzino (massimo quantità)

#Prodotto più costoso (massimo prezzo)
Prezzo_prodotti = 0
Prezzo_complessivo = 0
Prodotto_quantità_maggiore = 0
Nome_quantità_maggiore = ""
Prodotto_più_costoso = 0
nome_max_prezzo = ""

for prodotti in negozio:
    prezzo = prodotti["prezzo"]
    numero = prodotti["quantità"]
    nome = prodotti["prodotto"]

    quantità = prodotti["quantità"]
    Prezzo_prodotti = prezzo * numero
    Prezzo_complessivo += Prezzo_prodotti

    if quantità > Prodotto_quantità_maggiore:
        Prodotto_quantità_maggiore = quantità
        Nome_quantità_maggiore = nome

    if prezzo > Prodotto_più_costoso:
        Prodotto_più_costoso = prezzo
        nome_max_prezzo= nome

    print(f"Prezzo prodotto: {nome} {Prezzo_prodotti}")

print(f"Prezzo complessivo prodotti {Prezzo_complessivo}")
print(f"Prodotto quantità maggiore: {Nome_quantità_maggiore} {Prodotto_quantità_maggiore}")
print(f"Prodotto prezzo maggiore: {nome_max_prezzo}  {Prodotto_più_costoso}")


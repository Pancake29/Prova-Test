lista1 = [1, 2, 3]
lista2 = lista1
lista3 = lista1.copy()

print(id(lista1), id(lista2), id(lista3))
# Cosa pensi che stamperà? Quali id saranno uguali e quali diversi?lista1 = [1, 2, 3]
# lista2 = lista1
# lista3 = lista1.copy()
#
# print(id(lista1), id(lista2), id(lista3))
# # Cosa pensi che stamperà? Quali id saranno uguali e quali diversi?


# PERICOLO: Modifica inaspettata
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 è un ALIAS, non una copia

print(f"Stesso id? {id(lista1) == id(lista2)}")  # True → STESSO OGGETTO

lista1.append(999)
print(f"Dopo lista1.append(999):")
print(f"lista1 = {lista1}")  # [1, 2, 3, 999]
print(f"lista2 = {lista2}")  # [1, 2, 3, 999] ← ANCHE lista2 CAMBIATA!


# CASO 1: Oggetti DIVERSI hanno ID DIVERSI
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"a e b hanno lo stesso id? {id(a) == id(b)}")  # False
# Anche se le liste hanno gli STESSI VALORI, sono OGGETTI DIVERSI in memoria!

# CASO 2: Assegnazione crea un "ALIAS" (stesso oggetto, stesso id)
c = a  # c diventa un RIFERIMENTO alla STESSA lista di a
print(f"\nc = a (assegnazione)")
print(f"id(a) = {id(a)}, id(c) = {id(c)}")
print(f"a e c hanno lo stesso id? {id(a) == id(c)}")  # True
# Modificando a, cambi anche c perché puntano allo stesso oggetto!
a.append(4)
print(f"Dopo a.append(4): a = {a}, c = {c}")

# CASO 3: Interi piccoli hanno ID speciali (ottimizzazione di Python)
x = 10
y = 10
print(f"\nx = 10, id(x) = {id(x)}")
print(f"y = 10, id(y) = {id(y)}")
print(f"x e y hanno lo stesso id? {id(x) == id(y)}")  # True (per numeri piccoli!)
# Python ottimizza: interi tra -5 e 256 sono "singleton"
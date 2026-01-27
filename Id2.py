# 1. COPIA DI LISTA: .copy() vs list()
lista = [1, 2, 3]

# Metodo (più chiaro per liste)
copia_metodo = lista.copy()

# Built-in (funziona anche con altri iterabili)
copia_builtin = list(lista)        # list() è built-in
copia_da_tupla = list((1, 2, 3))  # Converti tupla in lista
copia_da_stringa = list("abc")    # ['a', 'b', 'c']

print(id(lista) != id(copia_metodo) != id(copia_builtin))  # Tutti oggetti diversi

# 2. CONTEGGIO: .count() vs len()
numeri = [1, 2, 2, 3, 2, 4]

# Metodo: conta QUANTE VOLTE compare un valore specifico
conteggio_2 = numeri.count(2)      # 3 (il 2 compare 3 volte)

# Built-in: conta TUTTI gli elementi
totale_elementi = len(numeri)      # 6 (elementi totali)

# 3. CONVERSIONE A STRINGA: .join() vs str()
lista = ['a', 'b', 'c']

# Metodo: unire elementi di una lista con separatore
stringa_unita = '-'.join(lista)    # 'a-b-c'

# Built-in: convertire QUALSIASI oggetto in stringa
numero = 42
stringa_numero = str(numero)       # '42'
stringa_lista = str(lista)         # "['a', 'b', 'c']" (rappresentazione)
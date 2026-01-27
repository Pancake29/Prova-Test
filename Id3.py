#Gli esercizi da risolvere erano questi (senza soluzione, per te):

# 1 - Contare quanti elementi ha [10, 20, 30, 40]? → len()

# 2 - Creare una nuova lista ordinata da [3, 1, 2] senza modificarla? → sorted()

# 3 - Unire le parole ['Ciao', 'mondo'] con uno spazio? → .join() (metodo)

# 4 - Convertire il numero 123 in stringa? → str()



# 1
lista = [1, 3, 7, 2, 4]
print (len(lista))
#2
print(sorted(lista))

# 3
parole = ['Ciao', 'mondo']
frase = ' '.join(parole)
print(f"3. Frase unita: '{frase}'")

# 4


name = "Peter"
age = 25

# 1. f-string (MODERNO, CONSIGLIATO)
print(f"My name is {name} and I am {age} years old.")

# 2. format() (VECCHIO MA ANCORA VALIDO)
print("My name is {} and I am {} years old.".format(name, age))

# 3. %-formatting (MOLTO VECCHIO, EVITARE)
print("My name is %s and I am %d years old." % (name, age))

prezzi = [1234.567, 9876.543, 150.999, 1000000.5]

print("Larghezza 12:")
for p in prezzi:
    print(f"|{p:12,.2f} €|")

print("\nLarghezza 15:")
for p in prezzi:
    print(f"|{p:15,.2f} €|")


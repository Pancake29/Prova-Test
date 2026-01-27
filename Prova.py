from operator import add

number = (5)
type(number)
print(type(number))

help(list)
help
help(add)
Lista = [1, 2, 4, 5, 9, 10]
len(Lista)
print(len(Lista))

help(isinstance)

Dic = {'a': 1, 'b': 2, 'c': 3, 'cba': 321}
print(isinstance(Dic, dict))
========================================================
def raddoppia(valore):
    """Raddoppia un numero. Se non è un numero, informa l'utente."""
    if not isinstance(valore, (int, float)):  # Controlla se è un numero intero O decimale
        print(f"Errore: {valore} non è un numero. Fornisci un int o float.")
        return None  # Esce dalla funzione senza causare un crash
    return valore * 2

# Test
print(raddoppia(10))     # Funziona: 20
print(raddoppia("ciao")) # Messaggio di errore controllato, nessun crash

============================================================
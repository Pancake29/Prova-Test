import re

# ESEMPIO 1: Estrai tutti i numeri da un testo
testo1 = "Ho 3 mele, 12 arance e 100 euro"
numeri = re.findall(r'\d+', testo1)
print(f"1. Numeri trovati: {numeri}")
# Output: ['3', '12', '100']

# ESEMPIO 2: Trova parole che iniziano con maiuscola
testo2 = "Python e Java sono linguaggi. javascript no."
parole_maiuscole = re.findall(r'\b[A-Z][a-z]*\b', testo2)
print(f"2. Parole maiuscole: {parole_maiuscole}")
# Output: ['Python', 'Java']

# ESEMPIO 3: Sostituisci numeri con "NUM"
testo3 = "Prezzo: 50€, Sconto: 20%"
sostituito = re.sub(r'\d+', 'NUM', testo3)
print(f"3. Dopo sostituzione: {sostituito}")
# Output: "Prezzo: NUM€, Sconto: NUM%"

# ESEMPIO 4: Estrai email
testo4 = "Contatti: mario@email.com, luigi@azienda.it"
email = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', testo4)
print(f"4. Email trovate: {email}")
# Output: ['mario@email.com', 'luigi@azienda.it']

# ESEMPIO 5: Dividi per punteggiatura
testo5 = "Ciao! Come stai? Bene, grazie."
parole = re.split(r'[!?.,]\s*', testo5)
print(f"5. Frasi separate: {parole}")
# Output: ['Ciao', 'Come stai', 'Bene', 'grazie', '']

# ESEMPIO 6: Conta vocali
testo6 = "Regular Expressions"
vocali = re.findall(r'[aeiouAEIOU]', testo6)
print(f"6. Vocali trovate ({len(vocali)}): {vocali}")
# Output: Vocali trovate (7): ['e', 'u', 'a', 'E', 'e', 'i', 'o']

# ESEMPIO 7: Trova orari (hh:mm)
testo7 = "Riunione alle 09:30 e poi alle 14:45"
orari = re.findall(r'\b\d{2}:\d{2}\b', testo7)
print(f"7. Orari: {orari}")
# Output: ['09:30', '14:45']

testo = "Ciao! Come stai? Bene."
# Puoi dividere solo per UN separatore fisso:
parti = testo.split("! ")
# ['Ciao', 'Come stai? Bene.']  ← solo "!", ignora "?"
print(parti)

parti_re = re.split(r'[!?.]\s*', testo)  # [!?.] = ! O ? O .
print(parti_re)  # ['Ciao', 'Come stai', 'Bene', '']
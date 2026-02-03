persone = [
    {"nome": "Mario", "età": 25, "città": "Roma"},
    {"nome": "Anna", "età": 30, "città": "Milano"},
    {"nome": "Luca", "età": 22, "città": "Napoli"}
]
anni_persona = 0
conta_over25 = 0


for persona in persone:
    print(persona["nome"])


for persona in persone:

    anni = persona["età"]

    if anni > 25:
        conta_over25 +=1
        print( conta_over25, persona["nome"])


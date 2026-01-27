class Animale:
    def __init__(self, nome):
        self.nome = nome
        print(f"Animale {self.nome} creato")

class Cane(Animale):
    def __init__(self, nome, razza):
        super().__init__(nome)  # Chiama il __init__ di Animale
        self.razza = razza      # Aggiunge un attributo proprio
        print(f"È un {self.razza}")

pluto = Cane("Pluto", "Labrador")
# Output:
# "Animale Pluto creato"
# "È un Labrador"
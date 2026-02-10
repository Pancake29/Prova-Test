lista_generi = generi["genere"]
for genere_nome in lista_generi:
        if genere_nome not in cantante_per_genere:
            cantante_per_genere[generi] = []
        cantante_per_genere[genere_nome].append(nomi)

print("titolo: " + nomi + " - genere: " + genere_nome)
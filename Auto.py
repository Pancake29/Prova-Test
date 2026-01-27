automobili = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tempi = [45.3, 52.1, 48.9, 47.2, 55.0, 51.8, 46.5, 53.7, 49.4, 50.6]
auto_tempi_inf_media = []
conteggio = 0

somma_tempi = sum(tempi)
print(f"Somma dei tempi {somma_tempi}")

tempo_piu_veloce = min(tempi)
print(f"Tempo piu veloce {tempo_piu_veloce}")

tempo_meno_veloce = max(tempi)
print(f"Tempo meno veloce {tempo_meno_veloce}")

media_tempi = somma_tempi / len(automobili)
print(f"Media tempi {media_tempi}")


for auto, tempo in zip(automobili, tempi):
    if tempo < 50:

        print(f"Auto Sotto la media {auto}   {tempo}")

    if tempo < media_tempi:
        auto_tempi_inf_media.append(str(auto))
        conteggio +=1
numeri_str = ", ".join(auto_tempi_inf_media)

print(f"Automobili con tempo inferiore alla media ({media_tempi}s): {numeri_str}")
print(f"Totale: {conteggio} auto")


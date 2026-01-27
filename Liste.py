voti = [8, 7, 9, 6, 10]
sum(voti)
max(voti)
min(voti)
len(voti)
media_voti = sum(voti) / len(voti)
delta_voti = max(voti) - min(voti)
print(f"{'Somma dei voti':>10} | {'Voto Max':>10} | {'Voto Min':>10} | {'Numero voti':>10} | {'Media voti':>10} | {'Delta voti':>10}")
print(f"{sum(voti):>13}  | {max(voti):>10} | {min(voti):>10} | {len(voti):>11} | {media_voti:>10} | {delta_voti:>10}")
#print(f"{'Media Voti':<25}  | {'':>10} | {'':>9}  | {media_voti:>10} | {delta_voti:>10}")
#print(f"{'Delta Max/Min':<25}  | {'':>10} | {'':>9}  | {delta_voti:>10}")


from collections import Counter

with open("Criptograma_1.txt", "r", encoding="utf-8") as f:
    texto = f.read()

texto_limpio = texto.replace(" ", "").replace("\n", "")
contador = Counter(texto_limpio)
total_letras = sum(contador.values())

print(f"Total de letras: {total_letras}\n")
print("Letra | Cantidad | Porcentaje")
print("-----------------------------")
for letra, cantidad in sorted(contador.items(), key=lambda x: x[1], reverse=True):
    porcentaje = (cantidad / total_letras) * 100
    print(f"  {letra}   |   {cantidad:7d} | {porcentaje:9.2f}%")
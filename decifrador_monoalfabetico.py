def decifrador(texto, alfabeto):
    resultado = ""

    for letra in texto:
        if letra in alfabeto:
            resultado+= alfabeto[letra]
        else:
            resultado+=letra
    
    return resultado

alfabeto = {
    "I": "E",
    "D": "Q",
    "T": "U",
    "G": "L",
    "Y": "Y",
    "V": "A",
    "Q": "D",
    "A": "I",
    "U": "V",
    "P": "R",
    "J": "N",
}

with open("Criptograma_2.txt", "r", encoding="UTF-8") as f:
    lectura = f.read()
print(f"Cifrado : {lectura}")

print("="*105)

print(f"Decifrado parcial: {decifrador(lectura,alfabeto)}")
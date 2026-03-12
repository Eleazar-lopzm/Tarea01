def decifrador(texto, alfabeto):
    resultado = ""

    for letra in texto:
        if letra in alfabeto:
            resultado+= alfabeto[letra]
        else:
            resultado+=letra
    
    return resultado

alfabeto = {
    "A": "I",
    "B": "J",
    "C": "D",
    "D": "F",
    "E": "B",
    "F": "K",
    "G": "L",
    "H": "M",
    "I": "E",
    "J": "N",
    "K": "O",
    "L": "P",
    "M": "Q",
    "N": "C",
    "O": "G",
    "P": "R",
    "Q": "S",
    "R": "T",
    "S": "H",
    "T": "U",
    "U": "V",
    "V": "A",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z"
}

with open("Criptograma_2.txt", "r", encoding="UTF-8") as f:
    lectura = f.read()
print(f"Cifrado : {lectura}")

print("="*105)

print(f"Decifrado parcial: {decifrador(lectura,alfabeto)}")
""" ALFABETO_NORMAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" """

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
    "M": "Q",
    "T": "U",
    "G": "L",
    "Y": "Y",
    "V": "A",
    "Q": "S",
    "A": "I",
    "U": "V",
    "P": "R",
    "J": "N",
    "O": "G",
    "R": "T",
    "K": "O",
    "L": "P",
    "N": "C",
    "B": "P",
    "S": "H",
    "C": "D",
    "D": "F",
    "H": "M",
    
}

""" def revisar_letras():
    faltantes = []
    for letra in ALFABETO_NORMAL:
        if letra not in alfabeto.values():
            faltantes.append(letra)

    return faltantes

print(revisar_letras()) """

with open("Criptograma_2.txt", "r", encoding="UTF-8") as f:
    lectura = f.read()
print(f"Cifrado : {lectura}")

print("="*105)

print(f"Decifrado parcial: {decifrador(lectura,alfabeto)}")
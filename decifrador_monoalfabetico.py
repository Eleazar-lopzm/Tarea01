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
    "Y": "Y",
    "V": "O",
    "A": "I",
    "G": "L",
    "K": "A"
}

texto = input("Ingresa el texto: ")

print(decifrador(texto,alfabeto))
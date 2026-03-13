with open("Criptograma_2.txt", "r", encoding="UTF-8") as f:
    lectura = f.read()


def contador_aparciones_ngrama(datos,longitud):
    digramas = {}
    datos = datos.split(" ")
    for palabra in datos:
        if len(palabra) == longitud:
            digramas[palabra] = digramas.get(palabra, 0) + 1

    return digramas

def imprimir(digramas,texto1):
    
    print(f"{texto1 :<10} | {'Cantidad' :>10}")
    print("="*30)
    for ngrama, cantidad in sorted(digramas.items(), key=lambda x: x[1], reverse=True):
        print(f"{ngrama:<10} | {cantidad:>10}")
    
    print("="*30)

def letras_dobles(datos):

    dobles = {}

    palabras = datos.split(" ")

    for palabra in palabras:
        for i in range(len(palabra)-1):
            if palabra[i] == palabra[i+1]:
                patron = palabra[i] + palabra[i]
                dobles[palabra] = dobles.get(palabra,0) +1
    return dobles


ngramas = contador_aparciones_ngrama(lectura,3)
imprimir(ngramas, "N-grama")

imprimir(letras_dobles(lectura), "DobleLetra")


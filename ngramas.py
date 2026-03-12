""" ruta = input("Ingresa la ruta del archivo: ") """
with open("Criptograma_2.txt", "r", encoding="UTF-8") as f:
    lectura = f.read()


def contador_aparciones_ngrama(datos,longitud):
    digramas = {}
    datos = datos.split(" ")
    for palabra in datos:
        if len(palabra) == longitud:
            digramas[palabra] = digramas.get(palabra, 0) + 1

    return digramas

def imprimir(digramas):
    
    print(f"{'N-grama':<10} | {'Cantidad':>10}")
    print("_"*30)
    for ngrama, cantidad in sorted(digramas.items(), key=lambda x: x[1], reverse=True):
        print(f"{ngrama:<10} | {cantidad:>10}")


digramas = contador_aparciones_ngrama(lectura,3)
imprimir(digramas)

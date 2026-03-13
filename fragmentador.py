def vigenere_cifrar(texto, clave):
    #Primero el texto en mayúsculas -> partimos en arreglo -> juntamos el arreglo -> quitamos espacios
    texto = ''.join(texto.upper().split())
    clave = clave.upper()

    resultado = ""
    #NOTA: ord hace que la letra la mapee a ascii, es decir, ord(a) es 65
    for i in range(len(texto)):
        #la p es, la letra del texto que cifraremos, y se le resta a para saber que letra es en nuestro alfabeto normal
        p = ord(texto[i]) - ord('A')
        #la k itera con módulo por la palabra cifrada, si excede las 9 letras, se vuelve a reiniciar, y mismo caso que con p, se le resta a para saber el número en el
        #alfabeto normal
        k = ord(clave[i % len(clave)]) - ord('A')
        #fórmula para recorrer nuestra tabla de cifrado
        c = (p + k) % 26
        #se anexa el resultado, es la inversa de los primeros casos, como es alfabeto normal, le sumamos A para hacerlo en ascii
        resultado += chr(c + ord('A'))

    #aquí solo se parte en base al tamaño de la clave
    tamaño = len(clave)
    fragmentos = [resultado[i:i+tamaño] for i in range(0, len(resultado), tamaño)]

    return fragmentos


texto = "PROMETEO ES EL TITAN AMIGO DE LOS MORTALES HONRADO PRINCIPALMENTE POR ROBAR EL FUEGO DE LOS DIOSES DARLO A LOS HOMBRES PARA SU USO Y POSTERIORMENTE SER CASTIGADO POR ZEUS POR ESTE MOTIVO"
clave = "MITOLOGIA"

print(vigenere_cifrar(texto, clave))
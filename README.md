# SOLUCIONES - CÓDIGO

Aquí se encuentran los códigos auxiliares usados para la tarea 01 de la materia **Criptografía y Seguridad**, los propietarios de las soluciones son:

- Castillo Hernández Antonio - 320017438  
- Sánchez Tapia Oscar - 320266076  
- Reyna Méndez Cristian Ignacio - 320149579  
- López Montúfar José Eleazar - 320207219  
- Garcia Ruiz Angel Isaac - 320139198  

## Prerrequisitos

Para ejecutar los códigos, asegúrese de tener instalado Python. No se requieren librerías externas fuera de la biblioteca estándar de Python.

```bash
python3 --version
```

## Ejecución

A continuación se muestra cómo ejecutar cada uno de los scripts proporcionados, todos los scripts deben de ejecutarse desde la terminal en el directorio principal del proyecto (`Tarea01`).


### 1. Cifrado Afín

Este script cifra un texto en claro utilizando la función afín $f(x) = (23x + 5) \pmod{26}$.

```bash
python3 cifrado_afin.py
```

**Salida esperada:** Muestra el texto original y su correspondiente texto cifrado.

### 2. Contador de Letras (Análisis de Frecuencias)

Cuenta la frecuencia de aparición de cada letra en un texto y calcula su porcentaje, ordenándolas de mayor a menor. 

```bash
python3 contador_letras.py
```

**Salida esperada:** Una tabla formateada con la letra, cantidad total de apariciones y el porcentaje de frecuencia.

### 3. Descifrador Monoalfabético (Criptograma 2)

Aplica un diccionario de sustitución (llave) definido manualmente tras el análisis de frecuencias para descifrar un texto cifrado por sustitución simple.

```bash
python3 decifrador_monoalfabetico.py
```

**Salida esperada:** Imprime el texto cifrado original y debajo el texto en claro (descifrado parcial/total) con la historia de los presagios funestos.

### 4. Descifrador Afín (Criptograma 1)

Toma el texto cifrado del Criptograma 1 y aplica la función de descifrado afín calculada matemáticamente: $f^{-1}(y) = 15(y - 8) \pmod{26}$ (derivada de la llave $a=7, b=8$).

```bash
python3 descifrador_afin.py
```

**Salida esperada:** Muestra la llave utilizada y el texto descifrado.

### 5. Fragmentador (Cifrado de Vigenère)

Utilizado como apoyo para el Punto 2. Este script toma una cadena de texto continuo y la divide en bloques de un tamaño específico (en este caso, bloques de 9 caracteres, que es la longitud de la palabra clave ***mitologia***) para facilitar la lectura del texto cifrado por Vigenère.

```bash
python3 fragmentador.py
```

**Salida esperada:** Un arreglo (lista) con los fragmentos del texto cifrado.

### 6. Buscador de N-gramas 

Script de apoyo para el Criptograma 2. Busca e imprime la frecuencia de digramas, trigramas y letras dobles (ej. "LL", "RR", "CC") para ayudar a identificar patrones característicos del idioma español (como el trigrama "DTI" $\to$ "QUE" o el digrama "GG" $\to$ "LL").

```bash
python3 ngramas.py
```

**Salida esperada:** Dos tablas; la primera muestra la cantidad de N-gramas (trigramas de 3 letras) repetidos y la segunda muestra las secuencias que contienen letras dobles idénticas juntas.

Algoritmo sin_titulo
	
    // Solicitar al usuario que ingrese un n�mero entre 1 y 10
    ESCRIBIR "Ingrese un n�mero entre 1 y 10: "
    LEER numero
	
    // Validar que el n�mero est� en el rango correcto
    SI numero < 1 O numero > 10 ENTONCES
        ESCRIBIR "El n�mero debe estar entre 1 y 10."
    SINO
        // Generar y mostrar la tabla de multiplicar del n�mero
        PARA i DESDE 1 HASTA 10 HACER
            ESCRIBIR numero, " x ", i, " = ", numero * i
        FIN PARA
    FIN SI

FinAlgoritmo

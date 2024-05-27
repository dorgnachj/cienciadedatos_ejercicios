Algoritmo sin_titulo
	
    // Solicitar al usuario que ingrese un número entre 1 y 10
    ESCRIBIR "Ingrese un número entre 1 y 10: "
    LEER numero
	
    // Validar que el número esté en el rango correcto
    SI numero < 1 O numero > 10 ENTONCES
        ESCRIBIR "El número debe estar entre 1 y 10."
    SINO
        // Generar y mostrar la tabla de multiplicar del número
        PARA i DESDE 1 HASTA 10 HACER
            ESCRIBIR numero, " x ", i, " = ", numero * i
        FIN PARA
    FIN SI

FinAlgoritmo

Algoritmo ejercicio6
	
    // Solicitar al usuario que ingrese un número
    ESCRIBIR "Ingrese un número: "
    LEER numero
	
    // Mostrar solo los números pares desde 0 hasta el número ingresado
    ESCRIBIR "Números pares desde 0 hasta ", numero, ":"
    PARA i DESDE 0 HASTA numero HACER
        SI i % 2 == 0 ENTONCES
            ESCRIBIR i
        FIN SI
    FIN PARA

FinAlgoritmo

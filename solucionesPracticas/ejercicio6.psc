Algoritmo ejercicio6
	
    // Solicitar al usuario que ingrese un n�mero
    ESCRIBIR "Ingrese un n�mero: "
    LEER numero
	
    // Mostrar solo los n�meros pares desde 0 hasta el n�mero ingresado
    ESCRIBIR "N�meros pares desde 0 hasta ", numero, ":"
    PARA i DESDE 0 HASTA numero HACER
        SI i % 2 == 0 ENTONCES
            ESCRIBIR i
        FIN SI
    FIN PARA

FinAlgoritmo

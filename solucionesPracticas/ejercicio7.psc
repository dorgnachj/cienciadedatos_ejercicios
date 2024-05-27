Algoritmo sin_titulo
	
    // Inicializar la suma de notas a 0
    sumaNotas = 0
	
    // Solicitar el número de estudiantes que rindieron el examen
    ESCRIBIR "Ingrese el número de estudiantes que rindieron el examen: "
    LEER numEstudiantes
	
    // Solicitar las notas de cada estudiante y calcular la suma de las notas
    PARA i DESDE 1 HASTA numEstudiantes HACER
        ESCRIBIR "Ingrese la nota del estudiante ", i, ": "
        LEER nota
        sumaNotas = sumaNotas + nota
    FIN PARA
	
    // Calcular el promedio de notas
    promedio = sumaNotas / numEstudiantes
	
    // Mostrar el promedio y evaluar el rendimiento
    ESCRIBIR "El promedio de las notas es: ", promedio
	
    SI promedio > 8 ENTONCES
        ESCRIBIR "El rendimiento ha sido elevado."
    SINO SI promedio >= 6 Y promedio <= 8 ENTONCES
			ESCRIBIR "El rendimiento ha sido aceptable."
		SINO
			ESCRIBIR "El rendimiento ha sido bajo."
		FIN SI

FinAlgoritmo

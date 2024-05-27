Algoritmo sin_titulo
    Escribir "Ingrese la cantidad de unidades que desea comprar: "
	Leer productos
	Escribir "¿Usted es jubilado?(si/no): "
	Leer jubilado
	
	si esjubilado = "si" Entonces
		Escribir "verdadero"
	SiNo
		Escribir "Falso"
	FinSi
	si productos > 12 Entonces
		Escribir "Descuento de 0.10"
	SiNo 
		Escribir "Descuento de 0.15"
	FinSi
	
	costoTotal=preicoUnidad*cantidad
	costofinal=costoTotal*productos
	Escribir "El costo total a pagar es: ",costofinal
FinAlgoritmo

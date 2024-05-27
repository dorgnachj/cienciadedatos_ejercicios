Algoritmo despensa
    
    // Inicializar precio por unidad
    precioUnidad = 1000
    
    // Solicitar al cliente la cantidad de unidades que desea comprar
    ESCRIBIR "Ingrese la cantidad de unidades que desea comprar: "
    LEER cantidad
    
    // Preguntar si el cliente es jubilado
    ESCRIBIR "¿Es usted jubilado? (SI/NO): "
    LEER respuesta
    
    SI respuesta = "SI" ENTONCES
        esJubilado = VERDADERO
    SINO
        esJubilado = FALSO
    FIN SI
    
    // Inicializar descuento a 0
    descuento = 0
    
    // Determinar el descuento basado en la cantidad de unidades compradas
    SI cantidad > 24 ENTONCES
        descuento = 0.15
    SINO SI cantidad > 12 ENTONCES
			descuento = 0.10
		FIN SI
		
		// Aplicar descuento adicional para jubilados
		SI esJubilado ENTONCES
			descuento = descuento + 0.10
		FINSI
		
		// Calcular el costo total sin descuentos
		costoTotal = precioUnidad * cantidad
		
		// Calcular el costo final aplicando el descuento
		costoFinal = costoTotal * (1 - descuento)
		
		// Mostrar el costo final al cliente
		ESCRIBIR "El costo total a pagar es: ", costoFinal, " pesos."
	FinSi
	

FinAlgoritmo


#Ejercicio1
#nota1 = int(input("Ingrese la nota de la materia 1: "))
#nota2 = int(input("Ingrese la nota de la materia 2: "))
#nota3 = int(input("Ingrese la nota de la materia 3: "))
#nota4 = int(input("Ingrese la nota de la materia 4: "))
#nota5 = int(input("Ingrese la nota de la materia 5: "))

#suma = (nota1+nota2+nota3+nota4+nota5)/5


#print(f"El promedio de notas es de {suma} ")

#Ejercicio2
#ancho = int(input("Ingrese el ancho de la pared en metros: "))
#alto = int(input("Ingrese el alto de la pared en metros: "))
#costo = int(input("Ingrese el costo de mano de obra por metro: "))

#area = ancho*alto
#costoFinal = area*costo

#print(f"El costo final es de {costoFinal} de mano de obra")

#Ejercicio3
#producto_leche = int(input("Ingrese la cantidad de leche que desea comprar: "))
#jubilado = input("Ingrese (no) si el cliente no es jubilado o ingrese (si) si lo es: ")

#monto = producto_leche*1000
#print(f"producto_leche {producto_leche} jubilado {jubilado} ")

#if producto_leche <= 12 and not jubilado:
 #   print("producto_leche <= 12 and not jubilado")
  #  montoapagar = monto
#elif producto_leche > 12 and producto_leche <= 24 and not jubilado:
 #   print("producto_leche > 12 and producto_leche <= 24 and not jubilado:")
  #  montoapagar = monto*0.9
#elif producto_leche > 24 and not jubilado:
 #   print("producto_leche > 24 and not jubilado")
 #   montoapagar = monto*0.85
#elif producto_leche <= 12 and jubilado:
 #   print("producto_leche <= 12 and jubilado")
  #  montoapagar = monto+0.9
#elif (producto_leche > 12 and producto_leche <= 24)and jubilado:
 #   print("producto_leche > 12 and producto_leche <= 24)and jubilado")
  #  montoapagar = monto*0.8
#elif producto_leche > 24 and jubilado:
 #   print("producto_leche > 24 and jubilado")
  #  montoapagar = monto*0.75

#print(f"El monto sin descuento es de: {monto} y el monto a pagar es de: {montoapagar} ")

#Ejercicio3
#unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente:"))
#esJubilado = int(input("Ingrese 0  si el cliente no es jubilado,1 si el cliente es Jubilado: "))

#montoParcial = unidadesDeLeche * 1000
#print(f"unidadesDeLeche {unidadesDeLeche} esJubilado {esJubilado}")
#unidadesDeLeche = 15 y esJubilado=1
#if(unidadesDeLeche <=12 and not esJubilado):
 #   print("unidadesDeLeche <=12 and not esJubilado")
  #  montoAPagar = montoParcial
#elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubilado):
 #   print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubilado")
  #  montoAPagar = montoParcial * 0.9
#elif(unidadesDeLeche > 24 and not esJubilado):
 #   print("unidadesDeLeche > 24 and not esJubilado")
  #  montoAPagar = montoParcial * 0.85
#elif(unidadesDeLeche <=12 and esJubilado):
 #   print("unidadesDeLeche <=12 and esJubilado")
  #  montoAPagar = montoParcial * 0.9
#elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubilado):#ok
 #   print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubilado")#ok
  #  montoAPagar = montoParcial * 0.8
#elif(unidadesDeLeche > 24 and esJubilado):
 #   print("unidadesDeLeche > 24 and esJubilado")
  #  montoAPagar = montoParcial * 0.75

#print(f"El monto sin descuento es: {montoParcial} y el monto total a pagar es: {montoAPagar}")


#Ejercicio4
#numero = int(input("Ingrese un numero: "))

#for i in range(0, numero + 1):
 #   print(i)

#Ejercicio5
#numero = int(input("Ingrese un numero: "))

#for i in range(0, numero + 1):
 #   if i % 2 == 0:
  #      print(i)

#ejercicio7
# Solicitar el número de estudiantes que rindieron el examen
#num_estudiantes = int(input("Ingrese el número de estudiantes que rindieron el examen: "))

# Inicializar la suma de notas a 0
#suma_notas = 0

# Solicitar las notas de cada estudiante y calcular la suma de las notas
#for i in range(1, num_estudiantes + 1):
#    nota = float(input(f"Ingrese la nota del estudiante {i}: "))
#    suma_notas += nota

# Calcular el promedio de notas
#promedio = suma_notas / num_estudiantes

# Mostrar el promedio y evaluar el rendimiento
#print(f"El promedio de las notas es: {promedio:.2f}")

#if promedio > 8:
 #   print("El rendimiento ha sido elevado.")
#elif 6 <= promedio <= 8:
 #   print("El rendimiento ha sido aceptable.")
#else:
#    print("El rendimiento ha sido bajo.")

#ejercicio8
# Solicitar al usuario que ingrese un número entre 1 y 10
#numero = int(input("Ingrese un número entre 1 y 10: "))

# Validar que el número esté en el rango correcto
#if numero < 1 or numero > 10:
 #   print("El número debe estar entre 1 y 10.")
#else:
    # Generar y mostrar la tabla de multiplicar del número
 #   for i in range(1, 11):
  #      print(f"{numero} x {i} = {numero * i}")

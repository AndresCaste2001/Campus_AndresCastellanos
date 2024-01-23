Algoritmo Edades
	definir edad, cont, sumEdad, maxEdad  Como Entero
	definir salida, salida2 Como Logico
	Definir opc Como entero
	definir promEdad Como Real
	
	
	salida = Falso
	salida2 = Falso
	maxEdad = 0
	
	
	Repetir
		Escribir "Ingrese edad: "
		leer edad
		Si edad > 0 Entonces
			cont = cont + 1
			sumEdad =  sumEdad + edad
			si edad > maxEdad Entonces
				maxEdad = edad
			FinSi
			
		SiNo
			Si edad < 0 Entonces
				Escribir "Un valor negativo ha sido ingresado"
				salida = Verdadero
			SiNo
				Si edad == 0 Entonces
					Escribir "Cero no es un valor valido"
				FinSi
			FinSi
		FinSi
	Hasta Que salida
	promEdad = sumEdad/cont
	
	Repetir
		Escribir "Ingrese una de las opciones: "
		Escribir "1.) Edad maxima "
		Escribir "2.) Promedio de edades"
		Escribir "0.) Salir"
		Leer  opc
			Segun opc
				1: Escribir "La edad mayor es: ", maxEdad
				2: Escribir "El promedio de edad es: ", promEdad
				0: Escribir "Saliendo..."
					salida2 = Verdadero
			FinSegun
		
	Hasta Que salida2
	
	
	
FinAlgoritmo

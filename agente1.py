#Agente Humidificador
#La ubicación de dicho agente está denominada por las letras HX,HY,HZ
#Estados: Humidificar=0 y Sin Humidificar = 1
#Definición de las variables
def agente():
    #Inicialización de cada estado
    habitaciones= {'HX': 0, 'HY': 0, 'HZ': 0}
    #Inicialización del costo 
    costo = 0
    #Ingreso de datos sobre la habitación a escoger
    ubicacion = input("Indique en que habitación se encuentra (HX,HY,HZ): ");

    #Condicional para la habitación HX
    if ubicacion == 'HX':
        #Si selecciona HX ingresa a la condición, donde debe seleccionar si desea humidificar la habitación
        encendido = input("Desea humidificar la habitación "+ubicacion+" (Si/No): ")
        if encendido == 'Si':
            #Si tiene respueta "Si" solicita ingresa el estado de dicha habitación
            estadoActivo = int(input("Indique el estado de la habitación (0/1): "))
            #Si el estado está en (1) debe humificar la habitación
            if estadoActivo == 1:
                #Permite seleccionar un aroma para realizar el proceso de humidificación
                aroma = input("Seleccionar esencia: \n Lavanda\n Menta\n Cedro del Atlas\n Eucalipto \n")
                #Imprime la esencia seleccionada
                print("Esencia selecionada: "+aroma)
                print("La habitación "+ubicacion+" se activo para humidificar con el aroma "+aroma)
                #El estado se inicializa en 0
                estadoActual = 0
                #El costo incrementa en 1
                costo += 1
                #Imprime un mensaje indicando las opciones agregadas
                print("El estado de la "+ubicacion+ " es "+str(estadoActual)+" y su costo es "+str(costo))
            else:
                #Imprime un mensaje para indicar que ya se encuentra humidificada la habitación
                print("La habitación se encuentra humidificada")
                #El costo no incrementa
                costo = costo
                #Imprime un mensaje indicando el estado de la habitación y su costo
                print("El estado de la "+ubicacion+ " es "+str(estadoActivo)+" y su costo es "+str(costo))
        else:
            print ("SALIR")
    elif ubicacion == "HY":
        encendido = input("Desea humidificar la habitación "+ubicacion+" (Si/No): ")
        if encendido == 'Si':
            estadoActivo = int(input("Indique el estado de la habitación (0/1): "))
            if estadoActivo == 1:
                aroma = input("Seleccionar esencia: \n Lavanda\n Menta\n Cedro del Atlas\n Eucalipto \n")
                print("Escencia selecionada: "+aroma)
                print("La habitación "+ubicacion+" se activo para humidificar con el aroma "+aroma)
                costo += 1
                estadoActual = 0
                print("El estado de la "+ubicacion+ " es "+str(estadoActual)+" y su costo es "+str(costo))
            else:
                print("La habitación se encuentra humidificada")
                costo = costo
                print("El estado de la "+ubicacion+ " es "+str(estadoActivo)+" y su costo es "+str(costo))
        else:
            print ("Fin")
    elif ubicacion == "HZ":
        encendido = input("Desea humidificar la habitación "+ubicacion+" (Si/No): ")
        if encendido == 'Si':
            estadoActivo = int(input("Indique el estado de la habitación (0/1): "))
            if estadoActivo == 1:
                aroma = input("Seleccionar esencia: \n Lavanda\n Menta\n Cedro del Atlas\n Eucalipto \n")
                print("Escencia selecionada: "+aroma)
                print("La habitación "+ubicacion+" se activo para humidificar con el aroma "+aroma)
                costo += 1
                estadoActual = 0
                print("El estado de la "+ubicacion+ " es "+str(estadoActual)+" y su costo es "+str(costo))
            else:
                print("La habitación se encuentra humidificada")
                costo = costo
                print("El estado de la "+ubicacion+ " es "+str(estadoActivo)+" y su costo es "+str(costo))
        else:
            print ("Fin")
            
agente()

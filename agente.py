#Agente Humidificador
#La ubicación de dicho agente está denominada por las letras HX,HY,HZ
#Estados: Humidificar=0 y Sin Humidificar = 1

#Definición de las variables

def agente():
    #Inicialización de cada estado

    habitaciones= {'HX': 0, 'HY': 0, 'HZ': 0}
    costo = 0
    ubicacion = input("Indique en que habitación se encuentra (HX,HY,HZ): ");

    if ubicacion == 'HX':
        encendido = input("Desea humidificar la habitación "+ubicacion+" (Si/No): ")
        if encendido == 'Si':
            estadoActivo = int(input("Indique el estado de la habitación (0/1): "))
            if estadoActivo == 1:
                aroma = input("Seleccionar esencia: \n Lavanda\n Menta\n Cedro del Atlas\n Eucalipto \n")
                print("Escencia selecionada: "+aroma)
                print("La habitación "+ubicacion+" se activo para humidificar con el aroma "+aroma)
                estadoActual = 0
                costo += 1
                print("El estado de la "+ubicacion+ " es "+str(estadoActual)+" y su costo es "+str(costo))
            else:
                print("La habitación se encuentra humidificada")
                costo = costo
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
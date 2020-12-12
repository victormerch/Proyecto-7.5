import random
#== Flags ==

Jugadores = True
Orden_Jugadores = False
Ronda = True
salir = False
inicio = False

#== Bases de datos ==
n_players = []
dict_players = {}
mazo = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1),

        (2, 1, 2), (2, 2, 2), (2, 3, 2), (2, 4, 2),
        (3, 1, 3), (3, 2, 3), (3, 3, 3), (3, 4, 3),
        (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4),
        (5, 1, 5), (5, 2, 5), (5, 3, 5), (5, 4, 5),
        (6, 1, 6), (6, 2, 6), (6, 3, 6), (6, 4, 6),
        (7, 1, 7), (7, 2, 7), (7, 3, 7), (7, 4, 7),
        (8, 1, 8), (8, 2, 8), (8, 3, 8), (8, 4, 8),
        (9, 1, 9), (9, 2, 9), (9, 3, 9), (9, 4, 9),
        (10, 1, 0.5), (10, 2, 0.5), (10, 3, 0.5), (10, 4, 0.5),
        (11, 1, 0.5), (11, 2, 0.5), (11, 3, 0.5), (11, 4, 0.5),
        (12, 1, 0.5), (12, 2, 0.5), (12, 3, 0.5), (12, 4, 0.5)]

while True:

    if not inicio:
        print("\t\tBIENVENIDOS A SIETE Y MEDIO\n"
               "1) Jugar\n"
               "2) Salir")
        option = input(">")
        if option == "1":
            Jugadores = True
            inicio = True
        elif option == "2":
            salir = True
        else:
            print("== OPCION NO DISPONIBLE ==")

    if salir:
        print("\n== HASTA LA PROXIMA ==\n")
        break
    
    #== Annadir jugadores ==
    while Jugadores:
        
        Jugadores = False

        n_jug = int(input('Introduce el numero de jugadores : '))  # NUMERO DE LOS JUGADORES
        while n_jug < 2 or n_jug > 8:
            print('ERROR! Cantidad de jugadores incorrecta')
            n_jug = int(input('Introduce el numero de jugadores : '))
        players = []
        print()

        for i in range(n_jug):  # NOMBRE DE LOS JUGADORES #
            print('--JUGADOR ', i + 1, '--')
            nombre = str(input('-NICKNAME: '))
            while (nombre[0] < 'A') or (nombre[0] > 'z') or (nombre.isalnum() is False) or (nombre in players):
                print()
                print('--JUGADOR ', i + 1, '--')
                nombre = str(input('Vuelve a introducir NICKNAME: '))
            players.append(nombre)
            print()
        Orden_Jugadores = True

    #== Reparte y ordena por carta ==
    
    while Orden_Jugadores:
        Orden_Jugadores = False
        turno = []
        cartas_eliminadas = []

        for i in range(len(players)):  # REPARTIR UNA CARTA A CADA JUGADOR (JUGADOR-CARTA) #
            v_carta = random.choice(mazo)
            turno.append([])
            turno[i] = ([players[i], v_carta])
            cartas_eliminadas.append(v_carta)
            mazo.remove(v_carta) # ELMINAMOS LA CARTA, ya repartida,  DEL MAZO #

        for i in range(len(turno) - 1):  # ORDENAR JUGADORES SEGUN EL VALOR DE SU CARTA Y PRIORIDAD
            for j in range(len(turno) - 1 - i):
                if turno[j][1][0] < turno[j + 1][1][0]:
                    turno[j], turno[j + 1] = turno[j + 1], turno[j]
                if (turno[j][1][1] > turno[j + 1][1][1]) and (turno[j][1][0] == turno[j + 1][1][0]):
                    turno[j], turno[j + 1] = turno[j + 1], turno[j]

        print('--ORDEN de los JUGADORES--')  # ORDEN DE LOS JUGADORES Y JUGADOR 'BANCA' #
        for i in range(len(turno)):
            if turno[i][1][1] == 1:
                print(i + 1, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de OROS ')
            elif turno[i][1][1] == 2:
                print(i + 1, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de COPAS ')
            elif turno[i][1][1] == 3:
                print(i + 1, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de ESPADAS ')
            else:
                print(i + 1, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de BASTOS ')
        print()

        dict_players[turno[0][0]] = {"cartas":[],"prioridad":1,"suma_puntos_cartas":0,"ultimo_repartido":0,"estado_mano":"jugando","puntos":20}
         # Aqui ya estoy declarando quien sera la banca
        print('BANCA: ', turno[0][0],"\n")
        #== Poner cartas eliminadas en el mazo ==
        for i in range(len(cartas_eliminadas)):
            mazo.append(cartas_eliminadas[i])
        

        for i in range(1,len(turno)):
            
            dict_players[turno[i][0]] = {"cartas":0,"prioridad":i,"suma_puntos_cartas":0,"ultimo_repartido":0,
                                         "estado_mano":"jugando","puntos":20,"puntos_apostados":0}
        
        #print(n_players)
        

    
    #== Bucle turnos ==

    while not(Orden_Jugadores, salir):
        cartas_eliminadas = []
        jugadores_turno = []
        cont_jugadores = 0
        cont_eliminados = 0

        for key in turno:# Filtrador para ver quien juega
            if dict_players[key]["estado_mano"] == "jugando":
                dict_players[key]["cartas"] = []
                jugadores_turno.append(key)
                cont_jugadores += 1




        puntos_apuestas = 0


        while not cont_eliminados == cont_jugadores:#Si hay alguno que este jugando se iniciara

            for key in jugadores_turno:

                carta = random.choice(mazo)
                cartas_eliminadas.append(carta)
                mazo.remove(carta)

                dict_players[key]["cartas"].append(carta)
                dict_players[key]["suma"]["suma_puntos_cartas"] += carta[2]

                print(key.upper(),
                      "\n-Cartas ->", dict_players[key]["cartas"],
                      "\n-Puntos cartas ->", dict_players[key]["suma"]["suma_puntos_cartas"],
                      "\n-Puntos ->", dict_players[key]["puntos"])
                print("1) Apostar\n"
                      "2) Retirarte")
                option_turno = input(">")

                while True:
                    if option_turno == "1":
                        while True:  # Comprobar si es posible apostar si tiene o no los suficientes puntos
                            cantidad_apuesta = int(input("-Introduce la cantidad de puntos que quieres apostar->"))

                            if cantidad_apuesta > dict_players[key]["puntos"] or cantidad_apuesta <= 0:
                                print("== Cantidad incorrecta ==")
                            else:
                                puntos_apuestas += cantidad_apuesta
                                dict_players[key]["puntos"] -= cantidad_apuesta
                                dict_players[key]["puntos_apostados"] += cantidad_apuesta
                                break
                        break
                    elif option_turno == "2":
                        dict_players[key]["estado_mano"] = "plantado"
                        cont_eliminados += 1
                        break

                    else:
                        print("\n== OPCION NO DISPONIBLE ==\n")

        for key in jugadores_turno:
            print("jajajaaj")
            
        

             


        #===============================================================    
        #LARIOS SI LES ESTO -> AQUI LLEGARIA SI YA ESTAN TODOS PLANTADOS,
        #ENTONCES SE TENDRIA QUE PONER LAS CARTAS ELIMINADAS EN EL MAZO, 
        #VER QUIEN ES EL GANADOR DEL TURNO Y REPARTIR LOS TURNOS
        #===============================================================
                

        
            
   

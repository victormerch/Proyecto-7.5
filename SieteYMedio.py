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
        (10, 1, 0.5), (10, 2, 0.5), (10, 3, 0.5), (10, 4, 0.5),
        (11, 1, 0.5), (11, 2, 0.5), (11, 3, 0.5), (11, 4, 0.5),
        (12, 1, 0.5), (12, 2, 0.5), (12, 3, 0.5), (12, 4, 0.5)]

while True:

    if not inicio:
        while True:
            print("\t\tBIENVENIDOS A SIETE Y MEDIO\n"
                  "1) Jugar\n"
                  "2) Salir")
            option = input(">")
            if option == "1":
                Jugadores = True
                inicio = True
                break
            elif option == "2":
                salir = True
                break
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
        cartas_prohibidas = [(8, 1, 8), (8, 2, 8), (8, 3, 8), (8, 4, 8),
                            (9, 1, 9), (9, 2, 9), (9, 3, 9), (9, 4, 9)]
        #== Annadir 8 y 9 ==
        for cartas in cartas_prohibidas:
            mazo.append(cartas)

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

        dict_players[turno[0][0]] = {"cartas":0,"prioridad":0,"suma_puntos_cartas":0,"ultimo_repartido":0,
                                         "estado_mano":"jugando","puntos":20,"puntos_apostados":0}
         # Aqui ya estoy declarando quien sera la banca
        print('BANCA: ', turno[0][0],"\n")

        #== Poner cartas eliminadas en el mazo ==
        for i in range(len(cartas_eliminadas)):
            mazo.append(cartas_eliminadas[i])
        #==
        # == Quitar 8 y 9 ==
        for cartas in mazo:
            if cartas in cartas_prohibidas:
                mazo.remove(cartas)

        

        for i in range(1,len(turno)):
            
            dict_players[turno[i][0]] = {"cartas":0,"prioridad":i,"suma_puntos_cartas":0,"ultimo_repartido":0,
                                         "estado_mano":"jugando","puntos":20,"puntos_apostados":0}
        
        #print(n_players)
        

    
    #== Bucle turnos ==
    contador_rondas = 0

    while not Orden_Jugadores:
        cont_plantados = 0
        contador_rondas += 1
        cartas_eliminadas = []
        jugadores_turno = []
        cont_jugadores = 0


        print("\n=== RONDA",contador_rondas,"===\n")


        for i in range(len(turno)):# Filtrador para ver quien juega
            if dict_players[turno[i][0]]["estado_mano"] == "jugando":
                dict_players[turno[i][0]]["cartas"] = []
                dict_players[turno[i][0]]["suma_puntos_cartas"] = 0
                jugadores_turno.append(turno[i][0])
                cont_jugadores += 1
        jugadores_turno.remove(jugadores_turno[0])
        jugadores_turno.append(turno[0][0])



        cont = 0
        while not cont_plantados == cont_jugadores :#Si hay alguno que este jugando se iniciara
            cont += 1
            if cont == 1:#== Primer turno ==
                for key in jugadores_turno:
                    if key == turno[0][0]:
                        continue
                    else:
                        if dict_players[key]["estado_mano"] == "jugando":
                            if dict_players[key]["puntos"] <= 0:
                                print("--El jugador", key,
                                      "se ha quedado sin puntos para apostar asique quedara plantado--")
                                dict_players[key]["estado_mano"] = "plantado"
                                cont_jugadores = 0
                                cont_plantados = cont_jugadores
                                break


                            else:
                                carta = random.choice(mazo)
                                cartas_eliminadas.append(carta)
                                mazo.remove(carta)

                                dict_players[key]["cartas"].append(carta)
                                dict_players[key]["suma_puntos_cartas"] += carta[2]

                                while True:
                                    print(key.upper(),
                                          "\n-Cartas ->", dict_players[key]["cartas"],
                                          "\n-Puntos cartas ->", dict_players[key]["suma_puntos_cartas"],
                                          "\n-Puntos de", key, " ->", dict_players[key]["puntos"])

                                    while True:  # Comprobar si es posible apostar si tiene o no los suficientes puntos
                                        cantidad_apuesta = int(
                                            input("-Introduce la cantidad de puntos que quieres apostar->"))

                                        if cantidad_apuesta > dict_players[key]["puntos"] or cantidad_apuesta <= 0:
                                            print("== Cantidad incorrecta ==")
                                        else:
                                            dict_players[key]["puntos"] -= cantidad_apuesta
                                            dict_players[key]["puntos_apostados"] += cantidad_apuesta
                                            break
                                    break
            else:#== Siguientes turnos turno ==
                for key in jugadores_turno:

                    if dict_players[key]["estado_mano"] == "jugando":
                        if dict_players[key]["puntos"] <= 0:
                            print("--El jugador", key,
                                  "se ha quedado sin puntos para apostar asique quedara plantado--")
                            dict_players[key]["estado_mano"] = "plantado"
                            cont_jugadores = 0
                            cont_plantados = cont_jugadores
                            break


                        else:
                            while True:
                                print(key.upper(),
                                      "\n1) Pedir carta",
                                      "\n2) Plantarte")
                                option_turno = input(">")

                                if option_turno == "1":
                                    carta = random.choice(mazo)
                                    cartas_eliminadas.append(carta)
                                    mazo.remove(carta)

                                    dict_players[key]["cartas"].append(carta)
                                    dict_players[key]["suma_puntos_cartas"] += carta[2]
                                    print("\n-Cartas ->", dict_players[key]["cartas"],
                                          "\n-Puntos cartas ->", dict_players[key]["suma_puntos_cartas"])

                                    break
                                elif option_turno == "2":
                                    dict_players[key]["estado_mano"] = "plantado"
                                    cont_plantados += 1
                                    break
                                else:
                                    print("\n== OPCION NO DISPONIBLE ==\n")



        #== Reponer las cartas al mazo ==
        for cartas in cartas_eliminadas:
            mazo.append(cartas)

        #== Repartimiento de puntos ==
        puntos_banca = 0
        puntos_ganador = 0
        ganador_puntos = 0
        ganadores = []
        nose_pasaron = []
        ganador = 0

        if cont_jugadores == 0 or cont_jugadores == 1 :
            print("==Partida finalizada==")

            #====Ver quien es el jugador segun las puntuaciones de cada uno===
            print("$$ El ganador es tupu $$")

            #====
            print("+Quieres jugar otra partida??\n"
                    "1)Si\n"
                    "Cualquier tecla)No")
            option_final = input(">")
            if option_final == "1":
                Jugadores = True
            else:
                salir = True
            Orden_Jugadores = True

        else:
            #Ver el numero de puntos mas alto
            for key in jugadores_turno:

                if dict_players[key]["suma_puntos_cartas"] > 7.5:

                    puntos_banca += dict_players[key]["suma_puntos_cartas"] + dict_players[key]["puntos"]
                    dict_players[turno[0][0]]["puntos"] += puntos_banca
                    dict_players[key]["estado_mano"] = "eliminado"
                    print("\n==El jugador", key,
                          "queda eliminado de esta partida y sus puntos van para la banca actual==\n")
                else:
                    if dict_players[key]["suma_puntos_cartas"] > ganador_puntos:
                        ganador_puntos = dict_players[key]["puntos_apostados"]
                        ganador = key
                        ganadores.append(key)
                    else:
                        puntos_ganador = dict_players[key]["puntos_apostados"]
                    dict_players[key]["estado_mano"] = "jugando"
                    nose_pasaron.append(key)
            #Comprobar empates
            for key in nose_pasaron:
                if dict_players[key]["suma_puntos_cartas"] == ganador_puntos:
                    ganadores.append(key)
            if len(ganadores) == 1:
                print("==El g")
                print("== El ganador de esta ronda es:", key.upper(), "==\n")
                if dict_players[key]["suma_puntos_cartas"] == 7.5:
                    # Cambio prioridad de banca
                    print("=+ El jugador", key, "pasa a ser la banca porque a llegado a 7.5 +=")
                    for i in range(len(turno)):
                        if turno[i][0] == ganador:
                            turno[i][0] = turno[0][0]

                    turno[0][0] = key
                    dict_players[turno[0][0]]["prioridad"] = dict_players[key]["prioridad"]
                    dict_players[key]["prioridad"] = 0

                else:
                    dict_players[key]["puntos"] += puntos_ganador
            elif len(ganadores) > 1:
                boolean = False
                for key in ganadores:
                    if dict_players[key]["prioridad"] == 0:
                        print("== Habia un empate entre",ganadores,"pero gana",key,"porque es la banca ==")
                        #Dar puntos
                        boolean = True
                        break
                if boolean == False:
                    print("== Ha habido un empate entre estos jugadores",ganadores,"==")

            dict_players[key]["cartas"] = 0
            dict_players[key]["suma_puntos_cartas"] = 0













        #===============================================================    
        #-Solucionar problema de puntos apustados y suma_puntos_cartas
        #-Si la banca se pasa paga a todos los jugadores que se han plantado
        #
        #===============================================================
                

        
            
   

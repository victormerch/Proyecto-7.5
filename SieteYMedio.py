import random

# == Flags ==

Jugadores = True
Orden_Jugadores = False
Ronda = True
salir = False
inicio = False
mod1 = False
mod2 = True
c_repartidas = []
# == Bases de datos ==
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
# atributos mod2


jugadores = True

Rondas = False
Menu = True
Ganador = True
Volver_a_jugar = False
Dict_Jugadores = {}


while True:

    if not inicio:
        while True:
            print("\t\tBIENVENIDOS A SIETE Y MEDIO\n"
                  "1) Jugar\n"
                  "2) Salir")
            option = input(">")
            if option == "1":
                while True:
                    print("Que modalidad quiers jugar?\n"
                          "1) Humanos VS Humanos\n"
                          "2) Humanos VS Bots")
                    option_mod = input(">")
                    if option_mod == "1":
                        mod1 = True
                        Jugadores = True
                        inicio = True
                        break
                    elif option_mod == "2":
                        mod2 = True
                        jugadores = True
                        inicio = True

                        Orden_Jugadores = True
                        break
                    else:
                        print("\n== OPCION NO DISPONIBLE ==\n")
                break
            elif option == "2":
                salir = True
                break
            else:
                print("== OPCION NO DISPONIBLE ==")

    if salir:
        print("\n== HASTA LA PROXIMA ==\n")
        break

    # == Annadir jugadores ==
    while mod1:
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

        # == Reparte y ordena por carta ==

        while Orden_Jugadores:
            Orden_Jugadores = False
            turno = []
            cartas_eliminadas = []
            cartas_prohibidas = [(8, 1, 8), (8, 2, 8), (8, 3, 8), (8, 4, 8),
                                 (9, 1, 9), (9, 2, 9), (9, 3, 9), (9, 4, 9)]
            # == Annadir 8 y 9 ==
            for cartas in cartas_prohibidas:
                mazo.append(cartas)

            for i in range(len(players)):  # REPARTIR UNA CARTA A CADA JUGADOR (JUGADOR-CARTA) #
                v_carta = random.choice(mazo)
                turno.append([])
                turno[i] = ([players[i], v_carta])
                cartas_eliminadas.append(v_carta)
                mazo.remove(v_carta)  # ELMINAMOS LA CARTA, ya repartida,  DEL MAZO #

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

            dict_players[turno[0][0]] = {"cartas": 0, "prioridad": 0, "suma_puntos_cartas": 0, "ultimo_repartido": 0,
                                         "estado_mano": "jugando", "puntos": 20, "puntos_apostados": 0,
                                         "rondas_ganadas": 0}
            # Aqui ya estoy declarando quien sera la banca
            print('BANCA: ', turno[0][0], "\n")

            # == Poner cartas eliminadas en el mazo ==
            for i in range(len(cartas_eliminadas)):
                mazo.append(cartas_eliminadas[i])
            # ==
            # == Quitar 8 y 9 ==
            for cartas in cartas_prohibidas:
                mazo.remove(cartas)

            for i in range(1, len(turno)):
                dict_players[turno[i][0]] = {"cartas": 0, "prioridad": i, "suma_puntos_cartas": 0,
                                             "ultimo_repartido": 0,
                                             "estado_mano": "jugando", "puntos": 20, "puntos_apostados": 0,
                                             "rondas_ganadas": 0}

            # print(n_players)

        # == Bucle turnos ==
        while True:
            print("Cuanatas rondas quieres jugar(15 min y 30 max)?")
            rondas = int(input(">"))
            if rondas<15 or rondas>30:
                print("\n== CANTIDAD INCORRECTA ==\n")
            else:
                break
        contador_rondas = 0

        while not Orden_Jugadores:
            cont_plantados = 0
            contador_rondas += 1
            cartas_eliminadas = []
            jugadores_turno = []
            cont_jugadores = 0

            print("\n=== RONDA", contador_rondas, "===\n")

            for i in range(len(turno)):  # Filtrador para ver quien juega
                if dict_players[turno[i][0]]["estado_mano"] == "jugando":
                    dict_players[turno[i][0]]["cartas"] = []
                    dict_players[turno[i][0]]["suma_puntos_cartas"] = 0
                    jugadores_turno.append(turno[i][0])
                    cont_jugadores += 1
            jugadores_turno.remove(jugadores_turno[0])
            jugadores_turno.append(turno[0][0])

            if contador_rondas > 1:
                print("\n-PUNTOS DE CADA JUGADOR:")
                for key in jugadores_turno:
                    print(key.upper(), ":", dict_players[key]["puntos"])
                print()
            cont = 0
            while not cont_plantados == cont_jugadores and not cont_plantados == cont_jugadores - 1:  # Si hay alguno que este jugando se iniciara

                cont += 1
                if cont == 1:  # == Primer turno ==
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
                                        print("\nTurno de ", key.upper(),
                                              "\n-Puntos de la carta ->", carta[2],
                                              "\n-Suma de puntos cartas ->", dict_players[key]["suma_puntos_cartas"],
                                              "\n-Puntos jugador", key, " ->", dict_players[key]["puntos"])

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
                else:  # == Siguientes turnos turno ==
                    for key in jugadores_turno:

                        if dict_players[key]["estado_mano"] == "jugando":
                            if dict_players[key]["puntos"] <= 0:
                                print("--El jugador", key,
                                      "se ha quedado sin puntos para apostar asique quedara plantado--")
                                dict_players[key]["estado_mano"] = "eliminado"
                                cont_jugadores -= 1
                                cont_plantados = cont_jugadores
                                break


                            else:
                                while True:
                                    print("\nTurno de ", key.upper(),
                                          "\n1) Pedir carta",
                                          "\n2) Plantarte")
                                    option_turno = input(">")

                                    if option_turno == "1":
                                        carta = random.choice(mazo)
                                        cartas_eliminadas.append(carta)
                                        mazo.remove(carta)

                                        dict_players[key]["cartas"].append(carta)
                                        dict_players[key]["suma_puntos_cartas"] += carta[2]
                                        print("-Puntos de la carta ->", carta[2],
                                              "\n-Suma de puntos cartas ->", dict_players[key]["suma_puntos_cartas"])
                                        print()

                                        if dict_players[key]["suma_puntos_cartas"] > 7.5:
                                            print("== El jugador", key,
                                                  "se quedara plantado porque se ha pasado de 7.5 ==")
                                            dict_players[turno[0][0]]["puntos"] += dict_players[key]["puntos_apostados"]
                                            dict_players[key]["estado_mano"] = "plantado"
                                            cont_plantados += 1
                                        break
                                    elif option_turno == "2":
                                        print("\n--El jugador", key.upper(), "se ha plantado--")
                                        input("Enter para continuar\n")
                                        dict_players[key]["estado_mano"] = "plantado"
                                        cont_plantados += 1
                                        break
                                    else:
                                        print("\n== OPCION NO DISPONIBLE ==\n")

            # == Reponer las cartas al mazo ==
            for cartas in cartas_eliminadas:
                mazo.append(cartas)

            # == Repartimiento de puntos ==

            puntos_ganador = 0
            ganador_puntos = 0
            ganadores = []
            nose_pasaron = []
            ganador = 0
            # Ver el numero de puntos mas alto
            for key in jugadores_turno:
                if dict_players[key]["suma_puntos_cartas"] > ganador_puntos and dict_players[key][
                    "suma_puntos_cartas"] <= 7.5:
                    ganador_puntos = dict_players[key]["suma_puntos_cartas"]
                    ganador = key
                    ganadores.append(key)
                else:
                    puntos_ganador += dict_players[key]["puntos_apostados"]
                dict_players[key]["estado_mano"] = "jugando"
                nose_pasaron.append(key)

            # Comprobar empates

            for key in jugadores_turno:
                if dict_players[key]["suma_puntos_cartas"] == ganador_puntos and ganador != key:
                    ganadores.append(key)

            if len(ganadores) == 1:  # == Si solamente hay un ganador
                print("== El ganador de esta ronda es:", ganadores[0].upper(), "==\n")
                if dict_players[ganadores[0]]["suma_puntos_cartas"] == 7.5:
                    # Cambio prioridad de banca
                    print("=+ El jugador", ganadores[0], "pasa a ser la banca porque a llegado a 7.5 +=")
                    for i in range(len(turno)):
                        if turno[i][0] == ganador:
                            turno[i][0] = turno[0][0]

                    turno[0][0] = ganadores[0]
                    dict_players[turno[0][0]]["prioridad"] = dict_players[ganadores[0]]["prioridad"]
                    dict_players[ganadores[0]]["prioridad"] = 0
                    dict_players[ganadores[0]]["rondas_ganadas"] += 1

                else:
                    dict_players[ganadores[0]]["puntos"] += puntos_ganador
                    dict_players[ganadores[0]]["rondas_ganadas"] += 1

            elif len(ganadores) > 1:  # == Si hay mas de un ganador
                boolean = False
                for key in ganadores:
                    if dict_players[key]["prioridad"] == 0:  # == Si uno es la banca
                        print("== Habia un empate entre", ganadores, "pero gana", key, "porque es la banca ==")
                        dict_players[turno[0][0]]["puntos"] = puntos_ganador
                        dict_players[turno[0][0]]["rondas_ganadas"] += 1
                        dict_players[turno[0][0]]["estado_mano"] = "jugando"
                        boolean = True
                        break
                if boolean == False:  # = Si no es la banca
                    print("== Ha habido un empate entre estos jugadores", ganadores, "==")
                    for key in ganadores:
                        dict_players[key]["puntos"] = dict_players[key]["puntos_apostados"] + 1
                        dict_players[key]["rondas_ganadas"] += 1
                        dict_players[key]["estado_mano"] = "jugando"

            # Reinicio estados de jugadores
            for key in jugadores_turno:
                dict_players[key]["cartas"] = 0
                dict_players[key]["suma_puntos_cartas"] = 0
                dict_players[key]["puntos_apostados"] = 0

            # Ver si ha acabado partida
            if cont_jugadores == 0 or cont_jugadores == 1 or contador_rondas == rondas:
                print("==Partida finalizada==")

                # ====Ver quien es el jugador segun las puntuaciones de cada uno===
                ganador_partida = []
                ganador_partida_puntos = 0
                for i in range(len(turno)):
                    if ganador_partida_puntos <= dict_players[turno[i][0]]["puntos"]:
                        ganador_partida_puntos = dict_players[turno[i][0]]["puntos"]
                        ganador_partida.append(turno[i][0])

                if len(ganador_partida) == 1:
                    print("\n#### EL GANADOR DE ESTA PARTIDA ES:", ganador_partida[0].upper(),
                          "con", dict_players[ganador_partida[0]]["puntos"], "puntos ####\n")

                elif len(ganador_partida) > 1:
                    rondas = 0
                    jugador_ronda = 0
                    for i in range(len(turno)):
                        if ganador_partida <= dict_players[turno[i][0]]["rondas_ganadas"]:
                            rondas = dict_players[turno[i][0]]["rondas_ganadas"]

                    print("==Ha habido un empate entre", ganador_partida, "===\n"
                                                                          "### El ganador del desempate por rondas es",
                          jugador_ronda.upper(), "###\n")
                #====FINAL PARTIDA ==
                print("+Quieres jugar otra partida??\n"
                      "1)Si\n"
                      "Cualquier tecla)No")
                option_final = input(">")
                if option_final == "1":
                    mod1 = False
                    inicio = False
                    mod2 = False
                else:
                    salir = True
                    mod2 = False
                    break
                Orden_Jugadores = True

    # ======MODALIDAD BOTS==============
    while mod2:
        # == Annadir jugadores ==
        while jugadores:

            jugadores = False


            n_jug = int(input('Introduce el numero de jugadores HUMANO : '))  # NUMERO DE LOS JUGADORES
            while n_jug < 0 or n_jug > 8:
                print('ERROR! Cantidad de jugadores incorrecta')
                n_jug = int(input('Introduce el numero de jugadores HUMANO : '))
            players = []
            if n_jug < 8:
                bot = int(input('Introduce el numero de jugadores BOTS : '))
                while (n_jug + bot) > 8 or (n_jug + bot) < 2:
                    print('ERROR! Cantidad de  incorrecta')
                    bot = int(input('Introduce el numero de jugadores BOTS : '))
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
            for j in range(bot):
                nom_bots = 'Bot ' + str(j + 1)
                players.append(nom_bots)

            for h in range(n_jug):  # Creacion diccionario HUMANOS
                Dict_Jugadores[players[h]] = {
                    'Tipo_jugador': 'Humano',
                    'Cartas': [],
                    'Puntos': 20,
                    'Suma_puntos_cartas': 0,
                    'Estado_ronda': True,
                    'Estado_Partida': True,
                    'Puntos_apostados': 0,
                    'Banca': False,
                    'Rondas_ganadas': 0
                }

            for g in range(bot):  # Creacion diccionario BOTS
                Dict_Jugadores[players[g + n_jug]] = {
                    'Tipo_jugador': 'Bot',
                    'Cartas': [],
                    'Puntos': 20,
                    'Suma_puntos_cartas': 0,
                    'Estado_ronda': True,
                    'Estado_Partida': True,
                    'Puntos_apostados': 0,
                    'Banca': False,
                    'Rondas_ganadas': 0
                }

            Orden_Jugadores = True

        # == Reparte y ordena por carta ==

        while Orden_Jugadores:
            Orden_Jugadores = False
            turno = []
            cartas_eliminadas = []

            for i in range(len(players)):  # REPARTIR UNA CARTA A CADA JUGADOR (JUGADOR-CARTA) #
                v_carta = random.choice(mazo)
                turno.append([])
                turno[i] = ([players[i], v_carta])
                c_repartidas.append(v_carta)
                mazo.remove(v_carta)  # ELMINAMOS LA CARTA, ya repartida,  DEL MAZO #
            for i in range(len(c_repartidas)):
                mazo.append(c_repartidas[i])
            print('cartas en el mazo: ', len(mazo))
            del c_repartidas
            for i in range(len(turno) - 1):  # ORDENAR JUGADORES SEGUN EL VALOR DE SU CARTA Y PRIORIDAD
                for j in range(len(turno) - 1 - i):
                    if turno[j][1][0] < turno[j + 1][1][0]:
                        turno[j], turno[j + 1] = turno[j + 1], turno[j]
                    if (turno[j][1][1] > turno[j + 1][1][1]) and (turno[j][1][0] == turno[j + 1][1][0]):
                        turno[j], turno[j + 1] = turno[j + 1], turno[j]

            print('--ORDEN de los JUGADORES--')  # ORDEN DE LOS JUGADORES Y JUGADOR 'BANCA' #
            for i in range(len(turno)):
                if turno[i][0] == turno[0][0]:
                    print('BANCA : ', turno[i][0])
                elif turno[i][1][1] == 1:
                    print(i, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de OROS ')
                elif turno[i][1][1] == 2:
                    print(i, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de COPAS ')
                elif turno[i][1][1] == 3:
                    print(i, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de ESPADAS ')
                else:
                    print(i, ')', turno[i][0].ljust(10), '-> VALOR de su CARTA:', turno[i][1][0], 'de BASTOS ')
            print()
            Dict_Jugadores[turno[0][0]]['Banca'] = True
            n_rondas = int(input('CUANTAS RONDAS QUIERES JUGAR ( MIN. 15 - MAX. 30) > '))
            print()
            # while n_rondas < 15 or n_rondas > 30:
            # print('--CANTIDAD INCORRECTA--')
            # n_rondas = input('cuantas rondas quieres jugar ( MIN. 15 - MAX. 30')
            Rondas = True

        # -EMPIEZA LA PARTIDA-#
        while Rondas:
            Rondas = False
            for i in range(n_rondas):
                Repartir = True
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
                c_repartidas = []
                jugadores_res = 0
                for key in Dict_Jugadores:
                    if Dict_Jugadores[key]['Estado_Partida'] == True:
                        jugadores_res = jugadores_res + 1
                if jugadores_res < 2:
                    break
                for key in Dict_Jugadores:  # añadimos la banca a la ultima posicion de los turnos y reiniciamos los puntos apostados
                    if Dict_Jugadores[key]['Banca'] == True:
                        for j in range(len(turno)):
                            if turno[j][0] == key and j != len(turno) - 1:
                                banca = turno[j]
                                turno.pop(j)
                                turno.append(banca)
                                break
                    Dict_Jugadores[key]['Puntos_apostados'] = 0
                    Dict_Jugadores[key]['Suma_puntos_cartas'] = 0
                    Dict_Jugadores[key]['Estado_ronda'] = True
                    Dict_Jugadores[key]['Cartas'] = []
                input()

                print('-' * 21, 'RONDA ', i + 1, '-' * 21)
                # REPARTIR CARTA INICIAL
                print('--CARTAS INICIALES DE LA RONDA--'.center(50))
                for j in range(len(turno)):
                    if Dict_Jugadores[turno[j][0]]['Estado_Partida'] == True:
                        if Dict_Jugadores[turno[j][0]]['Banca'] == True:
                            print(turno[j][0], ' --> BANCA (no obtiene puntos iniciales)')

                        elif Dict_Jugadores[turno[j][0]]['Tipo_jugador'] == 'Humano':
                            c_inicial = random.choice(mazo)
                            while c_inicial[0] == 8 or c_inicial[0] == 9:
                                c_inicial = random.choice(mazo)
                            c_repartidas.append(c_inicial)
                            Dict_Jugadores[turno[j][0]]['Cartas'].append(c_inicial)
                            Dict_Jugadores[turno[j][0]]['Suma_puntos_cartas'] += c_inicial[2]
                            mazo.remove(c_inicial)
                            print('JUGADOR: ', turno[j][0].ljust(8), ' CARTA: ', str(c_inicial).ljust(12), ' VALOR: ',
                                  c_inicial[2])

                        elif Dict_Jugadores[turno[j][0]]['Tipo_jugador'] == 'Bot':
                            c_inicial = random.choice(mazo)
                            while c_inicial[0] == 8 or c_inicial[0] == 9:
                                c_inicial = random.choice(mazo)
                            c_repartidas.append(c_inicial)
                            Dict_Jugadores[turno[j][0]]['Cartas'].append(c_inicial)
                            Dict_Jugadores[turno[j][0]]['Suma_puntos_cartas'] += c_inicial[2]
                            mazo.remove(c_inicial)
                            print('JUGADOR: ', turno[j][0].ljust(8), ' CARTA: ', str(c_inicial).ljust(12), ' VALOR: ',
                                  c_inicial[2])

                # APOSTAR CANTIDAD DE PUNTOS#
                input()
                print('--APUESTAS--')
                por_partida = 0.8 * n_rondas
                print()
                if i >= por_partida:
                    print('Puntos a apostar -- MIN : 6 / MAX 12--')
                    max = 12
                    min = 6
                else:
                    print('Puntos a apostar -- MIN: 2 / MAX: 5--')
                    max = 5
                    min = 2
                for r in range(len(turno)):
                    if Dict_Jugadores[turno[r][0]]['Estado_Partida'] == True and Dict_Jugadores[turno[r][0]][
                        'Banca'] == False:
                        if Dict_Jugadores[turno[r][0]]['Tipo_jugador'] == 'Humano':
                            print('Turno de ', turno[r][0])
                            print('Puntos disponibles: ', Dict_Jugadores[turno[r][0]]['Puntos'])
                            Dict_Jugadores[turno[r][0]]['Puntos_apostados'] = int(
                                input('Cuantos puntos quieres apostar: '))
                            while Dict_Jugadores[turno[r][0]]['Puntos_apostados'] > max or Dict_Jugadores[turno[r][0]][
                                'Puntos_apostados'] < min:
                                print()
                                print('--¡CANTIDAD APOSTADO NO ACEPTADA!--')
                                print('Puntos a apostar -- MIN: ', min, ' / MAX: ', max, '--')
                                print('Puntos disponibles: ', Dict_Jugadores[turno[r][0]]['Puntos'])
                                Dict_Jugadores[turno[r][0]]['Puntos_apostados'] = int(
                                    input('Cuantos puntos quieres apostar: '))
                            Dict_Jugadores[turno[r][0]]['Puntos'] = Dict_Jugadores[turno[r][0]]['Puntos'] - \
                                                                    Dict_Jugadores[turno[r][0]]['Puntos_apostados']
                            print(turno[r][0], ' ha apostado ', Dict_Jugadores[turno[r][0]]['Puntos_apostados'],
                                  ' puntos.')

                        elif Dict_Jugadores[turno[r][0]]['Tipo_jugador'] == 'Bot':
                            Dict_Jugadores[turno[r][0]]['Puntos_apostados'] = random.randint(min, max)
                            Dict_Jugadores[turno[r][0]]['Puntos'] = Dict_Jugadores[turno[r][0]]['Puntos'] - \
                                                                    Dict_Jugadores[turno[r][0]]['Puntos_apostados']
                            print('El ', turno[r][0], ' ha apostado ', Dict_Jugadores[turno[r][0]]['Puntos_apostados'],
                                  ' puntos.')
                    else:
                        print(turno[r][0], ' es la banca, no apuesta')
                    print()
                input()
                print('--RESUMEN APUESTAS--')
                for key in Dict_Jugadores:
                    if Dict_Jugadores[key]['Estado_Partida'] == True:
                        print(key.rjust(10), ' : ', Dict_Jugadores[key]['Puntos_apostados'])
                input()

                # Repartimos las cantidad de cartas que desee cada jugador#

                while Repartir:
                    Repartir = False
                    # COMPROBAMOS SI ESTA ACTIVO EN LA PARTIDA Y EN LA RONDA
                    j_activos = 0
                    for key in Dict_Jugadores:
                        if Dict_Jugadores[key]['Estado_Partida'] == True and Dict_Jugadores[key][
                            'Estado_ronda'] == True:
                            j_activos += 1

                    j_eliminados = 0
                    j_pasar = 0
                    while j_activos > (j_eliminados + j_pasar):
                        for p in range(len(turno)):
                            if Dict_Jugadores[turno[p][0]]['Estado_Partida'] == True and Dict_Jugadores[turno[p][0]][
                                'Estado_ronda'] == True:
                                input()
                                print('--TURNO DE ', turno[p][0])
                                # SI ES LA BANCA#

                                if Dict_Jugadores[turno[p][0]]['Banca'] == True:  # comprobamos si es la banca
                                    print('TOTAL JUGADORES :', j_activos, ' JUGADORES HAN PASADO : ', j_pasar,
                                          ' JUGADORES ELMINADOS : ', j_eliminados)
                                    if j_pasar > 0 and j_activos == ((j_eliminados + j_pasar) + 1):
                                        max_suma_puntos = 0  # MAXIMA PUNTUACION OBTENIDO ENTRE TODOS LOS JUGADORES ACTIVOS
                                        for llave in players:
                                            if Dict_Jugadores[llave]['Estado_Partida'] == True and \
                                                    Dict_Jugadores[llave]['Suma_puntos_cartas'] <= 7.5:
                                                if Dict_Jugadores[llave]['Suma_puntos_cartas'] > max_suma_puntos:
                                                    max_suma_puntos = Dict_Jugadores[llave][
                                                        'Suma_puntos_cartas']  # comprobamos la maxima suma de cartas (7.5) de TODOS los juagdores
                                        print('VALOR A SUPERAR POR LA BANCA : ', max_suma_puntos, ' puntos')
                                        while max_suma_puntos != 0 and Dict_Jugadores[turno[p][0]][
                                            'Suma_puntos_cartas'] < max_suma_puntos and Dict_Jugadores[turno[p][0]][
                                            'Suma_puntos_cartas'] != 7.5:
                                            input()
                                            nueva_carta = random.choice(mazo)
                                            while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                                nueva_carta = random.choice(mazo)
                                            c_repartidas.append(nueva_carta)
                                            Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                            Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] += nueva_carta[2]
                                            print('CARTA ROBADA: ', nueva_carta, ' por BANCA.')
                                            print('CARTAS DE ', turno[p][0], ' (banca) : ',
                                                  Dict_Jugadores[turno[p][0]]['Cartas'])
                                            print('PUNTOS BANCA: ', Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])
                                            mazo.remove(nueva_carta)
                                        print('LA BANCA A ACUMULADO: ',
                                              Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'], ' puntos')
                                        j_pasar += 1
                                        input()
                                        if Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] > 7.5:
                                            Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False

                                    elif j_activos > ((j_eliminados + j_pasar) + 1):
                                        print('--AUN QUEDAN JUGADORES ACTIVOS--')

                                    else:
                                        print('--TODOS LOS JUGADORES HAN SIDO ELIMINADOS--')
                                        j_pasar += 1


                                # SI ES HUMANO#

                                elif Dict_Jugadores[turno[p][0]]['Tipo_jugador'] == 'Humano':
                                    print(turno[p][0], ' tiene ', Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'],
                                          'puntos.')
                                    robar = str(
                                        input('Quieres otra carta?: SI = 1 / PLANTARSE = Cualquier otra tecla > '))
                                    if robar == '1':
                                        nueva_carta = random.choice(mazo)
                                        while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                            nueva_carta = random.choice(mazo)
                                        c_repartidas.append(nueva_carta)
                                        mazo.remove(nueva_carta)
                                        Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                        print('CARTA ROBADA: ', nueva_carta, ' por ', turno[p][0])
                                        print('CARTAS DE ', turno[p][0], ': ', Dict_Jugadores[turno[p][0]]['Cartas'])
                                        Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] = Dict_Jugadores[turno[p][0]][
                                                                                                'Suma_puntos_cartas'] + \
                                                                                            nueva_carta[2]
                                        print('PUNTOS DE LAS CARTAS: ',
                                              Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])

                                    else:  # JUGADOR PLANTADO, PARTICIPA EN LA RONDA
                                        print('-------------', turno[p][0], ' se ha plantado -------------')
                                        Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False
                                        j_pasar += 1
                                    print()

                                    if Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] == 7.5:
                                        print('-------------', turno[p][0], ' ha conseguido 7,5 puntos -------------')
                                        Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False
                                        j_pasar += 1

                                    if Dict_Jugadores[turno[p][0]][
                                        'Suma_puntos_cartas'] > 7.5:  # JUGADOR ELIMINADO DE LA RONDA
                                        j_eliminados += 1
                                        print('-------------!TE HAS PASADO¡ Fin de tu turno-------------')
                                        Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False

                                # SI ES BOT#

                                elif Dict_Jugadores[turno[p][0]]['Tipo_jugador'] == 'Bot':
                                    if Dict_Jugadores[turno[p][0]]['Puntos'] < Dict_Jugadores[turno[len(turno) - 1][0]][
                                        'Puntos']:
                                        nueva_carta = random.choice(mazo)
                                        while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                            nueva_carta = random.choice(mazo)
                                        c_repartidas.append(nueva_carta)
                                        mazo.remove(nueva_carta)
                                        Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                        print('CARTA ROBADA: ', nueva_carta, ' por ', turno[p][0])
                                        print('CARTAS DE ', turno[p][0], ': ', Dict_Jugadores[turno[p][0]]['Cartas'])
                                        Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] = Dict_Jugadores[turno[p][0]][
                                                                                                'Suma_puntos_cartas'] + \
                                                                                            nueva_carta[2]
                                        print('PUNTOS DE LAS CARTAS: ',
                                              Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])


                                    elif Dict_Jugadores[turno[p][0]]['Puntos'] > \
                                            Dict_Jugadores[turno[len(turno) - 1][0]]['Puntos']:
                                        # CALCULAR PROBABILIDAD
                                        p_restantes = 7.5 - Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas']
                                        c_posibles = 0
                                        for j in range(len(mazo)):
                                            if mazo[j][0] != 8 and mazo[j][0] != 9:
                                                if mazo[j][2] < p_restantes:
                                                    c_posibles = c_posibles + 1
                                        prob = (c_posibles / (len(
                                            mazo) - 8)) * 100  # TODAS LAS CARTAS MENOS LAS DE VALOR 8 Y 9, EN TOTAL 8 MENOS

                                        if prob > 65:
                                            print('PROBABILIDAD 65-100 -->', prob)
                                            nueva_carta = random.choice(mazo)
                                            while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                                nueva_carta = random.choice(mazo)
                                            c_repartidas.append(nueva_carta)
                                            mazo.remove(nueva_carta)
                                            Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                            print('CARTA ROBADA: ', nueva_carta, ' por ', turno[p][0])
                                            print('CARTAS DE ', turno[p][0], ': ',
                                                  Dict_Jugadores[turno[p][0]]['Cartas'])
                                            Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] = \
                                            Dict_Jugadores[turno[p][0]][
                                                'Suma_puntos_cartas'] + \
                                            nueva_carta[2]
                                            print('PUNTOS DE LAS CARTAS: ',
                                                  Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])



                                        elif prob >= 50 and prob <= 65:
                                            prob_robar = random.randint(0, 100)
                                            print('PROBABILIDAD 50-65 -->', prob)
                                            if prob_robar > 50 and prob_robar < 65:
                                                nueva_carta = random.choice(mazo)
                                                while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                                    nueva_carta = random.choice(mazo)
                                                c_repartidas.append(nueva_carta)
                                                mazo.remove(nueva_carta)
                                                Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                                print('CARTA ROBADA: ', nueva_carta, ' por ', turno[p][0])
                                                print('CARTAS DE ', turno[p][0], ': ',
                                                      Dict_Jugadores[turno[p][0]]['Cartas'])
                                                Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] = \
                                                Dict_Jugadores[turno[p][0]][
                                                    'Suma_puntos_cartas'] + \
                                                nueva_carta[2]
                                                print('PUNTOS DE LAS CARTAS: ',
                                                      Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])
                                            else:
                                                print('-------------', turno[p][0], ' se ha plantado -------------')
                                                Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False
                                                j_activos += 1
                                            print()

                                        elif prob < 50:
                                            print('PROBABILIDAD 0-50 -->', prob)

                                            prob_robar = random.randint(0, 100)
                                            p_3 = int(50 / 3)
                                            if prob_robar < p_3:
                                                nueva_carta = random.choice(mazo)
                                                while nueva_carta[0] == 8 or nueva_carta[0] == 9:
                                                    nueva_carta = random.choice(mazo)
                                                c_repartidas.append(nueva_carta)
                                                mazo.remove(nueva_carta)
                                                Dict_Jugadores[turno[p][0]]['Cartas'].append(nueva_carta)
                                                print('CARTA ROBADA: ', nueva_carta, ' por ', turno[p][0])
                                                print('CARTAS DE ', turno[p][0], ': ',
                                                      Dict_Jugadores[turno[p][0]]['Cartas'])
                                                Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] = \
                                                    Dict_Jugadores[turno[p][0]][
                                                        'Suma_puntos_cartas'] + \
                                                    nueva_carta[2]
                                                print('PUNTOS DE LAS CARTAS: ',
                                                      Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'])
                                            else:
                                                print('-------------', turno[p][0], ' se ha plantado -------------')
                                                Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False
                                                j_activos += 1
                                            print()

                                    if Dict_Jugadores[turno[p][0]]['Suma_puntos_cartas'] == 7.5:
                                        print('-------------', turno[p][0], ' ha conseguido 7,5 puntos -------------')
                                        Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False
                                        j_pasar += 1

                                    if Dict_Jugadores[turno[p][0]][
                                        'Suma_puntos_cartas'] > 7.5:  # JUGADOR ELIMINADO DE LA RONDA
                                        j_eliminados += 1
                                        print('-------------!TE HAS PASADO¡ Fin de tu turno-------------')
                                        Dict_Jugadores[turno[p][0]]['Estado_ronda'] = False

                print('--RESUMEN DE LA RONDA--')
                if Dict_Jugadores[turno[len(turno) - 1][0]][
                    'Suma_puntos_cartas'] == 7.5:  # si la banca tiene 7.5 gana a todos. se lleva todos los puntos
                    print('GANADOR: ', turno[len(turno) - 1][0], ' con 7.5 puntos')
                    Dict_Jugadores[turno[len(turno) - 1][0]]['Rondas_ganadas'] += 1
                    for key in Dict_Jugadores:
                        if Dict_Jugadores[key]['Banca'] == False:
                            Dict_Jugadores[turno[len(turno) - 1][0]]['Puntos'] = Dict_Jugadores[key][
                                                                                     'Puntos_apostados'] + \
                                                                                 Dict_Jugadores[
                                                                                     turno[len(turno) - 1][0]]['Puntos']
                            print(key, ' ha conseguido ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos.')

                elif Dict_Jugadores[turno[len(turno) - 1][0]]['Estado_ronda'] == False:  # si la banca se ha pasado
                    for key in Dict_Jugadores:
                        if Dict_Jugadores[key]['Estado_Partida'] == True:
                            if Dict_Jugadores[key]['Suma_puntos_cartas'] == max_suma_puntos:
                                print('GANADOR: ', key, ' con ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos')
                                Dict_Jugadores[key]['Rondas_ganadas'] += 1
                                if Dict_Jugadores[key]['Suma_puntos_cartas'] == 7.5:
                                    Dict_Jugadores[key]['Banca'] = True
                                    for llave in Dict_Jugadores:
                                        Dict_Jugadores[llave]['Banca'] = False
                                    Dict_Jugadores[key]['Banca'] = True
                                    Dict_Jugadores[key]['Puntos'] = Dict_Jugadores[key]['Puntos'] + (
                                                Dict_Jugadores[key]['Puntos_apostados'] * 2)
                                else:
                                    Dict_Jugadores[key]['Puntos'] = Dict_Jugadores[key]['Puntos'] + 1 + \
                                                                    Dict_Jugadores[key]['Puntos_apostados']
                            else:
                                print(key, ' ha conseguido ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos.')
                                Dict_Jugadores[key]['Puntos'] = Dict_Jugadores[key]['Puntos'] + Dict_Jugadores[key][
                                    'Puntos_apostados']
                        elif Dict_Jugadores[key]['Estado_Partida'] == True and Dict_Jugadores[key][
                            'Estado_ronda'] == False:
                            print(key, ' ha conseguido ', Dict_Jugadores[key]['Suma_puntos_cartas'],
                                  ' puntos. Se ha pasado de 7,5.')

                elif Dict_Jugadores[turno[len(turno) - 1][0]][
                    'Estado_ronda'] == True:  # si la banca no se ha pasado pero no es 7.5
                    for key in Dict_Jugadores:
                        if Dict_Jugadores[key]['Estado_ronda'] == True and Dict_Jugadores[key]['Suma_puntos_cartas'] > \
                                Dict_Jugadores[turno[len(turno) - 1][0]]['Suma_puntos_cartas']:
                            Dict_Jugadores[key]['Puntos'] = Dict_Jugadores[key]['Puntos'] + Dict_Jugadores[key][
                                'Puntos_apostados']
                            print(key, ' ha conseguido ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos.')
                        elif Dict_Jugadores[key]['Banca'] == True:
                            print('GANADOR: ', key, ' con ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos')
                            Dict_Jugadores[turno[len(turno) - 1][0]]['Rondas_ganadas'] += 1
                        else:
                            Dict_Jugadores[turno[len(turno) - 1][0]]['Puntos'] = \
                            Dict_Jugadores[turno[len(turno) - 1][0]]['Puntos'] + Dict_Jugadores[key]['Puntos_apostados']
                            print(key, ' ha conseguido ', Dict_Jugadores[key]['Suma_puntos_cartas'], ' puntos.')

                # Metemos las cartas repartidas en el mazo para una nueva ronda
                for i in range(len(c_repartidas)):
                    mazo.append([c_repartidas[i]])
                print('Cartas en el mazo: ', len(mazo))
                del c_repartidas

                # Mirar que jugadores se han quedado a 0 y eliminarlos de la partida
                if Dict_Jugadores[key]['Puntos'] < 1:
                    Dict_Jugadores[key]['Estado_Partida'] = False
                    Dict_Jugadores[key]['Puntos'] = 0

                print('--CLASIFICACION--'.center(80))
                print('Nombre'.ljust(20), 'Puntos Restantes'.ljust(20), 'Rondas Ganadas'.ljust(20),
                      'Estado en la partida')
                clas_jugadores = []
                for key in Dict_Jugadores:
                    clas_jugadores.append([key, Dict_Jugadores[key]['Puntos'], Dict_Jugadores[key]['Rondas_ganadas'],
                                           Dict_Jugadores[key]['Estado_Partida']])
                for i in range(len(clas_jugadores)):
                    for j in range(len(clas_jugadores) - 1):
                        if clas_jugadores[j][2] < clas_jugadores[j + 1][2]:
                            aux = clas_jugadores[j]
                            clas_jugadores[j] = clas_jugadores[j + 1]
                            clas_jugadores[j + 1] = aux
                        elif clas_jugadores[j][2] == clas_jugadores[j + 1][2]:
                            if clas_jugadores[j][1] < clas_jugadores[j + 1][1]:
                                aux = clas_jugadores[j]
                                clas_jugadores[j] = clas_jugadores[j + 1]
                                clas_jugadores[j + 1] = aux

                for h in range(len(clas_jugadores)):
                    if clas_jugadores[h][3] == True:
                        print(clas_jugadores[h][0].ljust(20), str(clas_jugadores[h][1]).ljust(20),
                              str(clas_jugadores[h][2]).ljust(20), 'JUGANDO'.ljust(20))
                    else:
                        print(clas_jugadores[h][0].ljust(20), str(clas_jugadores[h][1]).ljust(20),
                              str(clas_jugadores[h][2]).ljust(20), 'ELIMINADO'.ljust(20))

        while Ganador:
            Ganador = False
            print('Y EL GANADOR ES...')
            input('...3')
            input('...2')
            input('...1')
            print(clas_jugadores[0][0], '¡FELICIDADES!')
            input()

            Volver_a_jugar = True

        while Volver_a_jugar:
            print()
            Volver_a_jugar = False
            print('--FIN DE LA PARTIDA--')
            jugar = str(input('Quieres volver a jugar? SI = 1 / NO = Cualquier tecla'))
            if jugar != '1':
                salir = True
                mod2 = False
                break
            else:
                inicio = False
                mod2 = False
                break

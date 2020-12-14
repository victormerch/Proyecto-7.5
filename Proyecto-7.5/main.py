import random
siete_y_medio = True
Jugadores = True
Orden_Jugadores = False
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

while siete_y_medio:
    
    while Jugadores:
        print('--BIENVENIDOS AL SIETE Y MEDIO--'.center(100))
        Jugadores = False

        n_jug = int(input('Introduce el numero de jugadores : '))  # NUMERO DE LOS JUGADORES
        while n_jug < 2 or n_jug > 8:
            print('ERROR! Cantidad de jugadores incorrecta')
            n_jug = int(input('Introduce el numero de jugadores : '))
        jugadores = []
        print()

        for i in range(n_jug):  # NOMBRE DE LOS JUGADORES #
            print('--JUGADOR ', i + 1, '--')
            nombre = str(input('-NICKNAME: '))
            while (nombre[0] < 'A') or (nombre[0] > 'z') or (nombre.isalnum() is False) or (nombre in jugadores):
                print()
                print('--JUGADOR ', i + 1, '--')
                nombre = str(input('Vuelve a introducir NICKNAME: '))
            jugadores.append(nombre)
            print()
        Orden_Jugadores = True

    while Orden_Jugadores:
        Orden_Jugadores = False
        turno = []
        for i in range(len(jugadores)):  # REPARTIR UNA CARTA A CADA JUGADOR (JUGADOR-CARTA) #
            v_carta = random.choice(mazo)
            turno.append([])
            turno[i] = ([jugadores[i], v_carta])
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
        print('BANCA: ', turno[0][0])

    print()
    input('Presiona una tecla para salir')
    break
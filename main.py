import random
siete_y_medio = True
Jugadores = True
Orden_Jugadores = False
mazo = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1),
        (2, 1, 2), (2, 2, 2), (2, 3, 2), (2, 4, 2),
        (3, 1, 3), (3, 2, 3), (3, 3, 3), (3, 4, 3),
        (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4),
        (5, 1, 5), (5, 2, 5), (5, 3, 5), (5, 4, 5),
        (6, 1, 6), (6, 2, 6), (6, 3, 6), (6, 4,  6),
        (7, 1, 7), (7, 2, 7), (7, 3, 7), (7, 4, 7),
        (8, 1, 8), (8, 2, 8), (8, 3, 8), (8, 4, 8),
        (9, 1, 9), (9, 2, 9), (9, 3, 9), (9, 4, 9),
        (10, 1, 0.5), (10, 2, 0.5), (10, 3, 0.5), (10, 4, 0.5),
        (11, 1, 0.5), (11, 2, 0.5), (11, 3, 0.5), (11, 4, 0.5),
        (12, 1, 0.5), (12, 2, 0.5), (12, 3, 0.5), (12, 4, 0.5)]
"""for i in range (len(mazo)):
        if mazo[i][0] != 8 and mazo[i][0] != 9:
                if mazo[i][1] == 1:
                        print(mazo[i][0], ' de oros con valor de: ', mazo[i][2])
                elif mazo[i][1] == 2:
                        print(mazo[i][0], ' de copas con valor de: ', mazo[i][2])
                elif mazo[i][1] == 3:
                        print(mazo[i][0], ' de bastos con valor de: ', mazo[i][2])
                else:
                        print(mazo[i][0], ' de espadas con valor de: ', mazo[i][2])"""
while siete_y_medio:
        while Jugadores:
                print('--BIENVENIDOS AL SIETE Y MEDIO--'.center(100))
                Jugadores = False
                n_jug = int(input('Introduce el numero de jugadores : '))
                while n_jug < 2 or n_jug > 8:
                        print('ERROR! Cantidad de jugadores incorrecta')
                        n_jug = int(input('Introduce el numero de jugadores : '))
                jugadores = []
                print()
                for i in range(n_jug):
                        print('--JUGADOR ', i + 1, '--')
                        nombre = str(input('-NICKNAME: '))
                        while (nombre[0] < 'A') or (nombre[0] > 'z') or (nombre.isalnum() == False) or (nombre in jugadores):
                                print()
                                print('--JUGADOR ', i + 1, '--')
                                nombre = str(input('Vuelve a introducir NICKNAME: '))
                        jugadores.append(nombre)
                        print()
                Orden_Jugadores = True

        while Orden_Jugadores:
                Orden_Jugadores = False

                o_jug = []
                for i in range(len(jugadores)):
                        v_carta = random.randint(0, 40)
                        for j in range(len(o_jug)):
                                if mazo[v_carta][0] == o_jug[j][1]:
                                        print('cambiamos', v_carta, "ya que ya esta repartida a ", o_jug[j])
                                        v_carta = random.randint(0, 40)
                        v_carta = random.randint(0, 40)
                        o_jug.append([])
                        o_jug[i] = ([jugadores[i], mazo[v_carta]])

                for i in range(len(o_jug)-1):
                        for j in range(len(o_jug)-1-i):
                                if o_jug[j][1][0] < o_jug[j + 1][1][0]:
                                        o_jug[j], o_jug[j + 1] = o_jug[j + 1], o_jug[j]
                                if (o_jug[j][1][1] > o_jug[j+1][1][1]) and (o_jug[j][1][0] == o_jug[j + 1][1][0]):
                                        o_jug[j], o_jug[j + 1] = o_jug[j + 1], o_jug[j]
                print('--ORDEN de los JUGADORES--')
                for i in range(len(o_jug)):
                        if o_jug[i][1][1] == 1:
                                print(i+1, ')', o_jug[i][0].ljust(10), '-> VALOR de su CARTA:',  o_jug[i][1][0], 'de OROS ')
                        elif o_jug[i][1][1] == 2:
                                print(i+1, ')', o_jug[i][0].ljust(10), '-> VALOR de su CARTA:',  o_jug[i][1][0], 'de COPAS ')
                        elif o_jug[i][1][1] == 3:
                                print(i+1, ')', o_jug[i][0].ljust(10), '-> VALOR de su CARTA:',  o_jug[i][1][0], 'de ESPADAS ')
                        else:
                                print(i+1, ')', o_jug[i][0].ljust(10), '-> VALOR de su CARTA:',  o_jug[i][1][0], 'de BASTOS ')
                print()
                print('BANCA: ', o_jug[0][0])
        print()
        input('Presiona una tecla para salir')
        break



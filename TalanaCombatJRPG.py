
import json


def validaMovimientoPlayerJson(movimiento_player1):
 # Validar el largo de caracteres entregados en el archivo json en la llave movimientos
    for i in movimiento_player1:

        if len(i) <= 5:

            return True

        else:
            print('json con error en largo de caracteres para la llave golpes')
            quit()


def validaGolpePlayerJson(golpes_player1):
    # Validar el largo de caracteres entregados en el archivo json en la llave golpes

    for i in golpes_player1:

        if len(i) <= 1:

            return True

        else:
            print('json con error en largo de caracteres para la llave golpes')
            quit()


def leerJason(nombrejson):
    # Abro y leo el archivo json  posterior se valida que sea un archivo con las reglas de negocio para el largo de caracteres
    # en caso de que las validaciones sean true se retorna la data en la variable resultado para su posterior uso
    with open(nombrejson + '.json') as contenido:

        resultado = json.load(contenido)

        movimiento_player1 = resultado['player1']['movimientos']
        golpes_player1 = resultado['player1']['golpes']
        movimiento_player2 = resultado['player2']['movimientos']
        golpes_player2 = resultado['player2']['golpes']

        mov_player1 = validaMovimientoPlayerJson(movimiento_player1)
        mov_player2 = validaMovimientoPlayerJson(movimiento_player2)
        golp_player1 = validaGolpePlayerJson(golpes_player1)
        golp_player2 = validaGolpePlayerJson(golpes_player2)

        if mov_player1 == True and mov_player2 == True and golp_player1 == True and golp_player2 == True:

            return resultado


def primerAtacante(json_pelea):

    # Se realizan las validaciones necesarias para definir quien sera el primer atacante en el juego
    # el player 1 se define con numero 0 y el player 2 se define con numero 1
    # el valor retornado sera de quien empiece la partida

    player1 = 0
    player2 = 1

    mov_player1 = len(json_pelea['player1']['movimientos'])
    golp_player1 = len(json_pelea['player1']['golpes'])
    total_ataque_player1 = mov_player1 + golp_player1

    mov_player2 = len(json_pelea['player2']['movimientos'])
    golp_player2 = len(json_pelea['player2']['golpes'])
    total_ataque_player2 = mov_player2 + golp_player2

    if total_ataque_player1 < total_ataque_player2:

        return player1

    elif total_ataque_player1 > total_ataque_player2:

        return player2

    else:

        print('empate todo parte player 1 ')


def pelea(inicia_pelea, archivo_json):

    # lista con las combinaciones de golpes de cada personaje
    comgolpesPlayer1 = ['DSDP', 'SDK', 'P', 'K']
    comgolpesPlayer2 = ['SAK', 'ASAP', 'P', 'K']

    comienza = inicia_pelea

    vidaplayer2 = 6
    vidaplayer1 = 6

    while True:
        # con la posicion de posicion_en_json_player1 y posicion_en_json_player2 se recorre los golpes y movimientos dentro del archivo json
        # asi se identifica los diferentes golpes realizados
        # a medida que avanzan los turnos la posicion aumenta en 1 su valor
        posicion_en_json_player1 = 0
        posicion_en_json_player2 = 0

        movque_player1 = archivo_json['player1']['movimientos'][posicion_en_json_player1]
        golpe_player1 = archivo_json['player1']['golpes'][posicion_en_json_player1]

        movque_player2 = archivo_json['player2']['movimientos'][posicion_en_json_player2]
        golpe_player2 = archivo_json['player2']['golpes'][posicion_en_json_player2]

        ataque_player1 = movque_player1 + golpe_player1
        ataque_player2 = movque_player2 + golpe_player2

        if comienza == 0:

            for i in comgolpesPlayer1:

                if ataque_player1 in i:

                    if i == 'DSDP':
                        print('el luchador Tonyn da un Taladoken')

                        vidaplayer2 = vidaplayer2 - 3
                        comienza = 1

                    elif i == 'SDK':
                        print(
                            'el luchador Tonyn  envia un Remuyuken directo en su cara...')

                        vidaplayer2 = vidaplayer2 - 2
                        comienza = 1

                    elif i == 'P' or i == 'DP':
                        print(
                            'el luchador Tonyn  envia un Golpe pu ufffff que dolor...')

                        vidaplayer2 = vidaplayer2 - 1
                        comienza = 1

                    elif i == 'DK':
                        print(
                            'el luchador Tonyn  envia un Patada ufffff que dolor...')

                        comienza = 1
                        vidaplayer2 = vidaplayer2 - 1

                    elif i == 'D' or i == 'S' or i == 'W' or i == 'A':

                        print('el luchador Tonyn  se movio...'
                              )
                        comienza = 1

                    elif ataque_player1 not in i:

                        print(
                            'el luchador Tonyn  envia un ataque desconocido. No hace nada :( ...')

                    else:

                        print('no existe ese movimiento')

        elif comienza == 1:

            for j in comgolpesPlayer2:

                if ataque_player2 in j:

                    if j == 'SAK':
                        vidaplayer2 = vidaplayer2 - 3
                        comienza = 0
                        print(
                            'el luchador Arnaldor envia un Remuyuken ufffff que dolor...')

                    elif j == 'ASAP':

                        vidaplayer2 = vidaplayer2 - 2
                        comienza = 0
                        print(
                            'el luchador Arnaldor  envia un Taladoken y lo deja con mucho dolor...')

                    elif j == 'P':
                        vidaplayer2 = vidaplayer2 - 1
                        comienza = 0
                        print(
                            'el luchador Arnaldor envia un puño en el abdomen uuuuf...')

                    elif j == 'K' or j == 'AK':
                        vidaplayer2 = vidaplayer2 - 1
                        comienza = 0
                        print(
                            'el luchador Arnaldor envia una patada un golpe bajo uuuuu...')

                    elif j == 'D' or j == 'S' or j == 'W' or j == 'A':
                        comienza = 0
                        print('el luchador Arnaldor se movio...')

                    elif ataque_player2 not in i:

                        print(
                            'el luchador Arnaldor envia un ataque desconocido. No hace nada :( ...')

        posicion_en_json_player1 += 1
        posicion_en_json_player2 += 1

        if vidaplayer1 <= 0 or vidaplayer2 <= 0:

            print('fin de la pelea')

            break


if __name__ == '__main__':

    # Ingresar a traves de consola nombre del archivo json

    nombre_pelea = input('nombre archivo de pelea: ')
    json_prueba = leerJason(nombre_pelea)
    atacante = primerAtacante(json_prueba)
    pelea(atacante, json_prueba)

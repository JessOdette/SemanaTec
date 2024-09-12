"""Memory, puzzle game of number pairs.

Exercises:

1. Contar y desplegar el numero de taps JESSICA
2. Detectar cuando todos los cuadros se han destapado JESSICA
3. Central el dígito en el cuadro NICOLLE
4. Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos 
para resolver el juego y que al usuario le ayude a tener mejor memoria ? NICOLLE
"""


from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'taps': 0} #Se crea un diccionario con la marca y el número de taps
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()



def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    state['taps'] += 1  # Incrementar el contador de taps
    print(f"Taps: {state['taps']}")  # Imprimir el número de taps en la consola


    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Imprimir "Winner" si todos los cuadros están destapados
    if all(not hidden for hidden in hide):
        print("Winner")


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()


    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y + 5)  
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)



shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
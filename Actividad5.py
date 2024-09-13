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

tileColors = ["pink", "green", "red", "purple", "blue", "yellow", "orange", "cyan"] #Lista de nombres de colores posibles que puede tener una figura en cada cuadro del tablero
tileShapes = ["square", "circle", "triangle", "rectangle"] #Lista de nombres de figuras posibles que puede haber en cada cuandro del tablero
tiles = [(x, y) for x in tileShapes for y in tileColors] * 2 #Cada cuadro tiene una figura de determinado color al azar

state = {'mark': None, 'taps': 0} #Se crea un diccionario con la marca y el número de taps
hide = [True] * 64


#Figuras posibles que pueden estar en cada cuadro del tablero
def squareDraw(x, y, color):
    """Draw square in tile with given color"""
    up()
    goto(x, y) #Para que cuadrado se dibuje centrado
    down()
    fillcolor(color)
    begin_fill()

    for count in range(4):
        forward(50) #Tamaño corresponde con tamaño de cuadro de tablero
        left(90)

    end_fill()

def circleDraw(x, y, color):
    """Draw circle in tile with given color"""
    up()
    goto(x+25, y) #Para que circulo se dibuje centrado
    down()
    fillcolor(color)
    begin_fill()
    circle(25) #Tamaño de radio corresponde con tamaño de cuadro de tablero
    end_fill()

def triangleDraw(x, y, color):
    """Draw triangle in tile with given color"""
    up()
    goto(x, y) #Para que triangulo se dibuje centrado
    down()
    fillcolor(color)
    begin_fill()

    for _ in range(3):
        forward(50) #Tamaño corresponde con tamaño de cuadro de tablero
        left(120)

    end_fill()

def rectangleDraw(x, y, color):
    """Draw rectangle in tile with given color"""
    up()
    goto(x, y + 12) #Para que rectangulo se dubuje centrado
    down()
    fillcolor(color)
    begin_fill()

    for _ in range(2):
        forward(50) #Tamaño corresponde con tamaño de cuadro de tablero
        left(90)
        forward(25) #Lado más corto del tablero
        left(90)

    end_fill()


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
        #color('black')
        #write(tiles[mark], align="center", font=('Arial', 30, 'normal')) #Los numeros se alinean a centro con align center
        
        #Dibujar figura con color dependiendo del cuadro del tablero seleccionado
        shapeName, shapeColor = tiles[mark]
        if shapeName ==  "rectangle":
            rectangleDraw(x, y, shapeColor)
        elif shapeName == "circle":
            circleDraw(x, y, shapeColor)
        elif shapeName == "triangle":
            triangleDraw(x, y, shapeColor)
        elif shapeName == "square":
            squareDraw(x, y, shapeColor)

    update()
    ontimer(draw, 100)



shuffle(tiles) #Mezclar cuadros de tablero
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

"""Paint, for drawing shapes.

Exercises

1. Add a color. NICOLLE
2. Complete circle. NICOLLE
3. Complete rectangle. JESSICA
4. Complete triangle. JESSICA

"""

from turtle import *

from freegames import vector


#Dibuja una línea desde el punto de inicio hasta el punto final
def line(start, end):
    """Draw line from start to end."""
    up() #Levanta la pluma
    goto(start.x, start.y) #Va al punto de inicio
    down() #Baja la pluma
    goto(end.x, end.y) #Va al punto final


def square(start, end):
    """Draw square from start to end."""
    up() #Levanta la pluma
    goto(start.x, start.y) #Va al punto de inicio
    down() #Baja la pluma
    begin_fill() #Comienza a rellenar el cuadrado

    for count in range(4): #Dibuja los cuatro lados del cuadrado
        forward(end.x - start.x) #Mueve la pluma al punto final
        left(90) #Gira 90 grados

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up() #Levanta la pluma
    goto(start.x, start.y) #Va al punto de inicio
    down() #Baja la pluma
    begin_fill() #Comienza a rellenar el rectángulo

    # Dibujar dos lados largos y dos lados cortos
    forward(end.x - start.x)  # Lado largo
    left(90) # Gira 90 grados
    forward(end.y - start.y)  # Lado corto
    left(90) # Gira 90 grados
    forward(end.x - start.x)  # Lado largo
    left(90) # Gira 90 grados
    forward(end.y - start.y)  # Lado corto
    left(90) # Gira 90 grados

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up() #Levanta la pluma
    goto(start.x, start.y) #Va al punto de inicio 
    down() #Baja la pluma
    begin_fill() #Comienza a rellenar el triángulo

    # Dibujar tres lados del triángulo
    for _ in range(3):
        forward(end.x - start.x) #Va al punto final
        left(120) #Gira 120 grados para formar un triángulo equilátero

    end_fill() #Rellena el triángulo


#Esta función se activa cuando se da click en la pantalla
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start'] #Guarda el punto de inicio
 
    if start is None:
        state['start'] = vector(x, y) #Si no hay punto de inicio, guarda el punto donde se dio click
    else:
        shape = state['shape'] #Si ya hay un punto de inicio, guarda la figura que se va a dibujar
        end = vector(x, y) #Guarda el punto final
        shape(start, end) #Dibuja la figura
        state['start'] = None #Reinicia el punto de inicio


#Esta función se activa cuando se da click en la tecla correspondiente
def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') #Agregamos el color amarillo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done() #Comment


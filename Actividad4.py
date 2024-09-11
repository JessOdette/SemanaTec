"""Cannon, hitting targets with projectiles.

Exercises

1. La velocidad del movimiento para el proyectil y los balones sea más rápida
2. Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.
"""

from random import randrange
from turtle import *

from freegames import vector


ball = vector(-200, -200) #Posición inicial de la bola
speed = vector(0, 0) #Velocidad de la bola
targets = [] #Lista de objetivos
 

#Respoder al tap en la pantalla
def tap(x, y):
    """Respond to screen tap."""
    #
    if not inside(ball): #Si la bola no está dentro de la pantalla
        ball.x = -199 #Posición inicial de la bola
        ball.y = -199 #Posición inicial de la bola
        speed.x = (x + 200) / 10 #Velocidad de la bola
        speed.y = (y + 200) / 10 #Velocidad de la bola


#Verificar si la bola está dentro del grid
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


#Dibujar la bola y los objetivos
def draw():
    """Draw ball and targets."""
    clear()

    #Dibuja los targets
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    #Dibuja el proyectil
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(20) == 0: #Que tan seguido se crean los objetivos
        y = randrange(-150, 150) #Rango de aparición de los objetivos
        target = vector(200, y) #Posición de los objetivos a la derecha
        targets.append(target) #Agrega los objetivos a la lista

    #Mueve los objetivos hacia la izquierda
    for target in targets:
        target.x -= 1.5

    #Mueve el proyectil si está dentro de la pantalla
    if inside(ball):
        speed.y -= 0.35 #Gravedad que afecta al proyectil
        ball.move(speed) #Mueve el proyectil

    #Copia los objetivos
    dupe = targets.copy()
    targets.clear() #Limpia la lista de objetivos

    #Mantiene los objetivos que están dentro de la pantalla
    for target in dupe: 
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    #Reposiciona los objetivos a la derecha
    for target in targets:
        if not inside(target):
            target.x = 200 #Reposiciona los objetivos a la derecha

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False) 
onscreenclick(tap)
move()
done()

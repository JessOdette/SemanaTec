"""Snake, classic arcade game.

Exercises

1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana NICOLLE
2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, 
pero al azar, de una serie de 5 diferentes colores, excepto el rojo. JESSICA
3. Hacer la snake más rapida o más lenta.
"""

import random
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 200 #Inicializamos una varible de velocidad
snake_color = random.choice(["Pink", "Blue", "Green", "Yellow"])
food_color = random.choice(["Pink", "Blue", "Purple", "Green"])

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    global random_color
    global speed #Usamos keyword 'global' para cambiar los valores de la variable dentro de la función 
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        speed = speed - 10 #Aumentamos la velocidad conforme come la serpiente
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color) #Cambia el color de la serpiente

    square(food.x, food.y, 9, food_color) #Cambia el color de la comida
    update()
    ontimer(move, speed) #Actualizamos parametro

def random_color():	
	pass

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

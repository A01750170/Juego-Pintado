# Código modificado por:
# Autor: Erick Hernández Silva 
# Autor: Jeovani Hernández Bastida 

import turtle # Se importa turtle para dibujar el circulo
from turtle import *
from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up() # Levanta la pluma
    goto(start.x, start.y) # Nos lleva al punto inicial
    down() # Baja la pluma
    goto(end.x, end.y) # Nos lleva al punto final


def square(start, end):
    "Draw square from start to end."
    up() # Levanta la pluma
    goto(start.x, start.y) # Nos lleva al punto inicial
    down() # Baja la pluma
    begin_fill() # Comienza a rellenar la figura

    # Crea los cuatro lados del cuadrado
    for count in range(4):
        # Nos mueve hacia adelante
        forward(end.x - start.x)
        # Rotamos 90 grados a la izquierda
        left(90)
    end_fill() # Dejamos de rellenar la figura


def circle(start, end):
    """
    Genera el círculo tomando el radio del circulo como la resta el
    inicial y el x final
    """
    up() # Levanta la pluma
    goto(start.x, start.y) # Nos lleva al punto inicial
    down() # Baja la pluma
    radius = end.x - start.x # Calcula el radio del circulo                
    turtle.circle(radius) # Dibuja el circulo


def rectangle(start, end):
    "Draw rectangle from start to end."
    up() # Levanta la pluma 
    goto(start.x, start.y) # Nos lleva al punto inicial
    down() # Baja la pluma 
    begin_fill() # Comienza a rellenar la figura 

    """ 
    Se hace un ciclo para saber cual va ser la longitud de la linea
    dependiendo del punto donde se encuentre la pluma 
    """
    for count in range(4):
        if(count == 0 or 
                count == 2):
            forward(end.x - start.x)
            left(90)
        else:
            forward(end.y - start.y)
            left(90)

    end_fill # Dejamos de rellenar la figura 


def triangle(start, end):
    "Draw triangle from start to end."
    up() # Levanta la pluma 
    goto(start.x, start.y) # Nos lleva al punto inicial
    down() # Baja la pluma
    begin_fill() # Comienza a rellenar la figura 

    # Se crean los lados del triángulo 
    for count in range(3):
        if (count == 0):
            forward((end.x - start.x) * 2) # Hace la linea hacia adelante
        elif (count == 1):
            left(135) # Gira a la izquierda 135 al ser el punto 1
        elif (count == 2):
            forward((end.y - start.y) * 2) # Se mueve recto hacia el punto 2              
    end_fill() # Dejamos de rellenar la figura
    right(135) # Se vulve a poner recto el cursor 


def tap(x, y):
    """
    Store starting point or draw shape 
    Verifica si el click dado es el inicial o el final
    """
    start = state['start']
    # Si no tenemos un punto inicial
    if start is None:
        state['start'] = vector(x, y)

    # Si si tenemos un punto inicial
    else: 
        shape = state['shape'] # Obtenemos el estado o la figura a dibujar
        end = vector(x, y) # Asignamos los puntos xy del punto final
        shape(start, end) # Llamamos al método de la figura
        state['start'] = None # Borramos el punto inicial


def store(key, value):
    """
    Store value in state at key.
    Cambia la figura a dibujar
    """
    
    state[key] = value

# Se inicializa el estado inicial como una linea y sin punto inicial
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) # Se crea el canvas para dibujar
onscreenclick(tap) # Cuando se da un click
listen()    # Escucha los eventos del teclado 
onkey(undo, 'u') # Cuando se presiona 'u' se deshace la ultima acción

# Se definen las teclas que cambian de color
onkey(lambda: color('black'), 'K') 
onkey(lambda: color('white'), 'W') 
onkey(lambda: color('green'), 'G') 
onkey(lambda: color('blue'), 'B') 
onkey(lambda: color('red'), 'R') 
onkey(lambda: color('pink'), 'P') 

# Se definen las teclas asociadas con la figura
onkey(lambda: store('shape', line), 'l') 
onkey(lambda: store('shape', square), 's') 
onkey(lambda: store('shape', circle), 'c') 
onkey(lambda: store('shape', rectangle), 'r') 
onkey(lambda: store('shape', triangle), 't') 

done()
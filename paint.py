from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    up() #Levanta la pluma 
    goto(start.x, start.y) #Nos lleva al punto inicial
    down() #Baja la pluma 
    begin_fill() #Comienza a rellenar la figura 

    """ Se hace un ciclo para saber cual va ser la longitud de la linea
    dependiendo del punto donde se encuentre la pluma """
    for count in range(4):
        if(count == 0 or 
                count == 2):
            forward(end.x - start.x)
            left(90)
        else:
            forward(end.y - start.y)
            left(90)
    end_fill #Dejamos de rellenar la figura 

def triangle(start, end):
    "Draw triangle from start to end."
    up() #Levanta la pluma 
    goto(start.x, start.y) #Nos lleva al punto inicial
    down() #Baja la pluma
    begin_fill() #Comienza a rellenar la figura 

    #Se crean los lados del triángulo 
    for count in range(3):
        if (count == 0):
            forward((end.x - start.x) * 2) #Hace la linea hacia adelante
        elif (count == 1):
            left(135) #Gira a la izquierda 135 al ser el punto 1
        elif (count == 2):
            forward((end.y - start.y) * 2) #Se mueve recto hacia el punto 2              
    end_fill() #Dejamos de rellenar la figura
    right(135) #Se vulve a poner recto el cursor 

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
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
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
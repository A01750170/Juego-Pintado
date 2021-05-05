import turtle #Se importa turtle para dibujar el circulo
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up() #Levanta la pluma
    goto(start.x, start.y) #Nos lleva al punto inicial
    down() #Baja la pluma
    goto(end.x, end.y) #Nos lleva al punto final

def square(start, end):
    "Draw square from start to end."
    up() #Levanta la pluma
    goto(start.x, start.y) #Nos lleva al punto inicial
    down() #Baja la pluma
    begin_fill() #Comienza a rellenar la figura

    #Crea los cuatro lados del cuadrado
    for count in range(4):
        #Nos mueve hacia adelante
        forward(end.x - start.x)
        #Rotamos 90 grados a la izquierda
        left(90)
    end_fill() #Dejamos de rellenar la figura

"""Genera el círculo tomando el radio del circulo como la resta el
    inicial y el x final
"""
def circle(start, end):
    up() #Levanta la pluma
    goto(start.x, start.y) #Nos lleva al punto inicial
    down() #Baja la pluma
    radius = end.x - start.x #Calcula el radio del circulo                
    turtle.circle(radius) #Dibuja el circulo

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

""" Verifica si el click dado es el inicial o el final
"""
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']
    #Si no tenemos un punto inicial
    if start is None:
        state['start'] = vector(x, y)
    else: #Si si tenemos un punto inicial
        shape = state['shape'] #Obtenemos el estado o la figura a dibujar
        end = vector(x, y) #Asignamos los puntos xy del punto final
        shape(start, end) #Llamamos al método de la figura
        state['start'] = None #Borramos el punto inicial

"""Cambia la figura a dibujar"""
def store(key, value):
    "Store value in state at key."
    state[key] = value
#Se inicializa el estado inicial como una linea y sin punto inicial
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) #Se crea el canvas para dibujar
onscreenclick(tap) #Cuando se da un click
listen()
onkey(undo, 'u') #Cuando se presiona 'u' se deshace la ultima acción
#Se cambia a color negro al presionar 'K'
onkey(lambda: color('black'), 'K') 
#Se cambia a color blanco al presionar 'W'
onkey(lambda: color('white'), 'W') 
#Se cambia a color verde al presionar 'G'
onkey(lambda: color('green'), 'G') 
#Se cambia a color azul al presionar 'B'
onkey(lambda: color('blue'), 'B') 
#Se cambia a color rojo al presionar 'R'
onkey(lambda: color('red'), 'R') 
#Se cambia a color rosa al presionar 'P'
onkey(lambda: color('pink'), 'P') 
#Cambia la figura a linea al presionar 'l'
onkey(lambda: store('shape', line), 'l') 
#Cambia la figura a cuadrado al presionar 's'
onkey(lambda: store('shape', square), 's') 
#Cambia la figura a circulo al presionar 'c'
onkey(lambda: store('shape', circle), 'c') 
#Cambia la figura a rectangulo al presionar 'r'
onkey(lambda: store('shape', rectangle), 'r') 
#Cambia la figura a triangulo al presionar 't'
onkey(lambda: store('shape', triangle), 't') 
done()
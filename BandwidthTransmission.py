import turtle

def setup_write():
    skk.color("black")
    skk.penup()  # don't draw when turtle moves
    skk.goto(-450, 0)  # move the turtle to a location
    skk.showturtle()  # make the turtle visible
    skk.pendown()

def quadriallage():
    skk.color("blue")
    skk.penup()
    skk.goto(-450, -100)
    skk.left(90)
    for z in range(20):
        for i in range(20):
            skk.pendown()
            skk.forward(5)
            skk.penup()
            skk.forward(5)
        if z % 2 == 0:
            skk.right(90)
            skk.forward(50)
            skk.right(90)
            skk.forward(5)
        else:
            skk.left(90)
            skk.forward(50)
            skk.left(90)
            skk.forward(5)
    skk.right(90)



def write_NRZ(trame):
    for i in range(len(trame)):
        if trame[i] == '1' and trame[i - 1] == '0':
            skk.left(90)
            skk.forward(50)
            skk.right(90)
            skk.forward(50)
        if trame[i] == '0' and trame[i - 1] == '1':
            skk.right(90)
            skk.forward(50)
            skk.left(90)
            skk.forward(50)
        if trame[i] == trame[i - 1]:
            skk.forward(50)
    turtle.done()

def write_Machester(trame):
    for i in range(len(trame)):
        if trame[i] == '1':
            if trame[i - 1] == '1':
                skk.left(90)
                skk.forward(50)
                skk.right(90)
            skk.forward(25)
            skk.right(90)
            skk.forward(50)
            skk.left(90)
            skk.forward(25)
        if trame[i] == '0':
            if trame[i - 1] == '0':
                skk.right(90)
                skk.forward(50)
                skk.left(90)
            skk.forward(25)
            skk.left(90)
            skk.forward(50)
            skk.right(90)
            skk.forward(25)
    turtle.done()


def write_MachesterDif(trame):
    magic = True
    for i in range(len(trame)):
        if magic == False :
            if trame[i] == '1':
                skk.forward(25)
                skk.right(90)
                skk.forward(50)
                skk.left(90)
                skk.forward(25)
                magic = True
            if trame[i] == '0':
                skk.right(90)
                skk.forward(50)
                skk.left(90)
                skk.forward(25)
                skk.left(90)
                skk.forward(50)
                skk.right(90)
                skk.forward(25)
        else:
            if trame[i] == '0':
                skk.left(90)
                skk.forward(50)
                skk.right(90)
                skk.forward(25)
                skk.right(90)
                skk.forward(50)
                skk.left(90)
                skk.forward(25)
            if trame[i] == '1':
                skk.forward(25)
                skk.left(90)
                skk.forward(50)
                skk.right(90)
                skk.forward(25)
                magic = False
    turtle.done()

def write_Miller(trame):
    magic = True
    for i in range(len(trame)):
        if magic == False :
            if(trame[i] == '1' ):
                skk.forward(25)
                skk.right(90)
                skk.forward(50)
                skk.left(90)
                skk.forward(25)
                magic = True
            if trame[i] == '0':
                if trame[i - 1] == '0':
                    skk.left(90)
                    skk.forward(50)
                    skk.right(90)
                skk.forward(50)
                if i+1< len(trame) and trame[i + 1] == '0':
                    skk.right(90)
                    skk.forward(50)
                    skk.left(90)
                    magic = True
        else:
            if trame[i] == '0':
                skk.forward(50)
                if i+1< len(trame) and trame[i + 1] == '0':
                    magic = False
            if trame[i] == '1':
                skk.forward(25)
                skk.left(90)
                skk.forward(50)
                skk.right(90)
                skk.forward(25)
                magic = False
    turtle.done()


print("1. NRZ \n" + "2. Manchester \n" + "3. Manchester différentiel \n" + "4. Miller \n" + "5. Quitter")
print("Veuillez choisir votre codage : ")
inputChoix = int(input())


print("Veuillez saisir votre trame : ")
inputTrame = input()

skk = turtle.Turtle()
skk.speed(0)
quadriallage()
setup_write()


if(inputChoix == 1):
    write_NRZ(inputTrame)

if(inputChoix == 2):
    write_Machester(inputTrame)

if(inputChoix == 3):
    write_MachesterDif(inputTrame)

if(inputChoix == 4):
    write_Miller(inputTrame)

if(inputChoix == 5):
    quit(1)






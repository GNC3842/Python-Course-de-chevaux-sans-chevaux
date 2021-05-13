import turtle, time, random

LARGEUR, HAUTEUR = 0.75, 0.75
global couleurs 
couleurs = ['red', 'green', 'blue', 'orange', 'darkcyan', 'black', 'purple', 'navy', 'brown', 'cyan']

def initGame():
    #Screnen et nombre de tortue
    screen = turtle.Screen()
    screen.setup(LARGEUR,HAUTEUR)
    screen.title("CHEVREEEEEEEEE")
    NbreTortue = screen.numinput("Players","Combien de tortue? (2-8)",4,minval=2,maxval=8)
    NbreTortue = int(NbreTortue)
    #Dimension sreen
    global h
    global l
    h = screen.window_height()
    l = screen.window_width()
    screen.bgcolor("gray")
    #Ligne arrivée
    global arrivéX
    arrivéX = l//2 - (l*(1/10))
    turtle.penup()
    turtle.goto(arrivéX, h//2 )
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(h)
    return NbreTortue

def création_coureurs(NbreTortue):
    tortues = []
    for i in range(NbreTortue):
        coureur = turtle.Turtle()
        coureur.color(couleurs[i])
        coureur.setheading(0)
        coureur.penup()
        coureur.setposition(-(l//2)+(l*(1/50)),0 + ((h*(5/100))+(h*(5/100))*i)*((-1)**i))
        coureur.pendown()
        coureur.pensize(2)
        tortues.append(coureur)
    return tortues

def course(tortues):
    while True:
        for coureurs in tortues:
            d = random.randint(5,20)
            coureurs.forward(d)
            x,y = coureurs.position()
            if x >= arrivéX:
                return couleurs[tortues.index(coureurs)]


nbreT = initGame()
listeJoeuru = création_coureurs(nbreT)
couelurGagnate = course(listeJoeuru)
turtle.penup()
turtle.goto(-20,0)
turtle.hideturtle()   
turtle.write(("Le gagnant est la tortue",couelurGagnate), move=False, align="center", font=("Arial", 50, "bold"))
time.sleep(3)
turtle.bye()


# Elementpedia - An interactive display of the periodic table
import turtle as t

# Initialize screen
ptDisplay = t.Screen()
ptDisplay.title('Elementpedia - The Periodic Table')
ptDisplay.bgcolor('black')
ptDisplay.tracer(0) 

# Initialize pen
pen = t.Turtle()
pen.hideturtle()
pen.speed(0)

# Load file containing all data
ptData = open("allelements.txt", "r")

buttons = []

# Construct an array of dicts showing colours, element names, chemical symbols and positions of buttons

for line in ptData.readlines():
    split = line.split('/')
    if line != "\n":
        buttons.append({'x':int(split[0]),'y':int(split[1]),'t':split[2],'e':split[3],'cs':split[4],'an':split[5],'aw':split[6]})  

buttonSize = 40

# Customizable dict showing all the colours indicating element groups
typeColour = {
    "Alkali metal": "darkturquoise", # "cyan"
    "Alkaline earth metal": "indianred", # "red"
    "Transition metal": "mediumpurple", # "purple"
    "Post-transition metal": "mediumseagreen", # "green"
    "Metalloid": "khaki", # "yellow"
    "Reactive non-metal": "royalblue", # "blue"
    "Noble gas": "hotpink", # "magenta"
    "Lanthanide": "deepskyblue", # "lightblue"
    "Actinide": "sandybrown", # "orange"
    "Unknown": "silver", # "gray"
    }

# Function used for rendering buttons
def ptSquareButton(x, y, color, fillcolor, size, el, an, aw):
    # Set pen position and colours, then begin fill
    pen.goto(x,y)   # x and y are the position of the top-left corner of the square to be drawn   
    pen.color(color)   # Outline colour
    pen.fillcolor(fillcolor)   # Fill colour
    pen.begin_fill()
    pen.pendown()

    # Draw square according to size
    for i in range(0,4):
        pen.forward(size)   # Side length of square
        pen.right(90)

    # End fill and pen up
    pen.end_fill()
    pen.penup()

    # Setting colour
    pen.color('black')

    # Chemical symbol
    pen.goto(x+size/8, y-size/1.2)   
    pen.write(el, False, align="left", font=('Arial', round(size*0.4), 'normal'))

    # Atomic number
    pen.goto(x+size/1.05, y-size/3)   
    pen.write(an, False, align="right", font=('Arial', round(size*0.2), 'normal'))

    # Atomic weight
    pen.goto(x+size/1.05, y-size/1.05)   
    pen.write(aw, False, align="right", font=('Arial', round(size*0.15), 'normal'))
    
# Function triggered when clicked to check which element was clicked on
def detectClick(x, y):
    for button in buttons:
        # If the mouse coordinates are within those of an element, display information on that element
        if x < button['x']+buttonSize and x > button['x'] and y < button['y'] and y > button['y']-buttonSize:
            # Preview of the element clicked
            pen.seth(0)
            ptSquareButton(-370, 350, 'black', typeColour[button['t']], buttonSize*3, button['cs'], button['an'], button['aw'])

            # Preparing to clear the info area
            pen.fillcolor('black')
            pen.goto(-250,400)
            pen.begin_fill()

            # Clearing info area
            pen.goto(370,400)
            pen.goto(370,210)
            pen.goto(-250,210)
            pen.goto(-250,400)
            pen.end_fill()

            # Element name
            pen.color('white')
            pen.goto(-230, 300)   
            pen.write('Element: '+button['e'], False, align="left", font=('Arial', round(buttonSize*3*0.3), 'normal'))
            # Chemical symbol
            pen.goto(-230, 275)   
            pen.write('Chemical symbol: '+button['cs'], False, align="left", font=('Arial', round(buttonSize*3*0.15), 'normal'))
            # Atomic number
            pen.goto(-230, 255)   
            pen.write('Atomic number: '+button['an'], False, align="left", font=('Arial', round(buttonSize*3*0.1), 'normal'))
            # Element group (coloured) 
            pen.color(typeColour[button['t']])
            pen.goto(350, 254)   
            pen.write('Element group: '+button['t'], False, align="right", font=('Arial', round(buttonSize*3*0.1), 'normal'))
            # Element group (white)
            pen.color('white')
            pen.goto(350, 255)   
            pen.write('Element group: '+button['t'], False, align="right", font=('Arial', round(buttonSize*3*0.1), 'normal'))
            # Standard atomic weight
            pen.goto(-230, 235)   
            pen.write('Standard atomic weight: '+button['aw'], False, align="left", font=('Arial', round(buttonSize*3*0.1), 'normal'))

            # Reqriting group label
            pen.goto(0,215)
            pen.write('Group', False, align="center", font=('Arial', round(buttonSize*0.3), 'normal'))  
            '''print('------------------\nElement: '+button['e']
                  +'\nChemical symbol: '+button['cs']
                  +'\nAtomic number: '+button['an']
                  +'\nStandard atomic weight: '+button['aw']
                  +'\nElement group: '+button['t'])'''

# Function to load the periodic table

def loadPt():
    # Render all element blocks/buttons
    for button in buttons:
        ptSquareButton(button['x'],button['y'],'black',typeColour[button['t']],buttonSize,button['cs'],button['an'],button['aw'])

    # Preparing to render the key
    pen.goto(-370, -250)
    pen.seth(270)

    # This variable will keep track of iterations in the following for loop
    count = 0

    # Loop to display colour key/legend
    for group in typeColour:

        if count == 5:
            pen.goto(30, -250)
        pen.color('black')
        pen.fillcolor(typeColour[group])
        pen.begin_fill()
        pen.circle(buttonSize/6)
        pen.end_fill()
        pen.color('white')
        pen.seth(0)
        pen.forward(buttonSize/2)
        pen.seth(270)
        pen.forward(buttonSize/4)
        pen.write(group, False, align="left", font=('Arial', round(buttonSize*3*0.1), 'normal'))
        pen.seth(0)
        pen.backward(buttonSize/2)
        pen.seth(270)
        pen.forward(buttonSize/3)
        count += 1

    # The placeholder for the info to be shown in the info area
    pen.color('white')
    pen.goto(-230, 300)   
    pen.write('Click on an element to learn about it!', False, align="left", font=('Arial', round(buttonSize*3*0.18), 'normal'))

    pen.goto(-375,160)   
    for i in range(1,8):
        pen.write(str(i), False, align="right", font=('Arial', round(buttonSize*0.3), 'normal'))
        pen.forward(40)

    pen.goto(-350,190)   
    for i in range(1,19):
        pen.write(str(i), False, align="center", font=('Arial', round(buttonSize*0.3), 'normal'))
        pen.seth(0)
        pen.forward(40)
        if i == 3:
            pen.forward(20)

    pen.goto(0,215)
    pen.write('Group', False, align="center", font=('Arial', round(buttonSize*0.3), 'normal'))

    pen.goto(-390,10)
    pen.write('Period', False, align="right", font=('Arial', round(buttonSize*0.3), 'normal'))

    pen.goto(450, -385)   
    pen.write('Elementpedia v0.0 (WIP)', False, align="right", font=('Arial', round(buttonSize*3*0.1), 'normal'))

    # Onclick to trigger function detectClick()
    ptDisplay.onclick(detectClick, btn=1, add=None)

# Load periodic table
loadPt()

ptDisplay.mainloop()

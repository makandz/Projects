# Main Robot Drawing
robot = [
    # [partOfRobot, Type, Parent, Position/Values]
    # Rect: x, y, w, h
    [False, 'fill', 'ground', [160, 82, 45]],
    [False, 'rect', 'ground', [0, 500, 800, 100]],
    [False, 'fill', 'feet', [0, 0, 0]],
    [True, 'rect', 'foot_l', [275, 475, 60, 25]],
    [True, 'rect', 'foot_r', [390, 475, 60, 25]],
    [False, 'fill', 'legs', [150, 150, 150]],
    [True, 'rect', 'leg_l', [310, 375, 25, 100]],
    [True, 'rect', 'leg_r', [390, 375, 25, 100]],    
    [False, 'fill', 'box', [140, 140, 140]],
    [False, 'fill', 'arms', [150, 150, 150]],
    [True, 'rect', 'arm_l', [210, 230, 100, 25]],
    [True, 'rect', 'arm_r', [415, 230, 100, 25]],
    [False, 'fill', 'arms', [130, 130, 130]],
    [True, 'rect', 'fingers_l', [190, 230, 20, 10]],
    [True, 'rect', 'fingers_l', [190, 245, 20, 10]],
    [True, 'rect', 'fingers_r', [515, 230, 20, 10]],
    [True, 'rect', 'fingers_r', [515, 245, 20, 10]],
    
    # Moving Parts
    [False, 'fill', 'neck', [150, 150, 150]],
    [True, 'rect', 'neck', [350, 205, 25, 20]],
    [True, 'rect', 'broadcast', [359, 150, 5, 55]],
    [False, 'fill', 'bulb', [255, 0, 0]],
    [True, 'ellipse', 'bulb', [361, 150, 15, 15]],
    [False, 'fill', 'ears', [145, 145, 145]],
    [True, 'rect', 'wing_l', [307, 160, 70, 15]],
    [True, 'rect', 'ear_l', [313, 155, 12, 25]],
    [True, 'rect', 'wing_r', [348, 160, 70, 15]],
    [True, 'rect', 'ear_r', [400, 155, 12, 25]],
    # End Moving
    
    [False, 'fill', 'body', [130, 130, 130]],
    [True, 'rect', 'body', [310, 225, 105, 175]],
    [True, 'rect', 'box', [325, 240, 75, 40]],
    [False, 'fill', 'button_1', [225, 225, 225]],
    [True, 'ellipse', 'button_1', [345, 260, 20, 20]],
    [False, 'fill', 'button_2', [225, 225, 225]],
    [True, 'ellipse', 'button_2', [380, 260, 20, 20]],
    [False, 'fill', 'head', [170, 170, 170]],
    [True, 'rect', 'head', [325, 130, 75, 75]],
    [False, 'fill', 'eyes', [255, 255, 255]],
    [True, 'rect', 'eye_l', [335, 145, 15, 15]],
    [True, 'rect', 'eye_r', [375, 145, 15, 15]],
    [False, 'fill', 'pupils', [0, 0, 0]],
    [True, 'rect', 'pupil_l', [339, 149, 7, 7]],
    [True, 'rect', 'pupil_r', [379, 149, 7, 7]],
    [True, 'rect', 'mouth', [343, 180, 40, 5]],
    [False, 'textsize', 32],
    [True, 'text', ["M-Robo 7000", 100, 100]],
]

tick = 0
moveable = ['wing_l', 'wing_r', 'bulb', 'broadcast', 'head', 'ear_l', 'ear_r', 'pupil_l', 'pupil_r', 'eye_l', 'eye_r', 'mouth']

mov = [0, 0]
fall = False
button = [False, False]
hover = [0, 0]
head = [0, 0]

# First setup
def setup():
    print("Script is running..")
    size(800, 600) # Size of window (w, h)

# Main loop
def draw():
    global robot, mov, hover, tick
    tick += 1
    
    if hover[0] == 1:
        if hover[1] <= 60:
            hover[1] += 1
        else:
            hover[0] = 2
    elif hover[0] == 0 and hover[1] > 0:
        hover[1] -= 1
        
    if fall and mov[1] < 400:
        mov[1] += 8
    elif not fall and mov[1] > 0:
        mov[1] -= 8

    # Done every loop
    clear()
    background(135, 206, 235)

    # Loop and create.
    for part in robot:
        if part[0]:
            y = 0
            x = mov[0]

            if fall or (not fall and mov[1] > 0):
                print("fell", mov[1])
                if mov[1] + part[3][3] + part[3][1] >= 500:
                    y = 500 - part[3][3] - part[3][1]
                else:
                    y = mov[1]
            elif hover[0] >= 1 or (hover[0] == 0 and hover[1] > 0):
                if part[2] == "wing_l":
                    x += hover[1] * -1 / 2
                elif part[2] == "wing_r":
                    x += hover[1] / 2
                elif part[2] == "broadcast" or part[2] == "bulb":
                    y += hover[1] * -1
                elif part[2] == "neck":
                    y += hover[1]
                    
                if hover[0] == 2 and part[2] in moveable:
                    x += head[0]
                    y += head[1]

            pushMatrix()
            translate(x, y)
        
        # Is part an object?
        if part[1] == "fill":
            if button[0] and part[2] == "button_1":
                part[3][1] = 0
                part[3][2] = 0
            elif part[2] == "button_1":
                part[3][1] = 225
                part[3][2] = 225
            
            if button[1] and part[2] == "button_2":
                part[3][1] = 0
                part[3][2] = 0
            elif part[2] == "button_2":
                part[3][1] = 225
                part[3][2] = 225
                
            fill(part[3][0], part[3][1], part[3][2])
        elif part[1] == "rect":
            rect(part[3][0], part[3][1], part[3][2], part[3][3])
        elif part[1] == "ellipse":
            ellipse(part[3][0], part[3][1], part[3][2], part[3][3])
        elif part[1] == "text":
            text(part[3][0], part[3][1], part[3][2])
        elif part[1] == "textsize":
            textSize(part[3])
        else:
            print("Value does not exist!")
            
        if part[0]:
            popMatrix()

def keyPressed():
    global key, mov, fall, hover
    if key == "a" and mov[0] > -190:
        if hover[0] == 2:
            head[0] -= 5
        else:
            mov[0] -= 5
    if key == "d" and mov[0] < 265:
        if hover[0] == 2:
            head[0] += 5
        else:
            mov[0] += 5
    if key == "w" and head[1] > -100:
        if hover[0] == 2:
            head[1] -= 8
    if key == "s":
        print(head[1])
        if hover[0] == 2 and head[1] <= 0:
            head[1] += 10
    if key == "b":
        if hover[0] == 0:
            fall = not fall
            button[0] = not button[0]
    if key == "f":
        goHover()
    print("mov", mov)
    
def mouseClicked():
    global mouseX, mouseY, button, fall
    if mouseX in range(335 + mov[0], 356 + mov[0]) and mouseY in range(250 + mov[1], 271 + mov[1]):
        button[0] = not button[0]
        fall = not fall
    elif mouseX in range(370 + mov[0], 390 + mov[0]) and mouseY in range(250 + mov[1], 271 + mov[1]):
        goHover()
    print(mouseX, mouseY)

def goHover():
    global hover
    if hover[0] == 0:
        hover[0] = 1
    elif hover[0] == 2 and head[0] in range(-10, 10) and head[1] in range(-10, 10):
        hover[0] = 0
    else:
        return
    button[1] = not button[1]

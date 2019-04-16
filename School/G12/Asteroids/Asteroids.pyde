class Star():
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.size = state
        self.increase = True

    def render(self):
        fill(255)
        strokeWeight(0)
        ellipse(self.x, self.y, self.size * 0.12, self.size * 0.12)
        if tick % 2 == 0:
            self.increaseState()

    def increaseState(self):
        if self.increase:
            if self.size >= 40:
                self.increase = False
            else:
                self.size += 1
        else:
            if self.size <= 1:
                self.increase = True
                self.x = random(800)
                self.y = random(800)
            else:
                self.size -= 1

class Asteroid():
    def __init__(self, x, y, size, velocity = [0, 0]):
        self.x = x
        self.y = y
        self.size = size
        self.life = 3
        self.velocity = velocity

    def render(self):
        fill(255, 110)
        stroke(255)
        strokeWeight(3)
        ellipse(self.x, self.y, self.size, self.size)
        self.moveVelocity()

    def moveVelocity(self):
        if self.x + self.size > 950:
            self.x = -50
        elif self.x + self.size < -150:
            self.x = 850
        if self.y + self.size > 950:
            self.y = -50
        elif self.y + self.size < -150:
            self.y = 850
        
        self.x += self.velocity[0]
        self.y -= self.velocity[1]

class Ship():
    def __init__(self, x, y, velocity = [0, 0]):
        self.life = 5
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = 0
        self.moving = False
    
    def render(self):
        fill(0, 110)
        strokeWeight(4)
        stroke(255)
        pushMatrix()
        translate(ship.x, ship.y)
        rotate(radians(ship.angle))
        triangle(-20, 10, 20, 10, 0, -30)
        if self.moving:
            fill(255, 0, 0)
            strokeWeight(0)
            triangle(-20, 20, 20, 20, 0, 40)
        popMatrix()
        self.moveVelocity()

    def moveVelocity(self):
        if self.x + 20 > 900:
            self.x = -50
        elif self.x + 20 < -150:
            self.x = 850
        if self.y + 20 > 900:
            self.y = -50
        elif self.y + 20 < -150:
            self.y = 850
        
        # Friction
        if not 0 in self.velocity:
            angle = degrees(atan(abs(self.velocity[0]) / abs(self.velocity[1])))
        else:
            angle = 0
        
        friction = 1.2

        # TR 1
        if self.velocity[0] > 0 and self.velocity[1] > 0:
            self.velocity[0] -= sin(radians(angle)) * friction
            self.velocity[1] -= cos(radians(angle)) * friction
            if self.velocity[0] < 0 or self.velocity[1] < 0:
                self.velocity[0] = 0
                self.velocity[1] = 0
        # BR 2
        elif self.velocity[0] > 0 and self.velocity[1] < 0:
            self.velocity[0] -= sin(radians(angle)) * friction
            self.velocity[1] += cos(radians(angle)) * friction
            if self.velocity[0] < 0 or self.velocity[1] > 0:
                self.velocity[0] = 0
                self.velocity[1] = 0
        # BL 3
        elif self.velocity[0] < 0 and self.velocity[1] < 0:
            self.velocity[0] += sin(radians(angle)) * friction
            self.velocity[1] += cos(radians(angle)) * friction
            if self.velocity[0] > 0 or self.velocity[1] > 0:
                self.velocity[0] = 0
                self.velocity[1] = 0
        # TL 4
        elif self.velocity[0] < 0 and self.velocity[1] > 0:
            self.velocity[0] += sin(radians(angle)) * friction
            self.velocity[1] -= cos(radians(angle)) * friction
            if self.velocity[0] > 0 or self.velocity[1] < 0:
                self.velocity[0] = 0
                self.velocity[1] = 0
        # Y Only?
        elif self.velocity[0] == 0 and self.velocity[1] != 0:
            if self.velocity[1] > 0:
                self.velocity[1] -= 1
            else:
                self.velocity[1] += 1
        # X Only?
        elif self.velocity[1] == 0 and self.velocity[0] != 0:
            if self.velocity[0] > 0:
                self.velocity[0] -= 1
            else:
                self.velocity[0] += 1

        self.x += self.velocity[0] * 0.1
        self.y -= self.velocity[1] * 0.1

    def boost(self, bx, by):
        self.velocity = [self.velocity[0] + bx, self.velocity[1] + by]

class Bullet():
    def __init__(self, x, y, angle = 0, velocity = [0, 0]):
        self.life = 300
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = angle

    def render(self):
        fill(255, 110)
        stroke(255)
        strokeWeight(3)
        ellipse(self.x, self.y, 5, 5)
        self.moveVelocity()

tick = 0
stars = []
asteroids = []
shoots = []
ship = []
cooldown = 0

controls = {
    "w": False,
    "a": False,
    "d": False,
    "m": False
}

def setup():
    global ship

    size(800, 800)
    shapeMode(CENTER)
    for i in range(100):
        stars.append(Star(random(800), random(800), random(50)))
    for i in range(1):
        asteroids.append(
            Asteroid(random(800), random(800), random(50, 100), [random(-2, 2), random(-2, 2)])
        )
    ship = Ship(400, 400)

def keyPressed():
    global controls, key
    key = key.lower()
    if key in controls:
        controls[key] = True

def keyReleased():
    global controls, key
    key = key.lower()
    if key in controls:
        controls[key] = False

def render():
    background(0)
    for star in stars:
        star.render()

    # Ship Render
    ship.render()

    for shot in shoots:
        shot.render()

    for asteroid in asteroids:
        asteroid.render()

    # Stat render
    fill(255)
    textSize(14)
    text("FPS: " + str(round(frameRate)), 10, 20)
    text("Angle: " + str(round(ship.angle)), 10, 40)

def calculateVectors(angle, constant):
    if angle <= 90:
        bx = sin(radians(angle)) * constant
        by = cos(radians(angle)) * constant
    elif angle > 90 and angle <= 180:
        bx = cos(radians(angle - 90)) * constant
        by = -1 * sin(radians(angle - 90)) * constant
    elif angle > 180 and angle <= 270:
        bx = -1 * sin(radians(angle - 180)) * constant
        by = -1 * cos(radians(angle - 180)) * constant
    else:
        bx = -1 * cos(radians(angle - 270)) * constant
        by = sin(radians(angle - 270)) * constant

    return (bx, by)

def boostForward():
    global ship
    vectors = calculateVectors(ship.angle, 3)
    ship.boost(vectors[0], vectors[1])

def controlManager():
    global controls

    if controls['m']:
        if cooldown < 0:
            cooldown = 50
            shoot()
    if controls['a']:
        if ship.angle - 5 < 0:
            ship.angle = 360 + (ship.angle )
        ship.angle -= 5
    if controls['d']:
        if ship.angle + 5 > 360:
            ship.angle = (ship.angle + 5 - 360)
        ship.angle += 5
    if controls['w']:
        ship.moving = True
        boostForward()
    else:
        ship.moving = False

def game():
    global cooldown

    cooldown -= 1

def draw():
    global tick

    tick += 1
    controlManager()
    game()
    render()

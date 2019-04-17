# Asteroids - An ICS4U Project
# Shoot asteroids and get the highest score!
# -----------------------------------------------

class Star():
    def __init__(self, x, y, state):
        """initialize a new star"""
        self.x = x
        self.y = y
        self.size = state
        self.increase = True # increase state

    def render(self):
        """render star component"""
        fill(255) # white
        strokeWeight(0) # no stroke
        ellipse(self.x, self.y, self.size * 0.12, self.size * 0.12) # quite small, size isn't actual size
        if tick % 2 == 0: # increase every other tick
            self.increaseState()

    def increaseState(self):
        """change the size of stars"""
        if self.increase: # growing
            if self.size >= 40: # max
                self.increase = False # swap
            else:
                self.size += 1 # just increase
        else: # shrinking
            if self.size <= 1: # min
                self.increase = True
                self.x = random(800) # change locations
                self.y = random(800)
            else:
                self.size -= 1 # just decrease

class Asteroid():
    def __init__(self, x, y, size, velocity = [0, 0], life = 3):
        """initialize a new asteroid"""
        self.x = x
        self.y = y
        self.size = size
        self.life = life
        self.velocity = velocity # dir?

    def render(self):
        """rendering of the asteroids"""
        fill(255, 110) # white, transparent-ish
        stroke(255)
        strokeWeight(3) # outline
        ellipse(self.x, self.y, self.size, self.size) # CIRCLE! (diameter)
        self.moveVelocity() # move in render, not a good idea.

    def moveVelocity(self):
        """update the location based on velocity"""
        # off screen movement
        if self.x + self.size > 950:
            self.x = -50
        elif self.x + self.size < -150:
            self.x = 850
        if self.y + self.size > 950:
            self.y = -50
        elif self.y + self.size < -150:
            self.y = 850
        
        # update coordinates
        self.x += self.velocity[0]
        self.y -= self.velocity[1]

class Ship():
    def __init__(self, x, y, velocity = [0, 0]):
        """initialize a new ship"""
        self.life = 5
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = 0
        self.moving = False
        self.score = 0
    
    def render(self):
        """render ship component"""
        fill(0, 110) # black ship, transparent
        strokeWeight(4)
        stroke(255) # harder on the outline
        pushMatrix()
        translate(ship.x, ship.y) # translate for rotation
        rotate(radians(ship.angle)) 
        triangle(-20, 10, 20, 10, 0, -30) # size
        if self.moving: # moving fire animation
            fill(255, 0, 0) # trail
            strokeWeight(0)
            triangle(-20, 20, 20, 20, 0, 40)
        popMatrix()
        self.moveVelocity()

    def moveVelocity(self):
        """update the coordinates of the ship"""
        if self.x + 20 > 850:
            self.x = -25
        elif self.x + 20 < -50:
            self.x = 825
        if self.y + 20 > 850:
            self.y = -25
        elif self.y + 20 < -50:
            self.y = 825
        
        # Friction
        if not 0 in self.velocity:
            angle = degrees(atan(abs(self.velocity[0]) / abs(self.velocity[1]))) # get the angle of the velocity
        else:
            angle = 0 # treat as 0
        friction = 1.2 # friction vector

        """ This is where it gets confusing"""
        # The code here checks for the current position of the angle.
        # There are different quadrants that are checked.
        # Finding this will allow the program to calculate the opposite angle.
        # Which is used to slow down the ship with friction.
        # It's just some basic math with trig.

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
        """boost the ship forward"""
        if sqrt((self.velocity[0] ** 2) + (self.velocity[1] ** 2)) < 75: # max speed
            self.velocity = [self.velocity[0] + bx, self.velocity[1] + by]

class Bullet():
    def __init__(self, x, y, angle = 0, velocity = [0, 0]):
        """initialize a new bullet"""
        self.life = 200 # only 200 tick life
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = angle

    def render(self):
        """render the bullet element"""
        fill(255, 110)
        stroke(255)
        strokeWeight(3)
        ellipse(self.x, self.y, 5, 5) # CIRCLE!
        self.moveVelocity()

    def moveVelocity(self):
        """update the bullet coordinates"""
        self.x += self.velocity[0]
        self.y -= self.velocity[1]
        self.life -= 1 # reduce life

# Initialized global components
tick = 0 # current tick
stars = []
asteroids = [] 
shoots = []
ship = [] # only one, will rewrite
cooldown = 0 # cooldown for shots
state = 0 # 0 menu, 1 game, 2 death

# control manager
controls = {
    "w": False,
    "a": False,
    "d": False,
    "m": False
}

def setup():
    """setup of program"""
    global ship

    size(800, 800) # window size
    shapeMode(CENTER) # base on the center
    for i in range(100): # 100 stars
        stars.append(Star(random(800), random(800), random(50)))
    ship = Ship(400, 400) # ship spawn
    for i in range(5): # starting asteroid spawns
        size = random(75, 100)
        safe = safeSpawn(size)
        asteroids.append(Asteroid(safe[0], safe[1], size, [random(-2, 2), random(-2, 2)]))
    
def keyPressed():
    """is a key pressed?"""
    global controls, key, state, asteroids
    if state == 0: # state update
        state = 1
    elif state == 2: # state update
        asteroids = []
        ship = Ship(400, 400) # ship spawn
        for i in range(5): # restart asteroid spawns
            size = random(75, 100)
            safe = safeSpawn(size)
            asteroids.append(Asteroid(safe[0], safe[1], size, [random(-2, 2), random(-2, 2)]))
        state = 0
    elif key in controls:
        controls[key] = True

def keyReleased():
    """is a key released?"""
    global controls, key
    if key in controls:
        controls[key] = False

def render():
    """render game elements on the screen"""
    background(0)
    for star in stars:
        star.render()

    for shot in shoots:
        shot.render()

    # Ship Render
    ship.render() # only one ship

    for asteroid in asteroids:
        asteroid.render()

    # Stat render
    fill(255)
    textSize(14)
    text("FPS: " + str(round(frameRate)), 10, 20)
    text("Angle: " + str(round(ship.angle)), 10, 40)
    text("Tick: " + str(round(tick)), 10, 60)
    text("Entities: " + str(len(asteroids) + len(shoots) + 1), 10, 80)

    # Score render
    textSize(24)
    text("Score: " + str(ship.score), width - textWidth("Score: " + str(ship.score)) - 20, 40)
    lives = ship.life * " A"
    print(ship.life)
    text("Lives:" + str(lives), width - textWidth("Lives:" + str(lives)) - 20, 80)

def calculateVectors(angle, constant):
    """used to calculate components of a vector"""
    # This is also pretty confusing, but it's just some trig.
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

    return (bx, by) # return finalized vectors in a tuple

def boostForward():
    """user boosted the ship forward"""
    global ship
    vectors = calculateVectors(ship.angle, 3) # check for vectors
    ship.boost(vectors[0], vectors[1]) # boost in that direction

def shoot():
    """user has shot"""
    global shoots
    vectors = calculateVectors(ship.angle, 10) # check for vectors, again
    shoots.append(Bullet(ship.x, ship.y, ship.angle, vectors)) # shoot in that direction

def safeSpawn(size):
    """used to spawn elements in safe positions"""
    rando = 0 # random location
    while 1: # do until death
        rando = (random(0, 800), random(0, 800))
        failed = False # failed to find?
        for asteroid in asteroids: # check all asteroids
            if dist(rando[0], rando[1], asteroid.x, asteroid.y) < size + (asteroid.size / 2): # outside of range?
                failed = True
        if dist(rando[0], rando[1], ship.x, ship.y) < size + 20: # distance of ship
            failed = True
        if not failed: # didn't fail?
            break
    return rando # return coordinates

def collisionCheck():
    """check for collisions of elements"""
    global shoots, asteroids
    remove_queue = [] # elements to remove
    asteroid_killed = None # anything killed the ship?
    for asteroid in range(len(asteroids)): # all asteroids
        if dist(ship.x, ship.y, asteroids[asteroid].x, asteroids[asteroid].y) < 20 + (asteroids[asteroid].size / 2): # kill the ship?
            shipKilled() # ship was killed!
            asteroid_killed = asteroid # which one did it?
            break # no more looping needed
        for shot in range(len(shoots)): # any shots hit an asteroid?
            if dist(shoots[shot].x, shoots[shot].y, asteroids[asteroid].x, asteroids[asteroid].y) < 5 + (asteroids[asteroid].size / 2):
                ship.score += 1 # yep, winner!
                if not (shot, asteroid) in remove_queue: # add to the queue if not already
                    remove_queue.append((shot, asteroid)) # added
                if asteroids[asteroid].life > 1: # is the asteroid dead?
                    for _ in range(2): # nope, add two more
                        asteroids.append(
                            Asteroid(
                                asteroids[asteroid].x,
                                asteroids[asteroid].y,
                                asteroids[asteroid].size / 1.2,
                                [random(-2, 2), random(-2, 2)],
                                asteroids[asteroid].life - 1
                            )
                        )
    if asteroid_killed != None: # was the ship killed?
        asteroids.pop(asteroid_killed) # remove it only
    else: # nope
        removal_index = 0
        for i in remove_queue: # remove all of them
            shoots.pop(i[0] - removal_index)
            asteroids.pop(i[1] - removal_index)
            removal_index += 1

def shipKilled():
    """ship has been DESTROYED"""
    global state
    ship.life -= 1
    if ship.life < 1:
        state = 2
    ship.x = 400 # middle of screen again
    ship.y = 400
    ship.velocity = [0, 0]

def controlManager():
    """control management"""
    global controls, cooldown

    if controls['m'] and cooldown < 0: # shooting (must pass the cooldown)
        cooldown = 10
        shoot() # shoot a BOMB
    if controls['a']: # left
        if ship.angle - 5 < 0:
            ship.angle = 360 + (ship.angle)
        ship.angle -= 5
    if controls['d']: # right
        if ship.angle + 5 > 360:
            ship.angle = (ship.angle + 5 - 360)
        ship.angle += 5
    if controls['w']: # boost
        ship.moving = True
        boostForward()
    else:
        ship.moving = False # ships not boosting

def game():
    """basic game management"""
    global cooldown
    collisionCheck() # check for collisions
    cooldown -= 1 # reduce cooldown
    if tick % 500 == 0: # add a new asteroid every 500 ticks
        size = random(75, 100)
        safe = safeSpawn(size)
        asteroids.append(Asteroid(safe[0], safe[1], size, [random(-2, 2), random(-2, 2)]))

    removed = 0 # anything removed?
    for shot in range(len(shoots)): # shots out of life
        shoots[shot - removed].life -= 1
        if shoots[shot - removed].life <= 0:
            shoots.pop(shot - removed) # remove shot
            removed += 1 # reduce lives

def renderTitle():
    """render the title screen"""
    background(0)

    # misc render
    for star in stars:
        star.render()

    for asteroid in asteroids:
        asteroid.render()

    textSize(80)
    color(255)
    fill(255, 255)
    text("Asteroids", width / 2 - (textWidth("Asteroids") / 2), 200)
    textSize(30)
    color(200)
    text("Press any key to start", width / 2 - (textWidth("Press any key to start") / 2), 700)

def renderDead():
    """render the death screen"""
    background(100, 0, 0)

    textSize(80)
    color(255)
    fill(255, 255)
    text("You've lost!", width / 2 - (textWidth("You've lost!") / 2), 200)
    textSize(30)
    color(200)
    text("Press any key to continue", width / 2 - (textWidth("Press any key to continue") / 2), 700)

def draw():
    """stuff here is just the global draw"""
    global tick

    tick += 1 # update the tick
    if state == 0: # start
        renderTitle()
    elif state == 1: # game
        controlManager()
        game()
        render()
    elif state == 2: # death
        renderDead()
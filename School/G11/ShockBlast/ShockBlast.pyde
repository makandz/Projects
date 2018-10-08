# Audio library
add_library('minim')
minim = 0

tick = 0 # Tick count
status = 0 # 0: Menu 1 Playing 2 Death 3 Help
effects = {} # Sounds
images = {} # Images
waves = [ # Waves
    [2, 1, 0.75], # Amount, Health, Speed
    [2, 2, 0.8],
    [5, 2, 0.9],
    [5, 3, 1],
    [8, 4, 1],
    [8, 5, 1.1],
    [10, 6, 1.1],
    [10, 7, 1.15],
    [50, 1, 1.3],
    [100, 2, 1.5],
    [200, 100, 2], # Last Round
]

# Objects of scenery objects, don't move.
class Scene:
    location = [0, 0] # Current location
    item = 0 # Type

    # Init
    def __init__(self, location, item):
        # Set attributes
        self.item = item
        self.location = location
        print("Scene has been placed with settings: [item:", str(item), ", location: ", str(location), "]") # Debug

    # Scene rendering based on offset.
    def Render(self, offset = [0, 0]):
        rnView = renderView(self.location, offset) # Get offset of player location

        # Ground
        if self.item == 0:
            fill(124, 252, 0)
            rect(rnView[0], rnView[1], border[0], border[1])
        
        # Tree
        elif self.item == 1:
            fill(0, 150, 0, 240)
            ellipse(rnView[0], rnView[1], 150, 150)
            fill(0, 125, 0, 240)
            ellipse(rnView[0], rnView[1], 100, 100)
            fill(0, 100, 0, 240)
            ellipse(rnView[0], rnView[1], 50, 50)

        # House
        elif self.item == 2:
            fill(130, 82, 1, 240)
            rect(rnView[0], rnView[1], 200, 200)
            fill(100, 60, 0, 240)
            rect(rnView[0], rnView[1], 100, 100)
            
        # Reset color
        fill(0)

# Objects that move.
class Dynamic:
    location = [0, 0] # Current location
    position = [0, 0] # Location rendered
    item = 0 # Type
    angle = 0 # Direction
    renders = {} # Extra renders
    health = [0, 0] # Now, Start
    speed = 0 # Speed multiplier
    
    # Init
    def __init__(self, location, item, health, speed = 0):
        # Set values passed
        self.item = item
        self.location = location
        self.position = PVector(location[0], location[1])
        self.health = [float(health), health]
        self.speed = speed
        # If it is a player, render weapons
        if not item:
            self.renders['weapon'] = 1
            self.renders['ammo'] = 100
            self.renders['reload'] = 0
            self.renders['selected'] = 0 # Rifle, Sniper, LMG
        # Debug
        print("Dynamic has been placed with settings: [item:", str(item), ", location: ", str(location), "]")

    # Object rendering based on offset.
    def Render(self, offset = [0, 0]):
        rnView = renderView(self.location, offset) # Render based on player offset

        # Player
        if self.item == 0:
            # Direction algorithm: https://forum.processing.org/one/topic/rotate-shape-towards-mouse-with-easing.html
            dir = (atan2(mouseY - height / 2, mouseX - width / 2) - self.angle) / TWO_PI
            dir = (dir - round(dir)) * TWO_PI
            self.angle += dir * 0.1
            # End of algorithm

            # Update position based on location
            pushMatrix()
            self.position.add(PVector(self.location[0], self.location[1]).sub(self.position).mult(0.2))
            translate(self.position.x - self.location[0] + (width / 2), self.position.y - self.location[1] + (height / 2))
            rotate(self.angle)
            fill(255, 173, 96)
            ellipse(0, 0, 50, 50)
            # Weapon renders
            Weapon().Render(self.renders['weapon'])
            # Reload timer
            if self.renders['reload'] > 0:
                self.renders['reload'] -= 1
                # Reload is complete, reload the ammo based on weapon
                if not self.renders['reload'] and not self.renders['selected']: # Rifle
                    self.renders['ammo'] = 30
                elif not self.renders['reload'] and self.renders['selected'] == 1: # Sniper
                    self.renders['ammo'] = 10
                elif not self.renders['reload'] and self.renders['selected'] == 2: # LMG
                    self.renders['ammo'] = 60
            popMatrix()

        # Zombie
        elif self.item == 1:
            global zombies
            
            # Is the player in the view distance?
            pushMatrix()
            move = True
            if dist(self.location[0], self.location[1], player.location[0], player.location[1]) > 1500:
                move = False

            # Move the zombie based on location of the player.
            if move:
                self.position.add(PVector(player.location[0], player.location[1]).sub(self.position).normalize() * 3 * self.speed)
                self.location = [self.position.x, self.position.y]

            # Zombie renders
            translate(rnView[0], rnView[1])
            rotate(PVector(player.location[0], player.location[1]).sub(self.position).heading())
            fill(255 * (1 - (self.health[0] / self.health[1])), 255 * (self.health[0] / self.health[1]), 50)
            ellipse(0, 0, 50, 50)
            Weapon().Render(0)
            popMatrix()
            fill(0)

# Weapons
class Weapon:
    # Render of weapons
    def Render(self, item):
        # Fists
        if item == 0:
            ellipse(20, 20, 15, 15)
            ellipse(20, -20, 15, 15)
        
        # Rifle
        elif item == 1:
            pushMatrix()
            rotate(-90 * (PI / 180))
            fill(0)
            rect(0, 45, 7, 40)
            popMatrix()
            fill(255, 173, 96)
            ellipse(25, 3, 15, 15)
            ellipse(47, 5, 15, 15)

# Bullets
class Bullet:
    position = [0, 0] # Current location
    life = 50 # Lifetime
    angle = 0 # Direction

    # Init
    def __init__(self, angle):
        # Preset values sent
        self.angle = angle
        self.position = PVector(player.location[0], player.location[1])

    # Tracking and rendering of bullets
    def Track(self, offset = [0, 0]):
        rnView = renderView([self.position.x, self.position.y], offset) # Offset location based on player

        # Render of bullet
        pushMatrix()
        self.position.add(PVector(cos(self.angle) * 20, sin(self.angle) * 20))
        translate(rnView[0], rnView[1])
        rotate(self.angle)
        fill(0)
        ellipse(0, 0, 5, 5)
        popMatrix()
        
        # Reduce the lifetime
        self.life -= 1

# Returns a render with the offset.
def renderView(location, offset):
    return [(width / 2) + location[0] - offset[0], (height / 2) + location[1] - offset[1]]

# Spawn zombies away from each other.
def safeSpawn(obj):
    for attempts in range(5): # Attempts 5 times
        location = [int(random(border[0] / 2.5 * -1, border[0] / 2.5)), int(random(border[0] / 2.5 * -1, border[0] / 2.5))]
        fail = False # Failure to spawn
        for gameObj in obj:
            if gameObj.location[0] in range(location[0] - 250, location[0] + 250) and gameObj.location[1] in range(location[1] - 250, location[1] + 250):
                fail = True # Failed to find a valid location.
                break
        if not fail:
            return location # Return the location safe
    if fail:
        return None # Failed to find a location
        
# Check for collisions between a parent and object.
def collisionCheck(parent, object):
    if int(parent[0]) in range(int(object[0] - 50), int(object[0] + 50)) and int(parent[1]) in range(int(object[1] - 50), int(object[1] + 50)):
        return True # Have collided
    return False # Not

# Render overlays on the screen
def renderOverlays(wave, weapon, ammo, reload, health, starting):
    # Status: (Starting Wave, In a Wave) 0 - 1
    textSize(17)

    # Reload text
    if int(reload):
        text("Reloading..", width / 2 - (textWidth("Reloading..") / 2), height / 2 + 100)

    # Wave start text
    if int(starting):
        textSize(18)
        text("Starting in " + starting + " seconds", width / 2 - (textWidth("Starting in " + starting + " seconds") / 2), 65)
    else:
        fill(255, 0, 0)
    
    textSize(30)
    text("Wave " + wave, width / 2 - (textWidth("Wave " + wave) / 2), 40) # Wave count
    fill(0)
    textSize(30)
    text(ammo, width - textWidth(ammo) - 10, height - 10) # Health
    text(health + "%", 10, height - 10) # Percentage of health
    textSize(20)
    text(weapon, width - textWidth(weapon) - 10, height - 40) # Current weapon
    text("Health", 10, height - 40) # Text
    textSize(12)

# Check wave status and update
def waveControl():
    global wave

    passed = [str(wave[1]), "Fists", "0", str(player.renders['reload']), str(player.health[0] / 50 * 100), str(int(wave[2]))] # Passed values
    
    # Warmup
    if not wave[0]:
        if wave[2] > 0: # Timer not ended yet
            # Reduce current timer
            wave[2] -= millis() / 1000 - wave[3]
            wave[3] = millis() / 1000
        else: # Wave started
            for a in range(waves[wave[1] - 1][0]): # Begin spawn of zombies
                location = safeSpawn(zombies) # Find a safe location
                if location != None: # Location found
                    zombies.append(Dynamic(location, 1, waves[wave[1] - 1][1], waves[wave[1] - 1][2])) # Spawn zombie
            wave[0] = 1
    # In wave
    else:
        if len(zombies) == 0: # No more zombies
            wave = [0, wave[1] + 1, 5, millis() / 1000] # Swap the wave

    # Selected weapon
    if player.renders['weapon'] == 1: # Rifle
        if not player.renders['selected']:
            passed[1] = "Rifle"
        elif player.renders['selected'] == 1: # Sniper
            passed[1] = "Sniper"
        elif player.renders['selected'] == 2: # LMG
            passed[1] = "LMG"
        passed[2] = str(player.renders['ammo']) # Ammo
    
    renderOverlays(passed[0], passed[1], passed[2], passed[3], passed[4], passed[5]) # Render overlays

# Menu screen
def menuScreen():
    image(images['menu'], 0, 0)
    fill(150)
    # Button highlight
    if mouseX in range(width / 2 - 50, width / 2 + 50) and mouseY in range(215, 265):
        fill(255)
    rect(width / 2, 240, 100, 50)
    fill(150)
    if mouseX in range(width / 2 - 110, width / 2 + 110) and mouseY in range(300, 350):
        fill(255)
    rect(width / 2, 325, 220, 50)
    fill(0)
    textSize(50)
    # Title
    text("ShockBlast!", width / 2 - (textWidth("Shockblast!") / 2), 150)
    textSize(35)
    # Button text
    text("Play", width / 2 - (textWidth("Play") / 2), 252)
    text("How to Play", width / 2 - (textWidth("How to Play") / 2), 336)
    fill(150)
    # Class select boxes
    if mouseX in range(width / 4 - 55, width / 4 + 55) and mouseY in range(545, 595):
        fill(255)
    elif not player.renders['selected']:
        fill(255, 0, 0)
    rect(width / 4, 570, 110, 50)
    fill(150)
    if mouseX in range(width / 4 * 2 - 55, width / 4 * 2 + 55) and mouseY in range(555, 595):
        fill(255)
    elif player.renders['selected'] == 1:
        fill(0, 255, 0)
    rect(width / 4 * 2, 570, 110, 50)
    fill(150)
    if mouseX in range(width / 4 * 3 - 55, width / 4 * 3 + 55) and mouseY in range(555, 595):
        fill(255)
    elif player.renders['selected'] == 2:
        fill(0, 0, 255)
    rect(width / 4 * 3, 570, 110, 50)
    textSize(30)
    fill(0)
    # Weapon class text render
    text("Weapon Class", width / 2 - (textWidth("Weapon Class") / 2), 500)
    text("Rifle", width / 4 - (textWidth("Rifle") / 2), 580)
    text("Sniper", width / 4 * 2 - (textWidth("Sniper") / 2), 580)
    text("LMG", width / 4 * 3 - (textWidth("LMG") / 2), 580)

# Death screen
def deathScreen():
    background(255, 0, 0)
    fill(150)
    # Button highlighting
    if mouseX in range(width / 2 - 100, width / 2 + 100) and mouseY in range(215, 265):
        fill(255)
    rect(width / 2, 240, 200, 50)
    fill(150)
    if mouseX in range(width / 2 - 150, width / 2 + 150) and mouseY in range(300, 350):
        fill(255)
    rect(width / 2, 325, 300, 50)
    fill(0)
    textSize(50)
    # Title of death
    text("Ouch!", width / 2 - (textWidth("Ouch!") / 2), 150)
    textSize(35)
    # Button text
    text("Try Again", width / 2 - (textWidth("Try Again") / 2), 252)
    text("Return To Menu", width / 2 - (textWidth("Return To Menu") / 2), 336)

# Help screen  
def helpScreen():
    image(images['menu'], 0, 0)
    textSize(40)
    # Help screen text
    text("Controls", 75, 100)
    textSize(30)
    text("[WASD] ~ Player Movement", 75, 150)
    text("[MOUSE] ~ Player Direction", 550, 150)
    text("[LEFT-CLICK] ~ Shoot", 75, 200)
    text("[R] ~ Reload", 550, 200)
    text("[1] ~ Switch to Fists", 75, 250)
    text("[2] ~ Switch to Weapon", 550, 250)
    textSize(40)
    text("Objective", 75, 350)
    textSize(30)
    text("Your objective is to protect yourself from the waves of", 75, 400)
    text("zombies. Shoot as many zombies as you can per round, but", 75, 450)
    text("make sure you do it efficiently since waves get harder!", 75, 500)
    fill(150)
    # Button highlight
    if mouseX in range(width / 2 - 150, width / 2 + 150) and mouseY in range(575, 625):
        fill(255)
    rect(width / 2, 600, 300, 50)
    fill(0)
    textSize(35)
    # Button text
    text("Return To Menu", width / 2 - (textWidth("Return To Menu") / 2), 613)

# Reset gane stats
def setupGame():
    global wave, status, zombies

    # Change values to defaults
    wave = [0, 1, 5, millis() / 1000]
    player.health[0] = player.health[1]
    status = 1
    # Ammo depends on gun selected
    if not player.renders['selected']: # Rifle
        player.renders['ammo'] = 30
    elif player.renders['selected'] == 1: # Sniper
        player.renders['ammo'] = 10
    elif player.renders['selected'] == 2: # LMG
        player.renders['ammo'] = 60
    player.renders['reload'] = 0
    zombies = []

border = [2000, 2000] # Border
ground = Scene([0, 0], 0) # Ground
player = Dynamic([0, 0], 0, 50) # Player
# Render objects
zombies = []
scenery = []
bullets = []
wave = [0, 1, 5, 0] # Status (0 warmup, 1 started), wave, left, millis

# Controls
controls = {
    'mouse': False,
    'w': False,
    'a': False,
    's': False,
    'd': False,
    'r': False,
    '1': False,
    '2': False
}

# First time launch
def setup():
    global effects, images

    # Add data
    minim = Minim(this)
    effects = {"shoot": minim.loadFile("data/shoot.mp3"), "reload": minim.loadFile("data/reload.mp3"), 'walk': minim.loadFile("data/walk.mp3")} # Load audio
    images = {"menu": loadImage("data/menu.png")} # Load images
    size(1000, 700) # Window size
    rectMode(CENTER) # All rects start from center
    strokeWeight(2)
    for i in range(int(border[0] / 50)): # Spawn scenery
        spawn = safeSpawn(scenery) # Safe spawn
        if spawn != None: # Found a spot
            scenery.append(Scene(spawn, round(random(1, 2))))

# Draw every tick
def draw():
    global tick, status
    tick += 1 # Tick increases

    clear() # Reset screen to re-render.

    if not status: # Menu
        menuScreen()
    elif status == 2: # Death
        deathScreen()
    elif status == 3: # Help
        helpScreen()
    elif status == 1: # Playing
        background(0, 119, 190)
        controlRun() # Check for controls

        ground.Render(player.location) # Render the ground
        
        r_count = 0 # Used if removed, count increases
        for i in range(len(bullets)): # Check each bullet
            bullets[i - r_count].Track(player.location)
            if not bullets[i - r_count].life: # Is the bullet end of life?
                bullets.pop(i - r_count) # Remove bullet
                r_count += 1
            else:
                for j in range(len(zombies)): # Check collisions with zonbies
                    if collisionCheck([bullets[i - r_count].position.x, bullets[i - r_count].position.y], zombies[j].location):
                        # Depending on bullets, different health removed
                        if not player.renders['selected']:
                            zombies[j].health[0] -= 2
                        elif player.renders['selected'] == 1:
                            zombies[j].health[0] -= 4
                        elif player.renders['selected'] == 2:
                            zombies[j].health[0] -= 1
                        if zombies[j].health[0] <= 0: # Does the zombie have any health?
                            zombies.pop(j)
                        bullets.pop(i - r_count) # Bullet removed when hit.
                        r_count += 1
                        break
            
        # Check collisions of zombies with player
        for zombie in zombies:
            if collisionCheck(player.location, zombie.location):
                player.health[0] -= 0.05 # Reduce health of player if close
                if player.health[0] <= 0:
                    status = 2
            zombie.Render(player.location) # Render the zombie
            zombie.move = True

        player.Render() # Render player

        # Render all scenery
        for scene in scenery:
            scene.Render(player.location)
            
        waveControl() # Control all waves

    fill(0)
    textSize(11)

    # Just some stats
    text("FPS: " + str(round(frameRate)), 10, 20)
    text("Location: " + str(round(player.location[0])) + ", " + str(round(player.location[1])), 10, 35)
    text("Tick: " + str(tick), 10, 50)
        
# Check for mouse pressed
def mousePressed():
    global status, wave

    if status == 0: # Check button presses on menu
        if mouseX in range(width / 2 - 50, width / 2 + 50) and mouseY in range(215, 265):
            setupGame()
        if mouseX in range(width / 2 - 110, width / 2 + 110) and mouseY in range(300, 350):
            status = 3
        if mouseX in range(width / 4 - 55, width / 4 + 55) and mouseY in range(545, 595):
            player.renders['selected'] = 0
        if mouseX in range(width / 4 * 2 - 55, width / 4 * 2 + 55) and mouseY in range(545, 595):
            player.renders['selected'] = 1
        if mouseX in range(width / 4 * 3 - 55, width / 4 * 3 + 55) and mouseY in range(545, 595):
            player.renders['selected'] = 2
    elif status == 2: # Button presses in ouch.
        if mouseX in range(width / 2 - 100, width / 2 + 100) and mouseY in range(215, 265):
            setupGame()
        elif mouseX in range(width / 2 - 150, width / 2 + 150) and mouseY in range(300, 350):
            setupGame()
            status = 0
    elif status == 3: # Button for help screen
        if mouseX in range(width / 2 - 150, width / 2 + 150) and mouseY in range(575, 625):
            status = 0
    else: # In game, released and clicked
        if player.renders['weapon']:
            controls['mouse'] = True
    
def mouseReleased():
    controls['mouse'] = False # Released the mouse

# Key pressed
def keyPressed():
    global controls, key
    if key in controls:
        controls[key] = True
    if not status and controls['w'] or controls['a'] or controls['s'] or controls['d']: # Is player walking?
        effects['walk'].loop() # Walking effect
    
# Key released
def keyReleased():
    global controls, key
    if key in controls:
        controls[key] = False
    if not controls['w'] and not controls['a'] and not controls['s'] and not controls['d']: # All keys stopped
        effects['walk'].rewind() # Start from beginning
        effects['walk'].pause() # Remove sound

# Run control based on current keys
def controlRun():
    inc = [0, 0] # Player movement
    
    if controls['w'] and not (player.location[1] < border[1] / 2.1 * -1): # Up
        inc[1] -= 3
    if controls['s'] and not (player.location[1] > border[1] / 2.1): # Down
        inc[1] += 3
    if controls['a'] and not (player.location[0] < border[0] / 2.1 * -1): # Left
        inc[0] -= 3
    if controls['d'] and not (player.location[0] > border[0] / 2.1): # Right
        inc[0] += 3
    if controls['mouse']: # Mouse pressed, shoot
        if player.renders['ammo'] > 0 and not player.renders['reload']: # Depending on ammo and no reload, shoot
            if not tick % 10 and not player.renders['selected'] or \
            not tick % 20 and player.renders['selected'] == 1 or \
            not tick % 5 and player.renders['selected'] == 2:
                # Can shoot, bullet is added
                player.renders['ammo'] -= 1
                bullets.append(Bullet(player.angle))
                # Sound effects
                effects['shoot'].play()
                effects['shoot'].rewind()
        elif not player.renders['ammo'] and player.renders['reload'] == 0: # Player ran out of ammo
            player.renders['reload'] = 100 # Reload
            effects['reload'].play() # Sound effect
    if controls['r'] and not player.renders['reload']: # Player hit reload key
        if player.renders['ammo'] != 30 and not player.renders['selected'] or \
        player.renders['ammo'] != 10 and player.renders['selected'] == 1 or \
        player.renders['ammo'] != 60 and player.renders['selected'] == 2: # Can they even reload?
            # Reload it
            player.renders['reload'] = 100
            # Sound effects
            effects['reload'].rewind()
            effects['reload'].play()
    if controls['1']: # Switch to fists
        player.renders['weapon'] = 0 
    elif controls['2']: # Switch to weapon
        player.renders['weapon'] = 1
        
    # Dual presses reduced
    if abs(inc[0]) == 3 and abs(inc[1]) == 3:
        inc = [inc[0] / 1.25, inc[1] / 1.25]

    # Update location of player.
    player.location = [player.location[0] + inc[0], player.location[1] + inc[1]]

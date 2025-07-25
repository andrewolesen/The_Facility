import pygame, sys
import pygame.locals as gameGlobals
pygame.init()

# Defining constant and useful variables
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
GREY = (169,169,169)
BLUE = (0,0,255)
DARKGREY = (40,40,40)
LIGHTGREY = (200,200,200)
LIGHTBLUE = (0,200,200)
ORANGE = (255,165,0)
TILE_SIZE = 30
SPAWN_SIZE = 60
PLAYER_SIZE = 30
PLAYER_SPEED = 5
PROJECTILE_SIZE = 15
PROJECTILE_SPEED = 4
PROJECTILE_OFFSET = 5
FPS = 60
TURRET_TIMER = 90
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

#Creates a display
displayWidth = 1290
displayHeight = 960
displaySurface = pygame.display.set_mode((displayWidth, displayHeight))
"""
Level symbols legend
=: None
#: Wall
S: Spawn
E: End
W: Spikes
U: Up Turret
D: Down Turret
L: Left Turret
R: Right Turret
"""

"""
Map Template
[
'###########################################',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'###########################################'
]
"""
# Maps of the levels, written in the form of lists
levelMap1 = [
'###########################################',
'##########=======###=======###=======###E=#',
'##########=======###=======###=======###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'#S==========###=======###=======###=======#',
'#===========###=======###=======###=======#',
'###########################################'
]

levelMap2 = [
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'#S=########################################',
'#==D#D#D#D#D#D#D#D#D#D#D#D#D#D#D#D#D#D#D###',
'#=========================================#',
'#=========================================#',
'#=========================================L',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================#',
'#=========================================L',
'#=========================================#',
'#=========================================#',
'###U#U#U#U#U#U#U#U#U#U#U#U#U#U#U#U#U#U#UE=#',
'########################################==#',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################',
'###########################################'
]

levelMap3 = [
'###########################################',
'##########=====WWW=====WWW#################',
'##########=====WWW=====WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'##########=WWW=WWW=WWW=WWW#################',
'#S=========WWW=====WWW====E=###############',
'#==========WWW=====WWW======###############',
'###########################################'
]

levelMap4 = [
'###########################################',
'#############E================#############',
'#############===========W=====#############',
'############R=================L############',
'#############========WW=======#############',
'############R=================L############',
'#############====W============#############',
'############R==========W======L############',
'#############=================#############',
'############R=================L############',
'#############=================#############',
'############R====W============L############',
'#############=================#############',
'############R=================L############',
'#############============W====#############',
'############R=================L############',
'#############======W==========#############',
'############R=================L############',
'#############===W=============#############',
'############R============W====L############',
'#############=================#############',
'############R======W==========L############',
'#############=================#############',
'############R=================L############',
'#############=================#############',
'############R=========W=======L############',
'#############=================#############',
'############R=====W===========L############',
'###############===============#############',
'#############S================#############',
'#############=================#############',
'###########################################'
]

levelMap5 = [
'###########################################',
'#########W=======WWW=======WWW=======WWWE=#',
'#########W=======WWW=======WWW=======WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==#',
'#########W==WWW==WWW==WWW==WWW==WWW==WWW==L',
'#S==========WWW=======WWW=======WWW=======#',
'#===========WWW=======WWW=======WWW=======#',
'###########################################'
]

levelMap6 = [
'#############D##D##D##D##D##D##############',
'#############E================#############',
'#############=================#############',
'#############=================#############',
'#############WWWWWWWWWWWWWWWW=#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'#############=WWWWWWWWWWWWWWWW#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'#############WWWWWWWWWWWWWWWW=#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'#############=WWWWWWWWWWWWWWWW#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'#############WWWWWWWWWWWWWWWW=#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'#############=WWWWWWWWWWWWWWWW#############',
'#############=================#############',
'#############=================#############',
'#############=================#############',
'###############WWWWWWWWWWWWWW=#############',
'#############S================#############',
'#############=================#############',
'###########################################'
]

levelMap7 = [
'##########D#########D#########D#########D##',
'##########=======###=======###=======###E=#',
'##########=======###=======###=======###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'##########==###==###==###==###==###==###==#',
'##########==###==###==###==###==###==###==#',
'##########=W###W=###=W###W=###=W###W=###=W#',
'#S==========###=======###=======###=======#',
'#===========###=======###=======###=======#',
'################U#########U#########U######'
]

levels = [levelMap1, levelMap2, levelMap3, levelMap4, levelMap5, levelMap6, levelMap7]

class player():
    def __init__(self, changeY = 0, changeX = 0, upKey = pygame.K_UP, downKey = pygame.K_DOWN, leftKey = pygame.K_LEFT, rightKey = pygame.K_RIGHT, shape = pygame.Rect(60, displayHeight - 60, PLAYER_SIZE, PLAYER_SIZE)):
        self.changeY = changeY
        self.changeX = changeX
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey
        self.shape = shape
    

    def move(self):
        # Changes direction based on key pushed
        if event.type == pygame.KEYDOWN:
            if event.key == self.downKey:
                self.changeY = PLAYER_SPEED
                self.changeX = 0
            if event.key == self.upKey:
                self.changeY = -PLAYER_SPEED
                self.changeX = 0
            if event.key == self.leftKey:
                self.changeX = -PLAYER_SPEED
                self.changeY = 0
            if event.key == self.rightKey:
                self.changeX = PLAYER_SPEED
                self.changeY = 0
        # Stops the player after key is released
        if event.type == pygame.KEYUP:
            if event.key == self.downKey and self.changeY == PLAYER_SPEED:
                self.changeY -= PLAYER_SPEED
            if event.key == self.upKey and self.changeY == -PLAYER_SPEED:
                self.changeY += PLAYER_SPEED
            if event.key == self.leftKey and self.changeX == -PLAYER_SPEED:
                self.changeX += PLAYER_SPEED
            if event.key == self.rightKey and self.changeX == PLAYER_SPEED:
                self.changeX -= PLAYER_SPEED
        

    def update(self, collideList, projectileList, spawnPoint):
        # Changes the players position based on X or Y speed
        self.shape.y += self.changeY
        self.shape.x += self.changeX

        # Stops the player from leaving the top or the bottom of the display
        if self.shape.top <= 0:
            self.shape.top = 0
        if self.shape.bottom >= displayHeight:
            self.shape.bottom = displayHeight
        if self.shape.left <= 0:
            self.shape.left = 0
        if self.shape.right >= displayWidth:
            self.shape.right = displayWidth

        #Stops the player if they collide with a wall or a turret
        for prop in range(len(collideList)):
            if isinstance(collideList[prop], collision):
                if self.shape.colliderect(collideList[prop].shape):

                    # Kills the player if they collide with a spike
                    if isinstance(collideList[prop], spike):
                        self.shape.x = spawnPoint.x
                        self.shape.y = spawnPoint.y
                        self.changeX = 0
                        self.changeY = 0
                    if isinstance(collideList[prop], end):
                        return True
                    if self.changeX < 0:
                        self.shape.left = collideList[prop].shape.right
                    elif self.changeX > 0:
                        self.shape.right = collideList[prop].shape.left
                    elif self.changeY < 0:
                        self.shape.top = collideList[prop].shape.bottom
                    elif self.changeY > 0:
                        self.shape.bottom = collideList[prop].shape.top
                    break
        
        # Kills the player if they're hit by a projectile
        for projectile in range(len(projectileList)):
            if self.shape.colliderect(projectileList[projectile].shape):
                self.shape.x = spawnPoint.x
                self.shape.y = spawnPoint.y
                self.changeX = 0
                self.changeY = 0


# Parent class of objects that the player can collide with
class collision():
    def __init__(self) -> None:
        pass

#Stores the information on the turrets to shoot projectiles
class turret(collision):
    def __init__(self, x, y, shape, direction, projectileList = [], timer = TURRET_TIMER):
        self.x = x 
        self.y = y
        self.shape = shape
        self.direction = direction
        self.projectileList = projectileList
        self.timer = timer
    
    # Spawns a new projectile every 1.5 seconds
    def update(self):
        # Timer decreases every tick
        self.timer -= 1
            
        # Spawns a new projectile and chooses projectile trajectory based on turret direction 
        if self.timer == 0:
            if self.direction == 'left':
                newProjectile = projectile(x = self.x, y = self.y, shape = pygame.Rect(self.x, self.y + PROJECTILE_OFFSET, PROJECTILE_SIZE, PROJECTILE_SIZE), changeX = -PROJECTILE_SPEED)
            elif self.direction == 'right':
                newProjectile = projectile(x = self.x, y = self.y, shape = pygame.Rect(self.x, self.y + PROJECTILE_OFFSET, PROJECTILE_SIZE, PROJECTILE_SIZE), changeX = PROJECTILE_SPEED)
            elif self.direction == 'up':
                newProjectile = projectile(x = self.x, y = self.y, shape = pygame.Rect(self.x + PROJECTILE_OFFSET, self.y, PROJECTILE_SIZE, PROJECTILE_SIZE), changeY = -PROJECTILE_SPEED)
            elif self.direction == 'down':
                newProjectile = projectile(x = self.x, y = self.y, shape = pygame.Rect(self.x + PROJECTILE_OFFSET, self.y, PROJECTILE_SIZE, PROJECTILE_SIZE), changeY = PROJECTILE_SPEED)
            self.timer = TURRET_TIMER
            return newProjectile



# Stores the information on the projectiles
class projectile(collision):
    def __init__(self, x, y, shape, changeY = 0, changeX = 0, collide = False):
        self.changeY = changeY
        self.changeX = changeX
        self.x = x
        self.y = y
        self.shape = shape
        self.collide = collide
    
    # Moves projectile every tick
    def update(self):
        self.shape.x += self.changeX
        self.shape.y += self.changeY

# Stores the location of the player spawn
class spawn():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Stores the location of the end of the level
class end(collision):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

# Stores the shape of the wall
class wall(collision):
    def __init__(self, shape):
        self.shape = shape

# Stores the position of the spike and the hitbox
class spike(collision):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

"""
Generates a level that converts a list of strings into a list of objects
Input: List
Output: List
"""
def levelGenerator(level):
    # Stores the list of objects
    objectList = []
    for i in range(len(level)):
        for j, levelProp in enumerate(level[i]):
            # Stores the position of the object based off the position of the string in the list
            length = j * TILE_SIZE
            width = i * TILE_SIZE

            # Creates an object based on the string
            if levelProp == '#':
                prop = wall(shape = pygame.Rect(length, width, TILE_SIZE, TILE_SIZE))
                objectList.append(prop)
            elif levelProp == 'S':
                newSpawn = spawn(x = length, y = width)
                objectList.append(newSpawn)
            elif levelProp == 'E':
                endOfLevel = end(x = length, y = width, shape = pygame.Rect(length, width, SPAWN_SIZE, SPAWN_SIZE))
                objectList.append(endOfLevel)
            elif levelProp == 'W':
                prop = spike(x = length, y = width, shape = pygame.Rect(length + 10, width + 15, 10, 10))
                objectList.append(prop)
            elif levelProp == 'U':
                prop = turret(x = length, y = width, shape = pygame.Rect(length, width, TILE_SIZE, TILE_SIZE), direction = 'up')
                objectList.append(prop)
            elif levelProp == 'D':
                prop = turret(x = length, y = width, shape = pygame.Rect(length, width, TILE_SIZE, TILE_SIZE), direction = 'down')
                objectList.append(prop)
            elif levelProp == 'L':
                prop = turret(x = length, y = width, shape = pygame.Rect(length, width, TILE_SIZE, TILE_SIZE), direction = 'left')
                objectList.append(prop)
            elif levelProp == 'R':
                prop = turret(x = length, y = width, shape = pygame.Rect(length, width, TILE_SIZE, TILE_SIZE), direction = 'right')
                objectList.append(prop)
    
    # Returns list of objects
    return objectList
"""
Swaps which level the player is on 
input: List
output List, Object
"""
def levelSwapper(levelMap):
    # Generates the objects within the level
    objects = levelGenerator(levelMap)
    # Finds the spawn object in the list of objects and changes the players spawn
    for i in range(len(objects)):
        if isinstance(objects[i], spawn):
            spawnPoint = objects[i]
            break
    # Respawns the player and stops the player from moving
    player.shape.x = spawnPoint.x
    player.shape.y = spawnPoint.y  
    player.changeX =  0
    player.changeY = 0
    return objects, spawnPoint

player = player()
objects, spawnPoint = levelSwapper(levelMap1)
projectileList = []

# Stores which level the player is on
whichLevel = 0
text = 'Congratulations! You Win'


while True:
    clock.tick(FPS)
    displaySurface.fill(DARKGREY)

    # True if the player has completed the game
    if whichLevel == 8:
        # Renders text to inform the player that the game is completed
        largeText = font.render(text, True, WHITE)
        displaySurface.blit(largeText, (displayWidth/2 - 200, displayHeight/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == gameGlobals.QUIT:
                pygame.quit()
                sys.exit()
    
    else:
        # Iterates through the list of objects and draws and updates them.
        for i in range(len(objects)):
            if isinstance(objects[i], wall):
                pygame.draw.rect(displaySurface, LIGHTGREY, objects[i].shape)
            elif isinstance(objects[i], spawn):
                pygame.draw.rect(displaySurface, GREEN, pygame.Rect(objects[i].x, objects[i].y, SPAWN_SIZE, SPAWN_SIZE))
            elif isinstance(objects[i], end):
                pygame.draw.rect(displaySurface, LIGHTBLUE, objects[i].shape)
            elif isinstance(objects[i], spike):
                pygame.draw.polygon(displaySurface, RED, [[objects[i].x, objects[i].y + 30], [objects[i].x + 15, objects[i].y], [objects[i].x + 30, objects[i].y + 30]])
            elif isinstance(objects[i], turret):
                pygame.draw.rect(displaySurface, ORANGE, objects[i].shape)
                newProjectile = objects[i].update()
                if newProjectile != None:
                    projectileList.append(newProjectile)
        
        # Iterates through the list of projectiles and draws them
        for i in range(len(projectileList)):
            pygame.draw.ellipse(displaySurface, ORANGE, projectileList[i].shape)

        # Draws the player
        pygame.draw.rect(displaySurface, BLUE, player.shape)
        pygame.display.update()

    
        for event in pygame.event.get():
            if event.type == gameGlobals.QUIT:
                pygame.quit()
                sys.exit()
            player.move()
        
        # Updates player and determines whether the level is completed
        changeLevel = player.update(objects, projectileList, spawnPoint)

        # Updates every projectile on screen
        for i in range(len(projectileList)):
            projectileList[i].update()

        # Checks if a projectile has collided with a wall and deletes it if it has
        for prop in range(len(objects)):
            for i in range(len(projectileList)):
                if isinstance(objects[prop], wall) and projectileList[i].shape.colliderect(objects[prop].shape):
                    projectileList.pop(i)
                    break
        
        # Swaps the level if it has been completed
        if changeLevel:
            # Switches and resets the level
            whichLevel += 1
            projectileList = []
            objects, spawnPoint = levelSwapper(levels[whichLevel])
            changeLevel = False
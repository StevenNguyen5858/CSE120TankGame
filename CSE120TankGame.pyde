# Setup Variables
scale_ = .8
sW = 0
sH = 0
s = 0

# Saved colors
grey0 = 180
grey1 = 150
grey2 = 130
grey3 = 120

# Saved fonts
font1 = None

# Custom shapes
rhombusBig = None
rhombusSmall = None

# Global PGraphics
main = None
backDrop = None
boxGrid = None

# Global tanks
left = "left"
right = "right"
tank1 = None
tank2 = None
tank3 = None
tank4 = None
player1Tanks = None
player2Tanks = None

# Players
player1 = None
player2 = None
players = None

# Global buttons
fireB = None
playScreenButtons = None
playB = None
mainScreenButtons = None

# Global pages
mainP = None
playP = None
pages = None

# Misc
playerTurnIndex = 0
def settings():
    global sW
    global sH
    global s
    # sW = int((displayHeight*scale_)/32*0.7)*32
    # sH = int((displayHeight*scale_)/32)*32  
    sW = int((2160*scale_)/32*0.7)*32
    sH = int((2160*scale_)/32)*32
    size(sW, sH)
    s = int(sH/32)

    
def setup():
    global font1
    font1 = createFont("Font1.otf", 100)
    
    frameRate(60)
    stroke(255)
    textFont(font1)
    background(192, 64, 0)
    
    global boxGrid
    boxGrid = createGraphics(sW,sH)
    boxGrid.beginDraw()
    for x in range(32):
        for y in range(32):
            boxGrid.noFill();
            boxGrid.stroke(0);
            boxGrid.strokeWeight(1);
            boxGrid.rect(x*s,y*s,s,s);
    boxGrid.endDraw();
    
    global main
    main = createGraphics(sW,sH)
    main.beginDraw()
    main.background(192, 64, 0)
    main.image(boxGrid, 0, 0)
    main.fill(0)
    main.stroke(0)
    main.rect(0,int(sH*.75),sW,sH)
    main.stroke(255)
    main.line(0,int(sH*.75),sW,int(sH*.75))
    main.endDraw()
    
    global backDrop
    backDrop = createGraphics(sW,sH)
    backDrop.beginDraw()
    backDrop.background(192, 64, 0)
    backDrop.image(boxGrid, 0, 0)
    backDrop.fill(0)
    backDrop.stroke(0)
    backDrop.rect(0,int(sH*.75),sW,sH)
    backDrop.stroke(255)
    backDrop.line(0,int(sH*.75),sW,int(sH*.75))
    backDrop.endDraw()
    
    setupVariables()
       

def setupVariables():
    # Tanks
    global tank1
    global tank2
    global player1Tanks
    tank1 = tank(s, 23*s+.46*s, s, .54*s, True, False, 0, left, "T1", 101, 102)
    tank2 = tank(3*s, 23*s+.46*s, s, .54*s, True, False, 0, left, "T2", 101, 102)
    tank1.isTurn = True
    player1Tanks = [tank1, tank2]
    
    global tank3
    global tank4
    global player2Tanks
    tank3 = tank(s*20, 23*s+.46*s, s, .54*s, True, False, 0, left, "T3", 101, 102)
    tank4 = tank(s*18, 23*s+.46*s, s, .54*s, True, False, 0, left, "T3", 101, 102)
    tank3.isTurn = True
    player2Tanks = [tank3, tank4]
    
    # Players
    global player1
    global player2
    global players
    player1 = player("Player1", player1Tanks, True, left)
    player2 = player("Player2", player2Tanks, False, right)
    players = [player1,player2]
    
    # Buttons
    global fireB
    global playScreenButtons
    fireB = button(192,255, "fire.b", s, 29*s, 5*s, 2*s, functionFire, "Fire!!")
    playScreenButtons = [fireB]
    global playB
    global mainScreenButtons
    playB = button(0, 255, "play.b", 7*s, 14*s, 8*s, 2.5*s, functionPlay, "Begin")
    mainScreenButtons = [playB]
    
    # Pages
    global playP
    global mainP
    playP = page(playScreenButtons, "playScreen", backDrop)
    mainP = page(mainScreenButtons, "mainScreen", main)
    mainP.drawOnce = True
    global pages
    pages = [mainP, playP]
    
    
# Button functions to be passed as button arguments/members
def functionPlay():
    activatePage(playP)
    print("Activiating play page")
    
def functionFire():
    textSize(100)
    player1.tankHit(1)
    swapTurns()
    print("Firing projectile") 

# Misc Functions
def swapTurns():
    global playerTurnIndex
    p= players[playerTurnIndex]
    if p.tankTurnIndex<len(p.tanks)-1:
        p.tankTurnIndex = p.tankTurnIndex + 1
    else:
        p.tankTurnIndex = 0
        if playerTurnIndex<len(players)-1:
            playerTurnIndex = playerTurnIndex + 1
        else:
            playerTurnIndex = 0
            
    
    
# Shapes functions:
def playerBar(side):
    strokeWeight(1)
    fill(0,180)
    if side == "left":
        quad(.5*s, 2.5*s, .5*s, .5*s, 9*s, .5*s, 7*s, 2.5*s)
        noFill()
        line(6*s,.5*s,6*s,2.5*s)
        line(6.5*s,2.5*s,8.5*s,.5*s)
    else:
        quad(21.5*s, 2.5*s, 21.5*s, .5*s, 15*s, .5*s, 13*s, 2.5*s)
        noFill()
        line(15.5*s, .5*s, 13.5*s, 2.5*s)
        line(16*s, .5*s, 16*s, 2.5*s)
    
# Classes... All of them:
class entity(object):
    vx = 0 
    vy = 0
    def __init__(self, x, y, w, h, isTank, isProjectile, vox, voy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isTank = isTank
        self.isProjectile = isProjectile
        self.vox = vox
        self.voy = voy
        self.vx = vox
        self.vy = voy
    
    def updatePos(self):
        pass
    
    def drawEntity(self):
        fill(0)
        rect(self.x, self.y, self.w, self.h)
            
class tank(entity):
    def __init__(self, x, y, w, h, isTank, isProjectile, playerNum, side, tankName, vox, voy):
        entity.__init__(self, x, y, w, h, isTank, isProjectile, vox, voy)
        self.playerNum = playerNum
        self.side = side
        self.tankName = tankName
        self.health = 2
        self.isTurn = False
        self.fireAngle = 1.57
        self.power = 7 
        self.doDrawLine = False
        
    def drawEntity(self):
        stroke(255)
        strokeWeight(1)
        fill(0)
        rect(self.x, self.y, self.w, self.h)
        
    
class player(object):
    aimX = 0
    aimY = 0
    isTurn = False
    def __init__(self, playerName, tanks, isTurn, side):
        self.playerName = playerName
        self.tanks = tanks
        self.side = side
        self.totalHealth = 0
        for t in self.tanks:
            self.totalHealth = self.totalHealth + t.health
        self.isTurn = isTurn
        self.activeTank = tanks[0].tankName
        self.tankTurnIndex = 0;
    
    def drawFiringLine(self):
        strokeWeight(3)
        t = self.tanks[self.tankTurnIndex]
        x1 = t.x+t.w/2
        y1 = t.y - s*.5
        x2 = (t.power*s)*cos(t.fireAngle)
        y2 = (t.power*s)*sin(t.fireAngle)
        fill(255)
        line(x1,y1,x1+x2,y1-y2)
        strokeWeight(1)
                
    def tankHit(self,tankNum):
        self.tanks[tankNum-1].health = self.tanks[tankNum-1].health - 1
        self.totalHealth = 0
        for t in self.tanks:
            self.totalHealth = self.totalHealth + t.health
            
    def displayPlayerData(self):
        playerBar(self.side)
        textSize(1.5*s*.740)
        str = self.playerName
        fill(255)
        qs = .25*s
        if self.side == left:
            text(str, 1.*s, 1.65*s)
            text(self.activeTank, 6.25*s, 1.65*s)
            indexH = s
            strokeWeight(10)
            for h in range(self.totalHealth):
                line(indexH, 2*s, indexH+.5*s, 2*s)
                indexH = indexH + s
        else:
            text(str, 22*s-textWidth(str)-s, 2.2*s)
            text(self.activeTank, 14.75*s, 2.2*s)
            indexH = 21*s
            strokeWeight(10)
            for h in range(self.totalHealth):
                line(indexH, s, indexH-.5*s, s)
                indexH = indexH - s
        
    
    
    
class button(object):
    isSelected = False
    def __init__(self, co1or, strok3, name, x, y, w, h, buttonF, buttonDetail):
        self.co1or = co1or
        self.strok3 = strok3
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.buttonF = buttonF
        self.buttonDetail = buttonDetail
        if type(buttonDetail) == str:
            self.tSize = self.h*.740
            textSize(self.tSize)
            self.textX = (self.w-textWidth(buttonDetail))/2+self.x
            self.textY = self.y+self.h-((self.h-textAscent())/2)-s*.1
        if self.h <= 2*s:
            # detailThickness is extra 
            self.dT = s*.25
        else:
            self.dT = s*.5
    
    def drawButton(self):
        if self.co1or == 0:
            fill(self.co1or,100)
        else:
            # detail red
            fill(192,64,0, 100)
        stroke(self.strok3)
        rect(self.x-self.dT,self.y-self.dT,self.w+self.dT*2,self.h+self.dT*2)
        if self.co1or == 0:
            fill(self.co1or)
        else:
            # detail red
            fill(192,64,0)
        rect(self.x, self.y, self.w, self.h)
        if type(self.buttonDetail) == str:
            if self.co1or == 0:
                fill(255)
            else:
                fill(0)
            textSize(self.tSize)
            text(self.buttonDetail, self.textX, self.textY)     

       
    
    def buttonFunction(self): 
        self.buttonF()
        
    def hitCheck(self):
        if (self.x < mouseX < self.x+self.w) and (self.y < mouseY < self.y+self.h):
            self.buttonFunction()
            return True
        else:
            return False
            

class page(object):
    isActive = False
    drawOnce = False
    def __init__(self, pageButtons, pageTag, pageGraphics):
        self.pageButtons = pageButtons
        self.pageTag = pageTag
        self.pageGraphics  = pageGraphics
    
    def drawPage(self):
        if self.pageGraphics != "temp":
             image(self.pageGraphics, 0, 0)
        for b in self.pageButtons: b.drawButton()
    

# Misc functions
def activatePage(p1):
    for p in pages:
        if p1.pageTag != p.pageTag:
            p.isActive = False
    p1.drawOnce = True
    
    
    
    
    
# Globals:

def draw():
    for p in pages: 
        if p.drawOnce:
            image(boxGrid, 0, 0)
            p.drawPage()
            p.isActive = True
            p.drawOnce = False
    if playP.isActive:
        playP.drawPage()
        for p in players:
            p.displayPlayerData()
            for t in p.tanks:
                t.drawEntity()
            players[playerTurnIndex].drawFiringLine()
                
    
     
def mousePressed():
    for p in pages:
        if p.isActive:
            for b in p.pageButtons:
                b.hitCheck()

def mouseDragged():
    pass
    

# Functions... All of them:

    

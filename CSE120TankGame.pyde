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

# Global PGraphics
main = None
backDrop = None
boxGrid = None

# Global tanks
tank1 = None
tank2 = None
tanks = None

# Global buttons
fireB = None
playScreenButtons = None
playB = None
mainScreenButtons = None

# Global pages
mainP = None
playP = None
pages = None

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
    
# Button functions to be passed as button arguments/members
def detailRed(b):
    fill(192,64,0, 100)
    stroke(255)
    rect(b.x-s*.25, b.y-s*.25, b.w+s*.5, b.h+s*.5)
    fill(192,64,0)
    rect(b.x,b.y,b.w,b.h)
    fill(0)

def detailBlack(b):
    fill(0, 100)
    stroke(255)
    rect(6.5*s,13.5*s,9*s,3.5*s)
    fill(255)
    
def functionPlay():
    activatePage(playP)
    print("Activiating play page")
    
def detailPlay(b):
    detailBlack(b)
    textSize(100)
    text("Begin", 8.75*s, 15.9*s)
    list()
    
def functionFire():
    textSize(100)
    print("Firing projectile")    
    
def detailFire(b):
    detailRed(b)
    text("Fire!!", b.x+s*.4, b.y+s*1.7)

    
def setupVariables():
    # Tanks
    global tank1
    global tank2
    global tanks
    tank1 = tank(s, 23*s+.46*s, s, .54*s, True, False, "Player1", 10, 101, 102)
    tank2 = tank(s*20, 23*s+.46*s, s, .54*s, True, False, "Player2", 10, 101, 102)
    tanks = [tank1,tank2]
    
    # Buttons
    global fireB
    global playScreenButtons
    fireB = button(192,255, "fire.b", s, 29*s, 5*s, 2*s, functionFire, detailFire)
    playScreenButtons = [fireB]
    
    global playB
    global mainScreenButtons
    playB = button(0, 255, "play.b", 7*s, 14*s, 8*s, 2.5*s, functionPlay, detailPlay)
    mainScreenButtons = [playB]
    
    
    # Pages
    global playP
    global mainP
    playP = page(playScreenButtons, "playScreen", backDrop)

    mainP = page(mainScreenButtons, "mainScreen", main)
    mainP.drawOnce = True
    
    global pages
    pages = [mainP, playP]
    
    
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
    def __init__(self, x, y, w, h, isTank, isProjectile, playerName, health, vox, voy):
        entity.__init__(self, x, y, w, h, isTank, isProjectile, vox, voy)
        self.playerName = playerName
        self.health = health   
    

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
    
    def drawButton(self):
        if self.isSelected:
            stroke(255)
        else:
            fill(self.co1or)
            stroke(self.strok3)
            rect(self.x, self.y, self.w, self.h)
            if self.buttonDetail != "temp":
                self.buttonDetail(self)
    
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
            
            if playP.drawOnce:
                for t in tanks: t.drawEntity()
            p.isActive = True
            p.drawOnce = False
            print("Test")
    
     
def mousePressed():
    for p in pages:
        if p.isActive:
            for b in p.pageButtons:
                b.hitCheck()
    

# Functions... All of them:

    

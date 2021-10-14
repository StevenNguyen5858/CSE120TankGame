# Group_1------------------------------------------------------------------
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
font1Bold = None
chatText = None

# Custom shapes
rhombusBig = None
rhombusSmall = None

# Global PGraphics
main = None
playG = None
optionsG = None
boxGrid = None

# ChatBoxes
playerQueue = None

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
optionsB = None
exitB = None
mainScreenButtons = None
returnB = None
optionScreenButtons = None

# Global pages
mainP = None
playP = None
optionsP = None
pages = None


# Misc
playerTurnIndex = 0

# Group_2------------------------------------------------------------------
def settings():
    global sW
    global sH
    global s
    # sW = int((displayHeight*scale_)/32*0.7)*32
    # sH = int((displayHeight*scale_)/32)*32  
    sW = int((3840*scale_)/32)*32
    sH = int((3840*scale_)/32*.5625)*32
    size(sW, sH)
    s = int(sH/32)
    

def setup():
    global font1
    global font1Bold
    global chatText
    font1 = createFont("Font1.otf", 100)
    font1Bold = createFont("Font1Bold.otf", 100)
    chatText = createFont("ChatText.otf", 100)
    
    frameRate(60)
    stroke(255)
    textFont(font1)
    background(192, 64, 0)
    
    global boxGrid
    boxGrid = createGraphics(sW,sH)
    boxGrid.beginDraw()
    for x in range(57):
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
    main.textFont(font1Bold)
    main.textSize(3*s*.740)
    main.text("The Tank Game", 4*s, 6.8*s)
    
    main.stroke(255)
    main.noFill()
    main.rect(39*s,3*s,18*s,17*s)
    main.fill(0,120)
    main.rect(39*s,3*s,18*s,2*s)
    main.rect(39*s,19*s,18*s,1*s)
    
    main.fill(255)
    main.textFont(font1)
    main.textSize(2*s*.740)
    main.text("Player queue", 39.5*s, 4.5*s)
    main.textFont(chatText)
    main.textSize(1.3*s*.740)
    main.text("Type here :   ",39.5*s,(20*s)-((s-textAscent())/2)-s*.4)
    # Draw left player bar
    #main.stroke(255)
    #main.fill(0,180)
    #main.quad(.5*s, 2.5*s, .5*s, .5*s, 9*s, .5*s, 7*s, 2.5*s)
    #main.noFill()
    #main.line(6*s,.5*s,6*s,2.5*s)
    #main.line(6.5*s,2.5*s,8.5*s,.5*s)
    # Bottum black
    main.noStroke()
    main.fill(180,100)
    main.rect(0,int(sH*.75),sW,sH)
    main.stroke(255)
    main.fill(0)
    main.quad(0,sH*.75,34*s,sH*.75,30*s,sH,0,sH)
    main.quad(57*s,sH*.75,35*s,sH*.75,31*s,sH,sW,sH)
    #
    main.endDraw()
    
    global playG
    playG = createGraphics(sW,sH)
    playG.beginDraw()
    playG.background(192, 64, 0)
    playG.image(boxGrid, 0, 0)
    playG.fill(0)
    playG.stroke(0)
    playG.rect(0,int(sH*.75),sW,sH)
    playG.stroke(255)
    playG.line(0,int(sH*.75),sW,int(sH*.75))
    
    # Draw right player bar
    playG.fill(0,180)
    playG.quad(21.5*s, 2.5*s, 21.5*s, .5*s, 15*s, .5*s, 13*s, 2.5*s)
    playG.noFill()
    playG.line(15.5*s, .5*s, 13.5*s, 2.5*s)
    playG.line(16*s, .5*s, 16*s, 2.5*s)
    playG.endDraw()
    
    
    global optionsG
    optionsG = createGraphics(sW,sH)
    optionsG.beginDraw()
    optionsG.background(192, 64, 0)
    optionsG.image(boxGrid, 0, 0)
    optionsG.fill(0,100)
    optionsG.rect(0,0,sW,sH)
    optionsG.endDraw()

    setupVariables()
       

def setupVariables():
    testChat = ["[Game] Hello Player1!", "[Game] Use the text box below to enter messages."]
    # Chat boxes
    global playerQueue
    playerQueue = chatBox(39*s, 5*s, 18*s, 14, True, testChat, 0)
    
    # Tanks
    global tank1
    global tank2
    global player1Tanks
    tank1 = tank(1.5*s, 23*s+.73*s, .5*s, .27*s, True, False, 0, left, "T1", 101, 102)
    tank2 = tank(3.5*s, 23*s+.73*s, .5*s, .27*s, True, False, 0, left, "T2", 101, 102)
    tank1.isTurn = True
    player1Tanks = [tank1, tank2]
    
    global tank3
    global tank4
    global player2Tanks
    tank3 = tank(s*20.5, 23*s+.73*s, .5*s, .27*s, True, False, 0, left, "T3", 101, 102)
    tank4 = tank(s*18.5, 23*s+.73*s, .5*s, .27*s, True, False, 0, left, "T4", 101, 102)
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
    global optionsB
    global exitB
    global mainScreenButtons
    playB = button(0, 255, "play.b", 5*s, 10*s, 6*s, 2*s, functionPlay, "Begin")
    optionsB = button(0, 255, "options.b", 5*s, 13*s, 8*s, 2*s, functionOptions, "Options")
    exitB = button(0, 255, "exit.b", 5*s, 16*s, 5*s, 2*s, functionExit, "Exit")
    mainScreenButtons = [playB, optionsB, exitB]
    global optionScreenButtons
    returnB = button(0, 255, "return.b", 2*s, 25*s, 5*s, 2*s, functionReturn, "Back")
    exitB = button(0, 255, "exit.b", 2*s, 25*s, 5*s, 2*s, functionExit, "Exit")
    optionScreenButtons = [returnB]

    
    # Pages
    global playP
    global mainP
    global optionsP
    playP = page(playScreenButtons, "playScreen", playG, "temp")
    mainP = page(mainScreenButtons, "mainScreen", main, playerQueue.drawChatBox)
    optionsP = page(optionScreenButtons, "optionScreen", optionsG, "temp")
    mainP.drawOnce = True
    global pages
    pages = [mainP, playP, optionsP]
    
# Group_3------------------------------------------------------------------
# Button functions to be passed as button arguments/members
def functionPlay():
    activatePage(playP)
    print("Activiating play page")
    
def functionOptions():
    activatePage(optionsP)
    print("Activating options page")
    
def functionExit():
    exit()
    print("Exit program executed")
    
def functionFire():
    textSize(100)
    player1.tankHit(1)
    handleTurns()
    print("Firing projectile") 
    
def functionReturn():
    activatePage(mainP)
    print("Returning to main")

# Group_3.1-----------------------------------------------------------------
# Misc Functions
def handleTurns():
    global playerTurnIndex
    p = players[playerTurnIndex]
    if p.tankTurnIndex<len(p.tanks)-1:
        p.tankTurnIndex = p.tankTurnIndex + 1
        p.activeTank = p.tanks[p.tankTurnIndex].tankName
    else:
        p.tankTurnIndex = 0
        p.activeTank = p.tanks[p.tankTurnIndex].tankName
        if playerTurnIndex<len(players)-1:
            playerTurnIndex = playerTurnIndex + 1
        else:
            playerTurnIndex = 0
       
# ------------------------------------------------------------------Group_3.2
# Detail Functions:
def leftBarDetail():
    pushMatrix()
    # Draw left player bar
    fill(0,180)
    quad(.5*s, 2.5*s, .5*s, .5*s, 9*s, .5*s, 7*s, 2.5*s)
    noFill()
    line(6*s,.5*s,6*s,2.5*s)
    line(6.5*s,2.5*s,8.5*s,.5*s)
    popMatrix()
    
    
def rightBarDetail():
    pass
    
# ------------------------------------------------------------------Group_4
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
        
    def hasCollided(self, entity2):
        # Collision X
        if abs(self.x-entity2.x) <= (self.w+entity2.w):
            return True
        # Collision Y
        if abs(self.y-entity2.y) <= (self.h+entity2.h):
            return True
        return False
        

class box_(entity):
    def __init__(self, x, y, w, h, isTank, isProjectile, vox, voy, boxDetail):
        entity.__init__(self, x, y, w, h, isTank, isProjectile, vox, voy)
        self.boxDetail = boxDetail
        
    def drawEntity(self):
        if boxDetail != "temp":
            boxDetail
            
            
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
        rectMode(RADIUS)
        rect(self.x, self.y, self.w, self.h)
        rectMode(CORNER)
        
        
# Group_5------------------------------------------------------------------
class chatBox(object):
    def __init__(self, x, y, w, lines, fromTop, strs, displayIndex):
        self.x = x
        self.y = y
        self.w = w
        self.lines = lines
        self.fromTop = fromTop
        self.strs = strs
        self.displayIndex = displayIndex
        self.h = lines*s
    
    def drawChatBox(self):
        self.h = self.lines*s
        stroke(255)
        fill(0,120)
        if self.fromTop:
            rect(self.x, self.y, self.w, self.h)
            textFont(chatText)
            textSize(1.3*s*.740)
            fill(255)
            lenStr = len(self.strs)
            for i in range(min(lenStr,self.lines)):
                print(lenStr-i)
                text(self.strs[lenStr-i-1], self.x+.5*s, (self.y+self.h-i*s)-((s*1-textAscent())/2)-s*.2)
        else:
            rect(self.x, self.y+h, self.w, -self.h)
            
# ------------------------------------------------------------------Group_6
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
        x1 = t.x
        y1 = t.y - s*.5
        x2 = (t.power*s)*cos(t.fireAngle)
        y2 = (t.power*s)*sin(t.fireAngle)
        fill(255)
        line(x1,y1,x1+x2,y1-y2)
        strokeWeight(1)
                
    def tankHit(self, tankNum):
        self.tanks[tankNum-1].health = self.tanks[tankNum-1].health - 1
        self.totalHealth = 0
        for t in self.tanks:
            self.totalHealth = self.totalHealth + t.health
            
    def displayPlayerData(self):
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
        
# ------------------------------------------------------------------Group_7
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
            fill(0, 120)
        else:
            # detail red
            fill(192,64,0)
        rect(self.x, self.y, self.w, self.h)
        if type(self.buttonDetail) == str:
            if self.co1or == 0:
                fill(255)
            else:
                fill(0)
            textFont(font1)
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
    def __init__(self, pageButtons, pageTag, pageGraphics, pageDetails):
        self.pageButtons = pageButtons
        self.pageTag = pageTag
        self.pageGraphics = pageGraphics
        self.pageDetails = pageDetails
    
    def drawPage(self):
        if self.pageGraphics != "temp":
             image(self.pageGraphics, 0, 0)
        if self.pageDetails != "temp":
            self.pageDetails()
        for b in self.pageButtons: b.drawButton()
    

# Misc functions
def activatePage(p1):
    for p in pages:
        if p1.pageTag != p.pageTag:
            p.isActive = False
    p1.drawOnce = True


    
# ------------------------------------------------------------------Group_8
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

    

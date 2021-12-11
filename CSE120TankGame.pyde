import random
# Group_1------------------------------------------------------------------Group_1
# Setup Global Variables
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
currentKey = None
playerQueue = None

# Global tanks
left = "left"
right = "right"
tank1 = None
tank2 = None
tank3 = None
tank4 = None
clientTanks = None
entities = None
tankTurnIndex = 0

# Players
player1 = None
player2 = None
players = None

# Teams
team1 = None
team2 = None
team3 = None
teams = None

# Global buttons
timerB = None
fireB = None
playScreenButtons = None
playB = None
optionsB = None
exitB = None
mainScreenButtons = None
returnB = None
limiting_ammoB = None
moving_playerB = None
random_targetB = None
optionScreenButtons = None
angleBar = None
fireBar = None

# Global textButtons
chatBT = None
leftScrollBT = None
rightScrollBT = None
activeTBs = None

# Global pages
mainP = None
playP = None
optionsP = None
pages = None

# Misc
playerTurnIndex = 0

# Command values
maxTanks = 2

# Game settings
gameModeChallenge = True
GameRuleMoving = False
gameScore = 0

# Animation Booleans
animationSpawnOnce = None
fireLock = None
fireLockTimer = None

# Group_2------------------------------------------------------------------Group_2
# General setup for program. Screen size.
def settings():
    global sW
    global sH
    global s
    # displayHeight is no longer supported for python in processing.
    # sW = int((displayHeight*scale_)/32*0.7)*32
    # sH = int((displayHeight*scale_)/32)*32  
    sW = int((3840*scale_)/32)*32
    sH = int((3840*scale_)/32*.5625)*32
    size(sW, sH)
    s = int(sH/32)
    

def setup():
    # Animation setup
    global animationSpawnOnce
    global fireLock
    global fireLockTimer
    animationSpawnOnce = False
    fireLock = False
    fireLockTimer = 0
    # General setup for font sizes, backgrounds.
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
    
# Group_2.1-----------------------------------------------------------------Group_2.1
# Definitions for Pgraphics used as page backgrounds.
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
    # Player queue outlines
    main.stroke(255)
    main.noFill()
    main.rect(39.5*s,5.25*s,4.5*s,3.50*s)
    main.rect(45.5*s,5.25*s,4.5*s,3.50*s)
    main.rect(52*s,5.25*s,4.5*s,3.50*s)
    main.rect(39*s,3*s,18*s,17*s)
    main.fill(0,120)
    main.rect(39*s,3*s,18*s,2*s)
    main.rect(39*s,5*s,18*s,4*s)
    main.rect(39*s,19*s,18*s,1*s)
    main.fill(255)
    main.line(51*s,5*s,51*s,9*s)
    main.textFont(font1)
    main.textSize(2*s*.740)
    main.text("Player queue", 39.5*s, 4.5*s)
    main.textFont(chatText)
    main.textSize(1.3*s*.740)
    main.text("Type here",39.5*s,(20*s)-((s-textAscent())/2)-s*.4)
    # Bottum black
    main.noStroke()
    main.fill(180,100)
    main.rect(0,int(sH*.75),sW,sH)
    main.stroke(255)
    main.fill(0)
    main.quad(0,sH*.75,19*s,sH*.75,15*s,sH,0,sH)
    main.quad(57*s,sH*.75,20*s,sH*.75,16*s,sH,sW,sH)
    main.endDraw()

    global playG
    playG = createGraphics(sW,sH)
    playG.beginDraw()
    playG.background(192, 64, 0)
    playG.image(boxGrid, 0, 0)
    # Bottum black
    playG.noStroke()
    playG.fill(180,100)
    playG.rect(0,int(sH*.75),sW,sH)
    playG.stroke(255)
    playG.fill(0)
    playG.quad(57*s,sH*.75,20*s,sH*.75,16*s,sH,sW,sH)
    playG.endDraw()
    
    global optionsG
    optionsG = createGraphics(sW,sH)
    optionsG.beginDraw()
    optionsG.background(192, 64, 0)
    optionsG.image(boxGrid, 0, 0)
    optionsG.fill(0,100)
    optionsG.rect(0,0,sW,sH)
    optionsG.endDraw()

# Group_2.2-----------------------------------------------------------------Group_2.2
# Definitions for teams, players, tanks.
    testChat = ["[Game] Hello Player1!", "[Game] Use the text box below to enter messages."]
    # Chat boxes
    global playerQueue
    playerQueue = chatBox(39*s, 9*s, 18*s, 10, True, testChat, 0)
    
    # Players
    global player1
    global player2
    global players
    player1 = player("Player1", [], False)
    player2 = player("Player2", [], False)
    players = [player1, player2]
    
    # Teams
    global team1
    global team2
    global team3
    global teams
    team1 = team("Team1", left, [player1])
    team2 = team("Team2", right, [player2])
    team3 = team("Team3", left, players)
    
    # Tanks
    global tank1
    global tank2
    global tank3
    global tank4
    global clientTanks
    global entities
    tank1 = tank(9*s, 23*s+.73*s, .5*s, .27*s, 0, left, "T1", 101, 102)
    tank2 = tank(28*s, 23*s+.73*s, .5*s, .27*s, 0, right, "T2", 101, 102)
    tank3 = tank(36*s, 23*s+.73*s, .5*s, .27*s, 0, right, "T3", 101, 102)
    tank4 = tank(44*s, 23*s+.73*s, .5*s, .27*s, 0, right, "T4", 101, 102)
    clientTanks = [tank1, tank2, tank3, tank4]
    entities = []

# Group_2.3-----------------------------------------------------------------Group_2.3
# Definitions for buttons and pages.
    # Buttons
   
    global textButtons
    global fireB
    global timerB
    global fireBar
    global angleBar
    global burst1B
    global burst3B
    global burst5B
    global playScreenButtons
    angleBar = valueBar(19.5*s, 27.5*s, 10*s, " FireAngle", 79, 34, 50)
    fireBar = valueBar(19.5*s, 29.5*s, 10*s, "FirePower", 100, 0, 50)
    fireB = button(0,255, "fire!!.n", s, 27*s, 5*s, 2*s, functionFire, "")
    playScreenButtons = [fireB, fireBar, angleBar]
    
    global playB
    global optionsB
    global exitB
    global leftScrollBT
    global rightScrollBT
    global chatBT
    global mainScreenButtons
    playB = button(0, 255, "Begin.n", 5*s, 10*s, 6*s, 2*s, functionPlay, detailBlack)
    optionsB = button(0, 255, "Options.n", 5*s, 13*s, 8*s, 2*s, functionOptions, detailBlack)
    exitB = button(0, 255, "Exit.n", 5*s, 16*s, 5*s, 2*s, functionExit, detailBlack)
    leftScrollBT = button(0, 255, "left.b", 56*s, 9*s, 1*s, .75*s, "temp", "temp")
    rightScrollBT = button(0, 255, "left.b", 56*s, 10*s, 1*s, .75*s, "temp", "temp")
    chatBT = textButton(0, 255, "chat.tb", 43*s, 19*s, 14*s, 1*s, "TB", "tb.", playerQueue, "mainScreen")
    mainScreenButtons = [playB, optionsB, exitB, leftScrollBT, rightScrollBT, chatBT]
    
    global returnB
    global gameModeB
    global gameRuleB
    global exitB
    global optionScreenButtons
    
    gameModeB = button(0, 255, "Game Mode  .n", 2*s, 10*s, 9*s, 2*s, functionMode, detailMode)
    gameRuleB = button(0, 255, "Moving Tank.n", 2*s, 6*s, 9*s, 2*s, functionRule, detailRule)
    returnB = button(0, 255, "Return.n", 2*s, 25*s, 5*s, 2*s, functionReturn, "Back")
    optionScreenButtons = [gameModeB, gameRuleB, returnB]
    
    textButtons = [chatBT]
    global activeTBs
    activeTBs = set()
    
    # Pages
    global playP
    global mainP
    global optionsP
    playP = page(playScreenButtons, "playScreen", playG, "temp")
    mainP = page(mainScreenButtons, "mainScreen", main, detailMain)
    optionsP = page(optionScreenButtons, "optionScreen", optionsG, "temp")
    mainP.drawOnce = True
    global pages
    pages = [mainP, playP, optionsP]
    
    activatePage(mainP)
    
# Group_3------------------------------------------------------------------Group_3
# Functions.
def tankAssignment():
    entities.extend([tank1, tank4])
def spawnRandomTank():
    alreadyExist = True
    while(alreadyExist == True):
        randInt = random.randint(1, 3)
        alreadyExist = True
        for e in entities:
            if e == clientTanks[randInt]:
                alreadyExist = True
                
    entities.append(clientTanks[randInt])
    
    
# Group_3.2------------------------------------------------------------------Group_3.2
# Detail Functions for buttons. These print after basic button hitboxes:
def detailMode(x, y, w, h):
    fill(0, 120)
    stroke(255)
    rect(x+w+2*s,y,4*s,h)
    textX = (4*s-textWidth("False"))/2+x
    textY = y+h-((h-textAscent())/2)-s*.1
    fill(255)
    text(str(gameModeChallenge), textX+w+2*s, textY)
    
def detailRule(x, y, w, h):
    fill(0, 120)
    stroke(255)
    rect(x+w+2*s,y,4*s,h)
    textX = (4*s-textWidth("False"))/2+x
    textY = y+h-((h-textAscent())/2)-s*.1
    fill(255)
    text(str(GameRuleMoving), textX+w+2*s, textY)
    
def detailRed(x, y, w, h):
    # Outter button box
    fill(192,64,0, 100)
    stroke(255)
    if h <= 2*s:
        dT = s*.25
    else:
        dT = s*.5
    rect(x-dT,y-dT,w+dT*2,h+dT*2)

def detailBlack(x, y, w, h):
    # Outter button box
    fill(0,100)
    stroke(255)
    if h <= 2*s:
        dT = s*.25
    else:
        dT = s*.5
    rect(x-dT,y-dT,w+dT*2,h+dT*2)
        
def detailMain():
    displayQueueData()
    playerQueue.drawChatBox()
    
def displayQueueData():
    fill(255)
    textFont(chatText)
    textSize(1.3*s*.740)
    text(team1.teamName, 39.75*s, 6.25*s-((s*1-textAscent())/2)-s*.2)
    for i in range(len(team1.players)):
        if team1.players[i] != None:
            text("- "+team1.players[i].playerName, 39.75*s, 7.25*s+i*s-((s*1-textAscent())/2)-s*.2)
    text(team2.teamName, 45.75*s, 6.25*s-((s*1-textAscent())/2)-s*.2)
    for i in range(len(team2.players)):
        if team2.players[i] != None:
            text("- "+team2.players[i].playerName, 45.75*s, 7.25*s+i*s-((s*1-textAscent())/2)-s*.2)
    for i in range(len(team3.players)):
        if team3.players[i] != None:
            text("- "+team3.players[i].playerName, 52.5*s, 6.25*s+i*s-((s*1-textAscent())/2)-s*.2)
            
# Group_3.3------------------------------------------------------------------Group_3.3
# Button functions to be passed as button arguments/members
def functionMode():
    global gameModeChallenge
    gameModeChallenge = False if gameModeChallenge == True else True
    optionsP.drawPage()
    
def functionRule():
    global GameRuleMoving
    GameRuleMoving = False if GameRuleMoving == True else True
    optionsP.drawPage()
    
def functionPlay():
    if players != None and len(players) > 0:
        global gameScore
        global entities
        gameScore = 0
        entities = []
        tankAssignment()
        activatePage(playP)
        print("Activiating play page")
        
def functionOptions():
    activatePage(optionsP)
    print("Activating options page")
    
def functionExit():
    exit()
    print("Exit program executed")
    
def functionFire():
    if fireLock == False:
        fireBurst = 1
        t = clientTanks[tankTurnIndex]
        
        vx = 20*s*fireBar.valueRatio*cos(angleBar.valueRatio*3.141592653589793)
        vy = 20*s*fireBar.valueRatio*sin(angleBar.valueRatio*3.141592653589793)
        tempProjectile = projectile(t.x, t.y-s, .25*s, .25*s, -vx, vy, 0, 0)
        entities.append(tempProjectile)
        textSize(100)
        print("Firing projectile") 
        print("FirePower: ", fireBar.value)
        print("FireAngle: ", angleBar.value)
        global fireLock
        fireLock = True

def functionReturn():
    activatePage(mainP)
    print("Returning to main")
    
# Group_3.4------------------------------------------------------------------Group_3.4
# commands implement for chat based commands for the user.
def changeName(name):
    pass
    
def joinServer():
    pass
    
def swapWith(name):
    pass

# Group_4------------------------------------------------------------------Group_4
# Classes... All of them:
class entity(object):
    vx = 0 
    vy = 0
    type = "entity"
    def __init__(self, x, y, w, h, vox, voy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vox = vox
        self.voy = voy
        self.vx = vox
        self.vy = voy
    
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
    def __init__(self, x, y, w, h, vox, voy, boxDetail):
        entity.__init__(self, x, y, w, h, vox, voy)
        self.boxDetail = boxDetail
        
    def drawEntity(self):
        if boxDetail != "temp":
            boxDetail
            
            
class tank(entity):
    def __init__(self, x, y, w, h, playerNum, side, tankName, vox, voy):
        entity.__init__(self, x, y, w, h, vox, voy)
        self.playerNum = playerNum
        self.side = side
        self.tankName = tankName
        self.health = 2
        self.isTurn = False
        self.fireAngle = 2
        self.power = 7 
        self.doDrawLine = False
        
    def drawEntity(self):
        stroke(255)
        strokeWeight(1)
        fill(0)
        rectMode(RADIUS)
        rect(self.x, self.y, self.w, self.h)
        rectMode(CORNER)
        
        
class projectile(entity):
    timeElapsed = 0 
    def __init__(self, x, y, w, h, vox, voy, v, angle):
        entity.__init__(self, x, y, w, h, vox, voy)
        self.x0 = x
        self.y0 = y
        self.ax = 0
        self.ay = -9.8 * s
        self.timeStart = millis()
        self.vx = vox
        self.vy = voy
        w = s
        h = s
        self.type = "projectile"
    
    def hit(self):
        for e in entities:
            if e.type != "projectile":
                if e.x-e.w-s < self.x < e.x+e.w+s and e.y-e.h-s < self.y < e.y+e.h+s:
                    global gameScore
                    gameScore = gameScore + 1
                    entities.remove(self)
                    entities.remove(e)
                    spawnRandomTank()
                    break
            if self.y > sH*.73:
                entities.remove(self)
                del self
                break
        
    def updatePos(self):
        avx = (self.vx + self.vox) / 2
        t = (float(millis() - self.timeStart)) / 1000.00
        dx = float(avx) * float(t)
        self.x = self.x0 + float(dx)
        
        dy = float(self.vy * t) + float(0.5) * float(self.ay) * float(t*t)
        self.y = self.y0 - dy
        self.hit()
        
    def drawEntity(self):
        self.updatePos()
        rectMode(RADIUS)
        rect(self.x, self.y, self.w, self.h)
        rectMode(CORNER)

        
# Group_5------------------------------------------------------------------Group_5
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
    
    def addStr(self, str1):
        self.strs.append("["+player1.playerName+"] "+str1)
    
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
                text(self.strs[lenStr-i-1], self.x+.5*s, (self.y+self.h-i*s)-((s*1-textAscent())/2)-s*.2)
        else:
            rect(self.x, self.y+h, self.w, -self.h)
         
 
class valueBar(object):
    def __init__(self, x, y, w, name, valueMax, valueMin, value):
        self.x = x
        self.y = y-.3*s
        self.w = w
        self.name = name
        self.value = value
        self.valueMax = valueMax
        self.valueMin = valueMin
        self.valueRange = self.valueMax-self.valueMin
        self.valueRatio = float(self.value-self.valueMin)/float(self.valueRange)
        self.transX = textWidth(self.name)+ 2*s
        
    def incrementOne(self):
        if self.value < self.valueMax:
            self.value = self.value + 1
            self.valueRatio = (float(self.value)-float(self.valueMin))/float(self.valueRange)
        
    def incrementDownOne(self):
        if self.value > self.valueMin:
            self.value = self.value - 1
            self.valueRatio = (float(self.value)-float(self.valueMin))/float(self.valueRange)
            
    def hitCheck(self):
        if (self.x+self.transX < mouseX < self.x+self.transX+self.w) and (self.y-.5*s < mouseY < self.y++.5*s):
            x0 = self.x+self.transX
            x1 = self.x+self.transX+self.w
            xvalue = mouseX - x0
            self.value = int(((mouseX-x0)/(self.w))*(self.valueRange)+self.valueMin)
            self.valueRatio = (float(self.value)-float(self.valueMin))/float(self.valueRange)
            playP.drawPage()
            print(self.name, "equals", self.value, "ratio", self.valueRatio)
         
    def drawButton(self):
        stroke(255)
        fill(255)
        strokeWeight(10)
        
        textFont(font1)
        textSize(2*s*.740)
        text(self.name + ": ", self.x, self.y+.5*s)
        
        line(self.x+self.transX, self.y, self.x+self.transX+self.w, self.y)
        strokeWeight(20)
        transValue = ((float(self.value)-float(self.valueMin))/(self.valueRange)*self.w)
        line(self.x+self.transX+transValue, self.y-.5*s, self.x+self.transX+transValue, self.y+.5*s)
        
        
# Group_6------------------------------------------------------------------Group_6
class player(object):
    aimX = 0
    aimY = 0
    def __init__(self, playerName, tankNums, isTurn):
        self.playerName = playerName
        self.tankNums = tankNums
        self.isTurn = isTurn
    
    def drawFiringLine(self):
        strokeWeight(3)
        t = clientTanks[tankTurnIndex]
        x1 = t.x
        y1 = t.y - s*.5
        
        x2 = 5*s*fireBar.valueRatio*cos(angleBar.valueRatio*3.141592653589793)
        y2 = 5*s*fireBar.valueRatio*sin(angleBar.valueRatio*3.141592653589793)
        fill(255)
        line(x1,y1,x1-x2,y1-y2)
        strokeWeight(1)
    
        
class team(object):
    def __init__(self, teamName, side, players):
        self.teamName = teamName
        self.side = side
        self.players = players
        
        
# Group_7------------------------------------------------------------------Group_7
class button(object):
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
        
        self.tSize = self.h*.740
        textSize(self.tSize)
        self.textX = (self.w-textWidth(self.name[:-2]))/2+self.x
        self.textY = self.y+self.h-((self.h-textAscent())/2)-s*.1
    
    def drawButton(self):
        strokeWeight(2)
        textFont(font1)
        textSize(self.tSize)
        if self.buttonDetail == "basic":
            # Basic button hitbox
            if self.co1or == 0:
                fill(0, 120)
            else:
                # detail red
                fill(192,64,0)
            rect(self.x, self.y, self.w, self.h)
        else:
            # Button details
            if type(self.buttonDetail) != str:
                self.buttonDetail(self.x, self.y, self.w, self.h)
                
            # Basic button hitbox
            fill(0, 120)
            rect(self.x, self.y, self.w, self.h)
    
            # Name print
            if self.name[-2:] == ".n":
                if self.co1or == 0:
                    fill(255)
                else:
                    fill(0)
                text(self.name[:-2], self.textX, self.textY) 

    def buttonFunction(self): 
        if self.buttonF != "temp":
            self.buttonF()
            
    def hitCheck(self):
        if (self.x < mouseX < self.x+self.w) and (self.y < mouseY < self.y+self.h):
            self.buttonFunction()
            return True
        else:
            return False
            
            
class textButton(button):
    def __init__(self, co1or, strok3, name, x, y, w, h, buttonF, buttonDetail, chatBox, pageName):
        button.__init__(self, co1or, strok3, name, x, y, w, h, buttonF, buttonDetail)
        self.isSelected = False
        self.chatBox = chatBox
        self.pageName = pageName
        self.textX = self.x+.5*s
        self.tSize = 1.3*s*.740
        
    def drawButton(self):
        if self.isSelected:
            fill(0)
        else:
            noFill()
        rect(self.x, self.y, self.w, self.h)
        fill(255)
        textFont(chatText)
        textSize(self.tSize)
        text(self.buttonDetail[3:], self.textX, self.textY)  
        
    def drawPage(self):
        for p in pages:
            if p.pageTag == self.pageName:
                p.drawPage()
        
    def buttonFunction(self):
        self.isSelected = True
        global activeTBs
        activeTBs.add(self)
        self.drawButton()
    
            
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
                

class command():
    def __init__(self, comm, function, funcArg):
        self.comm = comm
        self.function = function
        self.funcArg = funcArg
    
    def commandFunction(self):
        if funcArg == "":
            self.function()
        else:
            self.function(funcArg)
    
# Misc functions
def activatePage(p1):
    for p in pages:
        if p1.pageTag != p.pageTag:
            p.isActive = False
    image(boxGrid, 0, 0)
    p1.drawPage()
    p1.isActive = True
    p1.drawOnce = True
    
def getActivePage():
    for p in pages:
        if p.isActive:
            return p
        
# Group_8------------------------------------------------------------------Group_8
def draw():
    if playP.isActive:
        playP.drawPage()
        text("Time: " + str(millis()/1000) + " Score: " + str(gameScore), (57*s/2)-textWidth("Time: " + str(millis()/1000) + "   Score: ")/2, 3*s)
        if gameModeChallenge:
            if millis()/1000 % 10 == 5 and animationSpawnOnce == False:
                global animationSpawnOnce
                animationSpawnOnce = True
                spawnRandomTank()
                if len(entities) > 3:
                    functionPlay()
            if millis()/1000 % 10 == 6:
                animationSpawnOnce = False
        if fireLock and fireLockTimer == 0:
            global fireLockTimer
            fireLockTimer = millis()
        if fireLock and millis()/1000 >= fireLockTimer/1000 + 1:
            global fireLock
            fireLock = False
            fireLockTimer = 0
            
        for p in players:
            for e in entities:
                e.drawEntity()
            players[playerTurnIndex].drawFiringLine()
                                                        
def mousePressed():
    print("X: ", mouseX/s, "Y: ", mouseY/s)
    for p in pages:
        if p.isActive:
            for b in p.pageButtons:
                b.hitCheck()

def mouseDragged():
    pass
        
def keyPressed():
    if enableTB():
        return 0
    runTB()
    if keyCode == UP:
        fireBar.incrementOne()
    if keyCode == DOWN:
        fireBar.incrementDownOne()
    if keyCode == LEFT:
        angleBar.incrementDownOne()
    if keyCode == RIGHT:
        angleBar.incrementOne()
    if keyCode == 32:
        functionFire()
    
# Functions... All of them:
def enableTB():
    if key == ENTER and len(activeTBs) == 0:
        for TB in textButtons:
            print("test")
            if TB.pageName == getActivePage().pageTag:
                print("test2")
                TB.buttonFunction()
        return True
    
def runCommand(comm):
    playerQueue.strs.append("[Game] That is not an existing command. Try /help")
    
def runTB():
    for i in activeTBs:
        if key == ENTER:
            i.chatBox.addStr(i.buttonDetail[3:])
            if i.buttonDetail[3:4] == '/':
                runCommand(i.buttonDetail[3:])
            i.buttonDetail = "tb."
            i.isSelected = False
            i.drawPage()
            activeTBs.remove(i)
        elif (key == BACKSPACE or key == DELETE) and len(i.buttonDetail) >3:
            i.buttonDetail = i.buttonDetail[0:len(i.buttonDetail)-1]
        elif key == CODED or key == BACKSPACE or key ==TAB or key == ENTER or key == RETURN or key == ESC or key == DELETE:
            pass
        else:
            i.buttonDetail = i.buttonDetail + str(key)
        i.drawButton()

# Group_1------------------------------------------------------------------Group_1
# Setup Variablest
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
fireB = None
playScreenButtons = None
playB = None
optionsB = None
exitB = None
mainScreenButtons = None
returnB = None
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

# Group_2------------------------------------------------------------------Group_2
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
    main.quad(0,sH*.75,34*s,sH*.75,30*s,sH,0,sH)
    main.quad(57*s,sH*.75,35*s,sH*.75,31*s,sH,sW,sH)
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
    playG.quad(56.5*s, 2.5*s, 56.5*s, .5*s, 50*s, .5*s, 48*s, 2.5*s)
    playG.noFill()
    playG.line(50.5*s, .5*s, 48.5*s, 2.5*s)
    playG.line(51*s, .5*s, 51*s, 2.5*s)
    # Draw left player bar
    playG.fill(0,180)
    playG.quad(.5*s, 2.5*s, .5*s, .5*s, 9*s, .5*s, 7*s, 2.5*s)
    playG.noFill()
    playG.line(6*s,.5*s,6*s,2.5*s)
    playG.line(6.5*s,2.5*s,8.5*s,.5*s)

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
    activatePage(mainP)
       

def setupVariables():
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
    tank1 = tank(1.5*s, 23*s+.73*s, .5*s, .27*s, 0, left, "T1", 101, 102)
    tank2 = tank(3.5*s, 23*s+.73*s, .5*s, .27*s, 0, left, "T2", 101, 102)
    tank3 = tank(s*20.5, 23*s+.73*s, .5*s, .27*s, 0, left, "T3", 101, 102)
    tank4 = tank(s*18.5, 23*s+.73*s, .5*s, .27*s, 0, left, "T4", 101, 102)
    clientTanks = [tank1, tank2, tank3, tank4]
    entities = []
    
    # Buttons
    global textButtons
    global fireB
    global playScreenButtons
    global fireBar
    global angleBar
    angleBar = valueBar(8*s, 27.5*s, 12*s, " FireAngle", 100, 50)
    fireBar = valueBar(8*s, 30.5*s, 12*s, "FirePower", 100, 50)
    fireB = button(192,255, "fire.b", s, 29*s, 5*s, 2*s, functionFire, "Fire!!")
    playScreenButtons = [fireB, fireBar, angleBar]
    global playB
    global optionsB
    global exitB
    global leftScrollBT
    global rightScrollBT
    global chatBT
    global mainScreenButtons
    playB = button(0, 255, "play.b", 5*s, 10*s, 6*s, 2*s, functionPlay, "Begin")
    optionsB = button(0, 255, "options.b", 5*s, 13*s, 8*s, 2*s, functionOptions, "Options")
    exitB = button(0, 255, "exit.b", 5*s, 16*s, 5*s, 2*s, functionExit, "Exit")
    leftScrollBT = button(0, 255, "left.b", 56*s, 9*s, 1*s, .75*s, "temp", "temp")
    rightScrollBT = button(0, 255, "left.b", 56*s, 10*s, 1*s, .75*s, "temp", "temp")
    chatBT = textButton(0, 255, "chat.tb", 43*s, 19*s, 14*s, 1*s, "TB", "tb.", playerQueue, "mainScreen")
    mainScreenButtons = [playB, optionsB, exitB, leftScrollBT, rightScrollBT, chatBT]
    global optionScreenButtons
    returnB = button(0, 255, "return.b", 2*s, 25*s, 5*s, 2*s, functionReturn, "Back")
    exitB = button(0, 255, "exit.b", 2*s, 25*s, 5*s, 2*s, functionExit, "Exit")
    optionScreenButtons = [returnB]
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
    
# Group_3------------------------------------------------------------------Group_3
# Button functions to be passed as button arguments/members
def functionPlay():
    if players != None and len(players) > 0:
        tankAssignment()
        activatePage(playP)
        print("Activiating play page")
    else:
        playerQueue.strs.append("[Game] Must have atleast 1 player ready to begin.")
        mainP.drawPage()
def functionOptions():
    activatePage(optionsP)
    print("Activating options page")
    
def functionExit():
    exit()
    print("Exit program executed")
    
def functionFire():
    textSize(100)
    print("Firing projectile") 
    print("FirePower: ", fireBar.value)
    print("FireAngle: ", angleBar.value)
    
def functionReturn():
    activatePage(mainP)
    print("Returning to main")
    
# Group_3.1-----------------------------------------------------------------Group_3.1
# Misc Functions
def tankAssignment():
    if maxTanks == 4:
        if team1.players.size() > 1:
            team1.players[0].tankNums.append(1)
            team1.players[1].tankNums.append(2)
        elif team1.players.size() == 1:
            team1.players[0].tankNums.extend([1,2])
        if team2.players.size() > 1:
            team2.players[0].tankNums.append(3)
            team2.players[1].tankNums.append(3)
        elif team2.players.size() == 1:
            team2.players[0].tankNums.extend([3,4])
        entities.extend([tank1, tank2, tank3, tank4])
    else:
        team1.players[0].tankNums.append(1)
        team2.players[0].tankNums.append(4)
        entities.extend([tank1, tank4])


def handleTurns():
    pass
       
       
       
# Group_3.2------------------------------------------------------------------Group_3.2
# commands
def changeName(name):
    pass
    
def joinServer():
    pass
    
def swapWith(name):
    pass

# Group_3.3------------------------------------------------------------------Group_3.3
# Detail Functions:
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
    

# Group_4------------------------------------------------------------------Group_4
# Classes... All of them:
class entity(object):
    vx = 0 
    vy = 0
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
    def __init__(self, x, y, w, name, valueMax, value):
        self.x = x
        self.y = y-.5*s
        self.w = w
        self.name = name
        self.valueMax = valueMax
        self.value = value
        self.transX = textWidth(self.name)+ 2*s
    
    def hitCheck(self):
        if (self.x+self.transX < mouseX < self.x+self.transX+self.w) and (self.y-.5*s < mouseY < self.y++.5*s):
            x0 = self.x+self.transX
            x1 = self.x+self.transX+self.w
            xvalue = mouseX - x0
            self.value = int((xvalue/self.w)*self.valueMax)
            playP.drawPage()
            print(self.name, "equals", self.value)
         
    def drawButton(self):
        stroke(255)
        fill(255)
        strokeWeight(10)
        textSize(2*s*.740)
        text(self.name + ": ", self.x, self.y+.5*s)
        
        line(self.x+self.transX, self.y, self.x+self.transX+self.w, self.y)
        strokeWeight(20)
        transValue = (float(self.value)/float(self.valueMax)*self.w)
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
        x2 = (t.power*s)*cos(t.fireAngle)
        y2 = (t.power*s)*sin(t.fireAngle)
        fill(255)
        line(x1,y1,x1+x2,y1-y2)
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
        if self.buttonDetail != "temp":
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
        if self.buttonDetail != "temp":
            # Prep for text
            if self.co1or == 0:
                fill(255)
            else:
                fill(0)
            if type(self.buttonDetail) == str:
                textFont(font1)
                textSize(self.tSize)
                text(self.buttonDetail, self.textX, self.textY)     

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

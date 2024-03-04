import copy
#Sample Grid
#8 X X X X X X X X
#7 X X X X X X X X
#6 X X X X X X X X
#5 X X X X X X X X
#4 X X X X X X X X
#3 X X X X X X X X
#2 X X X X X X X X
#1 X X X X X X X X
#  a b c d e f g h

#y is bottom to top, x is left to right

def PrintBoard():
    global board
    for i in range(8):
        print(8-i, end = " ")
        for j in range(8):
            getPiece(j,i).printcharacter()
            # getPiece(j,i).printType()
        print("")
    print("  aa bb cc dd ee ff gg hh")

def getPiece(x,y): #returns the piece at the given coordinates
    global board
    return board[y][x]

def outofbounds(x,y):
    return x<0|x>7|y<0|y>7

def move(PieceFrom, PieceTo):
    global board

    # GameDebug(StringBuilder("PieceFrom Move: ", PieceFrom.getcharacter(), " ", PieceFrom.getx(), " ", PieceFrom.gety()))
    # GameDebug(StringBuilder("PieceTo Move: ", PieceTo.getcharacter(), " ", PieceTo.getx(), " ", PieceTo.gety()))

    temp = copy.copy(PieceFrom)
    # PieceFrom = copy.copy(PieceTo)
    # PieceTo = copy.copy(temp)

    # GameDebug(StringBuilder("PieceFrom: ", type(PieceFrom), " ", PieceFrom.getcharacter(), " ", PieceFrom.getx(), " ", PieceFrom.gety()))
    # GameDebug(StringBuilder("PieceTo: ", type(PieceTo), " ", PieceTo.getcharacter(), " ", PieceTo.getx(), " ", PieceTo.gety()))

    # GameDebug(StringBuilder("PieceFrom: ", type(PieceFrom), " ", PieceFrom.getcharacter(), " ", PieceFrom.getx(), " ", PieceFrom.gety()))
    # GameDebug(StringBuilder("PieceTo: ", type(PieceTo), " ", PieceTo.getcharacter(), " ", PieceTo.getx(), " ", PieceTo.gety()))

    # PieceFrom.character = PieceTo.character
    # PieceFrom.value = PieceTo.value
    # PieceFrom.color = PieceTo.color

    board[PieceFrom.gety()][PieceFrom.getx()] = PieceTo
    board[PieceTo.gety()][PieceTo.getx()] = PieceFrom
    PieceFrom.x = PieceTo.getx()
    PieceFrom.y = PieceTo.gety()
    PieceTo.x = temp.getx()
    PieceTo.y = temp.gety()

    #check the piece has moved
    PieceFrom.hasMoved = True
    PieceTo.hasMoved = True
    GameDebug(StringBuilder("The intern presentation 1: ", board[PieceFrom.y][PieceFrom.x].getcharacter()))
    GameDebug(StringBuilder("The intern presentation 2: ", board[PieceTo.y][PieceTo.x].getcharacter()))

class Piece:
    def __init__(self, character, value, x, y, color):
        self.character=character
        self.value = value
        self.x = x
        self.y = y
        self.color = color
        self.hasMoved = False

    def getcharacter(self):
        return self.color + self.character
    
    def printcharacter(self):
        print(self.getcharacter(), end=" ")

    def printType(self):
        print(type(self).__name__, end = " ")

    def getvalue(self):
        return self.value

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
    def getLocation(self):
        return (self.x,self.y)

    def getcolor(self):
        return self.color
    
    def gethasMoved(self):
        return self.hasMoved
    
    def getOppcolor(self,tempx,tempy):
        if getPiece(tempx,tempy).getcolor()!=self.color and getPiece(tempx,tempy).getcolor()!="+":
            return True
        return False

    def getAttacker(self): # Return a list of all the pieces attacking this piece
        checklist=[]
        #Places to check:

        #Up
        tempy=self.y
        tempx=self.x
        while(tempy>=0):
            tempy-=1
            if self.tempConfig(tempx, tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()=="R" or getPiece(tempx,tempy).getcharacter()=="Q":
                GameDebug(StringBuilder("Attacking Piece Found: ",getPiece(tempx,tempy).getcharacter()))
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Up Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Down
        tempy=self.y
        tempx=self.x
        while tempy<8:
            tempy+=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()[1]=="R" or getPiece(tempx,tempy).getcharacter()[1]=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Down Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Left
        tempy=self.y
        tempx=self.x
        while(tempx>=0):
            tempx-=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()=="R" or getPiece(tempx,tempy).getcharacter()=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Left Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Right
        tempy=self.y
        tempx=self.x
        while(tempx<8):
            tempx+=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()=="R" or getPiece(tempx,tempy).getcharacter()=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Right Piece: ",getPiece(tempx,tempy).getcharacter()))
                break

        #Up-Left
        tempy=self.y
        tempx=self.x
        while tempy>=0 and tempx>=0:
            tempy-=1
            tempx-=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()=="B" or getPiece(tempx,tempy).getcharacter()=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()=="P" and getPiece(tempx,tempy).getcolor()=="B":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Up Left Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Up-Right
        tempy=self.y
        tempx=self.x
        while tempy>=0 and tempx<8:
            tempy-=1
            tempx+=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()[1]=="B" or getPiece(tempx,tempy).getcharacter()[1]=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()[1]=="P" and getPiece(tempx,tempy).getcolor()=="B":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Up Right Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Down-Left
        tempy=self.y
        tempx=self.x
        while tempy<8 and tempx>=0:
            tempy+=1
            tempx-=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()=="B" or getPiece(tempx,tempy).getcharacter()=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx, tempy).getcharacter()=="P" and getPiece(tempx,tempy).getcolor()=="W":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Down Left Piece: ",getPiece(tempx,tempy).getcharacter()))
                break
        #Down-Right
        tempy=self.y
        tempx=self.x
        while tempy<8 and tempx<8:
            tempy+=1
            tempx+=1
            if self.tempConfig(tempx,tempy): # Out of Bounds
                break
            if getPiece(tempx,tempy).getcharacter()[1]=="B" or getPiece(tempx,tempy).getcharacter()[1]=="Q":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()[1]=="P" and getPiece(tempx,tempy).getcolor()=="W":
                GameDebug("Attacking Piece Found: " + getPiece(tempx,tempy).getcharacter())
                checklist.append(getPiece(tempx,tempy))
                break
            if getPiece(tempx,tempy).getcharacter()!="++":
                GameDebug(StringBuilder("Down Right Piece: ",getPiece(tempx,tempy).getcharacter()))
                break

        #Knight
        if self.tempConfig(self.x+1,self.y+2)==False:
            if getPiece(self.x+1,self.y+2).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x+1,self.y+2).getcharacter())
                checklist.append(getPiece(self.x+1,self.y+2))
        if self.tempConfig(self.x+1,self.y-2)==False:
            if getPiece(self.x+1,self.y-2).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x+1,self.y-2).getcharacter())
                checklist.append(getPiece(self.x+1,self.y-2))
        if self.tempConfig(self.x-1,self.y+2)==False:
            if getPiece(self.x-1,self.y+2).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x-1,self.y+2).getcharacter())
                checklist.append(getPiece(self.x-1,self.y+2))
        if self.tempConfig(self.x-1,self.y-2)==False:
            if getPiece(self.x-1,self.y-2).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x-1,self.y-2).getcharacter())
                checklist.append(getPiece(self.x-1,self.y-2))
        if self.tempConfig(self.x+2,self.y+1)==False:
            if getPiece(self.x+2,self.y+1).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x+2,self.y+1).getcharacter())
                checklist.append(getPiece(self.x+2,self.y+1))
        if self.tempConfig(self.x+2,self.y-1)==False:
            if getPiece(self.x+2,self.y-1).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x+2,self.y-1).getcharacter())
                checklist.append(getPiece(self.x+2,self.y-1))
        if self.tempConfig(self.x-2,self.y+1)==False:
            if getPiece(self.x-2,self.y+1).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x-2,self.y+1).getcharacter())
                checklist.append(getPiece(self.x-2,self.y+1))
        if self.tempConfig(self.x-2,self.y-1)==False:
            if getPiece(self.x-2,self.y-1).getcharacter()=="&":
                GameDebug("Attacking Piece Found: " + getPiece(self.x-2,self.y-1).getcharacter())
                checklist.append(getPiece(self.x-2,self.y-1))

        return checklist
    
    def spider(self):
        #Find all pieces in a spider formation This function returns all the pieces
        # that are able to move onto that space, however the output does not need
        # to be captured in use
        Moveable = []
        GameDebug(StringBuilder("Spider: ",self.getcharacter()))
        #Up
        tempx = self.x
        tempy = self.y

        while tempy>=0:
            tempy-=1
            if self.tempConfig(tempx,tempy): #Out of bounds
                GameDebug(StringBuilder("Up: Out of bounds"))
                break
            if getPiece(tempx,tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Up: ",getPiece(tempx,tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break

        #Down
        tempx = self.x
        tempy = self.y

        while tempy<8:
            tempy+=1
            if self.tempConfig(tempx, tempy): # Out of bounds
                GameDebug(StringBuilder("Down: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Down: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Left
        tempx = self.x
        tempy = self.y
        while tempx>=0:
            tempx-=1
            if self.tempConfig(tempx, tempy): # Out of bounds
                GameDebug(StringBuilder("Left: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Left: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Right
        tempx = self.x
        tempy = self.y
        while tempx<8:
            tempx+=1
            if self.tempConfig(tempx, tempy): # Out of bounds
                GameDebug(StringBuilder("Right: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Right: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Up-Left
        tempx = self.x
        tempy = self.y
        while tempy>=0 and tempx>=0:
            tempy-=1
            tempx-=1
            if self.tempConfig(tempx, tempy): # Out of bounds
                GameDebug(StringBuilder("Up-Left: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Up-Left: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Up-Right
        tempx = self.x
        tempy = self.y
        while tempy>=0 and tempx<8:
            tempy-=1
            tempx+=1
            if self.tempConfig(tempx, tempy): # Out of bounds
                GameDebug(StringBuilder("Up-Right: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Up-Right: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Down-Left
        tempx = self.x
        tempy = self.y
        while tempy<8 and tempx>=0:
            tempy+=1
            tempx-=1
            if self.tempConfig(tempx, tempy):
                GameDebug(StringBuilder("Down-Left: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Down-Left: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        #Down-Right
        tempx = self.x
        tempy = self.y
        while tempy<8 and tempx<8:
            tempy+=1
            tempx+=1
            if self.tempConfig(tempx, tempy):
                GameDebug(StringBuilder("Down-Right: Out of bounds"))
                break
            if getPiece(tempx, tempy).getcharacter() != "++":
                GameDebug(StringBuilder("Down-Right: ", getPiece(tempx, tempy).getcharacter()))
                if getPiece(tempx,tempy).movecheck(self.x,self.y):
                    Moveable.append(getPiece(tempx,tempy))
                break
        GameDebug("Spider: End")
        GameDebug("=====================================")
        return Moveable

    def tempConfig(self,tempx,tempy): # if the piece is now out of the board
        if tempx<0 or tempx>7 or tempy<0 or tempy>7:
            return True
        return False

    def movecheck(self, otherPiece):
        pass # This method is left unimplemented intentionally
    
    def getPossibleMoves(self):
        pass # This method is left unimplemented intentionally

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__("P",1, x, y, color)
        self.enPassant = False
            
    def movecheck(self, tox, toy):
        #check if the pawn is moving in the correct direction
        GameDebug("--- Pawn: MoveCheck ---")
        if self.x !=tox and self.y != toy and abs(tox-self.x)==1 and abs(toy-self.y)==1:
            #if we are taking
            GameDebug("Attempting to take")
            if getPiece(tox, toy).color != self.color and getPiece(tox, toy).getcharacter() != "++":
                GameDebug("The Pawn is trying to take the opposite color")
                return True
            return False


        if self.color=="W":
            #piece is white
            GameDebug("White")
            if toy==self.y-1 and getPiece(self.x,self.y-1).getcharacter()!="++":
                #check for en passant
                enPassantPiece = getPiece(self.x-1, self.y-1)
                if enPassantPiece.getcharacter()!="++" and enPassantPiece.getcolor()!=self.color:
                    if enPassantPiece.getcharacter()[1]=="P" and enPassantPiece.gethasMoved()==True:
                        GameDebug(StringBuilder("White Pawn: MoveCheck: En Passant Success Left"))
                        self.enPassant= True
                        return True
                enPassantPiece = getPiece(self.x+1, self.y-1)
                if enPassantPiece.getcharacter()!="++" and enPassantPiece.getcolor()!=self.color:
                    if enPassantPiece.getcharacter()[1]=="P" and enPassantPiece.gethasMoved()==True:
                        GameDebug(StringBuilder("White Pawn: MoveCheck: En Passant Success Right"))
                        self.enPassant=True
                        return True

            GameDebug(StringBuilder("White Pawn: MoveCheck: ", toy, " to ", self.y))
            GameDebug(StringBuilder("White Pawn: MoveCheck: ", tox, " to ", self.x))

            if toy>=self.y:
                GameDebug(StringBuilder("Pawn: MoveCheck: Pawn cannot move backwards"))
                return False
            if self.hasMoved==False:
                if toy==self.y-2 and getPiece(self.x,self.y-2).getcharacter()=="++" and getPiece(self.x,self.y-1).getcharacter()=="++":
                    GameDebug(StringBuilder("Pawn: MoveCheck: Pawn can move 2 spaces"))
                    return True
            if toy==self.y-1 and getPiece(self.x,self.y-1).getcharacter()=="++":
                GameDebug(StringBuilder("Pawn: MoveCheck: Pawn can move 1 space"))
                return True

            GameDebug("Nothing was hit?")
            return False

        if self.color=="B":
            #piece is white
            GameDebug("Black")
            if toy==self.y-1 and getPiece(self.x,self.y-1)!="++":
                #check for en passant
                if getPiece(self.x-1,self.y-1).getcharacter()!="++" and getPiece(self.x-1,self.y-1).getcolor()!=self.color:
                    if getPiece(self.x-1,self.y-1).getcharacter()[1]=="P" and getPiece(self.x-1,self.y-1).gethasMoved()==True:
                        GameDebug(StringBuilder("White Pawn: MoveCheck: En Passant Success Left"))
                        self.enPassant=True
                        return True
                if getPiece(self.x+1,self.y-1).getcharacter()!="++" and getPiece(self.x+1,self.y-1).getcolor()!=self.color:
                    if getPiece(self.x+1,self.y-1).getcharacter()[1]=="P" and getPiece(self.x+1,self.y-1).gethasMoved()==True:
                        GameDebug(StringBuilder("White Pawn: MoveCheck: En Passant Success Right"))
                        self.enPassant=True
                        return True

            if toy<=self.y:
                GameDebug(StringBuilder("Pawn: MoveCheck: Pawn cannot move backwards"))
                return False
    
            if self.hasMoved==False:
                if toy==self.y+2 and getPiece(self.x,self.y+1).getcharacter()=="++" and getPiece(self.x,self.y+1).getcharacter()=="++":
                    GameDebug(StringBuilder("Pawn: MoveCheck: Pawn can move 2 spaces"))
                    return True
            if toy==self.y+1 and getPiece(self.x,self.y+1).getcharacter()=="++":
                GameDebug(StringBuilder("Pawn: MoveCheck: Pawn can move 1 space"))
                return True
            
        GameDebug("Nothing was hit?")
        return False

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__("R",5, x, y, color)

    # def getPossibleMoves(self, requestTile):
    #     #Returns a list of all possible moves for the rook
    #     #Tile is a variable that indicates the square to move to
    #     #Up
    #     tempx = self.x
    #     tempy = self.y
    #     while (tempy>=0):
    #         tempy-=1
    #         if self.tempConfig(tempx,tempy):
    #             break
    #         if getPiece(tempx,tempy).getcharacter()!="++":
    #             if getPiece(tempx,tempy).x==requestTile.x and getPiece(tempx,tempy).y==requestTile.y:
    #                 GameDebug("The Rook is located at " + self.x + " " + self.y + " and can move to " + requestTile.x + " " + requestTile.y)
    #                 return True
    #             break

    #     #Down
    #     tempx = self.x
    #     tempy = self.y
    #     while (tempy<8):
    #         tempy+=1
    #         if self.tempConfig(tempx, tempy):
    #             break
    #         if getPiece(tempx,tempy).getcharacter()!="++":
    #             if getPiece(tempx, tempy).x==requestTile.x and getPiece(tempx,tempy).y==requestTile.y:
    #                 GameDebug("The Rook is located at " + self.x + " " + self.y + " and can move to " + requestTile.x + " " + requestTile.y)
    #                 return True
    #     #Left
    #     tempx = self.x
    #     tempy = self.y
    #     while(tempx>=0):
    #         tempx-=1
    #         if self.tempConfig(tempx, tempy):
    #             break
    #         if getPiece(tempx,tempy).getcharacter()!="++":
    #             if getPiece(tempx,tempy).x==requestTile.x and getPiece(tempx,tempy).y==requestTile.y:
    #                 GameDebug("The Rook is located at " + self.x + " " + self.y + " and can move to " + requestTile.x + " " + requestTile.y)
    #                 return True
    #     #Right
    #     tempx = self.x
    #     tempy = self.y
    #     while(tempx<8):
    #         tempx+=1
    #         if self.tempConfig(tempx,tempy):
    #             break
    #         if getPiece(tempx,tempy).getcharacter()!="++":
    #             if getPiece(tempx,tempy).x==requestTile.x and getPiece(tempx,tempy).y==requestTile.y:
    #                 GameDebug("The Rook is located at " + self.x + " " + self.y + " and can move to " + requestTile.x + " " + requestTile.y)
    #                 return True

    def movecheck(self, tox, toy):
        global board

        if (tox!=self.x and toy!=self.y) or (tox==self.x and toy==self.y):
            GameDebug(StringBuilder("Rook: MoveCheck: Rook cannot move in two directions"))
            return False

        if getPiece(tox,toy).getcharacter()!= "++":
            GameDebug(StringBuilder("Rook: MoveCheck: Rook cannot move because the square is occupied", getPiece(tox,toy).getcharacter()))
            return False

        if tox==self.x:
            GameDebug(StringBuilder("Rook: MoveCheck: Rook can move in the y direction"))
            #y direction is changing
            tempy=self.y
            change=toy-tempy
            if change<0:
                change=-1
            if change>0:
                change=1
            tempy+=change
            if tempy>7 or tempy<0:
                GameDebug(StringBuilder("Rook: MoveCheck: Y: Out of bounds"))
                return False

            while tempy!=toy and getPiece(self.x,tempy).getcharacter()=="++":
                tempy+=change

            if tempy==toy:
                GameDebug(StringBuilder("Rook: MoveCheck: Y: Rook can move"))
                return True
            else:
                GameDebug(StringBuilder("Rook: MoveCheck: Y: Rook did not reach the target"))
                return False

        if toy==self.y:
            GameDebug(StringBuilder("Rook: MoveCheck: Rook can move in the x direction"))
            #x direction is changing
            tempx=self.x
            change=tox-tempx
            if change<0:
                change=-1
            if change>0:
                change=1
            tempx+=change
            if tempx>7 or tempx<0:
                GameDebug(StringBuilder("Rook: MoveCheck: X: Out of bounds"))
                return False

            while tempx!=tox and getPiece(tempx,self.y).getcharacter()=="++":
                tempx+=change

            if tempx==tox:
                GameDebug(StringBuilder("Rook: MoveCheck: X: Rook can move"))
                return True
            else:
                GameDebug(StringBuilder("Rook: MoveCheck: X: Rook did not reach the target"))
                return False
                    
        GameDebug(StringBuilder("Rook: MoveCheck: Rook cannot move"))
        return False

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__("&",3, x, y, color)

    # def getPossibleMoves(self, requestTile):
    #     if abs(requestTile.x-self.x)==2 and abs(requestTile.y-self.y)==1:
    #         GameDebug("The Knight is located at " + self.x + " " + self.y + " and can move to " + requestTile.x + " " + requestTile.y)
    #         return True

    def movecheck(self, tox, toy):

        if abs(tox-self.x)==2 and abs(toy-self.y)==1 and getPiece(tox,toy).getcharacter()=="++":
            GameDebug(StringBuilder("Knight: MoveCheck: Knight can move"))
            return True
        if abs(tox-self.x)==1 and abs(toy-self.y)==2 and getPiece(tox,toy).getcharacter()=="++":
            GameDebug(StringBuilder("Knight: MoveCheck: Knight can move"))
            return True
        GameDebug(StringBuilder("Knight: MoveCheck: Knight cannot move"))
        return False

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__("B",3, x, y, color)

    def movecheck(self, tox, toy):
        tempx=self.x
        tempy=self.y

        if abs(tox-self.x)!=abs(toy-self.y):
            GameDebug(StringBuilder("Bishop: MoveCheck: Bishop cannot move"))
            return False
        
        x_change=tox-self.x
        y_change=toy-self.y

        if x_change<0:
            x_change=-1
        if x_change>0:
            x_change=1
        if y_change<0:
            y_change=-1
        if y_change>0:
            y_change=1

        tempx+=x_change
        tempy+=y_change

        while tempx!=tox and tempy!=toy and getPiece(tempx,tempy).getcharacter()=="++":
            tempx+=x_change
            tempy+=y_change

        if tempx==tox and tempy==toy:
            GameDebug(StringBuilder("Bishop: MoveCheck: Bishop can move"))
            return True

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__("Q",9, x, y, color)
    
    def getPossibleMoves(self, requestTile):
        pass
    
    def movecheck(self,tox,toy):

        tempx=self.x
        tempy=self.y

        #Like bishop
        if abs(tox-self.x)==abs(toy-self.y):
        
            x_change=tox-self.x
            y_change=toy-self.y

            if x_change<0:
                x_change=-1
            if x_change>0:
                x_change=1
            if y_change<0:
                y_change=-1
            if y_change>0:
                y_change=1

            tempx+=x_change
            tempy+=y_change

            while tempx!=tox and tempy!=toy and getPiece(tempx,tempy).getcharacter()=="++":
                tempx+=x_change
                tempy+=y_change

            if tempx==tox and tempy==toy:
                GameDebug(StringBuilder("Queen: Bishop: MoveCheck: Queen can move"))
                return True

            #Like Rook
            
        if (tox!=self.x and toy==self.y) or (tox==self.x and toy!=self.y):

            if tox==self.x:
                #y direction is changing
                tempy=self.y
                change=toy-tempy
                if change<0:
                    change=-1
                if change>0:
                    change=1
                tempy+=change

                while tempy!=toy and getPiece(self.x,tempy).getcharacter()=="++":
                    tempy+=change
                
                if tempy==toy:
                    GameDebug(StringBuilder("Queen: Rook: MoveCheck: Queen can move"))
                    return True

            if toy==self.y:
                #x direction is changing
                tempx=self.x
                change=tox-tempx
                if change<0:
                    change=-1
                if change>0:
                    change=1

                tempx+=change

                while tempx!=tox and getPiece(tempx,self.y).getcharacter()=="++":
                    tempx+=change

                if tempy==toy:
                    GameDebug(StringBuilder("Queen: Rook: MoveCheck: Queen can move"))
                    return True
                
        GameDebug(StringBuilder("Queen: MoveCheck: Queen cannot move"))
        return False
    
class King(Piece):
    def __init__(self, x, y, color):
        super().__init__("K",100, x, y, color)

    def getPossibloeMoves(self, requestTile):
        pass

    def movecheck(self,tox,toy):
        if abs(tox-self.x)>1 or abs(toy-self.y)>1 or getPiece(tox,toy).getcharacter()!="++":
            GameDebug(StringBuilder("King: MoveCheck: King cannot move"))
            return False
        return True

class Empty(Piece):
    def __init__(self, x, y, color):
        super().__init__("+",0, x, y, color)

    def movecheck(self,tox,toy):
        GameDebug("Empty: MoveCheck: Empty cannot move")
        return False



global board

board=[[Rook(0,0,"B"),Knight(1,0,"B"),Bishop(2,0,"B"),Queen(3,0,"B"),King(4,0,"B"),Bishop(5,0,"B"),Knight(6,0,"B"),Rook(7,0,"B")],
        [Pawn(0,1,"B"),Pawn(1,1,"B"),Pawn(2,1,"B"),Pawn(3,1,"B"),Pawn(4,1,"B"),Pawn(5,1,"B"),Pawn(6,1,"B"),Pawn(7,1,"B")],
        [Empty(0,2,"+"),Empty(1,2,"+"),Empty(2,2,"+"),Empty(3,2,"+"),Empty(4,2,"+"),Empty(5,2,"+"),Empty(6,2,"+"),Empty(7,2,"+")],
        [Empty(0,3,"+"),Empty(1,3,"+"),Empty(2,3,"+"),Empty(3,3,"+"),Empty(4,3,"+"),Empty(5,3,"+"),Empty(6,3,"+"),Empty(7,3,"+")],
        [Empty(0,4,"+"),Empty(1,4,"+"),Empty(2,4,"+"),Empty(3,4,"+"),Empty(4,4,"+"),Empty(5,4,"+"),Empty(6,4,"+"),Empty(7,4,"+")],
        [Empty(0,5,"+"),Empty(1,5,"+"),Empty(2,5,"+"),Empty(3,5,"+"),Empty(4,5,"+"),Empty(5,5,"+"),Empty(6,5,"+"),Empty(7,5,"+")],
        [Pawn(0,6,"W"),Pawn(1,6,"W"),Pawn(2,6,"W"),Pawn(3,6,"W"),Pawn(4,6,"W"),Pawn(5,6,"W"),Pawn(6,6,"W"),Pawn(7,6,"W")],  
        [Rook(0,7,"W"),Knight(1,7,"W"),Bishop(2,7,"W"),Queen(3,7,"W"),King(4,7,"W"),Bishop(5,7,"W"),Knight(6,7,"W"),Rook(7,7,"W")]]

def GameDebug(information):
    # file=open("Chess/GameDebug.txt","a")
    file = open("GameDebug.txt", "a")
    file.write(information)
    file.write('\n')
    file.close()

def StringBuilder(*args):

    string=""
    for arg in args:
        string+=str(arg)
    return string

def alphaChar(char):

    if char=="a":
        return 0
    if char=="b":
        return 1
    if char == "c":
        return 2
    if char == "d":
        return 3
    if char == "e":
        return 4
    if char == "f":
        return 5
    if char == "g":
        return 6
    if char == "h":
        return 7

def ConfirmMove(firstx,firsty,secondx,secondy,color, taking):

    if firstx not in "abcdefgh" or secondx not in "abcdefgh" or firsty not in "12345678" or secondy not in "12345678":
        GameDebug(StringBuilder("Validate Move: Invalid Move: "))
        return False 

    pieceFrom=getPiece(alphaChar(firstx),8-(int(firsty)))

    if pieceFrom.getcolor()!=color:
        #The piece is not the correct color
        GameDebug(StringBuilder("Validate Move: Invalid Move: Incorrect Color:"))
        return False

    pieceTo=getPiece(alphaChar(secondx),8-int(secondy))

    if (pieceTo.getcharacter()!='++') ^ taking:
        #The intended square is not empty and we are not taking
        GameDebug(StringBuilder("Validate Move: Invalid Move: Square is not empty blocked by: ", pieceTo.getcharacter(), " at ", secondx, secondy))
        return False
    #Now we have passed all the checks, just making sure that the move will be done coorectly
    GameDebug(StringBuilder("Move Check: ", pieceFrom.getcharacter(), " ", pieceTo.getcharacter()))
    if pieceFrom.movecheck(alphaChar(secondx),8-int(secondy))==False:
        #The piece cannot move like that
        GameDebug(StringBuilder("Validate Move: Invalid Move: ",pieceFrom.getcharacter()," cannot move like that"))
        return False

    # if the piece that is being moved doesn't prevent a check
    GameDebug("Checking if the King is in check")
    move(pieceFrom, pieceTo)
    if len(inCheck(color).getAttacker())!=0:
        #If there is still attackers, then it didn't work
        GameDebug("The move failed, there is an attacker attacking the king")
        return False
    move(pieceTo, pieceFrom)


    #if all the squares between the two are empty
    GameDebug(StringBuilder("Validate Move: Valid Move: ",pieceFrom.getcharacter()," can move to ", secondx,secondy))
    return True

def ValidateMove(move,color):
    GameDebug(StringBuilder("Validate Move: ",move))
    if len(move)==4:
        #not Taking

        firstx=move[0]
        firsty=move[1]
        secondx=move[2]
        secondy=move[3]

        return ConfirmMove(firstx,firsty,secondx,secondy,color, False)

    elif len(move)==5:
        #Taking

        firstx=move[0]
        firsty=move[1]
        secondx=move[3]
        secondy=move[4]

        return ConfirmMove(firstx,firsty,secondx,secondy,color, True)     

    else:
        GameDebug(StringBuilder("Validate Move: Invalid Move: Too long/short",move))
        return False

def MakeMove(movingPiece,length):

    firstx=movingPiece[0]
    firsty=movingPiece[1]
    if length==4:
        secondx=movingPiece[2]
        secondy=movingPiece[3]
    else:
        secondx=movingPiece[3]
        secondy=movingPiece[4]

    pieceFrom=getPiece(alphaChar(firstx),8-(int(firsty)))
    if length ==5:
        pieceTo = Empty(alphaChar(secondx), 8-(int(secondy)), "+")
    else:
        pieceTo=getPiece(alphaChar(secondx),8-(int(secondy)))
    
    GameDebug(StringBuilder("MakeMove: ",pieceFrom.getcharacter(), " ", pieceTo.getcharacter()))
    move(pieceFrom, pieceTo)

def GetMove(color):

    move=""

    if color=="W":
        move=input("White Move: ")
    if color=="B":
        move=input("Black Move: ")

    while ValidateMove(move,color)==False:
        GameDebug(StringBuilder("GetMove: Invalid Move: ",move))
        move=input("Invalid Move, Try Again: ")
    MakeMove(move,len(move))
    GameDebug(StringBuilder("GetMove: Move Made: ",move))

def inCheck(color):
        GameDebug("--- Checking if the king is in check ---")
        #find the king and return the king item
        string=str(color)+"K"
        for i in range(8):
            for j in range(8):
                if getPiece(i,j).getcharacter()==string and getPiece(i,j).getcolor()==color:
                    GameDebug("King Found at: " + str(i)  + " " + str(j))
                    GameDebug("--- King Found ---")
                    return getPiece(i,j)
        GameDebug("--- King not found ---")

def CheckKing(king,i,j):
    #Checking if the king is able to move true if it is unable
    for i in range(-1,1,1):
        for j in range(-1,1,1):
            if i==0 and j==0:
                pass
            else:
                if king.getx()+i>=0 and king.getx()+i<8 and king.gety()+j>=0 and king.gety()+j<8:
                    if getPiece(king.getx()+i,king.gety()+j).getcharacter()=="++":
                        if len(inCheck(king.getcolor()).getAttacker())==0:
                            return False
    return True

def Blocking(item, color):
    defenderList = []
    GameDebug("Check for blockers")
    #Get a list of the tiles that are between the attacking piece and king
    #Get the coords of the attacking piece
    [attacker_x, attacker_y] = item.getLocation()
    #Get the coords of the king
    [king_x, king_y] = inCheck(color).getLocation()
    #Return a list of the tiles between the two
    GameDebug(StringBuilder("Attacker: ", attacker_x, " ", attacker_y))
    GameDebug(StringBuilder("King: ",king_x, " ", king_y))
    #If the attacker is a knight handle it differently
    #Otherwise
    emptylist = []
    [change_x, change_y] = [attacker_x-king_x, attacker_y-king_y]

    #This can't be extracted further as 0 needs to be 0
    if change_x>0: # If the change is positive
        change_x=1
    if change_x<0: # If the change is negative
        change_x=-1
    if change_y>0: # If the change is positive
        change_y=1
    if change_y<0: # If the change is negative
        change_y=-1

    attacker_x -= change_x 
    attacker_y -= change_y
    while (attacker_x != king_x and attacker_y != king_y):

        GameDebug(StringBuilder("Adding Piece: ", attacker_x, " ", attacker_y))
        emptylist.append({"Piece": getPiece(attacker_x, attacker_y), "x": attacker_x, "y": attacker_y})
        attacker_x -= change_x
        attacker_y -= change_y

    newpossible = []
    #empylist has dictionaries inside of it which contain the piece and the x and y coords
    for i in range(len(emptylist)):
        empty = emptylist[i]["Piece"]
        #Check for pieces that can block the check
        GameDebug("=====================================")
        GameDebug(StringBuilder("Empty: ", empty.getcharacter(), " ", emptylist[i]["x"], " ", emptylist[i]["y"]))
        possibleMoves = empty.spider()
        if len(possibleMoves)!=0:
            for j in range(len(possibleMoves)):
                possible = possibleMoves[j]
                #Once we have this list, we need to check if it can block
                if possible.getcolor() == color:
                    GameDebug("Opposite Color: " + possible.getcharacter() + " This piece can move to " + str(possible.getx()) + " " + str(possible.gety()) + " from " + str(emptylist[i]["x"]) + " " + str(emptylist[i]["y"]))
                    newpossible.append({"Piece": possible, "x": emptylist[i]["x"], "y": emptylist[i]["y"]})
        else:
            GameDebug("Empty List")
    if len(newpossible)!=0: #We have a list of pieces that can block the check
        GameDebug("Possible Moves")

        for new in newpossible:
            GameDebug(StringBuilder("Piece: ", new["Piece"].getcharacter(), " ", new["x"], " ", new["y"]))
            # Check if this move prevents the attack
            pieceFrom = new["Piece"]
            pieceTo = getPiece(new["x"], new["y"])
            move(pieceFrom, pieceTo)
            if len(inCheck(color).getAttacker())==0:
                #If the move does not prevent the attack, then it is not a valid move
                # We can break knowing that there is a move that can block the check
                GameDebug("We have reached this point in the code where something blocks the check")
                GameDebug("This is the piece that blocks the check: " + pieceTo.getcharacter() + " at " + str(pieceTo.getx()) + " " + str(pieceTo.gety()) + " from " + str(pieceFrom.getx()) + " " + str(pieceFrom.gety()))
                GameDebug("=====================================")
                defenderList.append(pieceTo)
            else:
                GameDebug("The move failed, iterating to next")
            move(pieceTo, pieceFrom)
            #If there are pieces that can block the check, then the king is not in checkmate
            # break
        if len(defenderList)!=0:
            GameDebug("Defender List")
            for defender in defenderList:
                GameDebug(StringBuilder("Defender: ", defender.getcharacter(), " ", defender.getx(), " ", defender.gety()))
                defender.spider()
            return 0
        else:
            GameDebug("Checkmate")
            GameDebug("=====================================")
            return 1

    else:
        GameDebug("Checkmate?")
        return 1
    #Now that we have a list of pieces which in theory blocks the check, we need to check that they block the check
    #If they do, then the king is not in checkmate

def Checkmate(color):
        GameDebug("Checking: " + color + "King")
        #exitLoop being false means that the King is able to move
        #exitLoop being true means that the King is unable to move
        exitLoop = False
        checklist = inCheck(color).getAttacker()
        if len(checklist)!=0:
            #if there is items in the list
            GameDebug("Check")
            counter = 0
            for item in checklist:
                GameDebug(StringBuilder("The item is: ", item.getcharacter()))

            #I need to work out what correct condition(s) are for this while loop
            # if the counter is not less than the length of the checklist or the exitLoop variable is true then break
            # while we havent reached the end of the list and we aren't exiting the loop
            while (counter < len(checklist)):
                item = checklist[counter]
                #For every item that can attack the king

                GameDebug("The piece checking the king is " + item.getcharacter())
                #Work out if we are able to avoid the check (whether by blocking or capturing the piece)
                item.spider()
                attackinglist = item.getAttacker() #Find out if the piece can be attacked
                if len(attackinglist)!=0:
                    #If the list is non-zero then we have something that can capture it
                    #Check the case for where the attacking piece is actually blocking a check
                    GameDebug("Attackers found")
                    for attacker in attackinglist:
                        GameDebug("The piece attacking the " + item.getcharacter()+ " is " + attacker.getcharacter())
                    exitLoop = False
                else:
                    #Check for blockers
                    exitLoop = Blocking(item, color)
                counter +=1
            #If exitLoop is true then that means that we have found a way to prevent the check, if it is false there is no way?
        else:
            GameDebug("There is no piece checking the king")
        GameDebug(StringBuilder("The Exit Code Here is ", exitLoop))
        return exitLoop

def main():

    file = open("GameDebug.txt", "w")
    file.close()

    #Variables
    movelog=[]
    GameOver=0
    while GameOver==0:
        #White Turn
        PrintBoard()
        GetMove("W")
        GameOver = Checkmate("W") + Checkmate("B")
        if not GameOver:
            PrintBoard()
            GetMove("B")
            GameOver = Checkmate("W") + Checkmate("B")

    print("The Game is over!")


main()
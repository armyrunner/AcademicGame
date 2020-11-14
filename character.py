class character: 
    
    def __init__(self,x,y,dx,dy,w,h):
        self.mX = x
        self.mY = y
        self.mW = w
        self.mH = h
        self.mDX = dx
        self.mDY = dy
        return 

    def getX(self):
        return self.mX
    
    def setX(self,x):
        self.mX = x
        return
      
    def getY(self):
        return self.mY
    
    def setY(self,y):
        self.mY = y
        return
      
    def getW(self):
        return self.mW

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def setDX(self,dx):
        self.mDX += dx

    def setDY(self,dy):
        self.mDY +=dy
    
    def setW(self,w):
        self.mW = w
        return
      
    def getH(self):
        return self.mH
    
    def setH(self,h):
        self.mH = h
        return

    def containsPoint(self, x, y):
        if( (x >= self.getX()) and (x <= self.getX() + self.getW()) and (y >= self.getY()) and (y <= self.getY() + self.getH()) ):
            return True
        return False

    def getEdges(self):
        redge = self.getX() + self.getW()
        tedge = self.getY() + self.getH()
        return [ (self.getX(),self.getY()), (self.getX(),tedge), (redge,tedge), (redge,self.getY()) ]
    
    def collision(self,other):
        ourborders = self.getEdges()
        
        theirborders = other.getEdges()

        for point in ourborders:
            x, y = point
            if other.containsPoint(x,y):
                return True

        for opoint in theirborders:
            x, y = opoint
            if self.containsPoint(x,y):
                return True
        
        return False
    
    def move(self,dt):
        self.mX += self.mDX*dt
        self.mY += self.mDY.dt
        return

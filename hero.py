from character import character

class Hero(character):

    def __init__(self,x,y,w,h,speed,ammo):
        character.__init__(self,x,y,w,h)
        self.mSpeed = speed
        self.mAmmo = ammo
        return

    def getSpeed(self):
        return self.mSpeed
    
    def setSpeed(self,speed):
        self.mSpeed = speed
        return

    def getAmmo(self):
        return self.mAmmo

    def setAmmo(self,ammo):
        self.mAmmo = ammo
        return

    def move(self,newX,newY):
        if (self.mX == newX and self.mY == newY) or (self.mX<0 or self.mY<0 or (self.mX+self.mW >700) or (self.mY+self.mH>800)): # Change if the height or width of the screen change
            return
        diffx = newX - self.mX
        diffy = newY - self.mY
        diff = abs(diffx) + abs(diffy)
        ratiox = float(diffx) / float(diff)
        ratioy = float(diffy) / float(diff)
        dx = int(ratiox * self.mSpeed)
        dy = int(ratioy * self.mSpeed)
        if abs(dx) > abs(diffx):
            dx = diffx
        if abs(dy) > abs(diffy):
            dy = diffy
        self.mX += dx
        self.mY += dy
        self.move(newX,newY)
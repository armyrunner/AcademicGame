from character import character

class Hero(character):

    def __init__(self,x,y,w,h,speed,ammo):
        character.__init__(self,x,y,w,h)
        self.mSpeed = speed
        self.mAmmo = ammo
        return

    def getSpeed(self):
        return mSpeed
    
    def setSpeed(self,speed):
        self.mSpeed = speed
        return

    def getAmmo(self):
        return mAmmo

    def setAmmo(self,ammo):
        self.mAmmo = ammo
        return
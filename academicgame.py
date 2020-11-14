import pygame
import environment
import hero
import bullet



class AcademicGame:
    def __init__(self,width,height):
        self.envShop = environment.ShopScene(width,height)
       #self.envAction = environment.ActionScene(width,height,heatlth,self.)
        self.ammo = bullet.Bullet(3,3,0,0,height,width)
        self.mHero = hero.Hero(3,3,width,height,2,self.ammo)
        self.mWidth = width
        self.mHeight = height
        self.GameOver = False
        self.HeroWins = False
        self.Right = False
        self.Left = False
        self.walkcount = 0
        self.isJump = False
        self.jumpCount = 10
        self.velocity = 5
        self.mX = 50
        self.mY = 400
        self.mObjWidth = 40
        self.mObjHeight = 60



    def evolve(self,dt):

        if self.GameOver:
            return
        

    def actionUP():
        pass

    def actionRIGHT():
        # if self.mX < self.mWidth - self.velocity - self.mObjWidth:
        #     self.mX += self.velocity
        #     self.left = True
        #     self.right = False
        # else:
        #     self.left = False
        #     self.right = False
        #     self.walkcount = 0
        pass

    def actionLEFT():
        # if self.mX > self.velocity:
        #     self.mX -= self.velocity
        #     self.left = False
        #     self.right = True
        pass
    
    def acitionDown():
        pass

    def actionSPACEBAR():
        pass
   

    def draw(self,surface):
        self.envShop.draw(surface)
        #self.envAction.draw(surface)


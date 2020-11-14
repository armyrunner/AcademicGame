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



    def draw(self,surface):
        self.envShop.draw(surface)
        #self.envAction.draw(surface)


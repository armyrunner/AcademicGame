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



    def evolve(self,dt):

        if self.GameOver:
            return
        

    def actionUP():
        pass

    def actionRIGHT():
        pass

    def actionLEFT():
        pass

    def acitionDown():
        pass
   

    def draw(self,surface):
        self.envShop.draw(surface)
        #self.envAction.draw(surface)


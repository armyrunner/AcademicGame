import pygame
import environment
import hero
import bullet



class AcademicGame:
    def __init__(self,width,height):
        self.envShop = environment.ShopScene(width,height)
       #self.envAction = environment.ActionScene(width,height,heatlth,self.)

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
        self.mHero = hero.Hero(3,3,0,0,width,height,2)
        self.mBullet = []

    def getmBullet(self):
        return self.mBullet

    def fire(self):

        if len(self.mBullet) != 3:
            firex = self.mHero.mX
            firey = self.mHero.mY
            firedx = self.mHero.mDX
            firedy = self.mHero.mDY
            ammo = bullet.Bullet(firex,firey,firedx,firedy,self.mHeight,self.mWidth)
            self.mBullet.append(ammo)
       

    def evolve(self,dt):

        if self.GameOver:
            return

    def ActionPressSpaceBar(self):
        self.ammo.Fire()


    def draw(self,surface):
        self.envShop.draw(surface)
        #self.envAction.draw(surface)
        for objects in self.mBullet:
            objects.draw(surface)


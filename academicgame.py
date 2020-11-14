import pygame
import environment


class AcademicGame:
    def __init__(self,width,height):
        self.envShop = environment.ShopScene(width,height)
        # self.envAction = environment.Scene(width,height)
        self.mWidth = width
        self.mHeight = height

    def evolve(self,dt):
        pass

    def draw(self,surface):
        self.envShop.draw(surface)
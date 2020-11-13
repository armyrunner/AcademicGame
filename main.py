import pygame
import game

import academicgame

"""
Team ToDo:://<InserRubberDuck>

"""

TITLE = " Quest For Knowledge"

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
DESIRED_RATE = 30

class PygameApp(gam.Game):

    def __init__(self,title,widht,height,frame_rate):
        game.Game.__init__(self,title,width,height,frame_rate)

        self.academicgame = academicgame.AcademicGame(WINDOW_WIDTH,WINDOW_HEIGHT)
        return


    def game_logic(self,keys,newkeys,buttons,newbuttions,mouse_position,dt):

        # how to controll the game with arrow keys orw wasd or mouse button

        if pygame.K_UP in newkeys:
            self.academicgame.actionUP()
        if pygame.K_DOWN in newkeys:
            self.academicgame.actionDOWN()
        if pygame.K_LEFT in newkeys:
            self.academicgame.actionLEFT()
        if pygame.K_RIGHT in newkeys:
            self.academicgame.actionRIGHT()
        
        self.academicgame.evolve(dt)

    def paint(self,surface):
        self.academicgame.draw(surface)

def main():
    pygame.font.init()
    game.PygameApp(TITLE,WINDOW_WIDTH,WINDOW_HEIGHT,DESIRED_RATE)
    game.main_loop()

if __name__ == "__main__":
    main()
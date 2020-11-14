import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import academicgame
import hero
"""
DNumber: D00090307
Name: Andrew Nelson
Picture: House
Assignment: FROGGER

"""
# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME


TITLE = "QUEST FOR KNOWLEDGE" # window title bar text

WINDOW_WIDTH  = 900# pixels width
WINDOW_HEIGHT = 780 # pixels high
DESIRED_RATE  = 30 # frames per second


class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.academicgame = academicgame.AcademicGame(width,height)
        self.hero = hero.Hero(5,500,10,10,0,0)
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        # KEYS TO MOVE HERO

        if pygame.K_UP in newkeys:
            self.academicgame.actionUP( )
        if pygame.K_DOWN in newkeys:
            self.academicgame.actionDOWN( )
        if pygame.K_LEFT in newkeys:
            self.academicgame.actionLEFT( )
        if pygame.K_RIGHT in newkeys:
            self.academicgame.actionRIGHT( )
        self.academicgame.evolve(dt)

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.academicgame.draw( surface )
        if self.hero.getSpeed() == 0:
            image = pygame.image.load(r'Images/R1.png') 
        elif self.hero.getSpeed() > 0: #somehow figure out direction he's walking, currently goes right.
            image = pygame.image.load(r'Images/R2.png')
        else:
            image = pygame.image.load(r'Images/L2.png')
        surface.blit(image, (self.hero.getX(), self.hero.getY())) 
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )

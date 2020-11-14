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


WALKRIGHT = [pygame.image.load('Images/R1.png'), pygame.image.load('Images/R2.png'), pygame.image.load('Images/R3.png'), pygame.image.load('Images/R4.png'), 
             pygame.image.load('Images/R5.png'), pygame.image.load('Images/R6.png'), pygame.image.load('Images/R7.png'), pygame.image.load('Images/R8.png'),
             pygame.image.load('Images/R9.png')]

WALKLEFT = [pygame.image.load('Images/L1.png'), pygame.image.load('Images/L2.png'), pygame.image.load('Images/L3.png'), pygame.image.load('Images/L4.png'),
            pygame.image.load('Images/L5.png'), pygame.image.load('Images/L6.png'), pygame.image.load('Images/L7.png'), pygame.image.load('Images/L8.png'),
            pygame.image.load('Images/L9.png')]

STANDING = pygame.image.load('Images/standing.png')


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
        self.WALKCOUNT = 0
        self.Left = False
        self.Right = False
        return

    def getWalkCount(self):
        return self.WALKCOUNT


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
      

        # KEYS TO MOVE HERO
        if self.WALKCOUNT + 1 >= 27:
            self.WALKCOUNT =0 
        if pygame.K_UP in keys:
            self.academicgame.actionUP( )
        if pygame.K_DOWN in keys:
            self.academicgame.actionDOWN( )
        if pygame.K_LEFT in keys:
            self.hero.moveLeft(5)
            self.WALKCOUNT += 1
            self.Left = True
            self.Right = False
        if pygame.K_RIGHT in keys:
            self.hero.moveRight(5,WINDOW_WIDTH)
            self.WALKCOUNT += 1
            self.Right = True
            self.Left = False
        self.academicgame.evolve(dt)

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.academicgame.draw( surface )
        if self.Right:
            surface.blit(WALKRIGHT[self.WALKCOUNT//3], (self.hero.getX(), self.hero.getY())) 
            #image = pygame.image.load(r'Images/R1.png') 
        elif self.Left: #somehow figure out direction he's walking, currently goes right.
            #image = pygame.image.load(r'Images/R2.png')
                surface.blit(WALKLEFT[self.WALKCOUNT//3], (self.hero.getX(), self.hero.getY())) 
        else:
            surface.blit(STANDING, (self.hero.getX(), self.hero.getY())) 
            return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )

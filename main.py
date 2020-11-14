import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import academicgame
"""
DNumber: D00090307
Name: Andrew Nelson
Picture: House
Assignment: FROGGER

"""
# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME


TITLE = "QUEST FOR KNOWLEDGE" # window title bar text

WINDOW_WIDTH  = 700# pixels width
WINDOW_HEIGHT = 800 # pixels high
DESIRED_RATE  = 30 # frames per second


class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.academicgame = academicgame.AcademicGame(width,height)
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
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )

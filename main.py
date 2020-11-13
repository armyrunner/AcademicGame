import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import acdemicgame
"""
DNumber: D00090307
Name: Andrew Nelson
Picture: House
Assignment: FROGGER

"""
# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME


TITLE = "FROGGER" # window title bar text

WINDOW_WIDTH  = 700# pixels width
WINDOW_HEIGHT = 800 # pixels high
DESIRED_RATE  = 30 # frames per second


class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.acdemicgame = acdemicgame.AcdemicGame(width,height)
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        # KEYS TO MOVE HERO

        if pygame.K_UP in newkeys:
            self.acdemicgame.actionUP( )
        if pygame.K_DOWN in newkeys:
            self.acdemicgame.actionDOWN( )
        if pygame.K_LEFT in newkeys:
            self.acdemicgame.actionLEFT( )
        if pygame.K_RIGHT in newkeys:
            self.acdemicgame.actionRIGHT( )
        self.acdemicgame.evolve(dt)

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.acdemicgame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )

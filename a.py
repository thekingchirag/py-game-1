# Import Necessary Libraries
import pygame
# initialize required modules
pygame.init()
# set up window geometry
screen = pygame.display.set_mode((400, 500))
# Create a loop to run till the game is quit by the user 
done = False
while not done:
    #clear the event queue
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
    #make the changes visible on the screen
    # pygame.display.flip()      